# Applied Databases Module:
# pymongo file:
# contains all mongo queries for the project's questions.
# All manipulation will be performed in the main file
# Author: Daniel Gonzalez

import pymongo

# -------------------------------------------------------------------------------------- #


myclient = None

# -------------------------------------------------------------------------------------- #


def connect():
    global myclient
    myclient = pymongo.MongoClient()
    myclient.admin.command('ismaster')

# -------------------------------------------------------------------------------------- #


def find(l):
    # Function for question 5.

    if not myclient:
        connect()

    mydb = myclient.movieScriptsDB
    docs = mydb.movieScripts

    query = docs.find({"subtitles": {"$exists": True, "$regex": "" + l + ""}},
                      {"_id": 1, "subtitles": 1})

    films = []  # list to be populated with filmID's

    for i in query:
        films.append((i["_id"]))  # append filmID to the list
    a = tuple(films)    # Makes a tuple of the list so it can be passed to the MySql query
    return a

# -------------------------------------------------------------------------------------- #


def new_script(id, keywords, subtitles):
    # Function for question 6

    if not myclient:
        connect()

    mydb = myclient.movieScriptsDB
    docs = mydb.movieScripts

    query = docs.insert({"_id":id, "Keywords":keywords, "subtitles":subtitles})
    return ""

# -------------------------------------------------------------------------------------- #
