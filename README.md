# Sentiment Analysis on Flipkart Customer Reviews Using NLP and Machine Learning

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

## 📂 Dataset Access
Due to GitHub file size limitations, the dataset is not included in this repository.

### How to Reproduce the Results
1. Download the Flipkart Products Review Dataset from Kaggle  
2. Rename the file to `Dataset.csv`  
3. Place the file inside the `data/` directory  

Once the dataset is added, the notebook can be executed from top to bottom without any changes.

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
This project demonstrates how **aspect-based sentiment analysis transforms unstructured reviews into decision-ready insights**.  
The approach is scalable and can be extended to real-time customer feedback systems in e-commerce and customer experience analytics.

---

## 🧰 Tech Stack
- Python  
- Pandas, NumPy  
- NLTK  
- Matplotlib  

---

## 📌 Future Enhancements
- Automate aspect refinement using clustering or embeddings  
- Scale aspect extraction to full dataset  
- Integrate real-time review streams  
