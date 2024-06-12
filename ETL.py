import subprocess
import json
from random import randint
import cx_Oracle

def curl_request(url):
    command = ['curl', url]
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout

def gen_key():
    value = randint(1, 9999)
    return str(value)

#_______________connect oracle part _______________
username = 'Admin_project'
password = 'sql123'
dsn = 'localhost:1521/xepdb1'  

connection = cx_Oracle.connect(username, password, dsn)

cursor = connection.cursor()

sql_insert = """INSERT INTO TPS09_Feedback (FeedCode, CusCode, point, DW09_Feedback, KnowFrom, timestamp, Favorite_place) VALUES (:1, :2, :3, :4, :5, TO_DATE(:6,'DD/MM/YYYY'), :7)"""
# ___________________________________________________

url = "http:///{}:{}@localhost:5984/{}/"
username = 'admin'
password = 'password'
tableName = 'feedback_01'

database_path = url.format(username, password, tableName)
keep_dic = {}

#get all json key in database
response = curl_request(database_path + "_all_docs")
all_dic = json.loads(response)

#get json by its key from previous code 
for a in all_dic["rows"]:
    api_res = curl_request(database_path + a["id"])
    api_dic = json.loads(api_res)

    if(api_dic.get("key") != None):
        # print("type 2")
        data_to_insert = (gen_key(), api_dic["key"]["cusCode"], api_dic["data"]["point"], api_dic["data"]["feedback"], api_dic["data"]["knowFrom"], api_dic["data"]["timestamp"], api_dic["data"]["favorite_place"])
    elif(api_dic.get("key") == None):
        # print("type 1")
        data_to_insert = (gen_key(), api_dic["cusCode"], api_dic["point"], api_dic["feedback"], api_dic["knowFrom"], api_dic["timestamp"], api_dic["favorite_place"])
    else:
        print("!!! something wrong !!!")
        break

    print(data_to_insert)

    cursor.execute(sql_insert, data_to_insert)

    # Commit the transaction
    connection.commit()
    print("Data inserted successfully!")



