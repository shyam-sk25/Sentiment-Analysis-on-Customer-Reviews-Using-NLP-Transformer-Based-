# 🏆 Aspect-Based Sentiment Analysis on Flipkart Customer Reviews Using NLP

---

## 📌 Project Overview

This project implements a **rule-based Aspect-Based Sentiment Analysis (ABSA)** pipeline on large-scale Indian e-commerce customer reviews.

Instead of analyzing only overall sentiment, the system extracts **specific product and service aspects** from reviews and evaluates sentiment at the aspect level to generate **actionable business insights**.

---

## 🎯 Objectives

- Extract key aspects discussed in customer reviews  
- Analyze sentiment (Positive / Neutral / Negative) at the aspect level  
- Normalize raw aspects into meaningful business categories  
- Identify major drivers of customer satisfaction and dissatisfaction  

---

## 📊 Dataset

- **Source:** Flipkart Products Review Dataset  
- **Size:** ~363,000 reviews  
- **Domain:** Indian E-commerce  
- **Fields Used:**
  - Review Title  
  - Review Text  
  - Rating (1–5 stars)

Dataset encoding issues were handled using appropriate character decoding.

> Ratings were used as **weak supervision** to derive sentiment labels without manual annotation.

---

## 📂 Dataset Access

Due to GitHub file size limitations, the dataset is not included in this repository.

### How to Reproduce the Results

1. Download the Flipkart Products Review Dataset from Kaggle  
2. Rename the file to `Dataset.csv`  
3. Place the file inside the `data/` directory  

Once added, the notebook can be executed from top to bottom without any changes.

---

## 🔄 Pipeline Architecture


---

## 🛠️ Methodology

### 1️⃣ Data Cleaning & Preparation
- Removed records with missing critical fields  
- Fixed mixed data types in ratings  
- Combined review title and review body for richer context  

### 2️⃣ Text Preprocessing
- Lowercasing  
- Noise removal (URLs, symbols, numbers)  
- Stopword removal  
- Lemmatization  

### 3️⃣ Aspect Extraction
- Used **Part-of-Speech (POS) tagging**  
- Extracted **noun phrases** as aspects using rule-based chunking  
- Aspect extraction was performed on a representative subset to balance scalability and computational efficiency  

### 4️⃣ Aspect-Based Sentiment Analysis
- Mapped ratings to sentiment classes:
  - 1–2 → Negative  
  - 3 → Neutral  
  - 4–5 → Positive  
- Linked extracted aspects with sentiment labels  

### 5️⃣ Aspect Normalization
Raw aspects were grouped into business-level categories:

- Product Quality  
- Value for Money  
- Purchase Experience  
- Delivery  
- Packaging  
- Other (emerging / uncategorized aspects)  

---

## 📈 Key Insights

- **Product Quality** is the strongest driver of both positive and negative sentiment  
- **Value for Money** reflects high price sensitivity in the Indian market  
- **Purchase Experience, Delivery, and Packaging** show stable positive sentiment  
- The **Other** category reveals emerging issues such as noise, cooling performance, and build quality  

---

## 📊 Visualization

A final visualization summarizes sentiment distribution across normalized aspects, enabling quick identification of priority improvement areas.

---

## 🚀 Conclusion

This project demonstrates how **rule-based aspect-based sentiment analysis transforms unstructured reviews into decision-ready insights**.

The approach is explainable, scalable, and can be extended to real-time customer feedback systems in e-commerce and customer experience analytics.

---

## 🧰 Tech Stack

- Python  
- Pandas  
- NumPy  
- NLTK  
- Matplotlib  
- Rule-based NLP (POS Tagging & Chunking)

---

## 📌 Future Enhancements

- Automate aspect refinement using clustering or embeddings  
- Scale aspect extraction to full dataset  
- Integrate real-time review streams  
- Explore transformer-based sentiment models for comparison  

---
