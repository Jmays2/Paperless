from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = MongoClient("mongodb+srv://cwilson:Cps41906243@cluster0-lftpp.gcp.mongodb.net/test")
db=client.cwilson
# Issue the serverStatus command and print the results
serverStatusResult=db.command("serverStatus")
pprint(serverStatusResult)

#class User(object):

#	firstName
#	lastName 
#	card_digits = ""
#	userID

	
