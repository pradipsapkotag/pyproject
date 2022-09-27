from crypt import methods
from databasedata import password, username ,host, port

from sqlalchemy import Boolean, column, create_engine, MetaData, Table, null
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String,BigInteger
from sqlalchemy.orm import sessionmaker,relationship
from flask import Flask,jsonify,request
import json
from sqlalchemy.sql import func
from sqlalchemy.types import Boolean, Date
from random import randint,choice
import pandas as pd
from sqlalchemy.exc import IntegrityError


app = Flask(__name__) 

Base = declarative_base()



engine = create_engine(f"mysql+pymysql://{username()}:{password()}@{host()}:{port()}/pyproject",echo= True)
metadata_obj = MetaData(bind=engine)
MetaData.reflect(metadata_obj)
connection = engine.connect()
Session = sessionmaker(bind = engine)
session = Session()





# CREATE TABLE Customer (
# customer_id int not null primary key,
# customer_name varchar(50),
# customer_address varchar(80),
# customer_phone int,
# customer_email varchar(60)
# );
class Customer(Base):
    __tablename__='customer'
    
    customer_id = Column(Integer,nullable = False,primary_key = True)
    customer_name= Column(String(50),nullable = False)
    customer_address=Column(String(80),nullable= True)
    customer_phone=Column(Integer, nullable = True)
    customer_email=Column(String(60),nullable = True)
    
    def __repr__(self):
        return (f'customer_id={self.customer_id},customer_name={self.customer_name},customer_address={self.customer_address},customer_phone={self.customer_phone},customer_email={self.customer_email}')	

# CREATE TABLE Company(
# company_id int not null primary key,
# company_name varchar(60),
# company_address varchar(60),
# company_phone int,
# company_email varchar(60)
# );

class Company(Base):
    __tablename__ = 'company'

    company_id = Column(Integer,primary_key = True, nullable = True)
    company_name = Column(String(60),nullable= False)
    company_address = Column(String(60),)
    company_phone = Column(Integer,nullable = False)
    company_email = Column(String(60),nullable = True)
    def __repr__(self):
        return(f'company_id={self.company_id},caomany_name = {self.company_name}, company_address={self.company_address}, company_phone={self.company_phone}, company_email = {self.company_email} ')

# CREATE TABLE Items(
# item_id int not null primary key,
# item_name varchar(60),
# item_brand varchar(60),
# item_price int,
# item_quantity int,
# item_availablity bool
# );
class Item(Base):
    __tablename__ = 'items'

    item_id = Column(Integer, primary_key = True,nullable = False)
    item_name = Column(String(60),nullable= False)
    item_brand = Column(String(60),nullable =True)
    item_price = Column(Integer(),nullable = True)
    item_quantity = Column(Integer(),nullable = False)
    
    
    def __repr__(self):
        return(f'item_id={self.item_id}, item_name = {self.item_name}, item_brand={self.item_brand}, item_price={self.item_price},item_quantit={self.item_quantity}')

# CREATE TABLE Inventory (
# inventory_id int not null primary key,
# inventory_name varchar(60),
# item_id int,
# FOREIGN KEY (item_id)
# 		REFERENCES Items(item_id)
# );

class Inventory(Base):
    __tablename__ = 'inventory'

    inventory_id = Column(Integer, primary_key = True,nullable = False)
    inventory_name = Column(String(60),nullable = False)
    item_id = Column(Integer(), ForeignKey('items.item_id'))
    
    
    def __repr__(self):
        return (f'inventory_id={self.inventory_id}, inventory_name = {self.inventory_name}, item_id={self.item_id}')
    
    
    
## create tables in database
@app.route('/create',methods = ['GET', 'POST'])
def create_table():
    Base.metadata.create_all(engine) 
    status = {'status':'success','message':'tables created successfully'}
    return (status)







## return customer details
@app.route('/customers',methods = ['GET'])
def customerdetail():
    sql = 'SELECT * FROM customer;'
    with engine.connect() as conn:
        query = conn.execute(sql) 
    results=query.fetchall()
    response_data =[]
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
            'status':'success',
            'customer_data':response_data
        })

    except:
        return jsonify({
            'status':'failed',
            'message':'data not found'
        })




## return company details
@app.route('/company',methods = ['GET'])
def companydetail():
    sql = 'SELECT * FROM company;'
    with engine.connect() as conn:
        query = conn.execute(sql) 
    results=query.fetchall()
    response_data =[]
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
            'status':'success',
            'company_data':response_data
        })

    except:
        return jsonify({
            'status':'failed',
            'message':'data not found'
        }) 


## show item detail
@app.route('/items',methods = ['GET'])
def itemsdetail():
    sql = 'SELECT * FROM items;'
    with engine.connect() as conn:
        query = conn.execute(sql) 
    results=query.fetchall()
    response_data =[]
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
            'status':'success',
            'company_data':response_data
        })

    except:
        return jsonify({
            'status':'failed',
            'message':'data not found'
        }) 






