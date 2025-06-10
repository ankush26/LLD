class Parent:
    def print_message(self, msg):
        print(f"Parent: {msg}")

class Child(Parent):
    def print_message(self, msg):
        print(f"Child: {msg}")

class Client:
    def __init__(self, parent):
        self.parent = parent

    def execute(self):
        self.parent.print_message("Hello from Client!")

# Example usage
if __name__ == "__main__":
    parent_instance = Parent()
    child_instance = Child()
    
    client_with_parent = Client(parent_instance)
    client_with_child = Client(child_instance)
    
    client_with_parent.execute()
    client_with_child.execute()