import pymysql
import os
from dotenv import load_dotenv

load_dotenv()
host = os.environ.get("mysql_host")
user = os.environ.get("mysql_user")
password = os.environ.get("mysql_pass")
database = os.environ.get("mysql_db")

connection = pymysql.connect(
    host,
    user,
    password,
    database
)
cursor = connection.cursor()

cursor.execute('SELECT Courier_id, Courier_name, Courier_company, phone FROM Courier_table')
rows = curser.fetchall()
for row in rows:
    print(f'Courier_id: {(row)[0]}, Courier_name: {row[1]}, Courier_company:{row[2]}, phone: {row[3]}')

cursor.close()

#connection.close()

