import writedb
import show
import update
import drop

fields = ["Name", "Description", "Value", "Categories"]

class Product:

    def __init__(self, name, description, value, categories):
        self.name = name
        self.description = description
        self.value = value
        self.categories = categories

    def createProduct(self):
        data = [ { "Name": self.name, "Description": self.description, "Value": self.value, "Categories": self.categories } ]
        writedb.write(data, 'products')

    def showProduct(self):
        data = { "Name": self.name, "Description": self.description, "Value": self.value, "Categories": self.categories }
        filter = {}
        for key, value in data.items():
            if(value != "" and value != [""]):
                filter.update({key: value})
                print({key: value})
        result = show.show('products', filter)
        return result
    
    def updateProduct(self, filter):
        data = { "Name": self.name, "Description": self.description, "Value": self.value, "Categories": self.categories }
        newdata = {}
        for key, value in data.items():
            if(value != "" and value != [""]):
                newdata.update({key: value})
                print({key: value})        
        update.update('products', filter, newdata)

    def deleteProduct(self):
        data = { "Name": self.name, "Description": self.description, "Value": self.value, "Categories": self.categories }
        filter = {}
        for key, value in data.items():
            if(value != "" and value != [""]):
                filter.update({key: value})
                print({key: value})     
        # print(filter)
        drop.delete('products', filter)