<h1> Web scraping tool</h1>

This is a web scraping tool for getting the html code that makes up a website, parse through it for relevant information and display the results.

This program conists of different functionalities:

- requesting_urls.py --> makes requests for a url from a given website
- filter_urls.py --> receives an html string and returns a list of all urls found in the text
- collect_dates.py --> receives an html string and returns a list of all dates found in the text in the format YYYY/MM/DD
- time_planner.py --> parse an html file and extracts the datetime objects representing the event for skiing season
- fetch_player_statistics.py --> script which visits the 2022 NBA playoffs website on wikipedia, collects, and plots some player statistics

<h3> Usage </h3>

To run the script you can either run each file with the required arguments or you can run each file by running the following command in the terminal:

```bash
pytest -vv tests
```

or 

```bash
pytest -vv [name of testfile]
```

<h3>Required dependencies and packages</h3>

The required packages are:

- Requests
- BeautifulSoup4

```requests``` can be installed with pip or conda:

```bash
python3 -m pip install requests
```
```beautifulsoup4``` can be installed with pip or conda:

```bash
python3 -m pip install beautifulsoup4
```

<h3>Tests</h3>

You can check that your tests pass by using the testing framework ```pytest``` in the terminal. To run all test run:

```bash
pytest -vv tests
```
