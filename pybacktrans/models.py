# -*- coding: utf-8 -*-
class BackTranslated(object):
    """BackTranslate result object

    :param src: source langauge
    :param mid: mid language
    :param src_text: original source text
    :param mid_text: mid-translated text
    :param text: backtranslated text
    """

    def __init__(self, src, mid, src_text, mid_text, text):
        self.src = src
        self.mid = mid
        self.src_text = src_text
        self.mid_text = mid_text
        self.text = text

    def __str__(self):
        return self.__unicode__()

    def __unicode__(self):
        rep_text = ' '.join(self.text[:80].split())  # Only show max 80 characters
        if len(self.text) > 80:
            rep_text += '...'
        return u'BackTranslated(src={src}, mid={mid}, text={text})'.format(src=self.src, mid=self.mid, text=rep_text)
