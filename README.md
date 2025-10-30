# 🌪️ Disaster Tweets Classification System

This app predicts whether a tweet is about a **real disaster or not** using **Natural Language Processing (NLP)** and **Machine Learning**.

---

### 🖥️ Streamlit App
<img width="1089" height="537" alt="app-demo" src="https://github.com/user-attachments/assets/0c556bc3-cada-4ec5-9ec8-608d4dd61e52" />

---

## 📘 Overview

Twitter is a powerful medium for sharing information during emergency situations such as **natural disasters**, **accidents**, or **crises**.  
This project leverages **machine learning algorithms** to classify tweets as either **disaster-related** or **non-disaster-related**, helping in **real-time monitoring and response efforts**.

---

## ⚙️ Techniques Used

### 🧠 Natural Language Processing (NLP)
Applied to process and analyze tweet text data.

### 🧹 Text Preprocessing
Steps include:
- Removing punctuation and stop words  
- Converting text to lowercase  
- Tokenization and stemming/lemmatization  
- Handling URLs, mentions, and hashtags  

### 🔍 Feature Engineering
Extracted meaningful features using:
- **Bag of Words (BoW)**  
- **TF-IDF (Term Frequency–Inverse Document Frequency)**  
- **N-grams**

### 🤖 Machine Learning Models
Trained and compared multiple classifiers:
- Logistic Regression  
- Naive Bayes  
- Random Forest  
- XGBoost  

---

## 📊 Model Performance

| Metric       | Value  |
|---------------|--------|
| **Accuracy**  | 0.84   |
| **Precision** | 0.82   |
| **Recall**    | 0.79   |
| **F1 Score**  | 0.80   |

📈 These metrics indicate a balanced model with strong generalization ability.

---

## 📈 Visualizations

### 🔹 Dataset Insights
<img width="600" alt="class-distribution" src="https://github.com/user-attachments/assets/example1.png" />

**Figure 1:** Class distribution of disaster vs non-disaster tweets.

### 🔹 Word Cloud
<img width="600" alt="wordcloud" src="https://github.com/user-attachments/assets/example2.png" />

**Figure 2:** Common keywords in disaster-related tweets.

### 🔹 Model Comparison
<img width="600" alt="model-performance" src="https://github.com/user-attachments/assets/example3.png" />

**Figure 3:** Model accuracy comparison chart.

---

## 🧩 Data and Model Training

The project uses a **labeled dataset of tweets**, annotated as disaster or non-disaster.  
Data is split into **training (70%)** and **testing (30%)** subsets.

Model performance is evaluated using the following:
- Confusion Matrix  
- ROC-AUC Curve  
- Precision-Recall Curve  

Example evaluation code:
```python
from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))
