from sklearn.naive_bayes import MultinomialNB

def train_model(x_train, y_train):

    model = MultinomialNB()
    model.fit(x_train, y_train)

    return model