# Disaster Tweets Classification System

This app predicts whether a tweet is about a **real disaster or not** using **Natural Language Processing (NLP)** and **Machine Learning**.

---

### Streamlit App
<img width="1089" height="537" alt="app-demo" src="https://github.com/user-attachments/assets/0c556bc3-cada-4ec5-9ec8-608d4dd61e52" />

---

## Overview

Twitter is a powerful medium for sharing information during emergency situations such as **natural disasters**, **accidents**, or **crises**.  
This project leverages **machine learning algorithms** to classify tweets as either **disaster-related** or **non-disaster-related**, helping in **real-time monitoring and response efforts**.

---

## Techniques Used

### Natural Language Processing (NLP)
Applied to process and analyze tweet text data.

### Text Preprocessing
Steps include:
- Removing punctuation and stop words  
- Converting text to lowercase  
- Tokenization and stemming/lemmatization  
- Handling URLs, mentions, and hashtags  

### Feature Engineering
Extracted meaningful features using:
- **Bag of Words (BoW)**  
- **TF-IDF (Term Frequency–Inverse Document Frequency)**  
- **N-grams**

### Machine Learning Models
Trained and compared multiple classifiers:
- Logistic Regression  
- Naive Bayes  
- Random Forest  
- XGBoost  

---

## Model Performance

| Metric       | Value  |
|---------------|--------|
| **Accuracy**  | 0.84   |
| **Precision** | 0.82   |
| **Recall**    | 0.79   |
| **F1 Score**  | 0.80   |

📈 These metrics indicate a balanced model with strong generalization ability.

---

## Visualizations

### 🔹 Dataset Insights
<img width="509" height="171" alt="image" src="https://github.com/user-attachments/assets/7aaa15c2-662b-40fa-8a07-beef408b8759" />

**Figure 1:** Class distribution of disaster vs non-disaster tweets.

### 🔹 Word Cloud
<img width="891" height="448" alt="image" src="https://github.com/user-attachments/assets/d455aeed-5b00-4a98-9195-0ae4bf274714" />

**Figure 2:** Common keywords in disaster-related tweets.

### 🔹 Model Comparison
<img width="385" height="142" alt="image" src="https://github.com/user-attachments/assets/1506dc80-0ef1-40ca-b90b-704e390756cb" />

**Figure 3:** Model accuracy comparison chart.

### 🔹 Testing Data Accuracy
<img width="250" height="107" alt="image" src="https://github.com/user-attachments/assets/85b20a59-2b9e-4f50-b980-72863d41dcd3" />


**Figure 4:** Model accuracy.

### 🔹 Testing Data Confusion Matrix
<img width="374" height="322" alt="image" src="https://github.com/user-attachments/assets/7add3f6d-5c99-4b38-98ea-c13e8bf82a14" />



**Figure 5:** Confusion Matrix

---

## Data and Model Training

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

## Future Improvements
- Incorporate **advanced deep learning models** (e.g., LSTMs or Transformers) to improve classification accuracy  
- Explore **ensemble techniques** to combine multiple models and boost performance  
- Enhance the system to handle **multi-language tweets** and adapt to various disaster scenarios  

---

## Contributions
Contributions, bug reports, and feedback are welcome!  
Feel free to open issues or submit pull requests on this repository.

---

## License
This project is licensed under the **MIT License**.  
See the [LICENSE](LICENSE) file for details.
