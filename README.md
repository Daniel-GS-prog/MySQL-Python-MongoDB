# MySQL-Python-MongoDB
python  application to interacts with both MySql and MongoDB databases.


## Table of contents
* [Project Description](#Project-Description)
* [Technologies](#Technologies)
* [Python program](#Python-program)
* [Databases description](#Databases-description)
    * [MySql](#MySql)
    * [MongoDB](#MongoDB)
* [Relation Question - Functions](#Relation-question-Functions)

## Project Description

The purpuse of this project is to build a python 
application to intereact with both MySql and MongoDB dabatases, as a final 
project for the module "Applied Databases" within the Higher Diploma in Data Analytics in GMIT.
<br>

## Technologies
 The programs used in this project, and required for it correct execution are:
 * Python 3
    * Modules:
        * pymysql
        * pymongo
 * MySql
 * MongoDB
 <br>
 
 ## Python program
 The project includes the files:
 
    * main.py: main program.
    * functions.py: with all the python functions used in the main program.
    * mysqldb.py: all pymysql queries. All manipulation is performed in the functions file. 
    * mongodb.py: all pymongo queries. All manipulation is performed in the functions file.
 <br>
 
 ## Databases description
 ### MySql
 The Database MoviesDB includes the following tables:
 
    * Actor
    * Certificate
    * Country
    * Director
    * Film
    * FilmCast
    * Genre
    * Language
    * Studio
            
   All tables are created in relation with the rest though 
   primary keys and constrains. 
  <br>  
 ### MongoDB
  The collection movieScripts (also in relation with the MySql database MoviesDB - 
    both id and several documents are related) has the following documents:
    
    * Keywords
    * Subtiles
    
### Relation question - Functions:

The following shows the functions used in each questions:

      * Question 1: functions.Display(), ,mysqldb.view_films()
      * question 2: functions.getyear(), functions.get_gender(), mysqldb.view_actors(), 
        mysqldb.view_actors_no_gender()
      * Question 3: functions.stored_studio_list(), mysqldb.studio_list()
      * Question 4: functions.get_countryID(), functions.get_ci¡ountryName(),
        mysqldb.new_country()
      * Question 5: functions.get_language(), mysqldb.get_suntitles(), mongodb.find()
      * Question 6: functions.getfilms(), functions.get_keywords(), functions.language_for_scripts(),
        ,ysqldb.movieScript(), mongodb.new_script()
