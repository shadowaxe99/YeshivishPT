```python
from gensim.models import Word2Vec
from nltk.tokenize import word_tokenize
import nltk

class NLPModel:
    def __init__(self):
        self.model = None

    def train_model(self, sentences):
        """
        Train the Word2Vec model with the provided sentences
        """
        # Tokenize the sentences
        tokenized_sentences = [word_tokenize(sentence) for sentence in sentences]

        # Train the Word2Vec model
        self.model = Word2Vec(tokenized_sentences, min_count=1)

    def translate(self, sentence):
        """
        Translate the provided Yeshivish sentence to English
        """
        # Tokenize the sentence
        tokenized_sentence = word_tokenize(sentence)

        # Translate the sentence
        translated_sentence = [self.model.wv.most_similar(word)[0][0] for word in tokenized_sentence]

        return ' '.join(translated_sentence)

nlp_model = NLPModel()
```