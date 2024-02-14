import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="srCSE150921@#",
    database="mydatabase"
)

mycursor=mydb.cursor()

#crete a table
sql_command=   """
                   UPDATE Student
                   SET first_name="Sobuj"
                   where roll=1;
               """
mycursor.execute(sql_command)
mydb.commit()
