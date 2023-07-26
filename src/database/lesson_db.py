```python
from pymongo import MongoClient
from src.models.lesson_model import LessonSchema

class LessonDB:
    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['yeshivishGPT']
        self.collection = self.db['lessons']

    def insert_lesson(self, lesson):
        if isinstance(lesson, LessonSchema):
            self.collection.insert_one(lesson.__dict__)
        else:
            raise ValueError("Input is not a valid Lesson")

    def get_lesson(self, lesson_id):
        lesson = self.collection.find_one({'_id': lesson_id})
        if lesson:
            return LessonSchema(**lesson)
        else:
            return None

    def update_lesson(self, lesson_id, lesson):
        if isinstance(lesson, LessonSchema):
            self.collection.update_one({'_id': lesson_id}, {"$set": lesson.__dict__})
        else:
            raise ValueError("Input is not a valid Lesson")

    def delete_lesson(self, lesson_id):
        self.collection.delete_one({'_id': lesson_id})
```