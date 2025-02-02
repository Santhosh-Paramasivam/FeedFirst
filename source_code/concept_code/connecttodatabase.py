import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="",
  password="",
  database="FeedFirst"  # Optionally, you can specify the database here
)

mycursor = mydb.cursor()

mycursor.execute("DESCRIBE Pantries;")
description = mycursor.fetchall()

for column in description:
    print(column)
