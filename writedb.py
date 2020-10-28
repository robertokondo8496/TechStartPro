# this module is responsible for inserting data into database

def write(category):
    import pymongo

    # creates a connection with database
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")

    db = myclient["techstart"]
    col = db["categories"]

    for element in category:
        dic = { "Category": element }
        x = col.insert_one(dic)
