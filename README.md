# Inventory Management System
### Using API, ORM and Pandas

# End Points 

 - Retrive all  items_data
    - 127.0.0.1:5000/api/items

 - Retrive all company_data 
    - 127.0.0.1:5000/api/company

 - Retrive all inventory_data
    - 127.0.0.1:5000/api/inventory   

 - Insert Customer Data
    - 127.0.0.1:5000/api/insert_customer

 - Insert New Company Data
    - 127.0.0.1:5000/api/insert_company

 - Insert new items
    - 127.0.0.1:5000/insert_items

 - Insert new Iventory
    - 127.0.0.1:5000/api/insert_inventory


# Pandas endpoints

 - Q.1 Show the all attributes of Company table.
     - 127.0.0.1:5000/api/company_attributes

 - Q.2 Show the item list where the item_price is at least 25000.
     - 127.0.0.1:5000/api/items_info

 - Q.3 How many items does the Items dataframe contains?
     - 127.0.0.1:5000/api/items_quantity  

 - Q.4 Which item does have highest quantity available in stock?       
      - 127.0.0.1:5000/api/max_quantity

 - Q.5 Which is the most 5 expensive amongst all the items?
      - 127.0.0.1:5000/api/top5_expensive     

 - Q.6 Create a dataframe having total price of item according to its quantity available?
      - 127.0.0.1:5000/api/total_price   

 - Q.7 Calculate the average item_price from all total items available.
      - 127.0.0.1:5000/api/avg_price   

 - Q.8 Check whether if price have null values or not.
      - 127.0.0.1:5000/api/check_null

 - Q.9 Create a dataframe that returns inventory_name,item_quantity.
      - 127.0.0.1:5000/api/return_req_data    
