#To insert multiple value in MySQL Database

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
s="INSERT INTO book(bookid ,title ,price) values (%s,%s,%s)"
books=(5,'AIES',45),(6,'OS',204),(7,'CSS',54)

#pass the value to cursor
cur.executemany(s,books)

#To save all changes
mydb.commit()
