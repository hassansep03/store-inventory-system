
class Product:
    def __init__(self, name, category, price, stock_quantity):
        self.name = name
        self.category = category
        self.price = price
        self.stock_quantity = stock_quantity

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError("Price must be greater than 0")
        self.__price = value

    @property
    def stock_quantity(self):
        return self.__stock_quantity

    @stock_quantity.setter
    def stock_quantity(self, value):
        if value < 0:
            raise ValueError("Stock quantity cannot be negative")
        self.__stock_quantity = value

    def __str__(self):
        return f"{self.name} ({self.category}) - ${self.price:.2f} | Stock: {self.stock_quantity}"
