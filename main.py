from modules.loader import load_dataset
from modules.cleaner import clean_text
from modules.vectorizer import prepare_data
from modules.trainer import train_model
from modules.evaluator import evaluate_model
from modules.predictor import predict_message

data = load_dataset("dataset/spam.csv")

data['message'] = data['message'].apply(clean_text)

x_train, x_test, y_train, y_test, vectorizer = prepare_data(data)

model = train_model(x_train, y_train)

accuracy = evaluate_model(model, x_test, y_test)

print(f"Accuracy: {accuracy * 100:.2f}%")

message = input("\nEnter a message: ")
result = predict_message(model, vectorizer, message)

print(f"\nPrediction: {result.upper()}")