import show
from bson import ObjectId

def readDictionaries(list):
    for dictionary in list:
        i = 0
        for key,value in dictionary.items():
            if(key == 'Categories'):
                for element in value:
                    a = show.show('categories', {'_id': ObjectId(element)})
                    print(a[0]["Category"])
            else:
                print('%s %s' % (key,value))