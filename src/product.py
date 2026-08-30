# class Product:
#     def __init__(self, name, category, price, stock_quantity):
#         self.name = name
#         self.category = category
#         self.price = price
#         self.stock_quantity = stock_quantity

#     @property
#     def price(self):
#         return self._price

#     @price.setter
#     def price(self, value):
#         if value <= 0:
#             raise ValueError("Price must be greater than 0")
#         self._price = value

#     @property
#     def stock_quantity(self):
#         return self._stock_quantity

#     @stock_quantity.setter
#     def stock_quantity(self, value):
#         if value < 0:
#             raise ValueError("Stock quantity cannot be negative")
#         self._stock_quantity = value

#     def __str__(self):
#         return f"{self.name} ({self.category}) - ${self.price:.2f} | Stock: {self.stock_quantity}"

class Product:
    def __init__(self, name, category, price, stock_quantity):
        if price <= 0:
            raise ValueError("Price must be greater than 0")

        if stock_quantity < 0:
            raise ValueError("Stock quantity cannot be negative")

        self.name = name
        self.category = category
        self.price = price
        self.stock_quantity = stock_quantity

    def __str__(self):
        return f"{self.name} ({self.category}) - ${self.price:.2f} | Stock: {self.stock_quantity}"