# Py-Backtrans

Python library for backtranslation

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
