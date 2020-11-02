import reader
import writedb
import insert
import show
import readDictionaries
from product import Product

fields = ["Name", "Description", "Value", "Categories"]
filter = {}

while(1):
    print('''
    --------------------------------------------------------
    ********************************************************
    TECHSTARTPRO
    
    Options:
    [0] - Create Product
    [1] - Read Product
    [2] - Update Product
    [3] - Delete Product
    [4] - Show Categories
    [5] - Update Categories from .csv
    [6] - Exit
    
    --------------------------------------------------------
    ********************************************************
    ''')
    opt = input("What option would you like to do:")

    if(int(opt) == 0):
        print("CREATE")
        prodData = insert.create()
        prod1 = Product(prodData[0], prodData[1], prodData[2], prodData[3])
        prod1.createProduct()

    elif(int(opt) == 1):
        print("READ")
        prodData = insert.create()
        prod1 = Product(prodData[0], prodData[1], prodData[2], prodData[3])
        prod = prod1.showProduct()
        readDictionaries.readDictionaries(prod)

    elif(int(opt) == 2):
        print('''UPDATE
        
        Please insert what product would you like to change:
        (You can insert one or more filters)

        ''')

        for element in fields:
            print(element)
            newelement = input()
            if(newelement != ""):
                filter.update({element: newelement})
        print('''
        
        Please insert now new data to write to selected product:

        ''')

        prodData = insert.create()
        prod1 = Product(prodData[0], prodData[1], prodData[2], prodData[3])   
        prod1.updateProduct(filter)

    elif(int(opt) == 3):
        print("DELETE")
        prodData = insert.create()
        prod1 = Product(prodData[0], prodData[1], prodData[2], prodData[3])  
        prod1.deleteProduct()

    elif(int(opt) == 4):
        readDictionaries.readDictionaries(show.show('categories'))

    elif(int(opt) == 5):
        cat = reader.read('categorias.csv')
        writedb.write(cat, 'categories')

    elif(int(opt) == 6):
        print("bye")
        break