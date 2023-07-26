```python
from pymongo import MongoClient
from src.database.database_connection import DatabaseConnection
from src.models.dictionary_schema import DictionarySchema

class DictionaryDB:
    def __init__(self):
        self.db_connection = DatabaseConnection()
        self.client = MongoClient(self.db_connection.connection_string)
        self.db = self.client['yeshivishgpt']
        self.collection = self.db['dictionary']

    def insert_entry(self, entry):
        if isinstance(entry, DictionarySchema):
            self.collection.insert_one(entry.__dict__)
        else:
            raise TypeError("Expected DictionarySchema object")

    def find_entry(self, yeshivish_word):
        return self.collection.find_one({"yeshivish_word": yeshivish_word})

    def update_entry(self, yeshivish_word, new_entry):
        if isinstance(new_entry, DictionarySchema):
            self.collection.update_one({"yeshivish_word": yeshivish_word}, {"$set": new_entry.__dict__})
        else:
            raise TypeError("Expected DictionarySchema object")

    def delete_entry(self, yeshivish_word):
        self.collection.delete_one({"yeshivish_word": yeshivish_word})

    def get_all_entries(self):
        return self.collection.find()
```