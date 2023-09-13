from hockey_database import hockey_collection

def team_handicap_in_competition(competition, team, spread):
    games = 0
    win = 0
    void = 0
    lost = 0

    for game in hockey_collection.find({"competition": competition}):
        if game["home"] == team:
            games += 1
            if game["home_ft"] + spread > game["away_ft"]:
                win += 1
            elif game["home_ft"] + spread == game["away_ft"]:
                void += 1
            else:
                lost += 1

        if game["away"] == team:
            games += 1
            if game["away_ft"] + spread > game["home_ft"]:
                win += 1
            elif game["away_ft"] + spread == game["home_ft"]:
                void += 1
            else:
                lost += 1

    if games == 0:
        games = 1

    return win / games, void / games, lost / games, games

def team_handicap_as_home(competition, team, spread):
    games = 0
    win = 0
    void = 0
    lost = 0

    for game in hockey_collection.find({"competition": competition}):
        if game["home"] == team:
            games += 1
            if game["home_ft"] + spread > game["away_ft"]:
                win += 1
            elif game["home_ft"] + spread == game["away_ft"]:
                void += 1
            else:
                lost += 1
    
    if games == 0:
        games = 1

    return win/games, void/games, lost/games, games

def team_handicap_as_away(competition, team, spread):
    games = 0
    win = 0
    void = 0
    lost = 0

    for game in hockey_collection.find({"competition": competition}):
        if game["away"] == team:
            games += 1
            if game["away_ft"] + spread > game["home_ft"]:
                win += 1
            elif game["away_ft"] + spread == game["home_ft"]:
                void += 1
            else:
                lost += 1

    if games == 0:
        games = 1

    return win/games, void/games, lost/games, games