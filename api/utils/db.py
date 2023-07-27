import os
from dotenv import load_dotenv

import mysql.connector

def connection():
    load_dotenv()
    try:
        conn = mysql.connector.connect(
            host=os.environ.get("host"),
            user=os.environ.get("user"),
            passwd=os.environ.get("password"),
            database=os.environ.get("db")
        )
    
    except mysql.connector.Error as err:
        if err.errno == "errorcode.ER_ACCESS_DENIED_ERROR":
            print("Something is wrong with your user name or password")
        elif err.errno == "errorcode.ER_BAD_DB_ERROR":
            print("Database does not exist")
        else:
            print(err)
    else:
        return conn