# pyproject

#### By Pradip Sapkota

| Routes | Operation Description |
| ----------- | ----------- |
| `http://127.0.0.1:5000/customers` | retrive all the customer details in the database |
| `http://127.0.0.1:5000/company` | retrive all company details in database |
| `http://127.0.0.1:5000/items` | retrive all item details in the database |
| `http://127.0.0.1:5000/inventory` | retrive all inventory detail in database |
| `http://127.0.0.1:5000/insert/customer` | insert customer detail in the customer table |
| `http://127.0.0.1:5000/insert/item` | insert item detail in the item table also automatically update inventory table according to item inserted |
| `http://127.0.0.1:5000/insert/company` | insert company detail in the company table |
| `http://127.0.0.1:5000/item/availability/<item_id>` | check whether the item is available or not |
| `http://127.0.0.1:5000/remove/customer/<customer_id>` | to remove customer detail from customer table in database |
| `http://127.0.0.1:5000/update/item/<item_id>` | to update item details in the database by passing json in the body |
| `http://127.0.0.1:5000/update/customer/<customer_id>` | to update customer details in the database by passing json in the body |
| `http://127.0.0.1:5000/update/company/<company_id>` | to update company details in the database by passing json in the body |
| `http://127.0.0.1:5000/totalstock` | to get the total stocks available |



# Pandas endpoints
#### By Saurav Karki

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
