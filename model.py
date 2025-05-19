# model.py
import joblib
import nltk
from nltk.stem.porter import PorterStemmer
import re
import string

# Load model and vectorizer
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# Text cleaning function
def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'\[.*?\]', '', text)
    text = re.sub(r'http\S+', '', text)
    text = re.sub(r'<.*?>+', '', text)
    text = re.sub(f'[{re.escape(string.punctuation)}]', '', text)
    text = re.sub(r'\n', '', text)
    text = re.sub(r'\w*\d\w*', '', text)
    return text

# Stemming Function
stemmer = PorterStemmer()
def stemming(text):
    words = text.split()
    words = [stemmer.stem(word) for word in words]
    return ' '.join(words)

# Prediction function
def predict_news(text):
    text=stemming(text)
    cleaned_text = preprocess_text(text)
    vectorized = vectorizer.transform([cleaned_text])
    prediction = model.predict(vectorized)
    return "Real News" if prediction[0] == 0 else "Fake News"
