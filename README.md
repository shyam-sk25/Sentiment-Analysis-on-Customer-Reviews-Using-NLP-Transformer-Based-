#  Sentiment Analysis on Customer Reviews Using NLP (Transformer-Based)

---

## 📌 Project Overview

This project implements a **Transformer-based Sentiment Analysis system** on large-scale Indian e-commerce customer reviews.

Using a fine-tuned **DistilBERT** model, the system classifies customer reviews into:

- ✅ Positive  
- ⚪ Neutral  
- ❌ Negative  

The trained model is deployed using **Streamlit** for real-time sentiment prediction and integrated with **Power BI** to generate business-level insights.

This project demonstrates a complete **end-to-end NLP pipeline**, covering data preprocessing, model training, deployment, and business analytics.

---

## 🎯 Objectives

- Build a 3-class sentiment classification model using NLP  
- Fine-tune a Transformer model (DistilBERT) on e-commerce review data  
- Evaluate model performance using standard metrics  
- Deploy the trained model using Streamlit  
- Generate business insights using Power BI  

---

## 📊 Dataset

- **Source:** Flipkart Product Reviews Dataset (Kaggle)  
- **Size:** ~300,000+ reviews  
- **Domain:** Indian E-commerce  

### Fields Used

- `Product_name`  
- `Price`  
- `Rating` (1–5 stars)  
- `Review`  
- `Summary`  

### Sentiment Labeling Strategy

Ratings were mapped to sentiment classes:

- 1–2 → **Negative**  
- 3 → **Neutral**  
- 4–5 → **Positive**  

This weak supervision approach enabled supervised learning without manual annotation.

---

## 🔄 Pipeline Architecture
Raw Reviews
↓
Data Cleaning
↓
Tokenization (DistilBERT Tokenizer)
↓
Fine-Tuning Transformer Model
↓
Model Evaluation
↓
Model Deployment (Streamlit)
↓
Business Intelligence (Power BI)
---

## 🛠️ Methodology

### 1️⃣ Data Cleaning & Preparation

- Removed records with missing values  
- Fixed encoding issues  
- Converted rating column to numeric format  
- Combined review title and body where required  
- Generated sentiment labels from ratings  

---

### 2️⃣ Text Preprocessing

- Tokenization using HuggingFace `AutoTokenizer`  
- Padding and truncation (`max_length = 128`)  
- Attention mask generation  
- Train-test split (80–20)  

---

### 3️⃣ Model Selection

**DistilBERT (Transformer-based architecture)**

#### Why DistilBERT?

- 6 transformer layers (BERT has 12)  
- ~40% smaller than BERT  
- ~60% faster inference  
- Retains ~97% of BERT’s performance  
- Suitable for deployment environments  

The model was fine-tuned for 3-class sentiment classification.

---

### 4️⃣ Model Training

- **Loss Function:** CrossEntropyLoss  
- **Optimizer:** AdamW  
- Fine-tuned on labeled e-commerce dataset  
- Backpropagation used for weight updates  
- Evaluated on hold-out test set  

---

### 5️⃣ Model Evaluation

The fine-tuned model achieved:

- 🎯 **Accuracy: 98.88%**  
- High Precision, Recall, and F1-score across all classes  
- Strong alignment between predicted sentiment and ratings  

Confusion matrix analysis showed minimal misclassification.

---

## 🚀 Deployment (Streamlit Application)

The trained model was saved using `save_pretrained()` and deployed using **Streamlit**.

### Features

- Real-time sentiment prediction  
- Product name & rating input  
- Confidence score visualization  
- Rating–Sentiment mismatch detection
 

This demonstrates practical model serving capability.
<img width="1361" height="675" alt="SEBTIMENTAL ANALYSIS" src="https://github.com/user-attachments/assets/1134c91e-d7f7-4c2a-8f3c-c459e6c2941e" />

---

## 📊 Business Intelligence Layer (Power BI)

After generating predictions for 20,000 representative reviews, a Power BI dashboard was created to analyze:

- Overall Sentiment Composition  
- Rating Distribution  
- Product-wise Sentiment Breakdown  
- Rating vs Sentiment Alignment  
- Key Business Insights  

This bridges Machine Learning with real-world decision-making analytics.
<img width="871" height="486" alt="Sentiment Analysis on Customer Reviews" src="https://github.com/user-attachments/assets/cd2ed03e-3817-404b-8754-b0e95eecaaff" />

---

## 📈 Key Insights

- ~75%+ reviews classified as **Positive**  
- Average rating indicates strong customer satisfaction  
- 5-star reviews strongly align with Positive sentiment  
- Negative sentiment concentrated in 1–2 star ratings  
- Product Quality and Value for Money are key satisfaction drivers  

---

## 🧰 Tech Stack

- Python  
- Pandas  
- NumPy  
- PyTorch  
- HuggingFace Transformers  
- Streamlit  
- Power BI  

---

## 📌 Future Enhancements

- Implement Aspect-Based Sentiment Analysis using transformers  
- Deploy as REST API (FastAPI)  
- Experiment with larger transformer models (BERT-base)  
- Implement Explainable AI (SHAP / LIME)  
- Real-time streaming sentiment analysis  

---

## 🎓 Skills Demonstrated

- NLP Pipeline Design  
- Transformer Fine-Tuning  
- Model Evaluation  
- Deployment Engineering  
- Business Analytics Integration  
- End-to-End AI System Development  

---

This project showcases the practical application of Transformer-based NLP models in real-world e-commerce analytics and customer experience intelligence.
