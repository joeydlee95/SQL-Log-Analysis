import analysisDB

# Gets the most viewed article (article name, views)
posts = analysisDB.get_mostviewed()

# Gets the article name and number of views of that article
if str(posts[0]) == "None": 
    print("There were no articles that got views.\n")
else:
  print("\"" + str(posts[0]) + "\" - " + str(posts[1]))

