import pymongo

brizenclient = pymongo.MongoClient("mongodb://localhost:27017")

brizendatabase = brizenclient["brizendatabase"]

football_collection = brizendatabase["football_games"]

def delete_all_games():
    x = football_collection.delete_many({})
    print(x.deleted_count)

def delete_games(competition):
    x = football_collection.delete_many({"competition": competition})
    print(x.deleted_count)