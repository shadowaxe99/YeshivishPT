```python
from pymongo import MongoClient
from src.database.database_connection import DatabaseConnection
from src.models.user_model import UserSchema

class UserDB:
    def __init__(self):
        self.db_connection = DatabaseConnection().get_connection()
        self.user_collection = self.db_connection['users']

    def add_user(self, user_data):
        user_schema = UserSchema()
        validated_user_data = user_schema.load(user_data)
        result = self.user_collection.insert_one(validated_user_data)
        return result.inserted_id

    def get_user(self, user_id):
        user_data = self.user_collection.find_one({"_id": user_id})
        if user_data:
            user_schema = UserSchema()
            return user_schema.dump(user_data)
        else:
            return None

    def update_user(self, user_id, user_data):
        user_schema = UserSchema()
        validated_user_data = user_schema.load(user_data)
        self.user_collection.update_one({"_id": user_id}, {"$set": validated_user_data})

    def delete_user(self, user_id):
        self.user_collection.delete_one({"_id": user_id})
```