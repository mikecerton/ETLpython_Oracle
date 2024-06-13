import cx_Oracle
import os
from dotenv import load_dotenv

load_dotenv()

def start_connect():
    try:
        connection = cx_Oracle.connect(orcl_username, orcl_password, orcl_dsn)
        return connection
    except cx_Oracle.Error as error:
        print("!! Something Wrong !! : ", error)
        return None

def insert_data(connection, sql_insert, data):
    try:
        cursor = connection.cursor()
        cursor.execute(sql_insert, data)
        connection.commit()
        cursor.close()
        print("Data Insertd Successfully")
    except cx_Oracle.Error as error:
        print("!! Something Wrong !! : ", error)

def delete_data(connection, sql_delete):
    try:
        cursor = connection.cursor()
        cursor.execute(sql_delete)
        connection.commit()
        cursor.close()
        print("Data Deleted Successfully")
    except cx_Oracle.Error as error:
        print("!! Something Wrong !! : ", error)

def update_data(connection, sql_update):
    try:
        cursor = connection.cursor()
        cursor.execute(sql_update)
        connection.commit()
        cursor.close()
        print("Data Updated Successfully")
    except cx_Oracle.Error as error:
        print("!! Something Wrong !! : ", error)

def query_data(connection, sql_query):
    try:
        cursor = connection.cursor()
        cursor.execute(sql_query)
        rows = cursor.fetchall()
        cursor.close()
        print(rows)
    except cx_Oracle.Error as error:
        print("!! Something Wrong !! : ", error)

orcl_username = os.getenv("orcl_username")
orcl_password = os.getenv("orcl_password")
orcl_dsn = os.getenv("orcl_dsn")  