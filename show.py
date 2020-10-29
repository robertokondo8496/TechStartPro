# this module is responsible for showing data into database
import pymongo

def show(collection, filter = {}):
    """This function is responsible for showing data into database"""
    # creates a connection with database
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    db = myclient["techstart"]
    col = db[collection]
    for x in col.find(filter):
        print(x)