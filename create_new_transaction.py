from pymongo import MongoClient

def createTransaction(*args):
    try:
        conn = MongoClient('mongodb+srv://admin:paperless123@cluster0-lftpp.gcp.mongodb.net/test')
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

#createTransaction(user_id,date_of_transaction,time_of_transaction,vendor_id,invoice_id,items_purchased)
