```python
import speech_recognition as sr

class VoiceModel:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def recognize_voice(self, audio_file):
        with sr.AudioFile(audio_file) as source:
            audio_data = self.recognizer.record(source)
            text = self.recognizer.recognize_google(audio_data)
            return text
```