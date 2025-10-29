import streamlit as st
import pandas as pd
import joblib
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
import emoji

# Load model and vectorizer
model = joblib.load("best_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# App title
st.set_page_config(page_title="🌋 Disaster Tweets Classifier", layout="wide")
st.title("🌋 Disaster Tweets Classification System")
st.markdown("This app predicts whether a tweet is **about a disaster** or **not** using NLP and ML models.")

# Sidebar
st.sidebar.header("📊 Model Overview")
st.sidebar.info("This model was trained on disaster tweets dataset.")

# Input
tweet = st.text_area("✍️ Enter a tweet here:", placeholder="e.g. Massive earthquake just hit the city!")

if st.button("🔍 Predict"):
    if tweet.strip() == "":
        st.warning("⚠️ Please enter a tweet.")
    else:
        X_input = vectorizer.transform([tweet])
        prediction = model.predict(X_input)[0]
        result = "🌪️ Disaster Tweet" if prediction == 1 else "🙂 Not a Disaster Tweet"
        color = "red" if prediction == 1 else "green"
        st.markdown(f"### Prediction: <span style='color:{color}'>{result}</span>", unsafe_allow_html=True)

# Optional Performance Metrics Section
st.markdown("---")
st.subheader("📈 Model Performance Summary")

# Load your test data (optional if you saved y_test, X_test earlier)
try:
    # Replace with your actual test data if you have
    y_test = joblib.load("y_test.pkl")
    X_test = joblib.load("X_test.pkl")

    X_test_vec = vectorizer.transform(X_test)
    y_pred = model.predict(X_test_vec)

    acc = accuracy_score(y_test, y_pred)
    prec = precision_score(y_test, y_pred)
    rec = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)

    st.sidebar.metric("✅ Accuracy", f"{acc*100:.2f}%")
    st.sidebar.metric("🎯 F1-Score", f"{f1:.2f}")
    st.sidebar.metric("📏 Precision", f"{prec:.2f}")
    st.sidebar.metric("📐 Recall", f"{rec:.2f}")

    cm = confusion_matrix(y_test, y_pred)
    fig, ax = plt.subplots()
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=["Not Disaster", "Disaster"], yticklabels=["Not Disaster", "Disaster"])
    ax.set_xlabel("Predicted")
    ax.set_ylabel("Actual")
    st.pyplot(fig)

except:
    st.info("ℹ️ Metrics will appear here if you upload your test data or metrics file.")
