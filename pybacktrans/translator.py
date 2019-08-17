# -*- coding: utf-8 -*-
from googletrans import Translator
import nltk
from nltk.tokenize import sent_tokenize

from pybacktrans.models import BackTranslated
from pybacktrans.constants import TEXT_MAX_LENGTH, LANGUAGES

try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')


class BackTranslator(object):
    """ 
    BackTranslate Class

    You have to create an instance of BackTranslator to use this library

    Translation service is based on Google Translate (http://translate.google.com)
    """

    def __init__(self):
        self.translator = Translator()  # Google translator object

    def backtranslate(self, text, src=None, mid=None):
        """
        Backtranslate the text (src lang -> mid lang -> src lang)

        e.g.
        text='Good Morning', src = 'en', mid='fr'
        English('Good Morning') -> French('Bonjour') -> English('Hello')

        :param text: The source text to be backtranslated
        :type text: :class:`str`

        :param src: Source language. You can set as 'auto' for auto detecting the source language.

        :param mid: Middle language.

        :rtype BackTranslated

        Basic usage:
            >>> from pybacktrans import BackTranslator
            >>> translator = BackTranslator()
            >>> result = translator.backtranslate('Good Morning', src='en', mid='fr')
            >>> result
            # <BackTranslated src=en, mid=fr, text=Hello>
            >>> result.src_text
            # 'Good Morning'
            >>> result.mid_text
            # 'Bonjour'
            >>> result.text
            # 'Hello'
        """
        # Check the src and mid
        if not src or src == 'auto':
            # Check with 100 characters of text and get the src language
            src = self.translator.detect(text[:100]).lang

        if not mid:
            if src == 'en':
                mid = 'fr'  # If src is 'en', then mid is 'fr.
            else:
                mid = 'en'  # Else, mid will be 'en' as default

        # Check whether the src and mid language is supported in Google Translation
        if src not in LANGUAGES:
            raise ValueError("'{}': Invalid source language".format(src))

        if mid not in LANGUAGES:
            raise ValueError("'{}': Invalid middle language".format(mid))

        if src == mid:
            raise ValueError("Source language({src}) and Middle Language({mid}) cannot be same".format(src=src, mid=mid))

            # Check whether the text is less than 5000(= MAX_LEN)
        if self._check_length_over_max(text):
            # Seperate the full text into multiple sentences
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

            back_text = back_text.rstrip()
        else:
            mid_text = self.translator.translate(text, src=src, dest=mid).text
            back_text = self.translator.translate(mid_text, src=mid, dest=src).text

        # Put final values into a new BackTranlated object
        result = BackTranslated(src=src, mid=mid,
                                src_text=text, mid_text=mid_text, text=back_text)

        return result

    def _check_length_over_max(self, text):
        # Check whether the text is longer than TEXT_MAX_LENGTH(5000 for google translate)
        if len(text.encode('utf-8')) > TEXT_MAX_LENGTH:
            return True
        return False

    def _split_into_sentences(self, text):
        return sent_tokenize(text)

    def _make_chunks(self, sentence_lst):
        """
        Chunk is a sentence that is not longer than TEXT_MAX_LENGTH

        By looping the list of sentences, we will make a new chunk which is not longer than TEXT_MAX_LENGTH, while as long as possible
        """
        input_chunk_lst = []
        chunk = ""
        for sentence in sentence_lst:
            if len((chunk.rstrip() + ' ' + sentence).encode('utf-8')) > TEXT_MAX_LENGTH:
                input_chunk_lst.append(chunk.rstrip())
                chunk = sentence + " "
            else:
                chunk = chunk + sentence + ' '
        input_chunk_lst.append(chunk.rstrip())
        return input_chunk_lst
