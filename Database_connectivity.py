#Database Connection using MySQL

#1.Import mysql.connector module
import mysql.connector

#2.Creating the connection
mydb=mysql.connector.connect(host='localhost',user='root',password='')

#printing the connection id
print(mydb.connection_id)

#3.creating the cursor object  
cur = mydb.cursor()  

#4.Execute the query
#To create a database in MySQL
cur.execute("CREATE DATABASE DB1_PYTHON")


