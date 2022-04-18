
# Applied Databases Module:
# Functions file
# contains all functions used in the main program
# Author: Daniel Gonzalez


def display_menu():
    print("")
    print("MENU")
    print("====")
    print("1 - View Films")
    print("2 - View Actors by Year of Birth & Gender")
    print("3 - View Studios")
    print("4 - Add New Country")
    print("5 - View Movies with Subtitles")
    print("6 - Add New MovieScript")
    print("x - Exit application")
    print("")


# -------------------------------------- #


def display(l):
    # Second function of question 1
    # Organises the list of films and actors

    a = 0
    b = 5
    c = len(l) - 1
    # Defines parameters to loop through the list

    while b < c:
        for i in range(a, b):
            print(l[a]["filmname"], "|", l[a]["actorname"])
            a += 1
        choice = input(" -- Quit(q) -- View five more results( Any Key) ")
        if choice != "q":
            b += 5
        else:
            print("End of list")
            break


# -------------------------------------- #

def stored_studio_list(a):
    # Creates a stores a copy of the list.
    # Will only access the database when empty.
    if len(a) == 0:
        studios = mysqldb.show_studios()
    else:
        studios = a

    return studios


# -------------------------------------- #

def get_year():
    # Second function of question 2
    # Returns year for the MySql query

    while True:
        try:
            year = int(input("Enter your year: "))
            break
        except ValueError:
            pass
    return year


# -------------------------------------- #


def get_gender():
    # Third Function of question 2
    # Returns gender for the MySql Query
    a = 0
    b = 2
    genders = ["Male", "Female", "male", "female"]

    while a < b:
        try:
            gender = input("Gender: ")
            if gender in genders:
                return gender
            a += 1
        except Exception as e:
            pass

    return ""


# -------------------------------------- #

def get_countryID():
    # Function for question 4.
    # Returns a countryID (int)
    while True:
        try:
            countryID = int(input("ID: "))
            break
        except ValueError:
            pass
    return countryID


# -------------------------------------- #

def get_countryName():
    # Function for question 4.
    # Returns a contryname (str)
    countryName = str(input("Name: "))
    while countryName.isdigit() or countryName == "":
        countryName = str(input("Name: "))

    return countryName


# -------------------------------------- #

def get_language():
    # Function for question 5.
    # Returns a language (str)
    language = input("Language: ")
    while language.isdigit() or language == "":
        language = str(input("Language: "))
    return language


# -------------------------------------- #

def get_filmID():
    # Function for question 6.
    # Returns a filmID (int)
    while True:
        try:
            id = int(input("ID: "))
            break
        except ValueError:
            pass
    return id

# -------------------------------------- #


def get_keyword():
    # function for question 6.
    # Returns a list of keywords
    list = []

    while True:
        data = input("keyword (-1 to End): ")
        if data == "-1":
            break
        if data == "":
            continue
        list.append(data)

    return list

# -------------------------------------- #


def language_for_script():
    # Function for questin 6.
    # Returns a list of languages for subtitles
    list = []

    while True:
        data = input("Language (-1 to End): ")
        if data == "-1":
            break
        if data == "":
            continue
        list.append(data)

    return list
