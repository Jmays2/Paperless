from pymongo import MongoClient

conn = MongoClient('mongodb+srv://admin:paperless123@cluster0-lftpp.gcp.mongodb.net/test')
    

# from pymongo import MongoClient
# # pprint library is used to make the output look more pretty
# from pprint import pprint
# # connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
# client = MongoClient('mongodb+srv://admin:paperless123@cluster0-lftpp.gcp.mongodb.net/test')
# db=client.admin
# # Issue the serverStatus command and print the results
# serverStatusResult=db.command("serverStatus")
# pprint(serverStatusResult)