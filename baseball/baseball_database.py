import pymongo

brizenclient = pymongo.MongoClient("mongodb://localhost:27017")

brizendatabase = brizenclient["brizendatabase"]

baseball_collection = brizendatabase["baseball_games"]

def delete_games(competition):
    x = baseball_collection.delete_many({"competition": competition})
    print(x.deleted_count)

def delete_all_games():
    x = baseball_collection.delete_many({})
    print(x.deleted_count)

delete_all_games()

def count_games():
    count = 0
    for game in baseball_collection.find({"competition": "mlb-2019"}):
        count += 1
    print(count)

def list_competitions():
    competitions = []

    for game in baseball_collection.find({}):
        if game["competition"] in competitions:
            pass
        else:
            competitions.append(game["competition"])
    
    for competition in competitions:
        print(competition)