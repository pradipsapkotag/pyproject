from multiprocessing import connection
from sqlite3 import IntegrityError
from sqlalchemy.orm import sessionmaker,relationship
from flask import Flask,jsonify,request
from sqlalchemy import create_engine, Table,MetaData,insert,select
from sqlalchemy.ext.declarative import declarative_base
import json
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Date
import pandas as pd



'''FOR MYSQL'''
engine = create_engine('mysql+mysqldb://root:mounteverest8848@localhost:3306/Inventory_Management')
metadata_obj = MetaData(bind=engine)
connection = engine.connect()

'''FOR SQL LITE'''
# engine = create_engine('sqlite:///inventory1.db', echo=True)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()
app = Flask(__name__)

# Model
#Company
class company(Base):
    __tablename__ = 'Company'

    company_id = Column(Integer(), primary_key = True,nullable=False)
    company_name = Column(String(60))
    company_address = Column(String(60))
    company_phone = Column(Integer())
    company_email = Column(String())
    def __repr__(self) -> str:
        return super().__repr__()

#Customer
class customer(Base):
    __tablename__ = 'Customer'

    customer_id = Column(Integer(), primary_key = True)
    customer_name = Column(String(60))
    customer_address = Column(String(60))
    customer_phone = Column(Integer())
    customer_email = Column(String(60))
    def __repr__(self) -> str:
        return super().__repr__()

#item
class items(Base):
    __tablename__ = 'Items'

    item_id = Column(Integer(), primary_key = True)
    item_name = Column(String(60))
    item_brand = Column(String(60))
    item_price = Column(Integer())
    item_quantity = Column(Integer())
    item_availabiltiy = Column(Boolean())

#Iventory
class inventory(Base):
    __tablename__ = 'Inventory'

    inventory_id = Column(Integer(), primary_key = True)
    inventory_name = Column(String(60))
    i_id = Column(Integer(), ForeignKey('Item.item_id'))
    def __repr__(self) -> str:
        return super().__repr__()

def create_table():
    Base.metadata.create_all(engine)


#Retrive all Customer_data
@app.route('/api/customers',methods=['GET'])
def all_customers():
    customers = Table('Customer',metadata_obj,autoload=True,autoload_with=engine)
    stmt = select([customers])
    results = connection.execute(stmt).fetchall()
    response_data = []
    
    try:
        for result in results:
            data_dict = dict()
            data_dict['customer_id'] = result.customer_id
            data_dict['customer_name'] = result.customer_name
            data_dict['customer_address'] = result.customer_address
            data_dict['customer_phone'] = result.customer_phone
            data_dict['customer_email'] = result.customer_email
            response_data.append(data_dict)
        
        return jsonify({
            'status':200,
            'customer_data':response_data
        })

    except:
        return jsonify({
            'status':400,
            'message':'data not found'
        })

# Retrive all  items_data
@app.route('/api/items',methods=['GET'])
def all_items():
    item = Table('Items',metadata_obj,autoload=True,autoload_with=engine)
    stmt = select([item])
    results = connection.execute(stmt).fetchall()
    response_data = []
    
    try:
        for result in results:
            data_dict = dict()
            data_dict['item_id'] = result.item_id
            data_dict['item_name'] = result.item_name
            data_dict['item_brand'] = result.item_brand
            data_dict['item_price'] = result.item_price
            data_dict['item_quantity'] = result.item_quantity
            response_data.append(data_dict)
        
        return jsonify({
            'status':200,
            'items':response_data
        })

    except:
        return jsonify({
            'status':400,
            'message':'data not found'
        })   


#Retrive all company_data
@app.route('/api/company',methods=['GET'])
def all_company():
    company = Table('Company',metadata_obj,autoload=True,autoload_with=engine)
    stmt = select([company])
    results = connection.execute(stmt).fetchall()
    response_data = []
    
    try:
        for result in results:
            data_dict = dict()
            data_dict['company_id'] = result.company_id
            data_dict['company_name'] = result.company_name
            data_dict['company_address'] = result.company_address
            data_dict['company_phone'] = result.company_phone
            data_dict['company_email'] = result.company_email
            response_data.append(data_dict)
        
        return jsonify({
            'status':200,
            'company_data':response_data
        })

    except:
        return jsonify({
            'status':400,
            'message':'data not found'
        }) 

