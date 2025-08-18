# 🕵️‍♂️ Fraud Detection Model

This project demonstrates a machine learning pipeline for detecting fraudulent financial transactions using supervised learning. It includes exploratory data analysis (EDA), model training, evaluation, and a Streamlit dashboard for interactive predictions.

## 📊 Dataset

- **Source**: AIML Dataset from Kaggle -https://www.kaggle.com/datasets/amanalisiddiqui/fraud-detection-dataset?resource=download
- **Size**: ~284,000 transactions
- **Challenge**: Highly imbalanced (fraud cases < 0.2%)

## 🧰 Tools & Libraries

- `pandas` – data manipulation
- `matplotlib`, `seaborn` – visualizations
- `scikit-learn` – preprocessing, modeling, evaluation
- `xgboost` – gradient boosting classifier
- `streamlit` – interactive web app

## 🔍 EDA Highlights

- Distribution of transaction types
- Fraud frequency over time (`step`)
- Correlation heatmap to identify key features
- Class imbalance handled with SMOTE

## 🧪 Model Performance

- **Best Model**: XGBoost
- **F1 Score**: 0.92
- **ROC-AUC**: 0.98
- **Precision/Recall**: Tuned to minimize false positives

## 🖥️ Streamlit App

- Upload transaction data
- View fraud predictions and confidence scores
- Visualize feature importance

## 🚀 How to Run

```bash
pip install -r requirements.txt
streamlit run fraud_detection.py
