# Spam Email Classifier

A Machine Learning + NLP project that classifies SMS messages as **Spam** or **Ham (Not Spam)** using **TF-IDF Vectorization** and **Multinomial Naive Bayes**.

---

## Features

- Load SMS dataset using pandas
- Text preprocessing
- TF-IDF vectorization
- Train spam classification model
- Accuracy evaluation
- Predict custom messages

---

## Project Structure

```txt
spam-email-classifier/
│
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── dataset/
│   └── spam.csv
│
├── modules/
│   ├── cleaner.py
│   ├── loader.py
│   ├── vectorizer.py
│   ├── trainer.py
│   ├── predictor.py
│   └── evaluator.py
│
└── model/
```

---

## Technologies Used

- Python
- Pandas
- Scikit-learn
- TF-IDF Vectorization
- Multinomial Naive Bayes
- NLP Text Preprocessing

---

## Installation

Clone repository:

```bash
git clone <your-github-link>
```

Go to project folder:

```bash
cd spam-email-classifier
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## How to Run

Run:

```bash
python main.py
```

Enter a custom message:

Example:

```txt
Win 5000 rupees now!!!
```

Output:

```txt
Prediction: Spam
```

---

## Example Accuracy

```txt
Accuracy: 97.85%
```

(Accuracy may vary slightly.)

---

## Future Improvements

- GUI version
- Email support
- Deep learning model
- Streamlit web app
- Save trained model

---

## Dataset

SMS Spam Collection Dataset from UCI Machine Learning Repository.

---

## Author

Ananth Jeeth Vuppala