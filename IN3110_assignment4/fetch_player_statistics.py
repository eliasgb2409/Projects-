import os
import re
from operator import itemgetter
from typing import Dict, List
from urllib.parse import urljoin
from webbrowser import get

import numpy as np
from bs4 import BeautifulSoup
from matplotlib import pyplot as plt
from requesting_urls import get_html

## --- Task 8, 9 and 10 --- ##

try:
    import requests_cache
except ImportError:
    print("install requests_cache to improve performance")
    pass
else:
    requests_cache.install_cache()

base_url = "https://en.wikipedia.org"


def find_best_players(url: str) -> None:
    """Find the best players in the semifinals of the nba.

    This is the top 3 scorers from every team in semifinals.
    Displays plot over points, assists, rebounds

    arguments:
        - html (str) : html string from wiki basketball
    returns:
        - None
    """
    # gets the teams
    teams = get_teams(url)
    #print(teams)
    
    # Gets the player for every team and stores in dict (get_players)
    all_players = {}
    
    for dict in teams:
        all_players[dict["name"]] = get_players(dict["url"])

    # If a player doesnt have registered stats we assign these values
    null_data = {"points": 0.0, "rebounds": 0.0, "assists": 0.0}
    
    # Iterate thorugh the every team and player
    # For every player in a team we get stats (ppg, rpg, apg)
    for team, players in all_players.items():
        #print(all_players[team])
        for players in all_players[team]:
            player_stats = get_player_stats(players["url"], team)
            if not player_stats:
                print("---IKKE DATA----")
                players.update(null_data)
  
            players.update(player_stats)
    
    # at this point, we should have a dict of the form:
    # {
    #     "team name": [
    #         {
    #             "name": "player name",
    #             "url": "https://player_url",
    #             # added by get_player_stats
    #             "points": 5,
    #             "assists": 1.2,
    #             # ...,
    #         },
    #     ]
    # }

    # Select top 3 for each team by points:
    best = {}
    #top_stat = ...
    for team, players in all_players.items():
        # Sort and extract top 3 based on points
        top_3 = []
        # Sort players stats for points and add the top 3 players for each team to the dict best{}
        best_players = all_players[team]
        best_players.sort(key=itemgetter('points'))
        top_3.append(best_players[-1])
        top_3.append(best_players[-2])
        top_3.append(best_players[-3])
        best[team] = top_3

    print(best)
    # Other stats to plot in graph
    stats_to_plot = ['points', 'rebounds', 'assists']
    for stat in stats_to_plot:
        plot_best(best, stat=stat)


# Colors for each team in graph
colors = {
    
    "Miami": "red",
    "Phoenix": "orange",
    "Memphis": "blue",
    "Golden State":"yellow",
    "Philadelphia": "cyan",  
    "Boston": "green",
    "Milwaukee": "black",
    "Dallas": "purple"
}

def plot_best(best: Dict[str, List[Dict]], stat: str = "points") -> None:
    """Plots a single stat for the top 3 players from every team.

    Arguments:
        best (dict) : dict with the top 3 players from every team
            has the form:

            {
                "team name": [
                    {
                        "name": "player name",
                        "points": 5,
                        ...
                    },
                ],
            }

            where the _keys_ are the team name,
            and the _values_ are lists of length 3,
            containing dictionaries about each player,
            with their name and stats.

        stat (str) : [points | assists | rebounds] which stat to plot.
            Should be a key in the player info dictionary.
    """
    
    """Plot NBA player statistics. In this case, just points"""
    
    stats_dir = "NBA_player_statistics"
    count_so_far = 0
    all_names = []

    # iterate through each team and the
    for team, players in best.items():
        # pick the color for the team, from the table above
        #color = color_table["b"]
        color = colors[team] #"black"
        # collect the points and name of each player on the team
        # you'll want to repeat with other stats as well
        points = []
        #assists = []
        #rebounds = []
        names = []
        for player in players:
            names.append(player["name"])
            points.append(player[stat])
            #rebounds.append(player["rebounds"])
            #assists.append(player["assists"])
        # record all the names, for use later in x label
        all_names.extend(names)

        # the position of bars is shifted by the number of players so far
        x = range(count_so_far, count_so_far + len(players))
        count_so_far += len(players)
        # make bars for this team's players points,
        # with the team name as the label
        bars = plt.bar(x, points, color=color, label=team)
        # add the value as text on the bars
        plt.bar_label(bars)

    # use the names, rotated 90 degrees as the labels for the bars
    plt.xticks(range(len(all_names)), all_names, rotation=90)
    # add the legend with the colors  for each team
    plt.legend(loc=0)
    # turn off gridlines
    plt.grid(False)
    # set the title
    plt.title(f"{stat} per game")
    # save the figure to a file
    filename = f"{stat}.png"
    os.makedirs(stats_dir, exist_ok=True)
    plt.savefig(f"{stats_dir}/{filename}")
    print(f"Creating {filename}")
    #plt.show()
    #os.path.join(stats_dir, filename)
    plt.clf()


