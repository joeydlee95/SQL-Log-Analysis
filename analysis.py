#!/usr/bin/python
#
# Joey Lee


import analysisDB
import datetime


# Gets the most viewed article ([Article name], [Number of views]).
posts = analysisDB.get_mostviewed()
# Checks if there is anything in posts
if str(posts[0]) == "None":
    print("There were no articles that got views.\n")
else:
    for post in posts:
        print("\"" + str(post[0]) + "\" - " + str(post[1]) + " views")


# Gets the most popular author ([Author's name], [Number of views]).
pop_authors = analysisDB.get_popular_author()
# Checks if there is anything in pop_author
if str(pop_authors[0]) == "None":
    print("There is were no authors that got views.\n")
else:
    for pop_author in pop_authors:
        print(str(pop_author[0]) + " - " + str(pop_author[1]) + " views")

# Gets the days that had more than 1% of requests lead to errors.
error_days = analysisDB.get_percent_error()
if str(error_days[0]) == "None":
    print("There were no days that had more that 1% errors.\n")
# Changes number formatted date to (month day, year) format.
for error_day in error_days:
    print('{0:%B %d, %Y} - {1:.1%} errors'.format(error_day[0], error_day[1]))
