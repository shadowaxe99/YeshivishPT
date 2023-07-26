```python
import os
import json
from pydub import AudioSegment

class PronunciationModel:
    def __init__(self):
        self.pronunciation_data = self.load_pronunciation_data()

    def load_pronunciation_data(self):
        pronunciation_data_path = os.path.join(os.getcwd(), 'data', 'pronunciation_data.json')
        with open(pronunciation_data_path, 'r') as file:
            pronunciation_data = json.load(file)
        return pronunciation_data

    def get_pronunciation(self, word):
        pronunciation = self.pronunciation_data.get(word.lower(), None)
        if pronunciation:
            return pronunciation
        else:
            return None

    def play_pronunciation(self, word):
        pronunciation = self.get_pronunciation(word)
        if pronunciation:
            audio_path = os.path.join(os.getcwd(), 'data', 'audio', f'{pronunciation}.mp3')
            audio = AudioSegment.from_mp3(audio_path)
            audio.play()
        else:
            print(f"No pronunciation guide available for {word}")
```