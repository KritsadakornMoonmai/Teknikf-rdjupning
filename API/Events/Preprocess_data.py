import os
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import string
import re

class PreprocessData:
        def __init__(self):
                nltk_data_path = os.path.join(os.getcwd(), 'nltk_data')
                nltk.data.path.append(nltk_data_path)

                self.stemmer = PorterStemmer()
                self.set_stopwords = set(stopwords.words('english'))
                self.set_punktation = set(string.punctuation)
        def set_stopword(self, words):
                return [word for word in words if word not in self.set_stopwords and word not in self.set_punktation]
        
        def Stemmings(self, words):
                return [self.stemmer.stem(word) for word in words]

        def custom_tokenize(self, text):
                return re.findall(r'\b\w+\b', text.lower())
        
        def Transform_text(self, message):
                # Tokenize
                tokens = self.custom_tokenize(message)
                # Remove special characters
                tokens = [re.sub(r'[^a-zA-Z0-9\s]', '', word) for word in tokens]
                # Remove stop words
                tokens = self.set_stopword(tokens)
                # Apply stemming
                tokens = self.Stemmings(tokens)
                # Join tokens back into a string
                return ' '.join(tokens)