# pyproject



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


