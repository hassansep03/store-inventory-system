class OrderProcessor:
    def __init__(self, inventory):
        self.inventory = inventory

    def create_order(self, items):
        order_items = []
        subtotal = 0

        for product_name, quantity in items:
            product = self.find_product(product_name)

            if product is None:
                raise ValueError(f"Product not found: {product_name}")

            if quantity <= 0:
                raise ValueError("Quantity must be greater than 0")

            if product.stock_quantity < quantity:
                raise ValueError(
                    f"Not enough stock for {product.name}"
                )

            product.stock_quantity -= quantity

            item_total = product.price * quantity
            subtotal += item_total

            order_items.append({
                "product": product.name,
                "quantity": quantity,
                "price": product.price,
                "total": item_total
            })

        discount = round(self.calculate_discount(subtotal), 2)
        total = round(subtotal - discount, 2)

        return {
            "items": order_items,
            "subtotal": subtotal,
            "discount": discount,
            "total": total
        }

    def find_product(self, product_name):
        for product in self.inventory.products:
            if product.name.lower() == product_name.lower():
                return product

        return None

    def calculate_discount(self, subtotal):
        if subtotal < 100:
            return 0

        if subtotal < 500:
            return subtotal * 0.05

        if subtotal < 1000:
            return subtotal * 0.10

        return subtotal * 0.15