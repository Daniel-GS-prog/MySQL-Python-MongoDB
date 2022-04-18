
# Applied Databases Module:
# Main program:
# contains all python functions corresponding to the project's questions
# Author: Daniel Gonzalez

import mysqldb
import mongodb
import functions as f

# -------------------------------------------------------------------------------------- #


def main():

    f.display_menu()

    while True:

        choice = input("Choice: ")

# -------------------------------------------------------------------------------------- #

        if choice == "1":
            films = mysqldb.view_films()
            f.display(films)
            f.display_menu()

# -------------------------------------------------------------------------------------- #

        elif choice == "2":
            year_of_birth = f.get_year()
            gender = f.get_gender()
            if gender:
                actors = mysqldb.view_actors(year_of_birth, gender)
            else:
                actors = mysqldb.view_actors_no_gender(year_of_birth)
            print("---------------")

            for actor in actors:
                print(actor["actorname"], "|", actor["monthname(actordob)"], "|", actor["actorgender"])
            print("--------------")

# -------------------------------------------------------------------------------------- #

        elif choice == "3":
            initial_list = mysqldb.studios_list # Initial list populated
            studios = f.stored_studio_list(initial_list) # initial list and updated only if empty. See line 104
            print("")
            print("Studios:")
            print("--------")
            for studio in studios:
                print(studio["StudioID"], "|", studio["StudioName"])
            f.display_menu()

# -------------------------------------------------------------------------------------- #

        elif choice == "4":
            countryID = f.get_countryID()
            countryName = f.get_countryName()
            try:
                mysqldb.new_country(countryID, countryName)
                print("Country: {}, {} added to the database.".format(countryID, countryName))
            except:
                print("*** ERROR ***: ID/or Name ({}, {}) already exists.".format(countryID, countryName))
            f.display_menu()

# -------------------------------------------------------------------------------------- #

        elif choice == "5":
            language = f.get_language()
            try:
                filmID = mongodb.find(language)
                a = mysqldb.get_subtitles(filmID)
                for i in a:
                    print(i["filmname"], "|", i["Synopsis"])
            except Exception as e:
                print("*** ERROR ***: Subtiltes language not available or case sensitive")
            f.display_menu()

# -------------------------------------------------------------------------------------- #

        elif choice == "6":
            id = f.get_filmID()
            keywords = f.get_keyword()
            languages = f.language_for_script()
            a = mysqldb.movieScript(id)
            if len(a) == 0:
                print("*** ERROR ***: movie with id: {} does not exists in MoviesDB".format(id))

            else:
                try:
                    newScript = mongodb.new_script(id, keywords, languages)
                    print("Movie Script: {} added to database.".format(id))
                except Exception as e:
                    print("*** ERROR ***: Movie Script with id: {} already exists.".format(id))
            f.display_menu()

# -------------------------------------------------------------------------------------- #

        elif choice == "x":
            # Exists the program
            print("--------")
            print("Good bye")
            print("--------")
            break


# -------------------------------------------------------------------------------------- #


if __name__ == "__main__":
    main()