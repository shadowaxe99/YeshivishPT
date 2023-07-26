```python
import unittest
from src.pronunciation_guide import guidePronunciation

class TestPronunciationGuide(unittest.TestCase):

    def setUp(self):
        self.pronunciation_guide = guidePronunciation()

    def test_pronunciation_guide(self):
        word = "Shalom"
        result = self.pronunciation_guide.get_pronunciation(word)
        self.assertIsNotNone(result)

    def test_invalid_word(self):
        word = "123456"
        with self.assertRaises(ValueError):
            self.pronunciation_guide.get_pronunciation(word)

    def test_empty_word(self):
        word = ""
        with self.assertRaises(ValueError):
            self.pronunciation_guide.get_pronunciation(word)

if __name__ == '__main__':
    unittest.main()
```