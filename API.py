from flask import Flask
from flask import jsonify
from flask import request
from getAllTransactions import getTransactions
#from pymongo import MongoClient

app = Flask(__name__)

@app.route("/getAllTransactions",  methods=['GET','POST'])
def index():
    #conn = MongoClient('mongodb+srv://admin:paperless123@cluster0-lftpp.gcp.mongodb.net/test')
    r = request.form.get("user_id")
    return getTransactions(r)

if __name__ == '__main__':
    app.run()