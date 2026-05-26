from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split

def prepare_data(data):

    x = data['message']
    y = data['label']

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

    vectorizer = TfidfVectorizer()
    x_train_vectors = vectorizer.fit_transform(x_train)
    x_test_vectors = vectorizer.transform(x_test)

    return (x_train_vectors, x_test_vectors, y_train, y_test, vectorizer)