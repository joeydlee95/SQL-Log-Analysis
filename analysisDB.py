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

def get_popular_author():
    """Gets the row with an author and number of views."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    # Join articles and authors to include the author's name
    # then count the number of views each author gets. 
    c.execute("select name, count(name) as views \
               from (select slug, name \
               from articles join authors \
               on articles.author = authors.id) as most_viewed \
               join log \
               on log.path LIKE '%' || most_viewed.slug \
               where log.path LIKE '/article/%' \
               group by most_viewed.name \
               order by views desc \
               limit 1;")
    posts = c.fetchone()
    db.close()
    return posts