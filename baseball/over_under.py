from baseball_database import baseball_collection


# Average in Competition
def average_in_competition(competition):
    games = 0
    runs = 0

    for game in baseball_collection.find({"competition": competition}):
        games += 1
        runs += (game["home_ft"] + game["away_ft"])

    return (runs / games)

# Average in Competition for Given Home Team
def average_in_competition_home(competition, home):
    games = 0
    runs = 0

    for game in baseball_collection.find({"competition": competition, "home": home}):
        games += 1
        runs += (game["home_ft"] + game["away_ft"])

    return (runs / games)

# Average in Competition for Given Home Team
def average_in_competition_away(competition, away):
    games = 0
    runs = 0

    for game in baseball_collection.find({"competition": competition, "away": away}):
        games += 1
        runs += (game["home_ft"] + game["away_ft"])

    return (runs / games)

    #print(f"Average in Competition for {away} as away team: {(runs/games):.2}")

# Over/Under FT in Competition
def totals_in_competition(competition, spread):
    games = 0
    over = 0
    push = 0
    under = 0

    for game in baseball_collection.find({"competition": competition}):
        games += 1
        if game["home_ft"] + game["away_ft"] > spread:
            over += 1
        elif game["home_ft"] + game["away_ft"] == spread:
            push += 1
        else:
            under += 1
    
    return over/games, push/games, under/games

def average_scored_home(competition, home):
    games = 0
    runs = 0

    for game in baseball_collection.find({"competition": competition, "home": home}):
        games += 1
        runs += game["home_ft"]

    return runs / games

def average_conceded_home(competition, home):
    games = 0
    runs = 0

    for game in baseball_collection.find({"competition": competition, "home": home}):
        games += 1
        runs += game["away_ft"]

    return runs / games

def average_scored_away(competition, away):
    games = 0
    runs = 0

    for game in baseball_collection.find({"competition": competition, "away": away}):
        games += 1
        runs += game["away_ft"]

    return runs / games

def average_conceded_away(competition, away):
    games = 0
    runs = 0

    for game in baseball_collection.find({"competition": competition, "away": away}):
        games += 1
        runs += game["home_ft"]

    return runs / games



