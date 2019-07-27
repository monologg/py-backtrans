from googletrans import Translator
import nltk
from nltk import tokenize
import time

try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')


class BackTranslator(object):
    def __init__(self):
        self.translator = Translator()  # Google translator object

    def backtranslate(self, src='en', mid='fr'):
        start_t = time.time()
        with open('text.txt', 'r', encoding='utf-8') as f:
            text = f.read()
        mid_text = self.translator.translate(text, src=src, dest=mid).text
        back_text = self.translator.translate(mid_text, src=mid, dest=src).text
        print(back_text)
        print(time.time()-start_t)


if __name__ == "__main__":
    backtrans = BackTranslator()
    backtrans.backtranslate()
