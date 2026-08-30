import json


def save_inventory(inventory, filename):
    data = []

    for product in inventory.products:
        data.append({
            "name": product.name,
            "category": product.category,
            "price": product.price,
            "stock_quantity": product.stock_quantity
        })

    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

def load_inventory(filename):
    from src.inventory import StoreInventory
    from src.product import Product

    inventory = StoreInventory()

    with open(filename, "r") as file:
        data = json.load(file)

    for item in data:
        product = Product(
            item["name"],
            item["category"],
            item["price"],
            item["stock_quantity"]
        )

        inventory.add_product(product)

    return inventory