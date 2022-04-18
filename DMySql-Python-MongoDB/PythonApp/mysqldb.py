# Applied Databases Module:
# mySQL file:
# contains all MySQL queries for the project's questions.
# All manipulation will be performed in the main file
# Author: Daniel Gonzalez


import pymysql


conn = None

# -------------------------------------------------------------------------------------- #


def connect():
    global conn
    conn = pymysql.connect(host="localhost", user="root", password="",
                           db="MoviesDB", autocommit=True, cursorclass=pymysql.cursors.DictCursor)


# -------------------------------------------------------------------------------------- #


def view_films():
    # Function of question 1.

    if not conn:
        connect()

    query = """
                SELECT f.filmname, a.actorname 
                from film f 
                inner join actor a 
                 on f.filmcountryid = a.actorcountryid 
                inner join filmcast fc 
                 on a.actorid = fc.castactorid 
                order by f.filmname, a.actorname;
            """

    with conn:
        conn.ping()
        cursor = conn.cursor()
        cursor.execute(query)
        x = cursor.fetchall()
        return x

# -------------------------------------------------------------------------------------- #


def view_actors(year, gender):
    # First Function fo question 2.
    # Query with gender

    if not conn:
        connect()

    query = """
                select actorname, monthname(actordob), actorgender 
                from actor 
                where year(actordob) = %s 
                and actorgender = %s;
            """

    with conn:
        conn.ping()
        cursor = conn.cursor()
        cursor.execute(query, (year, gender))
        x = cursor.fetchall()
        return x

# -------------------------------------------------------------------------------------- #


def view_actors_no_gender(year):
    # Second Function of question 2.
    # Query without gender

    if not conn:
        connect()

    query = """
                SELECT actorname, monthname(actordob), actorgender 
                from actor 
                where year(actordob) = %s 
                ;
            """

    with conn:
        conn.ping()
        cursor = conn.cursor()
        cursor.execute(query, year)
        x = cursor.fetchall()
        return x

# -------------------------------------------------------------------------------------- #


def show_studios():
    # Function for question 3.

    if not conn:
        connect()

    query = "SELECT * from studio order by studioid;"

    with conn:
        conn.ping()
        cursor = conn.cursor()
        cursor.execute(query)
        x = cursor.fetchall()
        cursor.close()
        return x


studios_list = show_studios()
# Initial list populated ( see line 35 in main file)


# -------------------------------------------------------------------------------------- #


def new_country(Id, name):
    # Function for question 4.

    if not conn:
        connect()

    query = "INSERT into country (countryid, countryname) values(%s, %s);"

    with conn:
        conn.ping()
        cursor = conn.cursor()
        x = cursor.execute(query, (Id, name))
        return x


# -------------------------------------------------------------------------------------- #

def get_subtitles(l):
    # Function for question 5 .
    # Takes a list of ID's from the pymongo function
    # Returns the film name and synopsis (30 charactes)

    if not conn:
        connect()

    query = 'SELECT filmname, SUBSTRING(filmsynopsis,1, 30) as Synopsis from film  where filmid in {};'.format(l)

    with conn:
        conn.ping()
        cursor = conn.cursor()
        x = cursor.execute(query)
        x = cursor.fetchall()
        return x

# -------------------------------------------------------------------------------------- #


def movieScript(id):
    # Function for question 6 .
    # If id exists, the query is passed to pymongo

    if not conn:
        connect()

    query = "SELECT filmid from film where filmid = {}".format(id)

    with conn:
        conn.ping()
        cursor = conn.cursor()
        x = cursor.execute(query)
        x = cursor.fetchall()
        return x