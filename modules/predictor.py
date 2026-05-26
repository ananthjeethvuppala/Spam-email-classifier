from modules.cleaner import clean_text

def predict_message(model, vectorizer, message):
    
    cleaned_message = clean_text(message)
    vector = vectorizer.transform([cleaned_message])
    prediction = model.predict(vector)

    return prediction[0]