import mysql.connector

dataBase=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='2324')

cursorObject=dataBase.cursor()

cursorObject.execute("CREATE DATABASE STUDYBUD")

print("All Done!")
