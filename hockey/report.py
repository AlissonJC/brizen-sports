from hockey_database import hockey_collection


competition = input("Competition: ")

def competition_draws(competition):
    draw = 0
    games = 0

    for game in hockey_collection.find({"competition": competition}):
        games += 1
        if game["home_ft"] == game["away_ft"]:
            draw += 1

    print(f"Draw %: {draw/games*100:.4}%")

def home_spread(competition, team, spread):
    win = 0
    void = 0
    lost = 0
    games = 0

    for game in hockey_collection.find({"competition": competition}):
        if game["home"] == team:
            games += 1
            if game["home_ft"] > game["away_ft"] + spread:
                win += 1
            if game["home_ft"] == game["away_ft"] + spread:
                void += 1
            else:
                lost += 1

    print(f"{team.upper()} in {competition.upper()}")
    print(f"Spread covered %: {(win+void)/games*100:.4}%")

def away_spread(competition, team, spread):
    win = 0
    void = 0
    lost = 0
    games = 0

    for game in hockey_collection.find({"competition": competition}):
        if game["away"] == team:
            games += 1
            if game["home_ft"]  + spread < game["away_ft"]:
                win += 1
            if game["home_ft"]  + spread == game["away_ft"]:
                void += 1
            else:
                lost += 1

    print(f"{team.upper()} in {competition.upper()}")
    print(f"Spread covered %: {(win+void)/games*100:.4}%")

def competition_report(competition):
    games = 0
    goals = 0

    for game in hockey_collection.find({"competition": competition}):
        games += 1
        goals += (game["home_ft"] + game["away_ft"])

    average = goals/games
    
    print(f"Jogos: {games}")
    print(f"Gols: {goals}")
    print(f"Média: {average:.3}")

    over = 0
    under = 0

    for game in hockey_collection.find({"competition": competition}):
        if game["home_ft"] + game["away_ft"] > average:
            over += 1
        if game["home_ft"] + game["away_ft"] < average:
            under += 1
        
    print(f"Over média: {over/games*100:.4}%")
    print(f"Under média: {under/games*100:.4}%")

competition_report(competition)