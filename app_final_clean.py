
import streamlit as st
import joblib

# Load model and features
model = joblib.load("rust_safety_rf_model.joblib")
feature_list = joblib.load("rust_safety_features_list.joblib")

# Define Rust keywords
rust_keywords = ['let', 'mut', 'fn', 'unsafe', 'match', 'impl', 'struct', 'enum',
                 'if', 'else', 'loop', 'while', 'for', 'return']

# Feature extraction
def extract_features(code):
    features = {}
    features["length"] = len(code)
    features["num_lines"] = code.count("\n") + 1
    features["num_unsafe"] = code.count("unsafe")
    features["num_pointer_ops"] = code.count("*mut") + code.count("*const")
    features["num_keywords"] = sum(code.count(kw) for kw in rust_keywords)
    return features

# Page settings
st.set_page_config(page_title="Rust Safety Predictor", page_icon="🦀")

# Header
st.markdown(
    "<h1 style='text-align: center;'>🦀 Rust Code Safety Predictor</h1>",
    unsafe_allow_html=True,
)
st.markdown(
    "<h4 style='text-align: center; color: gray;'>Operating Systems Project 2025 – Texas A&M University–San Antonio</h4>",
    unsafe_allow_html=True,
)
st.write("")

# Input
st.markdown("### 🔍 Paste your Rust code or upload a `.rs` file")
code_input = st.text_area("", placeholder="Paste your Rust code here...", height=200)
uploaded_file = st.file_uploader("📁 Or upload a .rs file", type=["rs"])

if uploaded_file:
    code_input = uploaded_file.read().decode("utf-8")

# Prediction
if st.button("🔮 Predict Safety"):
    if code_input.strip() == "":
        st.warning("Please provide Rust code input.")
    else:
        features = extract_features(code_input)
        feature_vector = [[features[feat] for feat in feature_list]]
        prediction = model.predict(feature_vector)[0]
        prob = model.predict_proba(feature_vector)[0]

        st.write("---")
        if prediction == 1:
            st.error("⚠️ **This Rust code is likely UNSAFE.**")
        else:
            st.success("✅ **This Rust code is likely SAFE.**")

        st.markdown("**Confidence Score:**")
        st.markdown(f"- 🟢 Safe: `{prob[0]:.2f}`")
        st.markdown(f"- 🔴 Unsafe: `{prob[1]:.2f}`")

# Footer
st.write("---")
st.markdown(
    "<div style='text-align: center; font-size: 0.9em; color: gray;'>"
    "Developed by <b>Saiharshavardhan Reddy Kalchuri</b> | Texas A&M University–San Antonio | © 2025"
    "</div>",
    unsafe_allow_html=True,
)
