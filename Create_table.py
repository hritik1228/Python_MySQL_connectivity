#To create a table in MySQL

#1.Import mysql.connector module
import mysql.connector

#2.Creating the connection
mydb=mysql.connector.connect(host='localhost',user='root',password='',database='db1_python')

#printing the connection id
print(mydb.connection_id)

#3.creating the cursor object  
cur = mydb.cursor()  

#4.Execute the query
#To create a table in database
s="create table book(bookid integer(4),title varchar(20),price float(3,2))"

#pass the value to cursor
cur.execute(s)


