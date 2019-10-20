from pymongo import MongoClient
from bson.json_util import dumps

conn = MongoClient('mongodb+srv://admin:paperless123@cluster0-lftpp.gcp.mongodb.net/test')

def getUserInfo(user_id):
    return dumps(conn['paperless']['user_data'].find({"user_id":user_id}))

def findAllTransactions(user_id):
    return dumps(conn['paperless']['transactions'].find({"user_id":user_id}))

def getTransaction(user_id,invoice_id):
    return dumps(conn['paperless']['transactions'].find({'$and':[{"user_id":user_id},{"invoice_id":invoice_id}]}))

def createTransaction(*args):
    try:
        db = conn['paperless']['transactions']

        new_transaction = {
            'date_of_transaction': args[0],
            'time_of_transaction': args[1],
            'user_id': args[2],
            'vendor_id': args[3],
            'invoice_id': args[4],
            'items_purchased': args[5],
        }
        
        db.insert_one(new_transaction)

    except:
        return False
    
    return True

def getVendorInfo(vendor_id):
    return dumps(conn['paperless']['vendor_data'].find({"vendor_id":vendor_id}))