def get_teams(url: str) -> list:
    """Extracts all the teams that were in the semi finals in nba

    arguments:
        - url (str) : url of the nba finals wikipedia page
    returns:
        teams (list) : list with all teams
            Each team is a dictionary of {'name': team name, 'url': team page
    """
    # Get the table
    html = get_html(url)
    soup = BeautifulSoup(html, "html.parser")
    table = soup.find(id="Bracket").find_next("table")

    # find all rows in table
    rows = table.find_all("tr")
    rows = rows[2:]
    #print("ROWS IN GET TEAM: ", rows)
    # maybe useful: identify cells that look like 'E1' or 'W5', etc.
    seed_pattern = re.compile(r"^[EW][1-8]$")

    # lots of ways to do this,
    # but one way is to build a set of team names in the semifinal
    # and a dict of {team name: team url}

    team_links = {}  # dict of team name: team url
    in_semifinal = set()  # set of teams in the semifinal

    # Loop over every row and extract teams from semi finals
    # also locate the links tot he team pages from the First Round column
    for row in rows:
        cols = row.find_all("td")
        # useful for showing structure
        # print([c.get_text(strip=True) for c in cols])

        # TODO:
        # 1. if First Round column, record team link from `a` tag
        # 2. if semifinal column, record team name

        # quarterfinal, E1/W8 is in column 1
        # team name, link is in column 2
        if len(cols) >= 3 and seed_pattern.match(cols[1].get_text(strip=True)):
            team_col = cols[2]
            #print("TEAM COL[2]: ", team_col.get_text(strip=True), "\n")
            a = team_col.find("a")
            team_links[team_col.get_text(strip=True)] = urljoin(base_url, a["href"])

        elif len(cols) >= 4 and seed_pattern.match(cols[2].get_text(strip=True)):
            team_col = cols[3]
            #print("TEAM COL[3]: ", team_col.get_text(strip=True), "\n")
            in_semifinal.add(team_col.get_text(strip=True))

        elif len(cols) >= 5 and seed_pattern.match(cols[3].get_text(strip=True)):
            team_col = cols[4]
            #print("TEAM COL[4]: ", team_col.get_text(strip=True), "\n")
            in_semifinal.add(team_col.get_text(strip=True))

    # return list of dicts (there will be 8):
    # [
    #     {
    #         "name": "team name",
    #         "url": "https://team url",
    #     }
    # ]

    assert len(in_semifinal) == 8
    return [
        {
            "name": team_name.rstrip("*"),
            "url": team_links[team_name],
        }
        for team_name in in_semifinal
    ]


