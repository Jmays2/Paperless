from pymongo import MongoClient
import json
from fpdf import FPDF

conn = MongoClient('mongodb+srv://admin:paperless123@cluster0-lftpp.gcp.mongodb.net/test')
db = conn['paperless']

vendorTable = db['vendor_data']
customerTable = db['user_data']
transactionTable = db['transactions']

customer = customerTable.find_one({"user_id":2221232135})
company = vendorTable.find_one({"vendor_id":5468938495})
#transaction = transactionTable.find({"user_id":[$eq: customer["user_id"]]})

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="Welcome to Python!", ln=1, align="C")
pdf.output("simple_demo.pdf")
