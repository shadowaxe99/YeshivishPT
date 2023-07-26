```python
import unittest
from src.dictionary import searchDictionary

class TestDictionary(unittest.TestCase):

    def setUp(self):
        self.query = "Shalom"
        self.expected_result = {
            "word": "Shalom",
            "meaning": "Peace",
            "usage": "Used as a greeting or farewell, and means peace."
        }

    def test_searchDictionary(self):
        result = searchDictionary(self.query)
        self.assertEqual(result, self.expected_result)

if __name__ == '__main__':
    unittest.main()
```