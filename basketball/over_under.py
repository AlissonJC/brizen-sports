from basketball_database import basketball_collection


# GENERAL OVER AND UNDER

# COMPETITION STATS
# over and under points ft stats about the competition
def over_under_competition(competition, spread):
    games = 0
    win = 0
    void = 0
    lost = 0

    for game in basketball_collection.find({"competition": competition}):
        games += 1
        if game["home_ft"] + game["away_ft"] > spread:
            win += 1
        elif game["home_ft"] + game["away_ft"] == spread:
            void += 1
        else:
            lost += 1

    if games == 0:
        print(f"There are no data for {competition.upper()}.")
    else:
        print(f"Games in {competition.upper()}: {games}.")
        print(f"Over {spread}: {win/games*100:.4}%")
        print(f"Equal {spread}: {void/games*100:.4}%")
        print(f"Under {spread}: {lost/games*100:.4}%")


# TEAM IN THE COMPETITION STATS
# over and under points ft stats in team's matches in competition (home/away)
def over_under_by_team_in_competition(competition, team, spread):
    games = 0
    win = 0
    void = 0
    lost = 0

    for game in basketball_collection.find({"competition": competition}):
        if game["home"] == team or game["away"] == team:
            games += 1
            if game["home_ft"] + game["away_ft"] > spread:
                win += 1
            elif game["home_ft"] + game["away_ft"] == spread:
                void += 1
            else:
                lost += 1

    if games == 0:
        print(f"There are no data for {team.upper()} in {competition.upper()}.")
    else:
        print(f"Games of {team.upper()} in {competition.upper()}: {games}.")
        print(f"Over {spread}: {win/games*100:.4}%")
        print(f"Equal {spread}: {void/games*100:.4}%")
        print(f"Under {spread}: {lost/games*100:.4}%")

# over and under points ft stats when team is at home
def over_under_when_team_is_home(competition, team, spread):
    games = 0
    win = 0
    void = 0
    lost = 0

    for game in basketball_collection.find({"competition": competition, "home": team}):
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

# over and under points ft stats when team is away
def over_under_when_team_is_away(competition, team, spread):
    games = 0
    win = 0
    void = 0
    lost = 0

    for game in basketball_collection.find({"competition": competition, "away": team}):
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

# ONLY BY ONE TEAM
# over and under points ft stats only by the team in competition (home/away)
def over_under_points_by_team_per_game_general(competition, team, spread):
    games = 0
    win = 0
    void = 0
    lost = 0

    for game in basketball_collection.find({"competition": competition}):
        if game["home"] == team:
            games += 1
            if game["home_ft"] > spread:
                win += 1
            elif game["home_ft"] == spread:
                void += 1
            else:
                lost += 1
        
        if game["away"] == team:
            games += 1
            if game["away_ft"] > spread:
                win += 1
            elif game["away_ft"] == spread:
                void += 1
            else:
                lost += 1

    if games == 0:
        print(f"There are no data for {team.upper()} in {competition.upper()}.")
    else:
        print(f"Games of {team.upper()} in {competition.upper()}: {games}.")
        print(f"Over {spread}: {win/games*100:.4}%")
        print(f"Equal {spread}: {void/games*100:.4}%")
        print(f"Under {spread}: {lost/games*100:.4}%")

# over and under only by the team when it is the home team
def over_under_points_by_team_as_home(competition, team, spread):
    games = 0
    win = 0
    void = 0
    lost = 0

    for game in basketball_collection.find({"competition": competition, "home": team}):
        games += 1
        if game["home_ft"] > spread:
            win += 1
        elif game["home_ft"] == spread:
            void += 1
        else:
            lost += 1

    if games == 0:
        games += 1

    return win/games, void/games, lost/games

# over and under only by the team when it is the away team
def over_under_points_by_team_as_visitor(competition, team, spread):
    games = 0
    win = 0
    void = 0
    lost = 0

    for game in basketball_collection.find({"competition": competition, "away": team}):
        games += 1
        if game["away_ft"] > spread:
            win += 1
        elif game["away_ft"] == spread:
            void += 1
        else:
            lost += 1

    if games == 0:
        games += 1

    return win/games, void/games, lost/games

# CONCEDED
# over and under points conceded only by the team in general (home/away)
def over_under_points_conceded_by_team_per_game_general(competition, team, spread):
    games = 0
    win = 0
    void = 0
    lost = 0

    for game in basketball_collection.find({"competition": competition}):
        if game["home"] == team:
            games += 1
            if game["away_ft"] > spread:
                win += 1
            elif game["away_ft"] == spread:
                void += 1
            else:
                lost += 1
        
        if game["away"] == team:
            games += 1
            if game["home_ft"] > spread:
                win += 1
            elif game["home_ft"] == spread:
                void += 1
            else:
                lost += 1

    if games == 0:
        games += 1

    return win/games, void/games, lost/games

# over and under points conceded only by the team when it is the home team
def over_under_points_conceded_by_team_as_home(competition, team, spread):
    games = 0
    win = 0
    void = 0
    lost = 0

    for game in basketball_collection.find({"competition": competition, "home": team}):
        games += 1
        if game["away_ft"] > spread:
            win += 1
        elif game["away_ft"] == spread:
            void += 1
        else:
            lost += 1

    if games == 0:
        games += 1

    return win/games, void/games, lost/games

# over and under points conceded only by the team when it is the away team
def over_under_points_conceded_by_team_as_visitor(competition, team, spread):
    games = 0
    win = 0
    void = 0
    lost = 0

    for game in basketball_collection.find({"competition": competition, "away": team}):
        games += 1
        if game["home_ft"] > spread:
            win += 1
        elif game["home_ft"] == spread:
            void += 1
        else:
            lost += 1

    if games == 0:
        games += 1

    return win/games, void/games, lost/games

