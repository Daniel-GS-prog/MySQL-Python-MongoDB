 
## Table of contents
* [Project Description](#Project-Description)
* [Technologies](#Technologies)
* [Python program](#Python-program)
* [Databases description](#Databases-description)
    * [MySql](#MySql)
    * [MySql queries](#MySql-queries)
    * [MongoDB](#MongoDB)
    * [MongoDB queries](#MongoDB-queries)
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
#### MySql qeries
1.
~~~~sql
  select c.certificate, f.filmname
 from certificate c
 inner join film f
  on c.certificateid = f.filmcertificateid
 inner join filmcast fc
  on f.filmid = fc.castfilmid
 inner join actor a
  on fc.castactorid = a.actorid
 where a.actorname = 'Temuera Morrison'
 order by f.filmname
 ;
~~~~
2. 
~~~~sql
select distinct f.filmname 
from film f 
inner join filmcast fc 
on f.filmid = fc.castfilmid 
inner join actor a 
on fc.castactorid = a.actorid 
inner join country c 
on a.actorcountryid = c.countryid 
where c.countryname = 'United Kingdom' 
order by f.filmname;
~~~~
3.
~~~~sql
select a.actorname, count(f.filmname) as 'count(*)' 
from film f 
inner join filmcast fc 
on f.filmid = fc.castfilmid 
inner join
actor a on fc.castactorid = a.actorid 
group by a.actorname 
order by count(f.filmname), 
a.actorname;
~~~~
4.
~~~~sql
select l.language, avg(f.filmruntimeminutes) as 'avg(FilmRunTimeMinutes)' 
from language l 
inner join film f 
on l.languageid = f.filmlanguageid 
group by l.language 
order by avg(f.filmruntimeminutes) asc, l.language;
~~~~

   
 ### MongoDB
  The collection movieScripts (also in relation with the MySql database MoviesDB - 
    both id and several documents are related) has the following documents:
    
    * Keywords
    * Subtiles
<br>

#### MongoDB queries
1. 
```
 db.employees.aggregate([{$bucket:{groupBy: "$salary", boundaries: [0, 38000, 48000, 50000], default:">50000", output: {"count": {$sum:1}}} }])
```

2. 
```
 db.employees.aggregate([{$project: {_id:1, "Salary Bracket":{"$cond":{if:{$lt:["$salary", 40000]}, then:"Low", else:{"$cond":{if:{$lt:["$salary", 48000]}, then:"Medium", else:"High"}}}}}},{"$sort":{_id:1}}])
```

3. 
```
 db.employees.aggregate([{$match:{"expertise":{$exists:1}}}, {$project:{"Area of expertise":{$size:"$expertise"}}}, {"$sort":{"Area of expertise":1, _id:1}}])

```

4. 
```
 db.employees.aggregate([{$match:{"pensionLevel":{$exists:1}}}, {$project:{_id:0, "Min Pension Level":"$pensionLevel"}}, {$sort:{"Min Pension Level":1}}, {$limit:1}])

``` 


    
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