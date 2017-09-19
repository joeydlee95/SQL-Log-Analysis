#!/usr/bin/python
#
# Joey Lee


import psycopg2
DBNAME = "newsdata"


def get_mostviewed():
    """Gets the row with the article and number of views it got."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()

    # Gets (title, total views) of the most viewed article
    c.execute("""SELECT title, count(path) AS views
               FROM articles LEFT JOIN log
               ON log.path = '/article/' || articles.slug
               GROUP BY title
               ORDER BY views DESC
               LIMIT 3;""")
    posts = c.fetchall()
    db.close()
    return posts


def get_popular_author():
    """Gets the row with an author and number of views."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    # Join articles and authors to include the author's name
    # then count the number of views each author gets.
    c.execute("""SELECT name, count(name) AS views
               FROM (SELECT slug, name
               FROM articles JOIN authors
               ON articles.author = authors.id) AS most_viewed
               JOIN log
               ON log.path = '/article/' || most_viewed.slug
               GROUP BY most_viewed.name
               ORDER BY views DESC;""")
    posts = c.fetchall()
    db.close()
    return posts


def get_percent_error():
    """Gets the row with a date and a fraction of errors over total."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    # Creates a view of date and total requests that day.
    c.execute("create view total_views as \
                   select date(time), count(date(time)) as total_count \
                   from log \
                   group by date(time);")
    # Creates a view of date and requests resulting in errors that day.
    c.execute("create view error_views as \
                   select date(time), count(date(time)) as error_count \
                   from log \
                   where status != '200 OK' \
                   group by date(time);")
    # Joins the two views and gets the percent of error requests.
    c.execute("""SELECT total_views.date,
               round(error_count/total_count::numeric, 3) AS percent_error
               FROM total_views JOIN error_views
               ON total_views.date = error_views.date
               WHERE round(error_count/total_count::numeric, 3) > 0.01;""")
    posts = c.fetchall()
    db.close()
    return posts
