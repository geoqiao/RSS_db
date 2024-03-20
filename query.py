# # import sqlite3

# # connection = sqlite3.connect("subscriptions.db")

# # cursor = connection.cursor()

# # cursor.execute("select * from subsriptions")

# # results = cursor.fetchall()

# # for raw in results:
# #     print(raw)


# from utils import Feed
# import feedparser
# url = "https://raw.githubusercontent.com/geoqiao/gitblog/main/feed.xml"

# feed = Feed(url)

# parser = feedparser.parse(url)

# for entry in parser.entries:
#     print(entry)

# # articles = feed.articles()
# # sorted_list = sorted(articles, key=lambda x: x['updated'],reverse=True)
# # print(sorted_list)
