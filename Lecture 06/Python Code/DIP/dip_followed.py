class Database:
    def save(self, data):
        raise NotImplementedError("Subclasses must implement this method.")

class MySQLDatabase(Database):
    def save(self, data):
        print(f"Executing SQL Query: INSERT INTO users VALUES('{data}');")

class MongoDBDatabase(Database):
    def save(self, data):
        print(f"Executing MongoDB Function: db.users.insert({{name: '{data}'}});")

class UserService:
    def __init__(self, database: Database):
        self.database = database

    def store_user(self, user):
        self.database.save(user)

if __name__ == "__main__":
    mysql_db = MySQLDatabase()
    mongodb_db = MongoDBDatabase()

    user_service_mysql = UserService(mysql_db)
    user_service_mysql.store_user("Alice")

    user_service_mongodb = UserService(mongodb_db)
    user_service_mongodb.store_user("Bob")