import sys,sqlite3,os
import mysql.connector
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="hugodemenez",
  password="password",
  database="database",
  auth_plugin='mysql_native_password',
)

cursor = mydb.cursor()
cursor.execute("INSERT OR REPLACE INTO user VALUES ({username},{password},{email})")




    