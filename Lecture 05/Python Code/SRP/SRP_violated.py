# filepath: c:\Users\ankus\Desktop\LLD\LLD\Lecture 05\Python Code\SRP\SRP_violated.py
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def calculate_total(self):
        total = sum(product.price for product in self.products)
        return total

    def print_invoice(self):
        print("Shopping Cart Invoice:")
        for product in self.products:
            print(f"{product.name} - Rs {product.price}")
        print(f"Total: Rs {self.calculate_total()}")

    # Violating SRP - Saves to DB (Should be in a separate class)
    def save_to_database(self):
        print("Saving shopping cart to database...")