#Retrive all inventory_data
@app.route('/api/inventory',methods=['GET'])
def all_inventory():
    inventory = Table('Inventory',metadata_obj,autoload=True,autoload_with=engine)
    stmt = select([inventory])
    results = connection.execute(stmt).fetchall()
    response_data = []
    
    try:
        for result in results:
            data_dict = dict()
            data_dict['inventory_id'] = result.inventory_id
            data_dict['inventory_name'] = result.inventory_name
            data_dict['item_id'] = result.item_id
            response_data.append(data_dict)
        
        return jsonify({
            'status':200,
            'inventory_data':response_data
        })

    except:
        return jsonify({
            'status':400,
            'message':'data not found'
        }) 


# ******POST METHODS********

#Insert Customer Data
@app.route('/api/insert_customer',methods=['POST'])
def insert_customer():
    body = request.get_json()
    customer = Table('Customer',metadata_obj,autoload=True,autoload_with=engine)
    stmt = insert(customer)

    try:
        connection.execute(stmt,body)
        return jsonify({
            'status':200,
            'message':'New Customer data inserted Successfully',
            'customer_data':body
        })
    
    except IntegrityError as ie:
        return jsonify({
            'status': 400,
            'message': "Duplicate input: program_code exists in database" if ie.orig.args[0] == 1062\
                        else "Invalid input",
            'data': {}
        })

    except:
        return jsonify({
            'status': 400,
            'message': "Duplicate input: program_code exists in database",
            'data': {}
            }) 


#Insert New Company Data
@app.route('/api/insert_company',methods=['POST'])
def insert_company():
    body = request.get_json()
    company = Table('Company',metadata_obj,autoload=True,autoload_with=engine)
    stmt = insert(company)

    try:
       connection.execute(stmt,body)
       return jsonify({
        "status":200,
        "message":"New Company details added successfully",
        "company_details":body
       })     
    except:
        return jsonify({
            'status': 400,
            'message': "Duplicate input: program_code exists in database",
            'data': {}
        })      

#Insert new items
@app.route('/api/insert_items',methods=['POST'])
def insert_items():
    body = request.get_json()
    items= Table('Items',metadata_obj,autoload=True,autoload_with=engine)
    stmt = insert(items)

    try:
       connection.execute(stmt,body)
       return jsonify({
        "status":200,
        "message":"New Company details added successfully",
        "company_details":body
       })  
         
    except:
        return jsonify({
            'status': 400,
            'message': "Duplicate input: program_code exists in database",
            'data': {}
        })    

#Insert new Iventory
@app.route('/api/insert_inventory',methods=['POST'])
def insert_inventory():
    body = request.get_json()
    inventory= Table('Inventory',metadata_obj,autoload=True,autoload_with=engine)
    stmt = insert(inventory)

    try:
       connection.execute(stmt,body)
       return jsonify({
        "status":200,
        "message":"New invemtory details added successfully",
        "company_details":body
       })  
         
    except:
        return jsonify({
            'status': 400,
            'message': "Duplicate input: program_code exists in database",
            'data': {}
        })  


#PANDAS IMPLEMENTATION

#Q1 Show the all attributes of Company table.
@app.route('/api/company_attributes',methods=['GET'])
def company_attributes():
    df = pd.read_sql("SELECT * FROM Customer",connection)
    attributes= df.columns  
    parsed = attributes.tolist()

    try:
       print(parsed) 
       return jsonify({  
        "status":200,
        "message":"Data loaded successfully",
        "columns":parsed
        # "data":json.loads( df.to_json(orient='index'))
       })  
         
    except:
        return jsonify({
            'status': 400,
            'message': "Invalid url or resource not found",
            'data': {}
        })  

#Q2. Show the item list where the item_price is at least 25000.
@app.route('/api/items_info',methods=['GET'])
def items_info():
  stmt = '''SELECT * FROM Items '''
  df = pd.read_sql(stmt,connection)  
  itms = df[df.item_price >= 25000] 
  try:
       print(itms) 
       return jsonify({  
        "status":200,
        "message":"Data loaded successfully",
        "data":json.loads(itms.to_json(orient='index'))
       })       
  except:
        return jsonify({
            'status': 400,
            'message': "Invalid url or resource not found",
            'data': {}
        }) 


