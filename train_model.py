import pandas as pd
import re
import tldextract
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib

# Load dataset
df = pd.read_csv("dataset.csv")

# Ensure correct column names
if 'label' not in df.columns:
    df.columns = ['url', 'label']

# Feature extraction function
def extract_features(df):
    df = df.copy()
    df['url_length'] = df['url'].apply(len)
    df['count_dots'] = df['url'].apply(lambda x: x.count('.'))
    df['count_hyphens'] = df['url'].apply(lambda x: x.count('-'))
    df['count_subdirs'] = df['url'].apply(lambda x: x.count('/'))
    df['has_https'] = df['url'].apply(lambda x: 1 if 'https' in x.lower() else 0)
    df['has_ip'] = df['url'].apply(lambda x: 1 if re.match(r'http[s]?://(?:[0-9]{1,3}\.){3}[0-9]{1,3}', x) else 0)
    df['has_suspicious_word'] = df['url'].apply(
        lambda x: 1 if any(word in x.lower() for word in ['login', 'verify', 'bank', 'account', 'update']) else 0
    )

    # New features using tldextract
    df['subdomain'] = df['url'].apply(lambda x: tldextract.extract(x).subdomain)
    df['subdomain_length'] = df['subdomain'].apply(len)
    df['is_misleading_subdomain'] = df['subdomain'].apply(
        lambda x: 1 if any(kw in x.lower() for kw in ['paypal', 'amazon', 'google', 'bank']) else 0
    )

    return df

# Extract features
df_features = extract_features(df)

# Prepare X and y
X = df_features.drop(['url', 'label', 'subdomain'], axis=1)  # Drop 'url' and 'subdomain' columns
y = df_features['label']

# Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print("📊 Classification Report:")
print(classification_report(y_test, y_pred))

# Save the trained model
joblib.dump(model, 'train_model.pkl')
print("✅ Model trained and saved and ready to run.")
