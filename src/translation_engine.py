```python
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from models.nlp_model import nlp_model

class TranslationEngine:
    def __init__(self):
        self.nlp_model = nlp_model

    def preprocess_text(self, text):
        # Tokenize the text
        tokens = word_tokenize(text)
        # Remove the stopwords
        tokens = [word for word in tokens if word not in stopwords.words('english')]
        return tokens

    def translate(self, text, source_lang, target_lang):
        # Preprocess the text
        tokens = self.preprocess_text(text)
        # Translate the text
        translation = self.nlp_model.translate(tokens, source_lang, target_lang)
        return translation

translation_engine = TranslationEngine()

def translate():
    text = input("Enter the text to translate: ")
    source_lang = input("Enter the source language: ")
    target_lang = input("Enter the target language: ")
    translation = translation_engine.translate(text, source_lang, target_lang)
    print(f"Translation: {translation}")
```