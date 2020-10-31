#coding: utf-8
import writedb

def create():

    name = input("Product: ")
    description = input("Description: ")
    value = input("Value: ")
    numcat = input("How many categories are you going to insert: ")
    if(numcat == ""):
        numcat = 1
    categories = []
    for i in range(int(numcat)):
        aux = input("Categories: ")
        categories.append(aux)

    product = [name, description, value, categories]
    return product