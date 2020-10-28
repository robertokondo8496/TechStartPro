#coding: utf-8
import writedb

def create():
    name = input("Product: ")
    description = input("Description: ")
    value = input("Value: ")
    numcat = input("How many categories are you going to insert: ")
    categories = []
    for i in range(int(numcat)):
        aux = input("Categories: ")
        categories.append(aux)

    data = [ { "Name": name, "Description": description, "Value": value, "Categories": categories } ]

    writedb.write(data, 'products')