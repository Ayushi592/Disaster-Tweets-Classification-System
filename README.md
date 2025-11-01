# 🚨 Disaster Tweets Classification System 
### Real-time Disaster Tweet Detection using NLP & Machine Learning


This project automatically classifies tweets into Disaster and Non-Disaster categories using Natural Language Processing and Machine Learning. It helps support emergency response systems by identifying real crisis-related tweets shared by users on social platforms.

## Project Overview

During disaster situations, Twitter becomes a primary communication platform. However, with millions of posts, manually identifying genuine emergency tweets is difficult.

The objective of this project is to develop an automated system that analyzes tweet text and predicts whether it refers to a real disaster event. This ensures faster crisis detection and supports real-time monitoring systems.

The project trains classification models on real labeled disaster tweets and deploys a Streamlit interface for real-time tweet classification.

## 🗂️ Dataset Overview
## 1️⃣ Training Dataset - Real Disaster Tweets (Kaggle)

Contains tweets marked as:

| Label | Meaning |
|------|---------|
| 1 | Disaster Tweet |
| 0 | Non-Disaster Tweet |


Includes real emergency tweet text, e.g., floods, earthquakes, explosions, fires, etc.

 📁 Dataset Source: Real Disaster Tweets (Kaggle)

## 2️⃣ Testing Dataset - Disaster Response Pipeline Messages 

Used to validate generalization capability across platforms.
Contains real messages tagged as emergency vs non-emergency scenarios.

 📁 Dataset Source: Figure Eight Disaster Response Messages Dataset

## ⚙️ NLP Processing Pipeline
| Step | Description |
|------|------------|
| Data Cleaning | Remove URLs, mentions, hashtags, emojis, numbers, punctuation |
| Lowercasing | Convert text to lowercase |
| Tokenization | Split text into tokens |
| Stopword Removal | Remove common non-meaningful words |
| Lemmatization | Convert words to base/root form |
| Feature Extraction | TF-IDF Vectorization |
| Train-Test Split | 70% training — 30% testing |
| Model Evaluation | Accuracy, Precision, Recall, F1-Score |

## 🤖 Models Trained
| Model | Description | Training Accuracy |
|-------|------------|------------------|
| Logistic Regression | Linear text classifier | **0.84** |
| Naive Bayes | Probabilistic classifier | 0.82+ |
| Random Forest | Ensemble decision trees | 0.83+ |
| XGBoost | Gradient boosting classifier | **0.85+** |

## ✅ Best Models: Logistic Regression & XGBoost

## 📊 Model Performance Summary
| Metric | Score |
|-------|------|
| **Accuracy** | **0.84** |
| Precision | 0.82 |
| Recall | 0.79 |
| F1-Score | 0.80 |


## ⭐ Features

Type any tweet and detect if it indicates a disaster

Shows classification label instantly

Confidence scores & result visualization

Modern UI with responsive design

## 🌐 Streamlit Web Application
An interactive Streamlit web app was built to make the Disaster Tweets Classifier accessible to users in real time.
The app leverages the trained TF-IDF vectorizer and Logistic Regression model to classify tweets into Disasters.

## 🚀 Deployment Link

🔗 https://raisable-unobligatory-deshawn.ngrok-free.dev

## 🖥️ Run Locally
```bash
git clone https://github.com/your-username/disaster-tweet-classifier.git
cd disaster-tweet-classifier
pip install -r requirements.txt
streamlit run app.py
```

 ## Future Work

Transformer-based models (BERT, RoBERTa)

Multi-language tweet support

Integration with live Twitter API for real-time monitoring

Emergency alert dashboard & notification system

Cloud deployment with AWS / GCP

## 👩‍💻 Author

Ayushi Nagpure
Computer Science Engineering Student
India

GitHub: https://github.com/Ayushi592

LinkedIn: https://linkedin.com/in/ayushinagpure

## 📜 License

This project is licensed under the MIT License - you are free to use, modify, and distribute it for educational or research purposes, provided that proper credit is given to the author.