## show inventory detail
@app.route('/inventory',methods = ['GET'])
def inventorydetail():
    sql = 'SELECT * FROM inventory;'
    with engine.connect() as conn:
        query = conn.execute(sql) 
    results=query.fetchall()
    response_data =[]
    try:
        for result in results:
            data_dict = dict()
            data_dict['inventory_id'] = result.inventory_id
            data_dict['inventory_name'] = result.inventory_name
            data_dict['item_id'] = result.item_id
        
            response_data.append(data_dict)
        
        return jsonify({
            'status':'success',
            'company_data':response_data
        })

    except:
        return jsonify({
            'status':'failed',
            'message':'data not found'
        }) 





## insert customer

@app.route('/insert/customer', methods=['POST'])
def insertcustomer():
    try:
        params = request.get_json(silent= True,force =True)
        customer_id = params["customer_id"]
        customer_name = params["customer_name"]
        customer_address= params["customer_address"]
        customer_phone = params["customer_phone"]
        customer_email=params["customer_email"]
        customer = Customer(customer_id = customer_id,customer_name=customer_name,customer_address=customer_address,customer_phone=customer_phone,customer_email=customer_email)
        session.add(customer)
        session.commit()
        return jsonify({
                'status': 'success',
                'message': 'Customer insertion successful',
                'data': {
                    'recods_inserted': params
                }
            })
    except IntegrityError as ie:
        session.rollback()
        return jsonify({
            'status': "failed",
            'message': "Duplicate input: sustomer exists in database" if ie.orig.args[0] == 1062\
                        else "Invalid input",
            'data': {}
        })
    




## insert item and inventory
@app.route('/insert/item', methods=['POST'])
def insertitem():
    try:
        params = request.get_json(force=True,silent=True)
        item_id = params["item_id"]
        item_name = params["item_name"]
        item_brand= params["item_brand"]
        item_price = params["item_price"]
        item_quantity=params["item_quantity"]
        item_inventory = params["item_inventory"]
        item = Item(item_id = item_id,item_name=item_name,item_brand=item_brand,item_price=item_price,item_quantity=item_quantity)
        session.add(item)
    
        sql = 'SELECT * FROM inventory;'
        with engine.connect() as conn:
            query = conn.execute(sql) 
        inventory_id=query.fetchall()[-1].inventory_id+1
        print(f'inventory_id:{inventory_id}')
        item= session.query(Item).filter_by(item_id = item_id).first()
        inventory = Inventory(inventory_id = inventory_id,inventory_name = item_inventory,item_id = item.item_id)
        session.add(inventory)
        session.commit()
        return jsonify({
                'status': 'success',
                'message': 'item insertion successful',
                'data': {
                    'recods_inserted': params
                }
            })
    except IntegrityError as ie:
        session.rollback()
        return jsonify({
            'status': "failed",
            'message': "Duplicate input: item exists in database" if ie.orig.args[0] == 1062\
                        else "Invalid input",
            'data': {}
        })




## insert company
@app.route('/insert/company', methods=['POST'])
def insertcompany():
    try:
        params = request.get_json(force=True,silent=True)
        company_id = params["company_id"]
        company_name = params["company_name"]
        company_address =params["company_address"]
        company_phone= params['company_phone']
        company_email = params["company_email"]
        company = Company(company_id = company_id,company_name= company_name,company_address=company_address,company_phone=company_phone,company_email=company_email)
        session.add(company)
    
        session.commit()
        return jsonify({
                'status': 'success',
                'message': 'company insertion successful',
                'data': {
                    'recods_inserted': params
                }
            })
    except IntegrityError as ie:
        session.rollback()
        return jsonify({
            'status': "failed",
            'message': "Duplicate input: company exists in database" if ie.orig.args[0] == 1062\
                        else "Invalid input",
            'data': {}
        })


### check availability of item
@app.route('/item/availability/<int:item_id>', methods=['GET'])
def itemavailability(item_id):
    item= session.query(Item).filter_by(item_id = item_id).first()
    if(item.item_quantity>=1):
        return jsonify({
                'status': 'success',
                'message': 'item available',
                'item_quantity': item.item_quantity
            })
    else:
        return jsonify({
                'status': 'failed',
                'message': 'item out of stock',
            })






## delete customer according to id

@app.route('/remove/customer/<int:customer_id>', methods=['GET','POST'])
def removecustomer(customer_id):
    
    try:
        result =session.query(Customer).filter_by(customer_id = customer_id).first()
        if(result.customer_id == customer_id):
            session.query(Customer).filter_by(customer_id = customer_id).delete()
            session.commit()
            return jsonify({
                    'status': 'success',
                    'message': 'customer deleted successfully',
                    'customer_id': customer_id
                })
        else:
            raise Exception('dataerror')
    except:
        return jsonify({
                'status': 'failed',
                'message': 'customer not found',
                'customer_id': customer_id
            })





@app.route('/update/item/<int:item_id>',methods=['PUT'])
def updateitem(item_id):
    try:
        pass

    except:
        pass

if __name__ == '__main__':
    # create_table()
    # add_new_person(3)
    app.run(debug=True)