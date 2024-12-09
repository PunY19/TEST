from .load_model import load_model
import warnings

warnings.filterwarnings("ignore")
warnings.filterwarnings("ignore", category=UserWarning, module="stanza")
nlp = load_model()

def depparse(text):
    token = nlp(text.replace(' ', ''))
    return token
