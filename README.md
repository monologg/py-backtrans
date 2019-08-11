# Py-Backtrans

Python library for backtranslation

## TODO

- 여기에 간단히 image 넣기
- QANet 논문 레퍼런스 달기

## Installation

```bash
$ pip install pybacktrans
```

## Usage

### Basic Usage

```python
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
```

## Reference

- [googletrans](https://github.com/ssut/py-googletrans)
