from modules.loader import load_dataset
from modules.cleaner import clean_text
from modules.vectorizer import prepare_data

data = load_dataset("dataset/spam.csv")

data['message'] = data['message'].apply(clean_text)

x_train, x_test, y_train, y_test, vectorizer = prepare_data(data)

print(data.head())
print(x_train.shape)
print(x_test.shape)