def get_players(team_url: str) -> list:
    """Gets all the players from a team that were in the roster for semi finals
    arguments:
        team_url (str) : the url for the team
    returns:
        player_infos (list) : list of player info dictionaries
            with form: {'name': player name, 'url': player wikipedia page url}
    """
    print(f"Finding players in {team_url}")

    # Get the table
    html = get_html(team_url)
    soup = BeautifulSoup(html, "html.parser")
    table = soup.find(id="Roster").find_next("table")

    # List of players for team
    players = []
    # Loop over every row and get the names from roster
    rows = table.find_all("tr")
    rows = rows[1:]
    for row in rows:
        # Get the columns
        cols = row.find_all("td")
        #values = [td.get_text(strip=True) for td in cols]
        
        # 1. Find the column for players
        # 2. Find a tags in the columns
        # 3. Get the url for each player and name of player in the a-tags
        if len(cols) >= 7:
            player_col = cols[2]
            a = player_col.find("a")
            
            if a: 
                href = a.get("href")
                name = a.text   # here we get the value between the tags e.g. <a href="blabla"> Value <\a>
                #newName = re.sub(r'\s+\(.*\)', "", name)
                player_url = urljoin(base_url, href)  
                # and add to players a dict with       
                player_links = {"name": name, "url": player_url}
                players.append(player_links)
    
    # return list of players
    
    return players


def get_player_stats(player_url: str, team: str) -> dict:
    """Gets the player stats for a player in a given team
    arguments:
        player_url (str) : url for the wiki page of player
        team (str) : the name of the team the player plays for
    returns:
        stats (dict) : dictionary with the keys (at least): points, assists, and rebounds keys
    """
    print(f"Fetching stats for player in {player_url}")

    # Get the table with stats    
    html = get_html(player_url)
    soup = BeautifulSoup(html, "html.parser")
    table = soup.find(id="Regular_season")
    
    # If table id is not Regular_season 
    if table is not None:
        table = table.find_next("table")
    else:
        table = soup.find(id="NBA").find_next("table")
    #print(table)
    
    stats = {}

    rows = table.find_all("tr")
    
    #colomuns = []

    # Loop over rows and extract the stats
    for row in rows:
        cols = row.find_all("td")
        
        #This is if rowspan is more than 1, meaning that the player has transfered teams during the season
        if len(cols) == 12: 
            data = cols[0]
            # Find a tags
            a = data.find("a")
            if a:
                # get the right team in the 2021-22 season if player is transfered                
                pattern = re.compile(r'2021.22 ' + re.escape(team))
                match = pattern.search(str(a))
                #print(match)
                # If there is a match we get the ppg, rpg and apg values
                # If the values contain a * in the end, we strip the value so we ignore " * "
                if match:
                    ppg = cols[-1].get_text(strip=True)
                    if "*" in ppg:
                        ppg = ppg[:-1]
                    rpg = cols[7].get_text(strip=True)
                    if "*" in rpg:
                        rpg = rpg[:-1]
                    apg = cols[8].get_text(strip=True)
                    if "*" in apg:
                        apg = apg[:-1]
                    
                    # Add data for stats
                    stats = {"points":float(ppg), "rebounds": float(rpg), "assists":float(apg)}
        
        # We do the same here, but this time the player has not been transfered during the 2021-22 season            
        if len(cols) == 13:
            data = cols[1]
            a = data.find("a")
            if a:
                #pattern = re.compile(r'.+title="(2021.22)' + re.escape(team))
                pattern = re.compile(r'2021.22 ' + re.escape(team))
                match = pattern.search(str(a))
                if match:
                    ppg = cols[-1].get_text(strip=True)
                    if "*" in ppg:
                        ppg = ppg[:-1]
                    rpg = cols[8].get_text(strip=True)
                    if "*" in rpg:
                        rpg = rpg[:-1]
                    apg = cols[9].get_text(strip=True)
                    if "*" in apg:
                        apg = apg[:-1]
                    
                    stats = {"points":float(ppg), "rebounds": float(rpg), "assists":float(apg)}
            
        # Check correct team (some players change team within season)
        

        # load stats from columns
        # keys should be 'points', 'assists', etc.
        

    return stats


# run the whole thing if called as a script, for quick testing
if __name__ == "__main__":
    url = "https://en.wikipedia.org/wiki/2022_NBA_playoffs"
    find_best_players(url)
