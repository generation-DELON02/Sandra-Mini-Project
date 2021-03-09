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

def get_drink_by_id(drink_id):
    sql = 'SELECT * FROM drinks_table WHERE drink_id = %s'
    cursor.execute(sql,(drink_id))
    result=cursor.fetchall()
    if len(result) == 0: #checking length of the result if the ID i type is wrong etc print none
        return None
    return {'drink_id':result[0][0], 'drink_name': result[0][1], 'drink_price': result[0][2]}  #result is a list of tuples



   
