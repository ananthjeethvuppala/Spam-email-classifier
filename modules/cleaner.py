import string

def clean_text(text):

    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    words = text.split()
    text = " ".join(words)

    return text