from src.product import Product

class StoreInventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product_name):
        for product in self.products:
            if product.name.lower() == product_name.lower():
                self.products.remove(product)
                return True

        return False

    def search_by_category(self, category):
        return [
            product
            for product in self.products
            if product.category.lower() == category.lower()
        ]

    def list_inventory(self):
        for product in self.products:
            print(product)