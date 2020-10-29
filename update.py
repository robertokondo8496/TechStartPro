import pymongo

def update(database, filter, dict):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    db = myclient["techstart"]
    col = db[database]
    col.update_one(filter, { "$set": dict })
    print("alteracao realizada com sucesso!")
