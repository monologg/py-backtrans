# Py-Backtrans

[![Release](https://img.shields.io/badge/release-v0.1.4-green)](https://pypi.org/project/pybacktrans/)
[![Downloads](https://pepy.tech/badge/pybacktrans)](https://pepy.tech/project/pybacktrans)
[![license](https://img.shields.io/badge/license-Apache%202.0-red)](https://github.com/monologg/pybacktrans/blob/master/LICENSE)

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
- [QANet](https://arxiv.org/abs/1804.09541)
