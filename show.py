# this module is responsible for showing data into database

def show(database):
    import pymongo
    # creates a connection with database
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")

    db = myclient["techstart"]
    col = db[database]
    for x in col.find():
        print(x)