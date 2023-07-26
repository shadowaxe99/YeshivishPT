```python
from src.models.lesson_model import LessonModel
from src.database.lesson_db import LessonDB

class Lessons:
    def __init__(self):
        self.lesson_db = LessonDB()
        self.lesson_model = LessonModel()

    def provideLesson(self, lesson_id):
        # Fetch lesson from the database
        lesson_data = self.lesson_db.get_lesson(lesson_id)

        # Use the lesson model to format the lesson data
        formatted_lesson = self.lesson_model.format_lesson(lesson_data)

        return formatted_lesson

    def get_all_lessons(self):
        # Fetch all lessons from the database
        all_lessons = self.lesson_db.get_all_lessons()

        # Use the lesson model to format each lesson
        formatted_lessons = [self.lesson_model.format_lesson(lesson) for lesson in all_lessons]

        return formatted_lessons

    def add_lesson(self, lesson_data):
        # Use the lesson model to validate the lesson data
        validated_lesson = self.lesson_model.validate_lesson(lesson_data)

        # Add the validated lesson to the database
        self.lesson_db.add_lesson(validated_lesson)

    def update_lesson(self, lesson_id, lesson_data):
        # Use the lesson model to validate the lesson data
        validated_lesson = self.lesson_model.validate_lesson(lesson_data)

        # Update the lesson in the database
        self.lesson_db.update_lesson(lesson_id, validated_lesson)

    def delete_lesson(self, lesson_id):
        # Delete the lesson from the database
        self.lesson_db.delete_lesson(lesson_id)
```