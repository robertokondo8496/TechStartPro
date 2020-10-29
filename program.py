import reader
import writedb
import insert
import show
import update
import drop

fields = ["Name", "Description", "Value", "Categories"]
filter = {}

while(1):
    print('''Options:
    [0] - Create Product
    [1] - Read Product
    [2] - Update Product
    [3] - Delete Product
    [4] - Exit''')
    opt = input("What option would you like to do:")

    if(int(opt) == 0):
        print("CREATE")
        insert.create()

    elif(int(opt) == 1):
        print("READ")
        numberFilters = input("Insert how many filters are you going to use (1-4): ")
        if(numberFilters == ""):
            numberFilters = 0
        for i in range(int(numberFilters)):
            print(fields[i])
            value = input()
            if(value != ""):
                filter.update({fields[i]: value})
        print(filter)
        show.show('products', filter)
        filter.clear() 

    elif(int(opt) == 2):
        print('''UPDATE
        
        Please insert what product would you like to change:
        (You can insert one or more filters)

        ''')
        newdict={}

        for element in fields:
            print(element)
            newelement = input()
            if(newelement != ""):
                filter.update({element: newelement})
        print('''
        
        Please insert now new data to write to selected product:

        ''')

        for element in fields:
            print(element)
            newelement = input()
            if(newelement != ""):
                newdict.update({element: newelement})
        update.update('products', filter, newdict)
        filter.clear()

    elif(int(opt) == 3):
        print("DELETE")
        
        for element in fields:
            print(element)
            newelement = input()
            if(newelement != ""):
                filter.update({element: newelement})
        drop.delete('products', filter)
        filter.clear()

    elif(int(opt) == 4):
        print("bye")
        break