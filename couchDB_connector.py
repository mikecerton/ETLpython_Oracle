import subprocess
import json
from random import randint
import os
from dotenv import load_dotenv

load_dotenv()

# connect to CouchDB using API
def curl_request(url):
    command = ['curl', url]
    result = subprocess.run(command, capture_output=True, text=True)
    return json.loads(result.stdout)

def gen_key():
    value = randint(1, 9999)
    return str(value)

# fetch data from CouchDB using API
def load_data():
    tmp = []
    all_dic = curl_request(database_path + "_all_docs")
    for a in all_dic["rows"]:
        api_dic = curl_request(database_path + a["id"])
        tmp.append([gen_key(), api_dic["cusCode"], api_dic["point"], api_dic["feedback"], api_dic["knowFrom"], api_dic["timestamp"], api_dic["favorite_place"]])
    return tmp

url = "http:///{}:{}@localhost:{}/{}/"
chDB_username = os.getenv("couchDB_username")
chDB_password = os.getenv("couchDB_password")
chDB_port = os.getenv("couchDB_port")
chDB_tableName = os.getenv("couchDB_tableName")

database_path = url.format(chDB_username, chDB_password, chDB_port, chDB_tableName)