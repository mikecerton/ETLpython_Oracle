import subprocess
import json
from random import randint
import os
from dotenv import load_dotenv

load_dotenv()

def curl_request(url):
    command = ['curl', url]
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout

def typeOne(api_dic):
    sql = "INSERT INTO TPS09_Feedback (FeedCode, CusCode, point, DW09_Feedback, KnowFrom, timestamp, Favorite_place) VALUES ({}, {}, {}, '{}', '{}', TO_DATE('{}','DD/MM/YYYY'), {});"
    return sql.format(gen_key(), api_dic["cusCode"], api_dic["point"], api_dic["feedback"], api_dic["knowFrom"], api_dic["timestamp"], api_dic["favorite_place"]) + "\n"
   
def typeTwo(api_dic):
    sql = "INSERT INTO TPS09_Feedback (FeedCode, CusCode, point, DW09_Feedback, KnowFrom, timestamp, Favorite_place) VALUES ({}, {}, {}, '{}', '{}', TO_DATE('{}','DD/MM/YYYY'), {});"
    return sql.format(gen_key(), api_dic["key"]["cusCode"], api_dic["data"]["point"], api_dic["data"]["feedback"], api_dic["data"]["knowFrom"], api_dic["data"]["timestamp"], api_dic["data"]["favorite_place"]) + "\n"

def gen_key():
    value = randint(1, 9999)
    return str(value)

url = "http:///{}:{}@localhost:{}/{}/"
couchDB_username = os.getenv("couchDB_username")
couchDB_password = os.getenv("couchDB_password")
couchDB_port = os.getenv("couchDB_port")
couchDB_tableName = os.getenv("couchDB_tableName")

database_path = url.format(couchDB_username, couchDB_password, couchDB_port, couchDB_tableName)
keep_dic = {}

#get all json key in database
response = curl_request(database_path + "_all_docs")
all_dic = json.loads(response)
keepAllSQL = ""

#get json by its key from previous code 
for a in all_dic["rows"]:
    api_res = curl_request(database_path + a["id"])
    api_dic = json.loads(api_res)

    if(api_dic.get("key") != None):
        keepAllSQL += typeTwo(api_dic)
    else:
        keepAllSQL += typeOne(api_dic)

print(keepAllSQL)





