import analysisDB

# Gets the most viewed article (article name, views)
posts = analysisDB.get_mostviewed()

# Gets the article name and number of views of that article
if str(posts[0]) == "None": 
    print("There were no articles that got views.\n")
else
  mv_article = posts[0].replace("/article/", "")
  mv_article = mv_article.replace("-", " ")
  print("\"" + mv_article.title() + "\" - " + str(posts[1]))

# Gets the most popular author (author, views)