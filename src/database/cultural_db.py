```python
from pymongo import MongoClient
from src.database.database_connection import get_db_connection

class CulturalDB:
    def __init__(self):
        self.db = get_db_connection()
        self.collection = self.db['cultural_insights']

    def get_cultural_insight(self, id):
        return self.collection.find_one({'_id': id})

    def add_cultural_insight(self, cultural_insight):
        return self.collection.insert_one(cultural_insight)

    def update_cultural_insight(self, id, cultural_insight):
        return self.collection.update_one({'_id': id}, {"$set": cultural_insight})

    def delete_cultural_insight(self, id):
        return self.collection.delete_one({'_id': id})

    def get_all_cultural_insights(self):
        return self.collection.find()
```