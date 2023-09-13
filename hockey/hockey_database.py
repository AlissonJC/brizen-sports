import pymongo
from bson.objectid import ObjectId

brizenclient = pymongo.MongoClient("mongodb://localhost:27017")

brizendatabase = brizenclient["brizendatabase"]

hockey_collection = brizendatabase["hockey_games"]

def delete_games(competition):
    x = hockey_collection.delete_many({"competition": competition})
    print(x.deleted_count)

def delete_n_by_id():
    n = int(input("Type the number of games: "))

    while n > 0:
        id = input("ID: ")
        hockey_collection.find_one_and_delete({'_id': ObjectId(id)})
        n -= 1


def delete_all_games():
    x = hockey_collection.delete_many({})
    print(x.deleted_count)

def count_games():
    count = 0
    for game in hockey_collection.find({"competition": "russia-pro-2020"}):
        count += 1
    print(count)

    
def show_games(competition):
    for game in hockey_collection.find({"competition": competition}):
        print(game)
        #print(f"{game['_id']}")
        #print(f"{game['home'].upper()} {game['home_ft']} x {game['away_ft']} {game['away'].upper()}")


def list_competitions():
    competitions = []

    for game in hockey_collection.find({}):
        if game["competition"] in competitions:
            pass
        else:
            competitions.append(game["competition"])
    
    for competition in competitions:
        print(competition)


def teams_in_competition(competition):
    teams = []

    for game in hockey_collection.find({"competition": competition}):
        if game["home"] in teams:
            continue
        else:
            teams.append(game["home"])

    print(teams)