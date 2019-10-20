from pymongo import MongoClient
import json
#from fpdf import FPDF

class PDFGenerate(object):
    def __init__(self,transaction_invoice:int):
 #       self.pdf = FPDF()
  #      self.pdf.add_page()
        self.conn = MongoClient('mongodb+srv://admin:paperless123@cluster0-lftpp.gcp.mongodb.net/test')
        self.invoice = transaction_invoice

    def template(self):
        db = self.conn['paperless']['transactions'].find({'invoice_id':self.invoice})[0]
        self.generate_vendor_data(db)
        self.generate_customer_data(db)

   #     self.pdf.output("simple_demo.pdf")
        self.conn.close()

    def generate_customer_data(self,transaction):
        db = self.conn['paperless']['user_data'].find({'user_id':transaction['user_id']})[0]

        full_name = "{0}, {1}".format(db['last_name'],db['first_name'])
        items = transaction['items_purchased']
    #    self.pdf.set_font('Arial', 'B', 12)

        i = 1
        subtotal = 0
        for row in items:
            combine = ''
            total_cost = row['quantity_purchased'] * row['item_price']
            subtotal += total_cost
            combine += "%d) %s x (%d)"%(i,row['item_name'],row['quantity_purchased'])
            self.pdf.cell(100, 15, txt=combine, ln=1, align="L")
            total =  '               Total: ${0:.2f}'.format(total_cost)
            self.pdf.cell(100, 1, txt=total, ln=1, align="L")
            i+=1

        #self.pdf.multi_cell(200.0,50.4,txt=subtotal,align="J")
            

    def generate_vendor_data(self,transaction):
        db = self.conn['paperless']['vendor_data'].find({'vendor_id':transaction['vendor_id']})[0]

        name = str(db['vendor_name'])
        address = str(db['vendor_address'])
        number = str(db['vendor_phone'])

        self.pdf.set_font('Arial', 'B', 35)
        self.pdf.cell(200, 17, txt=name, ln=1, align="C")
        self.pdf.set_font('Arial', 'B', 27)
        self.pdf.cell(200,17,txt=number,ln=1,align="C")
        self.pdf.set_font('Arial', 'B', 25)
        self.pdf.cell(200,17,txt=address,ln=1,align="C")
        self.pdf.set_font('Arial', 'B', 19)
        self.pdf.cell(150,20,txt='Cashier Name: Doe, John',ln=1,align='C')
        self.pdf.cell(19,10,txt='Invoice #: %d'%self.invoice,ln=1,align='C')


temp = PDFGenerate(78292)
temp.template()
