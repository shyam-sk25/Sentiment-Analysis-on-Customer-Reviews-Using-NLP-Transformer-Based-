# Aspect-Based Sentiment Analysis on Indian E-commerce Reviews

## 📌 Project Overview
This project implements an **Aspect-Based Sentiment Analysis (ABSA)** system on large-scale Indian e-commerce customer reviews.  
Instead of analyzing only overall sentiment, the system identifies **specific product and service aspects** and evaluates sentiment at the aspect level to generate **actionable business insights**.

---

## 🎯 Objectives
- Extract key aspects discussed in customer reviews
- Analyze sentiment (Positive / Neutral / Negative) at the aspect level
- Normalize raw aspects into meaningful business categories
- Identify major drivers of customer satisfaction and dissatisfaction

---

## 📊 Dataset
- **Source**: Flipkart Products Review Dataset  
- **Size**: ~363,000 reviews  
- **Domain**: Indian e-commerce  
- **Fields used**:
  - Review title
  - Review text
  - Rating (1–5 stars)

> Dataset encoding issues were handled using appropriate character decoding.

---

## 🛠️ Methodology

### 1. Data Cleaning & Preparation
- Removed records with missing critical fields
- Fixed mixed data types in ratings
- Combined review title and review body for richer context

### 2. Text Preprocessing
- Lowercasing
- Noise removal (URLs, symbols, numbers)
- Stopword removal
- Lemmatization

### 3. Aspect Extraction
- Used **Part-of-Speech tagging**
- Extracted **noun phrases** as aspects using rule-based chunking
- Applied extraction on a representative sample for scalability

### 4. Aspect-Based Sentiment Analysis
- Mapped ratings to sentiment classes:
  - 1–2 → Negative
  - 3 → Neutral
  - 4–5 → Positive
- Linked extracted aspects with sentiment labels

### 5. Aspect Normalization
- Grouped raw aspects into business-level categories:
  - Product Qu

