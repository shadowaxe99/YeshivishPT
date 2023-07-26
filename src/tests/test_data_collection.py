```python
import unittest
from src.data_collection import collectData

class TestDataCollection(unittest.TestCase):

    def setUp(self):
        self.sample_data = {
            "yeshivish": "Shalom Aleichem",
            "english": "Peace be upon you",
            "context": "A common greeting in Yeshivish"
        }

    def test_collectData(self):
        result = collectData(self.sample_data)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
```