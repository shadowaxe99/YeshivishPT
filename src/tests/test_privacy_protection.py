```python
import unittest
from src.privacy_protection import protectPrivacy

class TestPrivacyProtection(unittest.TestCase):

    def setUp(self):
        self.sample_data = {
            "name": "John Doe",
            "email": "johndoe@example.com",
            "yeshivish_phrase": "A gutten tag"
        }

    def test_privacy_protection(self):
        result = protectPrivacy(self.sample_data)
        self.assertNotIn("name", result)
        self.assertNotIn("email", result)
        self.assertIn("yeshivish_phrase", result)

if __name__ == '__main__':
    unittest.main()
```