# import from pradip
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
            raise Exception('DataError')
    except:
        return jsonify({
                'status': 'failed',
                'message': 'customer not found',
                'customer_id': customer_id
            })



#### updae item

@app.route('/update/item/<int:item_id>',methods=['POST'])
def updateitem(item_id):
    try:
        params = request.get_json(silent= True,force =True)
        # return params
        # try:
        #     customer_id = params["customer_id"]
        # except:
        #     raise Exception('DataError')
        # try:
        #     customer_name = params["customer_name"]
        # except:
        #     raise Exception('DataError')
        # try:
        #     customer_address= params["customer_address"]
        # except:
        #     raise Exception('DataError')
        # try:
        #     customer_phone = params["customer_phone"]
        # except:
        #     raise Exception('DataError')
        # try:
        #     customer_email=params["customer_email"]
        # except:
        #     raise Exception('DataError')
        update_query = session.query(Item).filter_by(item_id = item_id).update(params)
        session.commit()
        return jsonify({
            'status': "success",
            'message': "updated database",
            'data': params
        })
        

    except:
        return jsonify({
            'status': "failed",
            'message': "Invalid Entry",
            'data': {}
        })



## update customer
@app.route('/update/customer/<int:customer_id>',methods=['POST'])
def updatecustomer(customer_id):
    try:
        params = request.get_json(silent= True,force =True)
        update_query = session.query(Customer).filter_by(customer_id = customer_id).update(params)
        session.commit()
        return jsonify({
            'status': "success",
            'message': "updated database",
            'data': params
        })
        

    except:
        return jsonify({
            'status': "failed",
            'message': "Invalid Entry",
            'data': {}
        })



## update company
@app.route('/update/company/<int:company_id>',methods=['POST'])
def updatecompany(company_id):
    try:
        params = request.get_json(silent= True,force =True)
        update_query = session.query(Company).filter_by(company_id = company_id).update(params)
        session.commit()
        return jsonify({
            'status': "success",
            'message': "updated database",
            'data': params
        })
        

    except:
        return jsonify({
            'status': "failed",
            'message': "Invalid Entry",
            'data': {}
        })


## total item in the stock
@app.route('/totalstock',methods=['GET'])
def totalstock():
    sql = 'SELECT * FROM items;'
    with engine.connect() as conn:
        query = conn.execute(sql)
    result = query.fetchall()
    total_stock = 0
    for item in result:
        total_stock += item.item_quantity
    return jsonify({
            'status': "success",
            'totalstock': total_stock,
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





# Q.7 Calculate the average item_price from all total items available.
@app.route('/api/average_price',methods=["GET"])
def average_price():
    df = pd.read_sql("SELECT * FROM Items",connection)
    total_item_price = df
    # item_quantity=df.item_quantity.max()
    total_item_price['Total Price'] = df['item_price'] * df['item_quantity']
    avg=total_item_price['Total Price'].mean()
    try:
       print(avg) 
       return jsonify({  
        "status":200,
        "message":"The average price is:"+ str(avg),
       })  
         
    except:
        return jsonify({
            'status': 400,
            'message': "Invalid url or resource not found",
            'data': {}
        })






#Q.8 Check whether if price have null values or not.
@app.route('/api/check_null',methods=["GET"])
def check_null_values():
    df = pd.read_sql("SELECT * FROM Items",connection)
    df['item_price'].isna()
    total = df.item_price.count()
    non_null_count = df['item_price'].isna().count()
    try:
           print(df['item_price'].isna())
           return jsonify({  
            "status":200,
            "price":list(df['item_price'].isna()),
            "price_column_count":int(total),
            "non_null_price":int(non_null_count)
           })  
         
    except:
        return jsonify({
            'status': 400,
            'message': "Invalid url or resource not found",
            'data': {}
        }) 



#Q.9 Create a dataframe that returns inventory_id,inventory_name,item_name.
@app.route('/api/return_req_data',methods=["GET"])
def req_data():
    stmt = '''SELECT i.inventory_name,sum(it.item_quantity) AS item_quantity FROM
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
    # create_table()
    # add_new_person(3)
    app.run(debug=True)