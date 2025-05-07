
# Rust Code Safety Prediction using Machine Learning

This project uses machine learning to predict whether a given Rust code snippet is likely to be safe or unsafe. 
We trained a Random Forest model on labeled Rust code examples and created both a command-line tool and a Streamlit web app for easy usage.

## Features
- Detects unsafe Rust code using ML
- Accepts `.rs` files as input
- Provides prediction with confidence scores
- Includes web interface via Streamlit

## Project Structure

```
📁 rust_safety_checker/
├── app.py                 → Streamlit web app
├── predict_rust_safety.py → CLI prediction script
├── rust_safety_rf_model.joblib → Trained ML model
├── rust_code_dataset.csv  → CSV dataset (code + label)
├── requirements.txt       → Python packages
├── README.md              → This file
```

## Installation & Setup

```bash
# 1. Clone this repository
git clone https://github.com/your-username/rust-safety-checker.git
cd rust_safety_checker

# 2. Create a virtual environment (optional but recommended)
python -m venv venv
venv\Scripts\activate  # On Windows

# 3. Install required packages
pip install -r requirements.txt
```

## Running the CLI Tool

```bash
python predict_rust_safety.py --file test.rs
```

Make sure `test.rs` is a valid Rust function file.

## Running the Web App

```bash
streamlit run app.py
```

Then open the local URL provided by Streamlit (usually http://localhost:8501).

## Sample Output

```
🧠 Prediction Result:
✅ This Rust code is likely SAFE.
Confidence: Safe=0.83, Unsafe=0.17
```

## Dataset Info
- 50 manually labeled Rust functions
- `label = 0` → safe
- `label = 1` → unsafe

## Acknowledgment
Some parts of this project were assisted using ChatGPT for idea generation, code snippets, and documentation formatting.
