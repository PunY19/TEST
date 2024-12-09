from .load_model import load_model
import warnings

warnings.filterwarnings("ignore")
nlp = load_model()

def depparse(text):
    token = nlp(text.replace(' ', ''))
    return token
