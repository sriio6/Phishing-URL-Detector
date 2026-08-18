import tkinter as tk
from tkinter import messagebox
import joblib
import pandas as pd
import re

# 1) Load the trained model (Joblib + correct filename)
model = joblib.load("phishing_model.pkl")

# 2) Feature extraction — must match training exactly
def extract_features(url):
    return pd.DataFrame([{
        'url_length': len(url),
        'count_dots': url.count('.'),
        'count_hyphens': url.count('-'),
        'count_subdirs': url.count('/'),
        'has_https': int('https' in url.lower()),
        'has_ip': int(bool(re.match(r'^\d{1,3}(\.\d{1,3}){3}', url))),
        'has_suspicious_word': int(any(word in url.lower() 
                                      for word in ['login', 'secure', 'account', 'update']))
    }])

# 3) Prediction callback
def predict_url():
    url = url_entry.get().strip()
    if not url:
        messagebox.showwarning("Input Error", "Please enter a URL.")
        return

    features = extract_features(url)
    pred = model.predict(features)[0]
    if pred == 1:
        result_label.config(text="🔴 Phishing Website Detected!", fg="red")
    else:
        result_label.config(text="🟢 Legitimate Website", fg="green")

# 4) Clear callback
def clear_input():
    url_entry.delete(0, tk.END)
    result_label.config(text="")

# 5) Build GUI
root = tk.Tk()
root.title("Phishing Website Detector")
root.geometry("400x300")
root.configure(bg="#f0f0f0")

# Title Label
title_label = tk.Label(root, text="Phishing Website Detector", font=("Arial", 16, "bold"), bg="#f0f0f0")
title_label.pack(pady=10)

# URL Entry
tk.Label(root, text="Enter URL:", font=("Arial", 12), bg="#f0f0f0").pack(pady=5)
url_entry = tk.Entry(root, width=50, font=("Arial", 12))
url_entry.pack(pady=5)

# Buttons
button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=10)

check_button = tk.Button(button_frame, text="Check", command=predict_url, font=("Arial", 12), bg="#4CAF50", fg="white")
check_button.pack(side=tk.LEFT, padx=5)

clear_button = tk.Button(button_frame, text="Clear", command=clear_input, font=("Arial", 12), bg="#f44336", fg="white")
clear_button.pack(side=tk.LEFT, padx=5)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 14, "bold"), bg="#f0f0f0")
result_label.pack(pady=20)

root.mainloop()
