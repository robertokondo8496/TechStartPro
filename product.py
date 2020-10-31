import writedb
import show
import update
import drop

class Product:

    def __init__(self, name, description, value, categories):
        self.name = name
        self.description = description
        self.value = value
        self.categories = categories

    def createProduct(self):
        data = [ { "Name": self.name, "Description": self.description, "Value": self.value, "Categories": self.categories } ]
        writedb.write(data, 'products')

    def showProduct(self, filter = {}):
        result = show.show('products', filter)
        return result
    
    def updateProduct(self, filter, newdata):
        update.update('products', filter, newdata)

    def deleteProduct(self, filter):
        drop.delete('products', filter)