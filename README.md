Overview

This project is a Fake News Prediction system that utilizes Natural Language Processing (NLP) and Machine Learning (ML) techniques to classify news articles as either real or fake. The model is trained using a dataset of news articles and aims to improve the reliability of news consumption.

Features

Data loading and preprocessing

Text cleaning and stemming using NLTK

TF-IDF vectorization for feature extraction

Decision Tree classifier for prediction

Model evaluation and accuracy scoring

Pickle serialization for model deployment

Technologies Used

Python

Pandas, NumPy

Scikit-learn

Natural Language Toolkit (NLTK)

Swifter

Pickle

Installation

Clone the repository:

git clone https://github.com/your-repo/fake-news-prediction.git
cd fake-news-prediction

Install required dependencies:

pip install -r requirements.txt

Mount Google Drive (if using Google Colab):

from google.colab import drive
drive.mount('/content/drive')

Ensure the dataset (train1.csv) is available in the correct directory.

Contributors

Amisha Chand

License

This project is licensed under the MIT License. See LICENSE for details
