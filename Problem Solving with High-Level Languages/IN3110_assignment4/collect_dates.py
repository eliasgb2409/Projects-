import re
from typing import Tuple
import os

## -- Task 4 (IN3110 optional, IN4110 required) -- ##

# create array with all names of months
month_names = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

def get_date_patterns() -> Tuple[str, str, str]:
    """Return strings containing regex pattern for year, month, day
    arguments:
        None
    return:
        year, month, day (tuple): Containing regular expression patterns for each field
    """

    # Regex to capture days, months and years with numbers
    # year should accept a 4-digit number between at least 1000-2029
    year = r"(?P<year>...)"
    # month should accept month names or month numbers
    month = r"(?P<month>...)"
    # day should be a number, which may or may not be zero-padded
    day = r"(?P<day>...)"

    return year, month, day


def convert_month(s: str) -> str:
    """Converts a string month to number (e.g. 'September' -> '09'.

    You don't need to use this function,
    but you may find it useful.

    arguments:
        month_name (str) : month name
    returns:
        month_number (str) : month number as zero-padded string
    """
    # If already digit do nothing
    if s.isdigit():
        return zero_pad(str(s))

    # Iterate through the list of month names
    for i in range(len(month_names)):
        # If the month name passed as the argument is equal to one of the elements of the list of month names
        # We return a zero-padded string. The function zero_pad only zero-pads a number if it is bigger than 9
        if month_names[i].lower() == s.lower():
            return zero_pad(str(i+1))
    
    return "N/A"

def zero_pad(n: str):
    """zero-pad a number string

    turns '2' into '02'

    You don't need to use this function,
    but you may find it useful.
    """
    # We return a zero-padded string. The function zero_pad only zero-pads a number if it is bigger than 9
    m = n.zfill(2)
    return m


def find_dates(text: str, output: str = None) -> list:
    """Finds all dates in a text using reg ex

    arguments:
        text (string): A string containing html text from a website
    return:
        results (list): A list with all the dates found
    """
   # year, month, day = get_date_patterns()

    # Regex patterns for all months
    # 1. check whether month starts with big og small letter
    # 2. check if string contains whether the month name is shortend or the whole month name
    jan = r'\b[jJ]an(?:uary)?\b'
    feb = r'\b[fF]eb(?:ruary)?\b'
    mar = r'\b[mM]ar(?:ch)?\b'
    apr = r'\b[aA]pr(?:il)?\b'
    may = r'\b[mM]ay(?:ay)?\b'
    jun = r'\b[jJ]un(?:e)?\b'
    jul = r'\b[jJ]ul(?:y)?\b'
    aug = r'\b[aA]ug(?:ust)?\b'
    sep = r'\b[sS]ep(?:tember)?\b'
    okt = r'\b[oO]ct(?:ober)?\b'
    nov = r'\b[nN]ov(?:ember)?\b'
    dec = r'\b[dD]ec(?:ember)?\b'

    # Put all patterns in one variable to check if text contains either of the regex patterns
    months = rf'(?:{jan}|{feb}|{mar}|{apr}|{may}|{jun}|{jul}|{aug}|{sep}|{okt}|{nov}|{dec})'

    # Pattern for year - contains four digits between 0-9
    year = r'[0-9]{4}'
    # Pattern for year - contains either one or two digits between 0-9
    day = r'[0-9]{1,2}'

    # Month-pattern for dates in ISO-format - month can either be 0-(digit) or 1 (digit between 0 to 2)
    iso_month_format = r'(?:0\d|1[0-2])'
    #iso_day_format = r'\b(?:0\d|1[0-2])\b'

    # Date on format YYYY/MM/DD - ISO
    iso = rf"{year}-{iso_month_format}-{day}"

    # Date on format DD/MM/YYYY - DMY
    dmy = rf"{day}\s{months}\s{year}"

    # Date on format MM/DD/YYYY - MDY
    mdy = rf"{months}\s{day},\s{year}"  #MÅ LEGGE TIL KOMMA

    # Date on format YYYY/MM/DD - YMD
    ymd = rf"{year}\s{months}\s{day}"

    # list with all supported formats
    #formats = ...
    
    #the returned dates of year/month/day format
    dates = [] 

    # find all dates in with ISO-format in text
    print("\nISO: ")
    for date in re.findall(rf"{iso}", text):
        #YYYY/MM/DD
        # Subsitutes the order of year, month and day with " / " between each element
        date = re.sub(rf"({year})-({iso_month_format})-({day})", r"\1/\2/\3", date)
        print(date)
        date = date.split("/")
        newDate = date[0]+"/"+date[1]+"/"+date[2]
        dates.append(newDate)

    # find all dates in with DMY-format in text
    print("\nDMY: ")
    for date in re.findall(rf"{dmy}", text):
        #YYYY/MM/DD
        # Subsitutes the order of year, month and day with " / " between each element
        date = re.sub(rf"({day})\s({months})\s({year})", r"\3/\2/\1", date)
        print(date)
        # Splits the match with backslash
        date = date.split("/")
        # 1. Convert month to digit
        date[1] = convert_month(date[1])
        # 2. Zero pads days
        date[2] = zero_pad(date[2])

        # Adds the new converted date format to a new variable and appends it to the list of dates in YYYY/MM/DD format
        newDate = date[0]+"/"+date[1]+"/"+date[2]     
        dates.append(newDate)
    
    # find all dates in with MDY-format in text
    print("\nMDY: ")
    for date in re.findall(rf"{mdy}", text):
        #YYYY/MM/DD
        # Subsitutes the order of year, month and day with " / " between each element
        date = re.sub(rf"({months})\s({day}),\s({year})", r"\3/\1/\2", date)
        print(date)
        # Splits the match with backslash
        date = date.split("/")
        # 1. Convert month to digit
        date[1] = convert_month(date[1])
        # 2. Zero pads days
        date[2] = zero_pad(date[2])

        # Adds the new converted date format to a new variable and appends it to the list of dates in YYYY/MM/DD format
        newDate = date[0]+"/"+date[1]+"/"+date[2]           
        dates.append(newDate)

    # find all dates in with YMD-format in text
    print("\nYMD: ")
    for date in re.findall(rf"{ymd}", text):
        #YYYY/MM/DD
        # Subsitutes the order of year, month and day with " / " between each element
        date = re.sub(rf"({year})\s({months})\s({day})", r"\1/\2/\3", date)
        print(date)

        # Splits the match with backslash
        date = date.split("/")
        # 1. Convert month to digit
        date[1] = convert_month(date[1])
        # 2. Zero pads days
        date[2] = zero_pad(date[2])

        # Adds the new converted date format to a new variable and appends it to the list of dates in YYYY/MM/DD format
        newDate = date[0]+"/"+date[1]+"/"+date[2]           
        dates.append(newDate)       

    # Write to file if wanted
    if output:
        print(f"Writing to: {output}")
        output_file = open(output, "w")
        output_file.write(dates)
        output_file.close()

    return dates

