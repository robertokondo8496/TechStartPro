# this module is responsible for inserting data into database

def write(data, database):
    import pymongo
    # creates a connection with database
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")

    db = myclient["techstart"]
    col = db[database]
    x = col.insert_many(data)