from pymongo import MongoClient
from bson.json_util import dumps

def getUser(user_id):
    conn = MongoClient('mongodb+srv://admin:paperless123@cluster0-lftpp.gcp.mongodb.net/test')
    return dumps(conn['paperless']['user_data'].find({"user_id":user_id}))
