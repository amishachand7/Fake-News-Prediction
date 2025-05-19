
# 🚀 Fake News Detection Using Machine Learning & Flask Web App

## 📌 Overview

This project is a **Fake News Detection System** powered by **Machine Learning** and **Natural Language Processing (NLP)**. It classifies news articles as **Real** or **Fake** using a trained Decision Tree model. A fully interactive, stylish web interface is included to make it easy and intuitive for users to check the authenticity of any news article.

---

## 🌟 Key Features

✅ Preprocesses and cleans raw news data using **NLTK Stopwords** & **Porter Stemmer**  
✅ Vectorizes news content using **TF-IDF**  
✅ Trains a **Decision Tree Classifier** on labeled news data  
✅ Saves the model (`model.pkl`) and vectorizer (`vect.pkl`) for reuse  
✅ Provides a prediction function `fake_news(news)`  
✅ **Responsive, animated website** built with **Flask**, **HTML/CSS/JS**, and **canvas animation background**

---

## 🛠️ Dependencies

Make sure you have the following Python packages installed:

```bash
pip install pandas scikit-learn nltk flask joblib
```

---

## 🔄 How It Works

1. Dataset (`train1.csv`) is loaded and cleaned.
2. News text is preprocessed (removing special characters, stopwords, stemming).
3. TF-IDF vectorization transforms text to numerical format.
4. Decision Tree model is trained and saved using Pickle.
5. Flask serves a web page where users can enter news content.
6. Submitted text is processed, vectorized, and passed to the model to predict authenticity.

---

## 🖥️ Web Interface

The app features a **modern, animated, and responsive UI** with:

🎨 Centered cards with shadows, gradients, and animations  
📱 Mobile-first design  
🌌 Starfield background animation using `canvas`  
🧠 Displays real-time prediction with color-coded result  
🧾 Accessible and intuitive layout  

> 🔍 Built with **Flask**, **HTML5**, **CSS3**, **JavaScript**, and custom `background.js` animation

---

## 📝 Usage (Code Interface)

```python
import joblib
# Load the model and vectorizer
joblib.dump(model, 'model.pkl')
joblib.dump(vectorizer, 'vectorizer.pkl')

# Prediction function
def predict_news(text):
    text=stemming(text)
    cleaned_text = preprocess_text(text)
    vectorized = vectorizer.transform([cleaned_text])
    prediction = model.predict(vectorized)
    return "Real News" if prediction[0] == 0 else "Fake News"
```

---

## 📊 Dataset Format

**File:** `train1.csv`  
| Column | Description             |
|--------|-------------------------|
| text   | News article content    |
| label  | `0` = Real, `1` = Fake  |

---

## 📈 Model Performance

- **Accuracy**: ~80% (based on dataset split and preprocessing)
- **Precision**: 75%
- **Recall**: 85.71%
- **F1 Score**: 80%
- **Model**: Decision Tree Classifier
- **Vectorizer**: TF-IDF with unigrams and stopword filtering

---

## 🌍 Running the Web App

```bash
python app.py
```

Visit `http://127.0.0.1:5000` in your browser to interact with the fake news detector.

---

## 💡 Happy Coding & Stay Informed! 🚀
