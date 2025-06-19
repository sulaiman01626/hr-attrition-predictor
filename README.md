# hr-attrition-predictor
Predict employee attrition using ML + Streamlit"
# 🧑‍💼 HR Employee Attrition Predictor

This project uses a machine learning model to predict whether an employee will leave the company (attrition) based on HR data such as age, salary, education, and job level.

---

## 📁 Files Included

- `HR_Employee_Attrition.csv` – Sample HR dataset  
- `app.py` – Streamlit web application  
- `attrition_app.ipynb` – Google Colab notebook for training the ML model  

---

## 🚀 Live Demo (if using ngrok)

Once hosted, you can use [ngrok](https://ngrok.com/) to expose the Streamlit app and get a public URL.

---

## ⚙️ How to Run the Project

### ▶️ Option 1: Run in Google Colab

1. Upload all files (`.ipynb`, `.csv`, `.py`) to your Colab environment
2. Open `attrition_app.ipynb` and run all cells
3. Use `ngrok` public link to view the app

### ▶️ Option 2: Run Locally

```bash
# Clone the repository
git clone https://github.com/your-username/hr-attrition-predictor.git
cd hr-attrition-predictor

# Install dependencies
pip install streamlit scikit-learn pandas joblib

# Run the app
streamlit run app.py

📊 Features
Predict employee attrition (will leave / will stay)

Streamlit interface for easy input

Trained with RandomForestClassifier

Dataset encoded with LabelEncoder

Real-time prediction on user input
