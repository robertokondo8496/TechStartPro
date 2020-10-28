import pymongo

def delete(database, dict):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    db = myclient["techstart"]
    col = db[database]
    col.delete_one(dict)
    print('deletado com sucesso!')
