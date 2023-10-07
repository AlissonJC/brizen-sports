from hockey_database import hockey_collection
import os
import flag
import emoji
from handicap import *
import subprocess

likelihood = 0.62

def get_competition():

    competition = input("Type the competition: ").lower()

    check = ""

    for game in hockey_collection.find():
        if competition == game["competition"]:
            check = "Found."
            return competition
    
    if check == "":
        print(f"{competition.upper()} not found in Brizen Database.\n")
        return get_competition()
        
def get_home_team(competition):

    home = input("Type the home team: ").lower()

    check = ""

    for game in hockey_collection.find({"competition": competition}):
        if game["home"] == home or game["away"] == home:
            check = "Found."
            return home

    if check == "":
        print(f"{home.upper()} not found in Brizen Database in {competition.upper()}.\n")
        return get_home_team(competition)

def get_away_team(competition):

    away = input("Type the away team: ").lower()

    check = ""

    for game in hockey_collection.find({"competition": competition}):
        if game["home"] == away or game["away"] == away:
            check = "Found."
            return away

    if check == "":
        print(f"{away.upper()} not found in Brizen Database in {competition.upper()}.\n")
        return get_away_team(competition)


def handicap(competition, home, handicap_home):

    home_win, home_void, home_lost, games_home = team_handicap_in_competition(competition, home, handicap_home)

    odds_home = 0
    flag_home = 0

    if games_home >= 1:
        if (home_win + home_void) >= likelihood:
            flag_home = 1
            odds_home = (home_win + home_void)

    if flag_home == 1:
        print(f"{home}")
        return odds_home, handicap_home, home
    elif flag_home == 0:
        return 0, 0, None


def flags(competition):
    country = competition.split("-")

    flags = {
        "czechia": "CZ",
        "finland": "FI",
        "germany": "DE",
        "russia": "RU",
        "sweden": "SE",
        "usa": "US",
        "slovakia": "SK",
        "austria": "AT",
        "switzerland": "CH",
        "denmark": "DK",
        "belarus": "BY",
        "canada": "CA"
    }

    country_name = flag.flagize(f":{flags[country[0]]}:", subregions=True)
    return f"{country[0].upper()} {country_name} {emoji.emojize(':ice_hockey:')}\n"


def calculator(handicap_found, handicap_home, team):

    if handicap_found == 0:
        os.system("clear")
        exit()
    odd = float(input(emoji.emojize(":chart_increasing: Odd: ")))
    minimal = odd - (odd * 0.1)
    print_odd = emoji.emojize(":chart_increasing: Odd: ") + str(odd) + "\n" + emoji.emojize(f":chart_decreasing: Min: {minimal:.4}")
    print_stake = emoji.emojize(":heavy_dollar_sign:Stake: 1u")
    sign = ""
    if handicap_home >= 0:
        sign = "+"
        print(f"**{team.title()} {sign}{handicap_home}**\n")
        event_home = f"**{team.title()} {sign}{handicap_home}**\n"
        return event_home, print_odd, print_stake
    else:
        print(f"**{team.title()} {handicap_home}**\n")
        event_away = f"**{team.title()} {handicap_home}**\n"
        return event_away, print_odd, print_stake

try:
    competition = get_competition()
    home = get_home_team(competition)
    away = get_away_team(competition)
    handicap_home = float(input("Type the handicap line for the home team: "))
    os.system("clear")
    flag_choice = flags(competition)
    event_title = f"{home.title()} — {away.title()}\n"
    handicap_found, handicap_home, team = handicap(competition, home, away, handicap_home)
    event, print_odd, print_stake = calculator(handicap_found, handicap_home, team)
    data = flag_choice + "\n" + event_title + "\n" + event + "\n" + print_odd + "\n" + print_stake
    subprocess.run("pbcopy", universal_newlines=True, input=data)
    os.system("clear")
except KeyboardInterrupt:
    print("\n\nService terminated by user.")

