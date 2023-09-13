from soccer_database import soccer_collection

# over and under goals ft stats when team is at home
def over_under_when_team_is_home(competition, team, spread):
    games = 0
    win = 0
    void = 0
    lost = 0

    for game in soccer_collection.find({"competition": competition, "home": team}):
        games += 1
        if game["home_ft"] + game["away_ft"] > spread:
            win += 1
        elif game["home_ft"] + game["away_ft"] == spread:
            void += 1
        else:
            lost += 1

    if games == 0:
        games += 1

    return win/games, void/games, lost/games, games

# over and under goals ft stats when team is away
def over_under_when_team_is_away(competition, team, spread):
    games = 0
    win = 0
    void = 0
    lost = 0

    for game in soccer_collection.find({"competition": competition, "away": team}):
        games += 1
        if game["home_ft"] + game["away_ft"] > spread:
            win += 1
        elif game["home_ft"] + game["away_ft"] == spread:
            void += 1
        else:
            lost += 1

    if games == 0:
        games += 1

    return win/games, void/games, lost/games, games