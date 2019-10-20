from flask import Flask
from flask import jsonify
from flask import request
from getAllTransactions import getTransactions
from getOneTransaction import getTransaction
from getUserData import getUser
from create_new_transaction import createTransaction

app = Flask(__name__)

@app.route("/getAllTransactions",  methods=['GET','POST'])
def getAllTransactions():
    user_id = int(request.form.get("user_id"))
    return getTransactions(user_id)

@app.route("/getOneTransaction",  methods=['GET','POST'])
def getOneTransaction():
    user_id = int(request.form.get("user_id"))
    invoice_id = int(request.form.get("invoice_id"))
    return getTransaction(user_id, invoice_id)

@app.route("/getUserData",  methods=['GET','POST'])
def getUserData():
    user_id = int(request.form.get("user_id"))
    return getUser(user_id)

@app.route("/createNewTransaction",  methods=['GET','POST'])
def newTransaction():
    date_of_transaction = request.form.get("date_of_transaction")
    time_of_transaction = request.form.get("time_of_transaction")
    user_id = int(request.form.get("user_id"))
    vendor_id = int(request.form.get("time_of_transaction"))
    invoice_id = int(request.form.get(67767))
    items_purchased = list(request.form.get("items_purchased"))

    return createTransaction(user_id,date_of_transaction,time_of_transaction,vendor_id,invoice_id,items_purchased)

if __name__ == '__main__':
    app.run()