#import mysql.connector
import MySQLdb
import datetime

db = MySQLdb.connect(
  host="127.0.0.1",
  user="root",
  passwd="Abcd1234"
)
db_cursor = db.cursor()
db_cursor.execute("CREATE DATABASE probe3_db")
db_cursor.execute("SHOW DATABASES")


print(db)

#db = MySQLdb.connect(host="localhost", user="root", passwd="Abcd1234", db="mysql")
#cursor = db.cursor()

db.close()