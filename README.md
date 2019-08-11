# Py-Backtrans

Python library for backtranslation

## TODO

- google translate를 이용하여 진행한다는 것을 기록
- lang setting 인자에 관한 설명 간단히 달기
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
