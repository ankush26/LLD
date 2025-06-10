class Animal:
    # some common Animal methods
    pass

class Dog(Animal):
    # Additional Dog methods specific to Dogs.
    pass

class Parent:
    def get_animal(self):
        print("Parent: Returning Animal instance")
        return Animal()

class Child(Parent):
    def get_animal(self):
        print("Child: Returning Dog instance")
        return Dog()

class Client:
    def __init__(self, p):
        self.p = p

    def take_animal(self):
        self.p.get_animal()

# Example usage
if __name__ == "__main__":
    parent = Parent()
    child = Child()
    client = Client(child)
    client.take_animal()