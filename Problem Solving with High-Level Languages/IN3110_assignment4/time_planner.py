import re
from copy import copy
from dataclasses import dataclass

import bs4
import pandas as pd
from bs4 import BeautifulSoup
from requesting_urls import get_html

## --- Task 5, 6, and 7 ---- ##

# Dict over all types of events
event_types = {
    "DH": "Downhill",
    "SL": "Slalom",
    "GS": "Giant Slalom",
    "SG": "Super Giant slalom",
    "AC": "Alpine Combined",
    "PG": "Parallel Giant Slalom",
}


def time_plan(url: str) -> str:
    """Parses table from html text and extract desired information
    and saves in betting slip markdown file

    arguments:
        url (str) : URL for page with calendar table
    return:
        markdown (str) : string containing the markdown schedule
    """
    # Get the page
    html = get_html(url)
    # parse the HTML
    soup = BeautifulSoup(html, "html.parser")
    # locate the table
    calendar = soup.find(id="Calendar")
    soup_table = calendar.find_next("table", {"class": "wikitable"})
    # extract events into pandas data frame
    df = extract_events(soup_table)
    # Write the schedule markdown
    return render_schedule(df)


@dataclass
class TableEntry:
    """Data class representing a single entry in a table

    Records text content, rowspan, and colspan attributes
    """

    text: str
    rowspan: int
    colspan: int


def extract_events(table: bs4.element.Tag) -> pd.DataFrame:
    """Gets the events from the table
    arguments:
        table (bs4.element.Tag) : Table containing data
    return:
        df (DataFrame) : DataFrame containing filtered and parsed data
    """
    # Gets the table headers and saves their labels in `keys`
    headings = table.find_all("th")
    labels = [th.text.strip() for th in headings]
    data = []

    #print("Labels: ",labels)

    # Extracts the data in table, keeping track of colspan and rowspan
    rows = table.find_all("tr") 
    rows = rows[1:]
    for tr in rows:
        cells = tr.find_all("td")
        #cells = [td.text.strip() for td in cells]
        row = [] #[td.text.strip() for td in cells]#[td.text.strip() for td in cells] # row = [td.text.strip() for td in cells]
        for cell in cells:
            #print("Cells: ", cell)
            colspan = 1
            rowspan = 1
            # If datacell contains colspan we assign colspan 
            if cell.get("colspan"): 
                colspan = (int(cell.get("colspan")))
            # If datacell contains rowspan we assign rowspan value
            if cell.get("rowspan"): 
                rowspan = (int(cell.get("rowspan")))
            
            # Get info of that cell
            text = cell.text.strip()
            row.append(
                TableEntry(
                    text=text,
                    rowspan=rowspan,
                    colspan=colspan,
                )
            )
        data.append(row)
    #print("-----Data list: ", data, "\n")
    # at this point `data` should be a table (list of lists)
    # where each item is a TableEntry with row/colspan properties
    # expand TableEntries into a dense table

    all_data = expand_row_col_span(data)

    # List of desired columns
    wanted = ["Date", "Venue", "Type"]

    # Filter data and create pandas dataframe
    filtered_data = filter_data(labels, all_data, wanted)
    df = pd.DataFrame(filtered_data, columns=wanted)

    return df


def render_schedule(data: pd.DataFrame) -> str:
    """Render the schedule data to markdown

    arguments:
        data (DataFrame) : DataFrame containing table to write
    return:
        markdown (str): the rendered schedule as markdown
    """
    
    def expand_event_type(type_key):
        """Expand event type key (SL) to full name (Slalom)

        Useful with pandas Series.apply
        """
        return event_types.get(type_key[:2], type_key)

    # Here we expand type-key to full name of Event
    data["Type"]=data["Type"].apply(expand_event_type)
    
    return data.to_markdown(index=False)
    

def strip_text(text: str) -> str:
    """Gets rid of cruft from table cells, footnotes and setting limit to 20 chars

    It is not required to use this function,
    but it may be useful.

    arguments:
        text (str) : string to fix
    return:
        text (str) : the string fixed
    """

    text = text[:20]  # 20 char limit
    text = re.sub(r"\[.*\]", "", text)
    return text


def filter_data(keys: list, data: list, wanted: list):
    """Filters away the columns not specified in wanted argument

    It is not required to use this function,
    but it may be useful.

    arguments:
        keys (list of strings) : list of all column names
        data (list of lists) : data with rows and columns
        wanted (list of strings) : list of wanted columns
    return:
        filtered_data (list of lists) : the filtered data
            This is the subset of data in `data`,
            after discarding the columns not in `wanted`.
    """
    
    #List for wanted indexes of wanted arguments in keys
    wanted_index = []
    # List of filtered data
    new_data = []

    # Iterate through elements of wanted columns and find the indexes of these elemnts in the list of all column names
    for elem in wanted:
        wanted_index.append(keys.index(elem))

    # Iterate through rows in data
    for list in data:
        # Creates list of wanted columns per row
        wanted_data = []
        # Iterates through wanted columns
        for cols in wanted_index:
            # Appends wanted_data with the wanted columns that we find in data
            wanted_data.append(list[cols])
        # Append all wanted columns in the lists for filtered data
        new_data.append(wanted_data)

    return new_data


def expand_row_col_span(data):
    """Applies row/colspan to tabular data

    It is not required to use this function,
    but it may be useful.

    - Copies cells with colspan to columns to the right
    - Copies cells with rowspan to rows below
    - Returns raw data (removing TableEntry wrapper)

    arguments:
        data_table (list) : data with rows and cols
            Table of the form:

            [
                [ # row
                    TableEntry(text='text', rowspan=2, colspan=1),
                ]
            ]
    return:
        new_data_table (list): list of lists of strings
            [
                [
                    "text",
                    "text",
                    ...
                ]
            ]

            This should be a dense matrix (list of lists) of data,
            where all rows have the same length,
            and all values are `str`.
    """

    # first, apply colspan by duplicating across the column(s)
    new_data = []
    for row in data:
        new_row = []
        new_data.append(new_row)
        for entry in row:
            for _ in range(entry.colspan):
                new_entry = copy(entry)
                new_entry.colspan = 1
                new_row.append(new_entry)

    # apply row span by inserting copies in subsequent rows
    # in the same column
    for row_idx, row in enumerate(new_data):
        for col_idx, entry in enumerate(row):
            for offset in range(1, entry.rowspan):
                # copy to row(s) below
                target_row = new_data[row_idx + offset]
                new_entry = copy(entry)
                new_entry.rowspan = 1
                target_row.insert(col_idx, new_entry)
            entry.rowspan = 1

    # now that we've applied col/row span,
    # replace the table with the raw entries,
    # instead of the TableEntry objects
    return [[entry.text for entry in row] for row in new_data]


if __name__ == "__main__":
    # test the script on the past few years by running it:
    for year in range(20, 23):
        url = (
            f"https://en.wikipedia.org/wiki/20{year}–{year+1}_FIS_Alpine_Ski_World_Cup"
        )
        print(url)
        md = time_plan(url)
        print(md)
