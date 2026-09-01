# Store Inventory System

A simple Python-based store inventory and order processing system.

## Features

- Create and manage products
- Add and remove products from inventory
- Search products by category
- Display inventory
- Create orders
- Check product availability and stock
- Calculate discounts
- Save inventory to a JSON file
- Load inventory from a JSON file

## How to Run

Make sure Python 3 is installed.

Run:
python main.py

## Discount Table

| Subtotal | Discount |
|---|---:|
| Less than $100 | 0% |
| $100 - $199.99 | 5% |
| $200 - $499.99 | 10% |
| $500 or more | 15% |


 ## Testing and Verification

The application was tested by running `main.py` and verifying:

- Products can be added and displayed.
- Products can be searched by category.
- Products can be removed from inventory.
- Orders are created successfully.
- Discounts are calculated correctly.
- Stock is reduced after an order.
- Invalid products and insufficient stock are handled with errors.
- Inventory can be saved to and loaded from a JSON file.