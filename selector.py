# Input: home team, away team, competition
# Output: Best bet to place
import os
import flag
import emoji
from brizen_database import brizen_collection
from handicap import team_handicap_as_home
import subprocess


likelihood = 0.6

def get_competition():
    competition = input("Type the competition: ").lower()

    check = ""

    for game in brizen_collection.find():
        if competition == game["competition"]:
            check = "Found."
            return competition

    if check == "":
        print(f"{competition.upper()} not found in Brizen Database.\n")
        return get_competition()

def get_home_team(competition):

    home = input("Type the home team: ").lower()

    check = ""

    for game in brizen_collection.find({"competition": competition}):
        if game["home"] == home or game["away"] == home:
            check = "Found."
            return home

    if check == "":
        print(f"{home.upper()} not found in Brizen Database in {competition.upper()}.\n")
        return get_home_team(competition)

def get_away_team(competition):

    away = input("Type the away team: ").lower()

    check = ""

    for game in brizen_collection.find({"competition": competition}):
        if game["home"] == away or game["away"] == away:
            check = "Found."
            return away

    if check == "":
        print(f"{away.upper()} not found in Brizen Database in {competition.upper()}.\n")
        return get_away_team(competition)

def handicap(competition, home, handicap_home):
    
    home_win, home_void, home_lost, games_home = team_handicap_as_home(competition, home, handicap_home)

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
        print(f"*{team.title()} {sign}{handicap_home}*\n")
        event_home = f"**{team.title()} {sign}{handicap_home}**\n"
        return event_home, print_odd, print_stake
    else:
        print(f"*{team.title()} {handicap_home}*\n")
        event_away = f"**{team.title()} {handicap_home}**\n"
        return event_away, print_odd, print_stake

def get_values():

    handicap_home = float(input("Type the handicap line for the home team: "))

    handicap_home_string = str(handicap_home)

    if handicap_home < 0 and handicap_home_string[:-2] == 25:
            handicap_home -= 0.25
    elif handicap_home < 0 and handicap_home_string[:-2] == 75:
            handicap_home += 0.25
    elif handicap_home > 0 and handicap_home_string[:-2] == 25:
            handicap_home += 0.25
    elif handicap_home > 0 and handicap_home_string[:-2] == 75:
            handicap_home -= 0.25

    return handicap_home


def flags(competition):
    country = competition.split("-")

    flags = {
        "euro": "EU",
        "brazil": "BR",
        "england": "GB",
        "france": "FR",
        "germany": "DE",
        "italy": "IT",
        "mexico": "MX",
        "netherlands": "NL",
        "portugal": "PT",
        "russia": "RU",
        "spain": "ES",
        "turkey": "TR",
        "usa": "US",
        "romania": "RO",
        "poland": "PL",
        "serbia": "RS",
        "slovakia": "SK",
        "bulgaria": "BG",
        "argentina": "AR",
        "denmark": "DK",
        "sweden": "SE",
        "israel": "IL",
        "ecuador": "EC",
        "colombia": "CO",
        "bolivia": "BO",
        "costarica": "CR",
        "uruguay": "UY",
        "australia": "AU",
        "estonia": "EE",
        "paraguay": "PY",
        "venezuela": "VE",
        "czechrepublic": "CZ",
        "croatia": "HR",
        "hungary": "HU",
        "ireland": "IE",
        "peru": "PE",
        "chile": "CL",
        "japan": "JP",
        "korea": "KR",
        "belgium": "BE",
        "finland": "FI",
        "iceland": "IS",
        "norway": "NO",
        "saudiarabia": "SA",
        "slovenia": "SI",
        "belarus": "BY",
        "czechia": "CZ",
        "switzerland": "CH",
        "austria": "AT",
        "scotland": "GB-SCT",
        "greece": "GR",
        "qatar": "QA",
        "ukraine":"UA",
        "lithuania": "LT"
    }

    country_name = flag.flagize(f":{flags[country[0]]}:", subregions=True)
    return f"{country[0].upper()} {country_name}\n"

try:
    competition = get_competition()
    home = get_home_team(competition)
    away = get_away_team(competition)
    handicap_home = get_values()
    os.system("clear")
    flag_choice = flags(competition)
    event_title = f"{home.title()} — {away.title()}\n"
    handicap_found, handicap_home, team = handicap(competition, home, handicap_home)
    event, print_odd, print_stake = calculator(handicap_found, handicap_home, team)
    data = flag_choice + "\n" + event_title + "\n" + event + "\n" + print_odd + "\n" + print_stake
    subprocess.run("pbcopy", universal_newlines=True, input=data)
    os.system("clear")
except KeyboardInterrupt:
    print("\n\nService terminated by user.")