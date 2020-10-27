import csv

def read(file):
    categories = []

    with open(file, 'r') as csvfile:
        archive = csv.reader(csvfile, delimiter=',')
        next(archive)
        for column in archive:
            categories.append(column)
            print(categories)