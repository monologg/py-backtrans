from pybacktrans import BackTranslator


if __name__ == "__main__":
    # with open('text.txt', 'r', encoding='utf-8') as f:
    #     text = f.read()
    backtrans = BackTranslator()
    result = backtrans.backtranslate("Good Morning", src='auto')
    print(result.src_text)
    print(result.mid_text)
    print(result.text)
