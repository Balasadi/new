import mysql.MySQLdb
  db = MySQLdb.connect.connect(
  host= "localhost",
  user= "root",
  passwd= "Abcd1234",
  )
# creating database_cursor to perform SQL operation
db_cursor = db_connection.cursor()
# executing cursor with execute method and pass SQL query
db_cursor.execute("CREATE DATABASE my_first_db")
# get list of all databases
db_cursor.execute("SHOW DATABASES")
#print all databases
for db in db_cursor:
	print(db)