import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score
from sklearn.preprocessing import LabelEncoder
import nltk
nltk.data.path.append('nltk_data')  # Set path to a known directory on Render

# Ensure resources are downloaded to this path
nltk.download('punkt', download_dir='nltk_data')
nltk.download('stopwords', download_dir='nltk_data')
from imblearn.pipeline import Pipeline
from imblearn.over_sampling import SMOTE
from Events.Preprocess_data import PreprocessData as ppd
import joblib

class TrainModel():

    def __init__(self):
        self.encoder = LabelEncoder()
        self.ppd = ppd()
        
    def ProcessData(self, data):

        ####################Transform text##########################
        data['text_transform'] = data['Message'].apply(self.ppd.Transform_text)

        # Display the preprocessed data
        print(data[['Message', 'text_transform']].head())

        data['Category'] = self.encoder.fit_transform(data['Category'])
        data.sample(2)

        tfidv = TfidfVectorizer(max_features=10000)
        X = tfidv.fit_transform(data['Message']).toarray()
        y = data['Category']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=100)

        pipeline = Pipeline(steps = [
            ('smote', SMOTE(random_state=100)),
            ('nb_model', MultinomialNB())
        ])

        pipeline.fit(X_train, y_train)
        y_predict = pipeline.predict(X_test)
        accuracy_nb_model = accuracy_score(y_test, y_predict)
        print(f"Naive Bayes Accuracy: {accuracy_nb_model:.2f}")
        print("confusion Matrix :",confusion_matrix(y_test,y_predict))
        print("Precision Score: ",precision_score(y_test,y_predict))

        new_emails = [
            "Get a free iPhone now!",
            "Hey, how's it going?",
            "Congratulations! You've won a prize!",
            "Reminder: Meeting at 2 PM tomorrow."
        ]

        # Convert new data into numerical vectors using the trained tfidf_vectorizer
        new_X = tfidv.transform(new_emails)
        new_X_dense = new_X.toarray()

        # Use the trained SVM model to make predictions
        new_predictions = pipeline.predict(new_X_dense)

        # Print the predictions
        for email, prediction in zip(new_emails, new_predictions):
            if prediction == 1:
                print(f"'{email}' is predicted as spam.")
            else:
                print(f"'{email}' is predicted as ham.")


        joblib.dump(pipeline, 'Data/TrainedData/Model.pkl')
        joblib.dump(tfidv, 'Data/TrainedData/Vectorizer.pkl')

data = pd.read_csv('Data/spam.csv', encoding='latin-1')
trainModel = TrainModel()
trainModel.ProcessData(data)
    

    