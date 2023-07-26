```python
import speech_recognition as sr
from src.models.voice_model import VoiceModel

class VoiceRecognition:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.voice_model = VoiceModel()

    def recognize_voice(self, audio_file):
        with sr.AudioFile(audio_file) as source:
            audio_data = self.recognizer.record(source)
            text = self.recognizer.recognize_google(audio_data)
            return text

    def process_voice_input(self, audio_file):
        text = self.recognize_voice(audio_file)
        result = self.voice_model.predict(text)
        return result

    def handle_voice_input(self, audio_file):
        try:
            result = self.process_voice_input(audio_file)
            return {"VOICE_RECOGNITION_RESULT": result}
        except Exception as e:
            return {"error": str(e)}
```
