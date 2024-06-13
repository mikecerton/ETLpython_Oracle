import subprocess
import json
from random import randint
import os
from dotenv import load_dotenv

load_dotenv()

def curl_request(url):
    command = ['curl', url]
    result = subprocess.run(command, capture_output=True, text=True)
    return json.loads(result.stdout)

def gen_key():
    value = randint(1, 9999)
    return str(value)

def load_data():
    tmp = []
    all_dic = curl_request(database_path + "_all_docs")
    for a in all_dic["rows"]:
        api_dic = curl_request(database_path + a["id"])
        tmp.append([gen_key(), api_dic["cusCode"], api_dic["point"], api_dic["feedback"], api_dic["knowFrom"], api_dic["timestamp"], api_dic["favorite_place"]])
    return tmp

url = "http:///{}:{}@localhost:{}/{}/"
couchDB_username = os.getenv("couchDB_username")
couchDB_password = os.getenv("couchDB_password")
couchDB_port = os.getenv("couchDB_port")
couchDB_tableName = os.getenv("couchDB_tableName")

database_path = url.format(couchDB_username, couchDB_password, couchDB_port, couchDB_tableName)