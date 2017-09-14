#!/usr/bin/python
#
# Joey Lee


import psycopg2
DBNAME = "newsdata"


def get_mostviewed():
    """Gets the row with the article and number of views it got."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()

    # Gets (title, total views)
    c.execute("select title, count(path) as views \
               from log left join articles \
               on log.path LIKE '%' || articles.slug \
               where log.path LIKE '/article/%' \
               group by title \
               order by views desc \
               limit 1;")
    posts = c.fetchone()
    db.close()
    return posts

def popular_author():
    """Gets the row with an author and number of views."""
    db = psychopg2.connect(database=DBNAME)
    c = db.cursor("select author, count(author) from ;")
    c.execute()