Fake News Detection using Machine Learning
Overview
This project is a Fake News Detection System that uses Natural Language Processing (NLP) and Machine Learning techniques to classify news articles as reliable or unreliable. It is implemented in Python and utilizes scikit-learn, NLTK, Pandas, and Swifter for data preprocessing and classification.

Features
Loads and preprocesses a dataset (train1.csv) of news articles.
Cleans text data using NLTK Stopwords & Porter Stemming.
Transforms text using TF-IDF Vectorization.
Uses a Decision Tree Classifier to classify news articles.
Pickle serialization for model persistence.
Provides a function (fake_news(news)) to predict whether a given news article is fake or real.
Dependencies
Ensure you have the following libraries installed:

bash
Copy
Edit
pip install pandas scikit-learn nltk swifter pickle5
How It Works
The dataset is loaded and cleaned.
Text is preprocessed (removing special characters, stopwords, stemming).
The text is vectorized using TF-IDF.
A Decision Tree Classifier is trained on the dataset.
The trained model is saved using Pickle for later use.
A function fake_news(news) takes user input and predicts whether the news is fake or real.
Future Improvements
Implement Deep Learning models like LSTMs for better accuracy.
Improve preprocessing with lemmatization instead of stemming.
Deploy the model using Flask or FastAPI for real-world applications.
Author
This project was developed as part of a machine learning study and aims to contribute to fake news detection research.

Happy coding! 🚀
