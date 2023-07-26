```python
import unittest
from src.database import database_connection, dictionary_db, cultural_db, lesson_db, user_db

class TestDatabase(unittest.TestCase):

    def setUp(self):
        self.db_connection = database_connection.DatabaseConnection()

    def test_dictionary_db(self):
        dictionary = dictionary_db.DictionaryDB(self.db_connection)
        entry = dictionary.get_entry("YeshivishWord")
        self.assertIsNotNone(entry)
        self.assertEqual(entry['word'], "YeshivishWord")

    def test_cultural_db(self):
        cultural_db_instance = cultural_db.CulturalDB(self.db_connection)
        insight = cultural_db_instance.get_insight("OrthodoxPractice")
        self.assertIsNotNone(insight)
        self.assertEqual(insight['practice'], "OrthodoxPractice")

    def test_lesson_db(self):
        lesson_db_instance = lesson_db.LessonDB(self.db_connection)
        lesson = lesson_db_instance.get_lesson("Lesson1")
        self.assertIsNotNone(lesson)
        self.assertEqual(lesson['lesson_name'], "Lesson1")

    def test_user_db(self):
        user_db_instance = user_db.UserDB(self.db_connection)
        user = user_db_instance.get_user("TestUser")
        self.assertIsNotNone(user)
        self.assertEqual(user['username'], "TestUser")

if __name__ == '__main__':
    unittest.main()
```