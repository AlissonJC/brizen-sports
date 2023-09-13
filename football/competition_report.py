from football_database import football_collection


def all_football_average():

    competitions = []

    for game in football_collection.find({}):
        if game["competition"] in competitions:
            pass
        else:
            competitions.append(game["competition"])

    competitions.sort()

    games = 0
    home = 0
    away = 0

    for competition in competitions:
        for game in football_collection.find({"competition": competition}):
            games += 1
            if game["home_ft"] > game["away_ft"]:
                home += 1
            elif game["home_ft"] < game["away_ft"]:
                away += 1
    print(f"Home Winning: {home / games * 100:.4}%")
    print(f"Away Winning: {away / games * 100:.4}%")
    print(f"Games: {games}")

all_football_average()