# Q.3 How many items does the Items dataframe contains?
@app.route('/api/items_quantity',methods=['GET'])
def total_items_quantity():
    df = pd.read_sql("SELECT * FROM Items",connection)
    item_quantity=df.item_quantity.sum()
    try:
       print(item_quantity) 
       return jsonify({  
        "status":200,
        "message":"Data loaded successfully",
        "data":"Total items in Item table: "+str(item_quantity)
       })  
         
    except:
        return jsonify({
            'status': 400,
            'message': "Invalid url or resource not found",
            'data': {}
        })  


# Q.4 Which item does have highest quantity available in stock?
@app.route('/api/max_quantity',methods=['GET'])
def max_item_quantity():
    df = pd.read_sql("SELECT * FROM Items",connection)
    # item_quantity=df.item_quantity.max()
    df=df.sort_values('item_quantity',ascending=False)
    max_item_quantity=df.head(1)
    try:
       print(max_item_quantity) 
       return jsonify({  
        "status":200,
        "message":"Data loaded successfully",
        "max_quantity_item":json.loads(max_item_quantity.to_json(orient='index'))
       })  
         
    except:
        return jsonify({
            'status': 400,
            'message': "Invalid url or resource not found",
            'data': {}
        })  
      
# Q.5 Which is the most 5 expensive amongst all the items?
@app.route('/api/top5_expensive',methods=['GET'])
def top5_item_quantity():
    df = pd.read_sql("SELECT * FROM Items",connection)
    # item_quantity=df.item_quantity.max()
    df=df.sort_values('item_price',ascending=False)
    top5_expensive=df.head(5)
    try:
       print(top5_expensive) 
       return jsonify({  
        "status":200,
        "message":"Data loaded successfully",
        "top5_expensive_item":json.loads(top5_expensive.to_json(orient='index'))
       })  
         
    except:
        return jsonify({
            'status': 400,
            'message': "Invalid url or resource not found",
            'data': {}
        }) 

# Q.6 Create a dataframe having total price of item according to its quantity available?
@app.route('/api/total_price',methods=["GET"])
def total_item_price():
    df = pd.read_sql("SELECT * FROM Items",connection)
    total_item_price = df
    # item_quantity=df.item_quantity.max()
    total_item_price['Total Price'] = df['item_price'] * df['item_quantity']
    try:
       print(total_item_price) 
       return jsonify({  
        "status":200,
        "message":"Data loaded successfully",
        "data":json.loads(total_item_price.to_json(orient='index'))
       })  
         
    except:
        return jsonify({
            'status': 400,
            'message': "Invalid url or resource not found",
            'data': {}
        }) 

#Q.7 Return a dataframe that has null values.
@app.route('/api/check_null',methods=["GET"])
def check_null_values():
    df = pd.read_sql("SELECT * FROM Items",connection)
    df['item_price'].isna()
    try:
           print(df['item_price'].isna()) 
           return jsonify({  
            "status":200,
            "message":"Items has No Null Columns",
            "data":list(df['item_price'].isna())
           })  
         
    except:
        return jsonify({
            'status': 400,
            'message': "Invalid url or resource not found",
            'data': {}
        }) 

#Q.8 Create a dataframe that returns inventory_id,inventory_name,item_name.
@app.route('/api/return_req_data',methods=["GET"])
def req_data():
    stmt = '''SELECT i.inventory_id,i.inventory_name,sum(it.item_quantity) AS item_quantity FROM
              Inventory i 
              LEFT JOIN Items it
              ON i.item_id = it.item_id
              GROUP BY inventory_name
              '''
    df = pd.read_sql(stmt,connection)   
    try:
       print(df) 
       return jsonify({  
        "status":200,
        "message":"Data loaded successfully",
        "data":json.loads(df.to_json(orient='index'))
       })       
    except:
        return jsonify({
            'status': 400,
            'message': "Invalid url or resource not found",
            'data': {}
        }) 



if __name__ == '__main__':
    create_table()
    app.run(debug=True)

