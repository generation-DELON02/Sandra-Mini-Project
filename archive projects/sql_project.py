import pymysql
import os
from dotenv import load_dotenv

#1.Where to put this in your project (import file) into a function but where???
#2.Go back and define a primary key -- this is the ID from psuedo code
#3.copy and paste a new project
#4.make a list here of where of what funcions need to be changed
#5.how do you want you open and close this? where will you put the functions
#6.study this in the morn https://stackoverflow.com/questions/36708125/user-input-to-mysql-database 
#7.look at your notes for how to do input with mysql and python

#Load environment variables from .env file
load_dotenv()
host = os.environ.get("mysql_host")
user = os.environ.get("mysql_user")
password = os.environ.get("mysql_pass")
database = os.environ.get("mysql_db")

#Establish a database connection
connection = pymysql.connect(
    host,
    user,
    password,
    database
)

# A cursor is an object that represents a DB cursor,
# which is used to manage the context of a fetch operation.
cursor = connection.cursor()

# Execute SQL query
cursor.execute('SELECT Courier_id, Courier_name, Courier_company, phone FROM Courier_table') ## does this run if yes connected 

# Gets all rows from the result
rows = cursor.fetchall()
for row in rows:
    print(f'Courier_id: {(row[0])}, Courier_name: {row[1]}, Courier_company: {row[2]}, phone: {row[3]}')

# Can alternatively get one result at a time with the below code
# while True:
#     row = cursor.fetchone()
#     if row == None:
#         break
#     print(f'First Name: {str(row[0])}, Last Name: {row[1]}, Age: {row[2]}')

# Closes the cursor so will be unusable from this point 
cursor.close()

# Closes the connection to the DB, make sure you ALWAYS do this
connection.close()