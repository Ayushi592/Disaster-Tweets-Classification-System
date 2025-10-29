# Disaster Tweets Classification System

This app predicts whether a tweet is about a real disaster or not using NLP and machine learning.

### 📸 App Screenshot
![Streamlit App](<img width="1089" height="537" alt="image" src="https://github.com/user-attachments/assets/0c556bc3-cada-4ec5-9ec8-608d4dd61e52" />
.png)

This project aims to detect tweets related to disaster situations using machine learning techniques.

---

## Overview
Twitter is a popular social media platform where users often share information during emergency situations such as natural disasters, accidents, or crises.  
This project leverages **machine learning algorithms** to classify tweets as either **disaster-related** or **non-disaster-related**.  
The goal is to assist in **real-time monitoring and response efforts** during critical events.

---

## Techniques Used

### Natural Language Processing (NLP)
Various NLP techniques are employed to process and analyze the textual content of tweets.

### Text Preprocessing
Text data is cleaned and preprocessed by:
- Removing stop words and punctuation  
- Applying stemming or lemmatization  
- Normalizing and tokenizing text  

### Feature Engineering
Relevant features are extracted to represent tweet data, including:
- Word frequency  
- N-grams  
- TF-IDF (Term Frequency–Inverse Document Frequency)

### Machine Learning Classification
Classification models such as:
- **Naive Bayes**  
- **Support Vector Machines (SVM)**  
- **Recurrent Neural Networks (RNNs)**  

are trained to predict whether a tweet is related to a disaster or not.

---

## Data and Model Training
The project uses a labeled dataset of tweets, where each tweet is annotated as either **disaster** or **non-disaster**.  
The dataset is split into **training** and **testing** sets, and the models are trained on the training data.  
Performance is evaluated on the test set using metrics such as:
- Accuracy  
- Precision  
- Recall  
- F1 Score  

---

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

