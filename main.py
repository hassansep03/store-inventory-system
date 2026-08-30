# from src.product import Product

# product = Product(
#     "Laptop",
#     "Electronics",
#     999.99,
#     5
# )

# print(product)

# from src.product import Product

# product = Product(
#     "Laptop",
#     "Electronics",
#     0,
#     5
# )

# print(product)

# from src.product import Product


# product = Product(
#     "Laptop",
#     "Electronics",
#     999.99,
#     -1
# )

# print(product)

# from src.product import Product


# product = Product(
#     "Laptop",
#     "Electronics",
#     999.99,
#     5
# )

# print(product)

# product.price = 1099.99
# product.stock_quantity = 10

# print(product)

# from src.product import Product
# from src.inventory import StoreInventory


# inventory = StoreInventory()

# laptop = Product("Laptop", "Electronics", 999.99, 5)
# phone = Product("Phone", "Electronics", 699.99, 10)
# desk = Product("Desk", "Furniture", 250.00, 3)

# inventory.add_product(laptop)
# inventory.add_product(phone)
# inventory.add_product(desk)

# print("All Products:")
# inventory.list_inventory()

# print("\nElectronics:")
# electronics = inventory.search_by_category("electronics")

# for product in electronics:
#     print(product)

# print("\nRemoving laptop:")
# inventory.remove_product("LAPTOP")

# inventory.list_inventory()

# from src.product import Product
# from src.inventory import StoreInventory
# from src.order import OrderProcessor


# inventory = StoreInventory()

# laptop = Product("Laptop", "Electronics", 999.99, 5)
# phone = Product("Phone", "Electronics", 699.99, 10)

# inventory.add_product(laptop)
# inventory.add_product(phone)

# order_processor = OrderProcessor(inventory)

# order = order_processor.create_order([
#     ("Laptop", 10)
# ])

# print("Order:")
# print(order)

# print("\nRemaining Stock:")
# inventory.list_inventory()

# from src.product import Product
# from src.inventory import StoreInventory
# from src.persistence import save_inventory, load_inventory


# inventory = StoreInventory()

# laptop = Product("Laptop", "Electronics", 999.99, 5)
# phone = Product("Phone", "Electronics", 699.99, 10)

# inventory.add_product(laptop)
# inventory.add_product(phone)

# save_inventory(inventory, "inventory.json")

# print("Inventory saved.")

# loaded_inventory = load_inventory("inventory.json")

# print("\nLoaded Inventory:")
# loaded_inventory.list_inventory()


from src.product import Product
from src.inventory import StoreInventory
from src.order import OrderProcessor
from src.persistence import save_inventory, load_inventory


# Create inventory
inventory = StoreInventory()

# Create products
laptop = Product("Laptop", "Electronics", 999.99, 5)
phone = Product("Phone", "Electronics", 699.99, 10)
desk = Product("Desk", "Furniture", 250.00, 3)

# Add products
inventory.add_product(laptop)
inventory.add_product(phone)
inventory.add_product(desk)

# Display inventory
print("All Products:")
inventory.list_inventory()

# Search by category
print("\nElectronics:")
for product in inventory.search_by_category("electronics"):
    print(product)

# Create an order
order_processor = OrderProcessor(inventory)

order = order_processor.create_order([
    ("Laptop", 1),
    ("Phone", 1)
])

print("\nOrder:")
print(order)

# Show remaining stock
print("\nRemaining Stock:")
inventory.list_inventory()

# Save inventory
save_inventory(inventory, "inventory.json")
print("\nInventory saved.")

# Load inventory
loaded_inventory = load_inventory("inventory.json")

print("\nLoaded Inventory:")
loaded_inventory.list_inventory()