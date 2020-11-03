# TechStartPro

## Project Description

This is a program that implements an product registrator. Basically, it does an interface between user, who inserts some data about the products and the database, which stores data about those products.

## Requirements

You must have installed on your PC the following items:

- Python 3.9.0
- MongoDB 4.4.1

## Installation

### Database

Install MongoDB from https://www.mongodb.com/try/download/community.
Start the MongoDB server, typing mongod on console.
Create a database called "techstart":

```
use techstart
```

### Program

Install python 3.9.0 from https://www.python.org/downloads/
In the directory of the project, type on console "python3 program.py".
First time running the program is necessary to import the data from "categorias.csv". Please choose the option in the main menu.

## Testing

Before running those tests, please make sure that you are running the MongoDB server.

### testread.py

For testing the module that reads the csv reader, type on console:

```
python3 testread.py
```

### testshow.py

For testing the module that goes tho the database and searches for some data using specified filters by user, type on console:

```
python3 testshow.py
```

## About the working environment used

To develop this application, some resources were used:

- OS Windows 10 Home
- IDE Microsoft Visual Studio Code
- Libraries: pymongo (for database), bson ObjectId (for working with MongoDB ObjectIds) and unittest (for unit testing).

