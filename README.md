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
### OLD_TEXTS

옛한글이 포함된 텍스트를 다루는 클래스입니다. 완성형이 포함된 텍스트를 조합형으로 전환하고, 인덱싱(Indexing)과 슬라이싱(Slicing), `len()`, `get_jamo()`를 지원합니다. 

```python
from OldHangeul import OLD_TEXTS
a=OLD_TEXTS('스님이 免帖 나 주시고') #완성형이 포함된 텍스트입니다
print(a)
```

스스ᇰ님이 免帖 ᄒᆞ나ᄒᆞᆯ 주시고


```python
>>> len(a)
15
>>> a[1]
스ᇰ
```

---
### text_to_jamo

텍스트를 자음과 모음으로 분리합니다. 낱자는 space로 구분되어 있으며, 문서 내의 공백은 _로 나타냅니다. 

Compatibility: 초성과 종성을 동일한 유니코드로 통일하여 처리

spacing: 문서 내 공백 표현 

   


```python
>>> from OldHangeul import OLD_TEXTS
>>> text_to_jamo('스스ᇰ님이 免帖 ᄒᆞ나ᄒᆞᆯ 주시고', Compatibility=False, spacing=True)
```
ᄉ ᅳ ᄉ ᅳ ᇰ ᄂ ᅵ ᆷ ᄋ ᅵ _ 免 帖 _ ᄒ ᆞ ᄂ ᅡ ᄒ ᆞ ᆯ _ ᄌ ᅮ ᄉ ᅵ ᄀ ᅩ


```python
>>> text_to_jamo('스스ᇰ님이 免帖 ᄒᆞ나ᄒᆞᆯ 주시고', Compatibility=True, spacing=True)
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

