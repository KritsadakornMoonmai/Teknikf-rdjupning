import joblib
import pandas as pd
from Events.Train_model import TrainModel

class FetchModel:
    def __init__(self):
        try:
            self.model = joblib.load('Data/TrainedData/Model.pkl')
            self.vectorizer = joblib.load('Data/TrainedData/Vectorizer.pkl')
        except FileNotFoundError:
            self.model = None
            self.vectorizer = None
        self.data = pd.read_csv('Data/spam.csv', encoding='latin-1')

    def fetch(self):
        if self.model is None or self.vectorizer is None:
            TrainModel.ProcessData(self.data)
            self.model = joblib.load('Data/TrainedData/Model.pkl')
            self.vectorizer = joblib.load('Data/TrainedData/Vectorizer.pkl')

        return [self.model, self.vectorizer]