#Delete table record in MySQL


#1.Import mysql.connector module
import mysql.connector

#2.Creating the connection
mydb=mysql.connector.connect(host='localhost',user='root',password='',database='db1_python')

#printing the connection id
print(mydb.connection_id)

#3.creating the cursor object  
cur = mydb.cursor()
s="DELETE from book where title='OpenCV' "
cur.execute(s)
mydb.commit()