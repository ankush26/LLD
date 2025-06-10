# filepath: c:\Users\ankus\Desktop\LLD\LLD\Lecture 06\Python Code\LSP_Rules\SignatureRules\exception_rule.py

class Parent:
    def risky_method(self):
        print("Parent: Performing a risky operation.")
        raise ValueError("An error occurred in the parent class.")

class Child(Parent):
    def risky_method(self):
        try:
            super().risky_method()
        except ValueError as e:
            print(f"Child: Handling exception - {e}")

def main():
    parent = Parent()
    try:
        parent.risky_method()
    except ValueError as e:
        print(f"Main: Caught an exception from parent - {e}")

    child = Child()
    child.risky_method()

if __name__ == "__main__":
    main()