# filepath: c:\Users\ankus\Desktop\LLD\LLD\Lecture 05\Python Code\OCP\OCP_followed.py
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

class InvoicePrinter:
    @staticmethod
    def print_invoice(cart):
        print("Shopping Cart Invoice:")
        for product in cart.products:
            print(f"{product.name} - Rs {product.price}")
        print(f"Total: Rs {cart.calculate_total()}")

# Example usage
if __name__ == "__main__":
    cart = ShoppingCart()
    cart.add_product(Product("Laptop", 50000))
    cart.add_product(Product("Mouse", 2000))
    
    InvoicePrinter.print_invoice(cart)