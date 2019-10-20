from pymongo import MongoClient
from bson.json_util import dumps

def getTransactions(user_id):
    
    conn = MongoClient('mongodb+srv://admin:paperless123@cluster0-lftpp.gcp.mongodb.net/test')
    return dumps(conn['paperless']['transactions'].find({"user_id":user_id}))

