```python
import unittest
from src.lessons import provideLesson
from src.models.lesson_model import LessonModel

class TestLessons(unittest.TestCase):

    def setUp(self):
        self.lesson_model = LessonModel()

    def test_provide_lesson(self):
        # Mocking a lesson
        lesson = {
            'title': 'Introduction to Yeshivish',
            'content': 'Yeshivish is a sociolect of English spoken by Yeshiva students and Orthodox Jews...',
            'quiz': {
                'question': 'What is Yeshivish?',
                'options': ['A language', 'A city', 'A food', 'A dance'],
                'answer': 'A language'
            }
        }

        self.lesson_model.add_lesson(lesson)

        # Test if the function returns the correct lesson
        result = provideLesson('Introduction to Yeshivish')
        self.assertEqual(result, lesson)

        # Test if the function returns None for a non-existent lesson
        result = provideLesson('Non-existent lesson')
        self.assertEqual(result, None)

    def tearDown(self):
        self.lesson_model.delete_lesson('Introduction to Yeshivish')

if __name__ == '__main__':
    unittest.main()
```