
import argparse
import joblib
import os

# Define Rust keywords for feature extraction
rust_keywords = ['let', 'mut', 'fn', 'unsafe', 'match', 'impl', 'struct', 'enum', 'if', 'else', 'loop', 'while', 'for', 'return']

def extract_features(code):
    features = {}
    features['length'] = len(code)
    features['num_lines'] = code.count('\n') + 1
    features['num_unsafe'] = code.count('unsafe')
    features['num_pointer_ops'] = code.count('*mut') + code.count('*const')
    features['num_keywords'] = sum(code.count(kw) for kw in rust_keywords)
    return features

def main():
    parser = argparse.ArgumentParser(description="Predict if a Rust code snippet is Safe or Unsafe using ML")
    parser.add_argument('--file', type=str, required=True, help='Path to the Rust (.rs) file')
    args = parser.parse_args()

    # Load code from file
    if not os.path.exists(args.file):
        print(f"File not found: {args.file}")
        return

    with open(args.file, 'r') as f:
        code = f.read()

    # Load model and feature list
    model = joblib.load('rust_safety_rf_model.joblib')
    feature_list = joblib.load('rust_safety_features_list.joblib')

    # Extract features
    features = extract_features(code)
    feature_vector = [[features[feat] for feat in feature_list]]

    # Predict
    prediction = model.predict(feature_vector)[0]
    prob = model.predict_proba(feature_vector)[0]

    print("\n🧠 Prediction Result:")
    if prediction == 1:
        print("⚠️  This Rust code is likely UNSAFE.")
    else:
        print("✅ This Rust code is likely SAFE.")

    print(f"Confidence: Safe={prob[0]:.2f}, Unsafe={prob[1]:.2f}\n")

if __name__ == "__main__":
    main()
