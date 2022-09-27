from multiprocessing import connection
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
class item(Base):
    __tablename__ = 'Item'

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
    stmt = select([customer])
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
            'data':response_data
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
            'data':response_data
        })

    except:
        return jsonify({
            'status':400,
            'message':'data not found'
        })   

if __name__ == '__main__':
    create_table()
    app.run(debug=True)

