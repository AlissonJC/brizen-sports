import pymongo

brizenclient = pymongo.MongoClient("mongodb://localhost:27017")

brizendatabase = brizenclient["brizendatabase"]

soccer_collection = brizendatabase["games"]


def delete_games(competition):
    x = soccer_collection.delete_many({"competition": competition})
    print(x.deleted_count)


def delete_all_games():
    x = soccer_collection.delete_many({})
    print(x.deleted_count)

def count_games(competition):
    count = 0
    for game in soccer_collection.find({"competition": competition}):
        count += 1
    print(count)


def list_games(competition):
    for game in soccer_collection.find({"competition": competition}):
        print(f"{game['home'].upper()} {game['home_ft']} x {game['away_ft']} {game['away'].upper()}")


def list_competitions():
    competitions = []

    for game in soccer_collection.find({}):
        if game["competition"] in competitions:
            pass
        else:
            competitions.append(game["competition"])

    competitions.sort()

    for competition in competitions:
        print(competition)