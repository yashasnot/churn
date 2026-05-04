# 🚀 Customer Churn Prediction System

Predict whether a customer is likely to churn using Machine Learning.  
This project demonstrates a complete end-to-end ML pipeline from data preprocessing to deployment.

---

## 🌐 Live Demo
👉 https://churn-1-4e4x.onrender.com

---

## 📌 Project Overview

Customer churn is a critical problem in telecom and subscription-based businesses.  
In this project, we build a machine learning model to predict whether a customer will leave the service.

The solution uses **Logistic Regression** along with proper preprocessing and deployment using Streamlit.

---

## ⚙️ Features

- 📊 Data preprocessing using **ColumnTransformer**
- 🔢 Categorical encoding using **OneHotEncoder**
- 📉 Model training using **Logistic Regression**
- 🎯 Hyperparameter tuning with **GridSearchCV**
- ⚖️ Handling class imbalance (`class_weight='balanced'`)
- 🌐 Interactive UI using **Streamlit**
- 🚀 Deployed on **Render**

---

## 📈 Model Performance

- ROC-AUC Score: **0.84**
- Accuracy: **~80%**
- Optimized Threshold: **0.35**

---

## 🧠 Key Insights

- Customers with **low tenure** are more likely to churn  
- **Month-to-month contracts** increase churn probability  
- Higher **monthly charges** increase churn risk  
- Lack of **tech support & online security** leads to higher churn  

---

## 🏗️ Project Structure

<img width="178" height="368" alt="image" src="https://github.com/user-attachments/assets/e9a298a6-9d39-4850-867b-c38c33920154" />


---

## 🛠️ Tech Stack

- Python  
- Pandas, NumPy  
- Scikit-learn  
- Streamlit  
- Render  

---

## ▶️ Run Locally

```bash
git clone https://github.com/yashasnot/churn.git
cd churn/streamlit

pip install -r requirements.txt
streamlit run app.py
