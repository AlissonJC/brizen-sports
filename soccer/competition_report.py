from soccer_database import soccer_collection

def get_competition():

    competition = input("Type the competition: ").lower()

    check = ""

    for game in soccer_collection.find():
        if competition == game["competition"]:
            check = "Found."
            return competition
    
    if check == "":
        print(f"{competition.upper()} not found in Brizen Database.\n")
        return get_competition()

def get_home_team(competition):
    home = input("Type the home team: ").lower()

    check = ""

    for game in soccer_collection.find({"competition": competition}):
        if game["home"] == home or game["away"] == home:
            check = "Found."
            return home

    if check == "":
        print(f"{home.upper()} not found in Brizen Database in {competition.upper()}.\n")
        return get_home_team(competition)

def totals_competition(competition):
    games = 0

    goals_sum = 0
    home_goals = 0
    away_goals = 0

    goals = {
        "0": 0,
        "1": 0,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 0,
        "6": 0,
        "7+": 0
    }

    for game in soccer_collection.find({"competition": competition}):
        games += 1
        goals_sum += game["home_ft"] + game["away_ft"]
        home_goals += game["home_ft"]
        away_goals += game["away_ft"]
        if game["home_ft"] + game["away_ft"] == 0:
            goals["0"] += 1
        elif game["home_ft"] + game["away_ft"] == 1:
            goals["1"] += 1
        elif game["home_ft"] + game["away_ft"] == 2:
            goals["2"] += 1
        elif game["home_ft"] + game["away_ft"] == 3:
            goals["3"] += 1
        elif game["home_ft"] + game["away_ft"] == 4:
            goals["4"] += 1
        elif game["home_ft"] + game["away_ft"] == 5:
            goals["5"] += 1
        elif game["home_ft"] + game["away_ft"] == 6:
            goals["6"] += 1
        elif game["home_ft"] + game["away_ft"] >= 7:
            goals["7+"] += 1

    print("")
    print(f"0 gols: {goals['0']} - {goals['0']/games*100:.4}%")
    print(f"1 gols: {goals['1']} - {goals['1']/games*100:.4}%")
    print(f"2 gols: {goals['2']} - {goals['2']/games*100:.4}%")
    print(f"3 gols: {goals['3']} - {goals['3']/games*100:.4}%")
    print(f"4 gols: {goals['4']} - {goals['4']/games*100:.4}%")
    print(f"5 gols: {goals['5']} - {goals['5']/games*100:.4}%")
    print(f"6 gols: {goals['6']} - {goals['6']/games*100:.4}%")
    print(f"7+ gols: {goals['7+']} - {goals['7+']/games*100:.4}%")
        
    print(f"Average: {(goals_sum)/games:.3}")
    print(f"Home Average: {home_goals/games:.3}")
    print(f"Away Average: {away_goals/games:.3}")

def btts(competition):
    games = 0
    btts = 0

    for game in soccer_collection.find({"competition": competition}):
        games += 1
        if game["home_ft"] > 0 and game["away_ft"] > 0:
            btts += 1
    
    print(f"BTTS: {btts/games*100:.4}%")

def all_home_winning():

    competitions = []

    for game in soccer_collection.find({}):
        if game["competition"] in competitions:
            pass
        else:
            competitions.append(game["competition"])

    competitions.sort()

    games = 0
    home = 0
    away = 0
    draw = 0

    for competition in competitions:
        for game in soccer_collection.find({"competition": competition}):
            games += 1
            if game["home_ft"] > game["away_ft"]:
                home += 1
            elif game["home_ft"] < game["away_ft"]:
                away += 1
            else:
                draw += 1
        print(f"{competition.upper()} Home Winning: {home / games * 100:.4}% | Draw: {draw/games*100:.4}% | Away: {away/games*100:.4}%")
        games = 0
        home = 0
        away = 0
        draw = 0

def count_games():
    count = 0
    for game in soccer_collection.find({}):
        count += 1
    print(f"Brizen has now {count} football games.\n")

def all_soccer_average():

    competitions = []

    for game in soccer_collection.find({}):
        if game["competition"] in competitions:
            pass
        else:
            competitions.append(game["competition"])

    competitions.sort()

    games = 0
    home = 0
    away = 0
    draw = 0

    for competition in competitions:
        for game in soccer_collection.find({"competition": competition}):
            games += 1
            if game["home_ft"] > game["away_ft"]:
                home += 1
            elif game["home_ft"] < game["away_ft"]:
                away += 1
            else:
                draw += 1
    print(f"Home Winning: {home / games * 100:.4}%")
    print(f"Away Winning: {away / games * 100:.4}%")
    print(f"Draw: {draw / games * 100:.4}%")
    print(f"Games: {games}")


def competition_soccer_average():

    games = 0
    home = 0
    away = 0
    draw = 0

    for game in soccer_collection.find({"competition": "chile-cup-2019"}):
        games += 1
        if game["home_ft"] > game["away_ft"]:
            home += 1
        elif game["home_ft"] < game["away_ft"]:
            away += 1
        else:
            draw += 1
    print(f"Home Winning: {home / games * 100:.4}%")
    print(f"Away Winning: {away / games * 100:.4}%")
    print(f"Draw: {draw / games * 100:.4}%")
    print(f"Games: {games}")

#competition = get_competition()
#team = get_home_team(competition)
#handicap = float(input("Type the handicap: "))
all_home_winning()
#all_soccer_average()
#competition_soccer_average()