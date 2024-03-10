import sqlite3

connection = sqlite3.connect("subscriptions.db")

cursor = connection.cursor()

cursor.execute("select * from subscriptions")

results = cursor.fetchall()

for raw in results:
    print(raw)
