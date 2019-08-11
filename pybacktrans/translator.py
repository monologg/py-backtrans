from googletrans import Translator
import nltk
from nltk.tokenize import sent_tokenize
import time

from constants import MAX_LEN

try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')


class BackTranslator(object):
    def __init__(self):
        self.translator = Translator()  # Google translator object

    def backtranslate(self, text, src='en', mid='fr'):
        # Check whether the text is less than 5000(= MAX_LEN)
        if self._check_length_over_max(text):
            # TODO: Seperate the full text into multiple sentences
            src_chunk_lst = self._make_chunks(self._split_into_sentences(text))
            mid_text = ""
            for chunk in src_chunk_lst:
                mid_text = mid_text + self.translator.translate(chunk, src=src, dest=mid).text + " "
            mid_text = mid_text.rstrip()

            # Mid text also need check for length
            mid_chuck_lst = self._make_chunks(self._split_into_sentences(mid_text))
            back_text = ""
            for chunk in mid_chuck_lst:
                back_text = back_text + self.translator.translate(chunk, src=mid, dest=src).text + " "

            return back_text.rstrip()
        else:
            mid_text = self.translator.translate(text, src=src, dest=mid).text
            back_text = self.translator.translate(mid_text, src=mid, dest=src).text
            return back_text

    def _check_length_over_max(self, text):
        if len(text.encode('utf-8')) > MAX_LEN:
            return True
        return False

    def _split_into_sentences(self, text):
        return sent_tokenize(text)

    def _make_chunks(self, sentence_lst):
        input_chunk_lst = []
        chunk = ""
        for sentence in sentence_lst:
            if len(chunk.rstrip()) + len(sentence) > MAX_LEN:
                input_chunk_lst.append(chunk.rstrip())
                chunk = ""
            else:
                chunk = chunk + sentence + ' '
        input_chunk_lst.append(chunk.rstrip())
        return input_chunk_lst


class BackTransResult(object):
    def __init__(self):
        self.mid_text = None
        self.text = None


if __name__ == "__main__":
    with open('text.txt', 'r', encoding='utf-8') as f:
        text = f.read()
    backtrans = BackTranslator()
    print(backtrans.backtranslate(text))
