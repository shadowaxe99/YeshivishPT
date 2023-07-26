```python
from models.pronunciation_model import PronunciationModel

class PronunciationGuide:
    def __init__(self):
        self.model = PronunciationModel()

    def guidePronunciation(self, word):
        pronunciation = self.model.getPronunciation(word)
        if pronunciation:
            return {
                'PRONUNCIATION_GUIDE_RESULT': {
                    'word': word,
                    'pronunciation': pronunciation
                }
            }
        else:
            return {
                'PRONUNCIATION_GUIDE_RESULT': {
                    'error': 'Pronunciation guide not found for the given word.'
                }
            }
```