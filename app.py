from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Date

engine = create_engine('sqlite:///inventory1.db', echo=True)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

# model

class company(Base):
    __tablename__ = 'Company'

    company_id = Column(Integer(), primary_key = True)
    company_name = Column(String)
    company_address = Column(String)
    company_phone = Column(Integer())
    company_email = Column(String())

class customer(Base):
    __tablename__ = 'Customer'

    customer_id = Column(Integer(), primary_key = True)
    customer_name = Column(String)
    customer_address = Column(String)
    customer_phone = Column(Integer())
    customer_email = Column(String())

class item(Base):
    __tablename__ = 'Item'

    item_id = Column(Integer(), primary_key = True)
    item_name = Column(String)
    item_brand = Column(String)
    item_price = Column(Integer())
    item_quantity = Column(Integer())
    item_availabiltiy = Column(Boolean())

class inventory(Base):
    __tablename__ = 'Inventory'

    inventory_id = Column(Integer(), primary_key = True)
    inventory_name = Column(String)
    i_id = Column(Integer(), ForeignKey('Item.item_id'))

def create_table():
    Base.metadata.create_all(engine)

if __name__ == '__main__':
    create_table()
    app.run(host= '127.0.0.3', port=5000, debug=True)
