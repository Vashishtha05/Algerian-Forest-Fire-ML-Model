# 🔥 Algerian Forest Fire — End-to-End Machine Learning Project

<p align="center">
  <img src="https://img.shields.io/badge/Python-Machine%20Learning-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/Scikit--Learn-Modeling-orange?style=for-the-badge">
  <img src="https://img.shields.io/badge/ElasticNet-Regularization-success?style=for-the-badge">
  <img src="https://img.shields.io/badge/Project-End--to--End%20ML-black?style=for-the-badge">
</p>

<p align="center">
  An end-to-end Machine Learning workflow built on the Algerian Forest Fire dataset.  
  This project demonstrates Exploratory Data Analysis, Feature Engineering, Regression Modeling,  
  and deployment-ready model serialization using Python, Scikit-Learn and streamlit.
</p>

---

## 📌 Table of Contents

* Overview
* Project Goals
* Dataset Information
* Project Workflow
* Features
* Tech Stack
* Folder Structure
* Model Pipeline
* Algorithms Used
* Results & Evaluation
* How to Run
* Skills Demonstrated
* Future Improvements
* Author

---

## 🧠 Overview

Wildfire prediction is a critical real-world application of Machine Learning.
This repository showcases a complete ML lifecycle:

* Data Cleaning & EDA
* Regression Modeling (Linear → Elastic Net)
* Model Evaluation
* Saving trained models
* Preparing a prediction application

The goal is not just prediction — but demonstrating strong **ML engineering fundamentals**.

---

## 🎯 Project Goals

* Perform structured Exploratory Data Analysis
* Understand feature relationships
* Compare multiple regression algorithms
* Apply regularization techniques
* Build a deployable ML pipeline

---

## 📊 Dataset Information

Dataset: Algerian Forest Fires Dataset

Features include:

* Temperature
* Relative Humidity
* Wind Speed
* Rain
* FFMC, DMC, ISI indices
* Region classification

Target:

* Fire Weather Index (FWI)

---

## 🔄 Project Workflow

1. Data Cleaning
2. Feature Engineering
3. Exploratory Data Analysis
4. Model Training
5. Model Comparison
6. Hyperparameter Tuning
7. Model Serialization

---

## ✨ Features

* Structured ML pipeline
* Multiple regression models
* Elastic Net regularization
* Model saving using `.pkl`
* Notebook-based experimentation
* Modular project layout

---

## 🧱 Tech Stack

| Technology       | Purpose               |
| ---------------- | --------------------- |
| Python           | Core Language         |
| Pandas           | Data Processing       |
| NumPy            | Numerical Computation |
| Scikit-Learn     | Modeling              |
| Matplotlib       | Visualization         |
| Jupyter Notebook | Experimentation       |

---

## 📂 Folder Structure

```
25 ML Project
│
├── 3.0-Model+Training/
├── models/
│   ├── ridge.pkl
│   └── scaler.pkl
├── application.py
├── train_revised.csv
├── notebooks (.ipynb)
└── README.md
```

---

## ⚙️ Model Pipeline

Data → Preprocessing → Scaling → Model Training → Evaluation → Saved Model

Pipeline Includes:

* StandardScaler
* Linear Regression
* Ridge Regression
* Lasso Regression
* Elastic Net

---

## 🤖 Algorithms Used

* Simple Linear Regression
* Multiple Linear Regression
* Ridge Regression
* Lasso Regression
* Elastic Net Regression

Regularization helped reduce overfitting and improved model stability.

---

## 📈 Results & Evaluation

Evaluation Metrics:

* Mean Squared Error
* R² Score
* Cross Validation

Elastic Net provided a balanced trade-off between bias and variance.

---

## 🚀 How to Run

Clone repository:

```
git clone https://github.com/YOUR-USERNAME/Algerian-Forest-Fire-ML-Model.git
```

Install dependencies:

```
pip install pandas numpy scikit-learn matplotlib
```

Run training notebook or application:

```
python application.py
```

---

## 🧩 Skills Demonstrated

* Exploratory Data Analysis
* Regression Modeling
* Feature Engineering
* Model Regularization
* Machine Learning Workflow Design
* Python Project Structuring

---

## 🔮 Future Improvements

* Hyperparameter Optimization with GridSearchCV
* Model Deployment via Flask API
* Automated Training Pipeline

---

## 🧑‍💻 Author

**Vashishtha Verma**

- Electrical Engineering Student  
- Machine Learning Enthusiast

---

<p align="center">
⭐ If you found this project useful, consider giving it a star.
</p>
