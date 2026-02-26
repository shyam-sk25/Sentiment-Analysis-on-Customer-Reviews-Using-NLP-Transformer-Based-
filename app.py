import streamlit as st
import torch
import torch.nn.functional as F
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import pandas as pd
import os
import datetime

# ---------------------------------------------------
# Page Config
# ---------------------------------------------------
st.set_page_config(
    page_title="Marketplace Sentiment Analyzer",
    page_icon="🛒",
    layout="wide"
)

# ---------------------------------------------------
# Custom CSS (Flipkart-inspired palette)
# ---------------------------------------------------
st.markdown("""
<style>
    body { background-color: #f1f3f6; }
    .header-bar {
        background-color: #2874F0;
        padding: 15px 30px;
        color: white;
        font-size: 28px;
        font-weight: 600;
    }
    .card {
        background-color: white;
        padding: 25px;
        border-radius: 10px;
        box-shadow: 0px 2px 8px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    .sentiment-box {
        padding: 18px;
        border-radius: 10px;
        text-align: center;
        font-size: 22px;
        font-weight: 600;
        color: white;
    }
    .rating-star {
        font-size: 18px;
        font-weight: 500;
        color: #212121;
    }
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# Header
# ---------------------------------------------------
st.markdown('<div class="header-bar">🛒 Marketplace Sentiment Intelligence</div>', unsafe_allow_html=True)
st.markdown("")

# ---------------------------------------------------
# Resolve Paths
# ---------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.abspath(os.path.join(BASE_DIR, "..", "fine_tuned_distilbert_flipkart"))
CSV_PATH = os.path.abspath(os.path.join(BASE_DIR, "..", "predictions.csv"))

# ---------------------------------------------------
# Load Model
# ---------------------------------------------------
@st.cache_resource
def load_model():
    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
    model = AutoModelForSequenceClassification.from_pretrained(MODEL_PATH)
    return tokenizer, model

with st.spinner("Loading AI Model..."):
    tokenizer, model = load_model()

labels = {0: "Negative", 1: "Neutral", 2: "Positive"}

# ---------------------------------------------------
# Product Card Section
# ---------------------------------------------------
st.markdown('<div class="card">', unsafe_allow_html=True)

col1, col2 = st.columns([2, 1])

with col1:
    product_name = st.text_input("Product Name", placeholder="Example: iPhone 14 128GB Blue")

with col2:
    rating = st.slider("Customer Rating (Stars)", 1, 5, 4)

st.markdown(f'<div class="rating-star">Customer Rating: {"⭐" * rating}</div>', unsafe_allow_html=True)

review_text = st.text_area(
    "Customer Review",
    placeholder="Write the customer review here..."
)

st.markdown('</div>', unsafe_allow_html=True)

# ---------------------------------------------------
# Prediction Section
# ---------------------------------------------------
if st.button("Analyze Review 🚀"):

    if review_text.strip() == "":
        st.warning("Please enter a review.")
    else:
        inputs = tokenizer(review_text, return_tensors="pt", truncation=True, padding=True)

        with torch.no_grad():
            outputs = model(**inputs)
            probabilities = F.softmax(outputs.logits, dim=1)

        prediction = torch.argmax(probabilities, dim=1).item()
        confidence_scores = probabilities.squeeze().tolist()
        sentiment = labels[prediction]

        # Dynamic color
        if sentiment == "Positive":
            color = "#28a745"
        elif sentiment == "Negative":
            color = "#dc3545"
        else:
            color = "#ffc107"

        st.markdown('<div class="card">', unsafe_allow_html=True)

        st.markdown(
            f'<div class="sentiment-box" style="background-color:{color};">'
            f"Predicted Sentiment: {sentiment}</div>",
            unsafe_allow_html=True
        )

        # Mismatch Detection
        if (rating >= 4 and sentiment == "Negative") or (rating <= 2 and sentiment == "Positive"):
            st.warning("⚠ Rating and review sentiment appear inconsistent.")

        st.subheader("Confidence Distribution")

        confidence_df = pd.DataFrame({
            "Sentiment": ["Negative", "Neutral", "Positive"],
            "Probability": confidence_scores
        })

        st.bar_chart(confidence_df.set_index("Sentiment"))

        # ---------------------------------------------------
        # SAVE TO CSV (Persistent Storage)
        # ---------------------------------------------------
        new_record = pd.DataFrame([{
            "Timestamp": datetime.datetime.now(),
            "Product": product_name,
            "Rating": rating,
            "Review": review_text,
            "Predicted_Sentiment": sentiment,
            "Negative_Prob": confidence_scores[0],
            "Neutral_Prob": confidence_scores[1],
            "Positive_Prob": confidence_scores[2]
        }])

        try:
            existing = pd.read_csv(CSV_PATH)
            updated = pd.concat([existing, new_record], ignore_index=True)
        except FileNotFoundError:
            updated = new_record

        updated.to_csv(CSV_PATH, index=False)

        st.success("Prediction saved to analytics database ✅")

        st.markdown('</div>', unsafe_allow_html=True)

# ---------------------------------------------------
# Footer
# ---------------------------------------------------
st.markdown("---")
st.caption("Flipkart-style UI | Transformer-based Sentiment Model | Built with Streamlit")