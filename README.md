# OldHangeul

`OldHangeul`은 Python에서 옛한글을 편리하게 다루기 위해 개발한 패키지입니다. 

파이썬에서는 한양 PUA로 인코딩된 완성형 옛한글을 지원하지 않습니다. 그래서 옛한글이 포함된 텍스트는 유니코드 정규화(Unicode normalization)가 작동하지 않고, `string index`와 `len()`에서 문제가 발생합니다. `OldHangeul`은 텍스트를 조합형으로 전환하여 이러한 문제를 해결했습니다. 더불어 자음과 모음으로 옛한글을 처리할 수 있는 기능이 있습니다. 




## 설치


```python
pip install OldHangeul
```



## 사용법

`OldHangeul`은 파이썬에서 작동합니다. 

---
### OldTexts

옛한글이 포함된 텍스트를 다루는 클래스입니다. 완성형이 포함된 텍스트를 조합형으로 전환하고, 인덱싱(Indexing)과 슬라이싱(Slicing), `len()`, `get_jamo()`를 지원합니다. 

```python
from OldHangeul import OldTexts
text=OldTexts('스님이 免帖 나 주시고') #완성형이 포함된 텍스트입니다
print(text)
```

OldTexts 사용 예시입니다. 
```python
스스ᇰ님이 免帖 ᄒᆞ나ᄒᆞᆯ 주시고
```

OldTexts는 문자열의 길이를 손쉽게 계산할 수 있으며, 인덱싱(indexing)과 슬라이싱(slicing) 기능도 제공합니다.

```python
len(text)
#15

text[1]
#스ᇰ
```

---
### text_to_jamo

텍스트를 자음과 모음으로 분리합니다. 낱자는 space로 구분되어 있으며, 문서 내의 공백은 _로 나타냅니다. 

compatibility: 초성과 종성을 동일한 유니코드로 통일하여 처리

spacing: 문서 내 공백 표현 

   


```python
from OldHangeul import text_to_jamo
text=text_to_jamo('스스ᇰ님이 免帖 ᄒᆞ나ᄒᆞᆯ 주시고', compatibility=False, spacing=True)
print(text)
```
ᄉ ᅳ ᄉ ᅳ ᇰ ᄂ ᅵ ᆷ ᄋ ᅵ _ 免 帖 _ ᄒ ᆞ ᄂ ᅡ ᄒ ᆞ ᆯ _ ᄌ ᅮ ᄉ ᅵ ᄀ ᅩ


```python

from OldHangeul import text_to_jamo
text=text_to_jamo('스스ᇰ님이 免帖 ᄒᆞ나ᄒᆞᆯ 주시고', compatibility=True, spacing=True)
print(text)
```
ㅅ ㅡ ㅅ ㅡ ㆁ ㄴ ㅣ ㅁ ㅇ ㅣ _ 免 帖 _ ㅎ ㆍ ㄴ ㅏ ㅎ ㆍ ㄹ _ ㅈ ㅜ ㅅ ㅣ ㄱ ㅗ



---
### hNFD

[유니코드 정규화](https://ko.wikipedia.org/wiki/%EC%9C%A0%EB%8B%88%EC%BD%94%EB%93%9C_%EB%93%B1%EA%B0%80%EC%84%B1) 중 NFD의 기능입니다. 옛한글이 포함된 텍스트에도 작동하며, 소리마디(한양 PUA)를 첫가끝 코드로 변환합니다. 


```python
>>>from OldHangeul import hNFD
>>> hNFD('스님이 免帖 나 주시고')
```
스스ᇰ님이 免帖 ᄒᆞ나ᄒᆞᆯ 주시고


---
### hNFC

[유니코드 정규화](https://ko.wikipedia.org/wiki/%EC%9C%A0%EB%8B%88%EC%BD%94%EB%93%9C_%EB%93%B1%EA%B0%80%EC%84%B1) 중 NFC의 기능입니다. 옛한글이 포함된 텍스트에도 작동하며, 첫가끝 코드를 소리마디(한양 PUA)로 변환합니다. 변환이 안 된 텍스트는 `activation failed`로 안내됩니다. 


```python
>>>from OldHangeul import hNFC
>>> hNFC('스스ᇰ님이 免帖 ᄒᆞ나ᄒᆞᆯ 주시고')
```
스님이 免帖 나 주시고

---
### old_hNFD

[유니코드 정규화](https://ko.wikipedia.org/wiki/%EC%9C%A0%EB%8B%88%EC%BD%94%EB%93%9C_%EB%93%B1%EA%B0%80%EC%84%B1) 중 NFD의 기능입니다. 옛한글이 포함된 텍스트에도 작동하며, 전체 텍스트 중 옛한글이 포함된 낱자만 첫가끝(조합형)으로 변환합니다. 


```python
>>>from OldHangeul import old_hNFD
>>> old_hNFD('스스ᇰ님이 免帖 ᄒᆞ나ᄒᆞᆯ 주시고')
```
스스ᇰ님이 免帖 ᄒᆞ나ᄒᆞᆯ 주시고

