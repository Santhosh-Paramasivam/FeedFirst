import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

mydb = mysql.connector.connect(
  host="localhost",
  user=os.getenv("FF_USERNAME"),
  password=os.getenv("FF_PASSWORD"),
  database="FeedFirst"
)

mycursor = mydb.cursor()