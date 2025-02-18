🚀 Fake News Detection Using Machine Learning

📌 Overview

This project is a Fake News Detection System that uses Natural Language Processing (NLP) and Machine Learning techniques to classify news articles as reliable or unreliable. It is implemented in Python and utilizes scikit-learn, NLTK, Pandas, and Swifter for data preprocessing and classification.

🌟 Features

✅ Loads and preprocesses a dataset (train1.csv) of news articles.
✅ Cleans text data using NLTK Stopwords & Porter Stemming.
✅ Transforms text using TF-IDF Vectorization.
✅ Uses a Decision Tree Classifier to classify news articles.
✅ Pickle serialization for model persistence.
✅ Provides a function (fake_news(news)) to predict whether a given news article is fake or real.

🛠️ Dependencies

Ensure you have the following libraries installed:

pip install pandas scikit-learn nltk swifter pickle5

🔄 How It Works

1️⃣ The dataset is loaded and cleaned.
2️⃣ Text is preprocessed (removing special characters, stopwords, stemming).
3️⃣ The text is vectorized using TF-IDF.
4️⃣ A Decision Tree Classifier is trained on the dataset.
5️⃣ The trained model is saved using Pickle for later use.
6️⃣ A function fake_news(news) takes user input and predicts whether the news is fake or real.

📝 Usage

import pickle

# Load the trained model
vector_form = pickle.load(open('vect.pkl', 'rb'))
load_model = pickle.load(open('model.pkl', 'rb'))

# Function to predict news authenticity
def fake_news(news):
    news = stemming(news)  # Apply preprocessing
    input_data = [news]
    vector_form1 = vector_form.transform(input_data)
    prediction = load_model.predict(vector_form1)
    return prediction

# Example News Prediction
news_text = """Sample news article text here..."""
result = fake_news(news_text)

if result == ['0']:
    print("✅ Reliable: News is not fake")
else:
    print("❌ Unreliable: News is fake")

📊 Dataset

The dataset (train1.csv) consists of:

📝 text: The news article content.

🏷️ label: 0 for real news, 1 for fake news.

📈 Model Performance

The accuracy of the model is displayed after training, typically around 84.51% (varies based on dataset and training).

🚀 Future Improvements

🔹 Implement Deep Learning models like LSTMs for better accuracy.
🔹 Improve preprocessing with lemmatization instead of stemming.
🔹 Deploy the model using Flask or FastAPI for real-world applications.

This project was developed as part of a machine learning study and aims to contribute to fake news detection research.

💡 Happy coding! 🚀
