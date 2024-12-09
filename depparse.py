from .load_model import load_model



nlp = load_model()

def depparse(text):
    token = nlp(text.replace(' ', ''))
    return token
