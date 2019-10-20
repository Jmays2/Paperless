from pymongo import MongoClient
from bson.json_util import dumps

def getTransaction(user_id,invoice_id):
    conn = MongoClient('mongodb+srv://admin:paperless123@cluster0-lftpp.gcp.mongodb.net/test')
    return dumps(conn['paperless']['transactions'].find({'$and':[{"user_id":user_id},{"invoice_id":invoice_id}]}))