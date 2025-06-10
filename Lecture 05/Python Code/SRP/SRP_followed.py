# filepath: c:\Users\ankus\Desktop\LLD\LLD\Lecture 05\Python Code\SRP\SRP_followed.py
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
        return sum(product.price for product in self.products)

class ShoppingCartPrinter:
    def __init__(self, cart):
        self.cart = cart

    def print_invoice(self):
        print("Shopping Cart Invoice:")
        for product in self.cart.products:
            print(f"{product.name} - Rs {product.price}")
        print(f"Total: Rs {self.cart.calculate_total()}")