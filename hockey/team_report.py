from hockey_database import hockey_collection
import os

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

def goals_in_competition(competition, team):
    games_home = 0
    games_away = 0
    goals_scored_home = 0
    goals_scored_away = 0
    goals_conceded_home = 0
    goals_conceded_away = 0

    for game in hockey_collection.find({"competition": competition, "home": team}):
        games_home += 1
        goals_scored_home += game["home_ft"]
        goals_conceded_home += game["away_ft"]

    for game in hockey_collection.find({"competition": competition, "away": team}):
        games_away += 1
        goals_scored_away += game["away_ft"]
        goals_conceded_away += game["home_ft"]

    print(f"Average goals scored home: {goals_scored_home/games_home:.2}")
    print(f"Average goals conceded home: {goals_conceded_home/games_home:.2}")
    print(f"Average goals scored away: {goals_scored_away/games_away:.2}")
    print(f"Average goals conceded away: {goals_conceded_away/games_away:.2}")


def team_average_spread(competition, team, spread):
    games_home = 0
    games_away = 0

    #WHEN TEAM PLAYS AT HOME
    win_home = 0
    void_home = 0
    lost_home = 0

    #WHEN TEAM PLAYS AWAY
    win_away = 0
    void_away = 0
    lost_away = 0

    for game in hockey_collection.find({"competition": competition, "home": team}):
        games_home += 1
        if game["home_ft"] + spread > game["away_ft"]:
            win_home += 1
        elif game["home_ft"] + spread == game["away_ft"]:
            void_home += 1
        else:
            lost_home += 1
    
    for game in hockey_collection.find({"competition": competition, "away": team}):
        games_away += 1
        if game["home_ft"] < game["away_ft"] + spread:
            win_away += 1
        elif game["home_ft"] == game["away_ft"] + spread:
            void_away += 1
        else:
            lost_away += 1

    print("\n")
    print(f"{team.upper()} playing home Handicap {spread}:")
    print(f"WIN {win_home/games_home*100:.4}%")
    print(f"VOID {void_home/games_home*100:.4}%")
    print(f"LOST {lost_home/games_home*100:.4}%\n")

    print(f"{team.upper()} playing away Handicap {spread}:")
    print(f"WIN {win_away/games_away*100:.4}%")
    print(f"VOID {void_away/games_away*100:.4}%")
    print(f"LOST {lost_away/games_away*100:.4}%")
    
    
    


competition = get_competition()
team = get_home_team(competition)
os.system("clear")
goals_in_competition(competition, team)
team_average_spread(competition, team, spread=0)
# team_average_spread(competition, team, spread=-0.5)
# team_average_spread(competition, team, spread=-1)