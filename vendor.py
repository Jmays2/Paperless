from pymongo import MongoClient
import json

class Vendor(object):
    def __init__(self,vendor):
        # connects to the database so that all methods can access this
        # throughout the class
        self.conn = MongoClient('mongodb+srv://admin:paperless123@cluster0-lftpp.gcp.mongodb.net/test')
        self.vendor = vendor

    def populate_vendor_data(self):
        db = self.conn['paperless']['vendor_data']
        vendData = json.load(self.vendor)

        db.insert_one(vendData)
