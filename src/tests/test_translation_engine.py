```python
import unittest
from src.translation_engine import translate

class TestTranslationEngine(unittest.TestCase):

    def setUp(self):
        self.yeshivish_sentence = "A gutten morgen"
        self.english_sentence = "Good morning"

    def test_translate_yeshivish_to_english(self):
        result = translate(self.yeshivish_sentence, 'yeshivish', 'english')
        self.assertEqual(result, self.english_sentence)

    def test_translate_english_to_yeshivish(self):
        result = translate(self.english_sentence, 'english', 'yeshivish')
        self.assertEqual(result, self.yeshivish_sentence)

    def test_invalid_language_input(self):
        with self.assertRaises(ValueError):
            translate(self.yeshivish_sentence, 'yeshivish', 'spanish')

    def test_empty_string_input(self):
        with self.assertRaises(ValueError):
            translate("", 'yeshivish', 'english')

if __name__ == '__main__':
    unittest.main()
```