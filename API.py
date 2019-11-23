from flask import Flask
from flask import request
from flask import render_template
from get_data import findAllTransactions,getUserInfo,getTransaction,createTransaction,getVendorInfo

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.htm")

@app.route('/about/')
def about():
    return render_template("about_us.htm")

@app.route('/login/')
def login():
    return render_template("login_page.htm")

@app.route('/contact_us/')
def contact():
    return render_template("contact_page.htm")

@app.route("/getAllTransactions",  methods=['GET','POST'])
def getTransactions():
    return findAllTransactions(int(request.form.get("user_id")))

@app.route("/getOneTransaction",  methods=['GET','POST'])
def getOneTransaction():
    user_id = int(request.form.get("user_id"))
    invoice_id = int(request.form.get("invoice_id"))
    return getTransaction(user_id, invoice_id)

@app.route("/getUserData",  methods=['GET','POST'])
def getUserData():
    user_id = int(request.form.get("user_id"))
    return getUserInfo(user_id)

@app.route("/createNewTransaction",  methods=['GET','POST'])
def newTransaction():
    date_of_transaction = request.form.get("date_of_transaction")
    time_of_transaction = request.form.get("time_of_transaction")
    user_id = int(request.form.get("user_id"))
    vendor_id = int(request.form.get("vendor_id"))
    invoice_id = int(request.form.get("invoice_id"))
    # should be passed in by a one-line argument as a string list
    items_purchased = request.form.get("items_purchased")

    return createTransaction(user_id,date_of_transaction,time_of_transaction,vendor_id,invoice_id,items_purchased)

@app.route("/getVendorData",  methods=['GET','POST'])
def getVendorData():
    vendor_id = int(request.form.get("vendor_id"))
    return getVendorInfo(vendor_id)

if __name__ == '__main__':
    app.run(debug=True)
