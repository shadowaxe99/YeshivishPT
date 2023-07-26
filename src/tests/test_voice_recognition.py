```python
import unittest
from src.voice_recognition import recognizeVoice
from src.models.voice_model import VoiceModel

class TestVoiceRecognition(unittest.TestCase):

    def setUp(self):
        self.voice_model = VoiceModel()
        self.test_phrase_yeshivish = "Gut Voch"
        self.test_phrase_english = "Good Week"

    def test_recognizeVoice_yeshivish(self):
        result = recognizeVoice(self.test_phrase_yeshivish, self.voice_model)
        self.assertEqual(result, self.test_phrase_english)

    def test_recognizeVoice_english(self):
        result = recognizeVoice(self.test_phrase_english, self.voice_model)
        self.assertEqual(result, self.test_phrase_yeshivish)

if __name__ == '__main__':
    unittest.main()
```