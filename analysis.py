import analysisDB
import datetime

# Gets the most viewed article ([Article name], [Number of views]).
posts = analysisDB.get_mostviewed()
# Checks if there is anything in posts
if str(posts[0]) == "None":
    print("There were no articles that got views.\n")
else:
    print("\"" + str(posts[0]) + "\" - " + str(posts[1]) + " views")


# Gets the most popular author ([Author's name], [Number of views]).
pop_author = analysisDB.get_popular_author()
# Checks if there is anything in pop_author
if str(pop_author[0]) == "None":
    print("There is were no authors that got views.\n")
else:
    print(str(pop_author[0]) + " - " + str(pop_author[1]) + " views")

# Gets the days that had more than 1% of requests lead to errors.
error_days = analysisDB.get_percent_error()
# Changes number formatted date to (month day, year) format.
error_date = error_days[0].strftime("%B %d, %Y")
error_percent = error_days[1] * 100
print(error_date + " - " + str(round(error_percent, 1)) + "% errors")
