from googletrans import Translator
import nltk
from nltk import tokenize

try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')
