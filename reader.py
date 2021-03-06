# this module is responsible for reading a csv file and storing it in a list
import csv

def read(file):
    categories = []

    with open(file, 'r', encoding='utf-8') as csvfile:
        archive = csv.reader(csvfile, delimiter=',')
        next(archive)
        for column in archive:
            aux = {"Category": str(column[0])}
            categories.append(aux)
    return categories