Phishing URL Detector

Phishing URL Detector is a simple Python project that checks whether a website URL is likely to be phishing or legitimate. The project uses machine learning to identify patterns in URLs and provides the result through a small desktop application.

Features

- Check a URL for possible phishing activity
- Extract useful features from the URL
- Use a trained Random Forest model for prediction
- Display the result through a simple GUI
- Clear the entered URL and check another one

Technologies Used 

- Python
- Pandas
- Scikit-learn
- Tkinter
- Joblib
- Regular Expressions
- TLDExtract

How It Works

The project extracts different features from a URL, such as its length, number of dots and hyphens, number of subdirectories, HTTPS usage, IP address usage, and suspicious words.

These features are given to a trained Random Forest model, which predicts whether the URL is phishing or legitimate.

How to Run

Install the required Python libraries:

```bash
pip install pandas scikit-learn joblib tldextract
```

Run the application:

```bash
python phishing_gui.py
```

Enter a URL in the application and click **Check** to get the prediction.

Files

- `phishing_gui.py` — Desktop application for checking URLs
- `train_model.py` — Code used to train the machine learning model
- `phishing_model.pkl` — Trained Random Forest model



Future Improvements

- Add more URL features
- Improve the model using a larger and more diverse dataset
- Add support for checking URLs directly from a web browser
- Improve the graphical interface
