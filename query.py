
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="sakila"
)

cur = mydb.cursor()

def fetch():
    cur.execute("SELECT first_name FROM actor")
    for i in cur:
        yield i
        
for i in fetch():
    print(i)

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="sakila"
)

cur = mydb.cursor()

def fetch():
    cur.execute("SELECT first_name FROM actor")
    for i in cur:
        yield i
        
for i in fetch():
    print(i)

