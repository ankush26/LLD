# filepath: c:\Users\ankus\Desktop\LLD\LLD\Lecture 06\Python Code\DIP\dip_violated.py
# This file demonstrates a violation of the Dependency Inversion Principle.

class MySQLDatabase:
    def save(self, data):
        print(f"Executing SQL Query: INSERT INTO users VALUES('{data}');")

class UserService:
    def __init__(self):
        # Directly instantiating a specific database class
        self.db = MySQLDatabase()

    def store_user(self, user):
        self.db.save(user)

# Example usage
if __name__ == "__main__":
    service = UserService()
    service.store_user("Aditya")