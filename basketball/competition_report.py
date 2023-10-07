from basketball_database import basketball_collection


def get_competition():
    competition = input("Type the competition: ").lower()

    check = ""

    for game in basketball_collection.find():
        if competition == game["competition"]:
            check = "Found."
            return competition

    if check == "":
        print(f"{competition.upper()} not found in Brizen Database.\n")
        return get_competition()


def get_home_team(competition):

    home = input("Type the home team: ").lower()

    check = ""

    for game in basketball_collection.find({"competition": competition}):
        if game["home"] == home or game["away"] == home:
            check = "Found."
            return home

    if check == "":
        print(f"{home.upper()} not found in Brizen Database in {competition.upper()}.\n")
        return get_home_team(competition)


def totals_competition(competition):
    games = 0

    points_sum = 0
    home_points = 0
    away_points = 0

    points = {
        "200/-200": 0,
        "201 - 210": 0,
        "211 - 220": 0,
        "221 - 230": 0,
        "231 - 240": 0,
        "241 - 250": 0,
        "250+": 0,
    }

    for game in basketball_collection.find({"competition": competition}):
        games += 1
        points_sum += game["home_ft"] + game["away_ft"]
        home_points += game["home_ft"]
        away_points += game["away_ft"]
        if game["home_ft"] + game["away_ft"] <= 200:
            points["200/-200"] += 1
        elif 201 >= game["home_ft"] + game["away_ft"] <= 210:
            points["201 - 210"] += 1
        elif 211 >= game["home_ft"] + game["away_ft"] <= 220:
            points["211 - 220"] += 1
        elif 221 >= game["home_ft"] + game["away_ft"] <= 230:
            points["221 - 230"] += 1
        elif 231 >= game["home_ft"] + game["away_ft"] <= 240:
            points["231 - 240"] += 1
        elif 241 >= game["home_ft"] + game["away_ft"] <= 250:
            points["241 - 250"] += 1
        elif game["home_ft"] + game["away_ft"] >= 251:
            points["250+"] += 1

    print("")
    print(f"200/-200 pontos: {points['200/-200']} - {points['200/-200'] / games * 100:.4}%")
    print(f"201 - 210 pontos: {points['201 - 210']} - {points['201 - 210'] / games * 100:.4}%")
    print(f"211 - 220 pontos: {points['211 - 220']} - {points['211 - 220'] / games * 100:.4}%")
    print(f"221 - 230 pontos: {points['221 - 230']} - {points['221 - 230'] / games * 100:.4}%")
    print(f"231 - 240 pontos: {points['231 - 240']} - {points['231 - 240'] / games * 100:.4}%")
    print(f"241 - 250 pontos: {points['241 - 250']} - {points['241 - 250'] / games * 100:.4}%")
    print(f"250+ pontos: {points['250+']} - {points['250+'] / games * 100:.4}%")

    print(f"Average: {(points_sum) / games:.4}")
    print(f"Home Average: {home_points / games:.4}")
    print(f"Away Average: {away_points / games:.4}")


def home_winning(competition):
    games = 0
    home = 0
    away = 0

    for game in basketball_collection.find({"competition": competition}):
        games += 1
        if game["home_ft"] > game["away_ft"]:
            home += 1
        elif game["home_ft"] < game["away_ft"]:
            away += 1
    
    print(f"{competition} - Home: {home/games*100:.4}%")


def all_home_winning():

    competitions = []

    for game in basketball_collection.find({}):
        if game["competition"] in competitions:
            pass
        else:
            competitions.append(game["competition"])

    competitions.sort()

    games = 0
    home = 0
    away = 0

    for competition in competitions:
        for game in basketball_collection.find({"competition": competition}):
            games += 1
            if game["home_ft"] > game["away_ft"]:
                home += 1
            elif game["home_ft"] < game["away_ft"]:
                away += 1
        print(f"{competition.upper()} Home Winning: {home / games * 100:.4}%")
        games = 0
        home = 0
        away = 0

def all_basketball_average():

    competitions = []

    for game in basketball_collection.find({}):
        if game["competition"] in competitions:
            pass
        else:
            competitions.append(game["competition"])

    competitions.sort()

    games = 0
    home = 0
    away = 0

    for competition in competitions:
        for game in basketball_collection.find({"competition": competition}):
            games += 1
            if game["home_ft"] > game["away_ft"]:
                home += 1
            elif game["home_ft"] < game["away_ft"]:
                away += 1
    print(f"Home Winning: {home / games * 100:.4}%")



def competition_spread(competition):
    games = 0
    home = 0
    away = 0

    for game in basketball_collection.find({"competition": competition}):
        games += 1
        home += game["home_ft"]
        away += game["away_ft"]

    home_advantage = (home - away) / games

    print(f"Home Advantage in {competition.upper()}: {home_advantage:.2}")


def team_home_win_percentage(competition, handicap, team):
    games = 0
    win = 0
    void = 0
    lost = 0

    for game in basketball_collection.find({"competition": competition, "home": team}):
        games += 1
        if game["home_ft"] + handicap > game["away_ft"]:
            win += 1
        elif game["home_ft"] + handicap == game["away_ft"]:
            void += 1
        else:
            lost += 1

    print(f"Win: {win / games * 100:.4}%")
    print(f"Void: {void / games * 100:.4}%")
    print(f"Lost: {lost / games * 100:.4}%")

def favorite_win():
    competitions = []

    for game in basketball_collection.find({}):
        if game["competition"] in competitions:
            pass
        else:
            competitions.append(game["competition"])

    competitions.sort()

    games = 0
    home_win = 0
    away_win = 0
    fav_win = 0
    home_ft = 0
    away_ft = 0

    for competition in competitions:
        for game in basketball_collection.find({"competition": competition}):
            if game["odds_home"] and game["odds_away"] != 0:
                games += 1
                if game["home_ft"] > game["away_ft"] and game["odds_home"] < game["odds_away"]:
                    home_ft += game["home_ft"]
                    away_ft += game["away_ft"]
                    home_win += 1
                    fav_win += 1
                elif game["home_ft"] < game["away_ft"] and game["odds_home"] > game["odds_away"]:
                    away_win += 1
                    fav_win += 1
        home_advantage = (home_ft - away_ft)/games
        print(f"{competition.upper()} {fav_win/games*100:.2f}% favorite win. --- Home Advantage: {home_advantage:.2f}\n")
        games = 0
        home_win = 0
        away_win = 0
        fav_win = 0
        home_ft = 0
        away_ft = 0



#competition = get_competition()
#team = get_home_team(competition)
#handicap = float(input("Type the handicap: "))

#team_home_win_percentage(competition, handicap, team)
#all_home_winning()
#print()
#all_basketball_average()

favorite_win()