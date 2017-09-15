# Log Analysis

Dong Lee (Joey) 9/15/2017

## Background
This is a reporting tool that uses an existing database with over a million rows of data answering these questions. I use psycopg2 DB-API in python to interact with the postgres database.

* What are the most popular three articles of all time?
* Who are the most popular article authors of all time?
* On which days did more than 1% of requests lead to errors?
    
## How to Run
1. vagrant up
2. vagrant ssh
3. cd /vagrant
4. unzip the newsdata.zip
5. run "python analysis.py"


## Files

analysisDB.py: Contains the methods that answers the above questions.
  
  * get_mostviewed() - sends a select query to obtain the title of the article and the number of views it got.

  * get_popular_author() - sends a select query to obtain the author with the most views. 

  * get_percent_error() - creates 2 views and then joins them to obtain the date and % of errors that day.

analysis.py: Calls the methods in analysisDB.py and prints the answers to the question.


## Sources
https://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior
  - Contains information on the uses for stftime and how to print datetimes.