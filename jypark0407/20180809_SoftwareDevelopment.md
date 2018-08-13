## Test-Driven Software Development

* What's Good Code?

- * **Clean Code That Works**
  * Minimize Repetition
- Python Conventions
  - 2 lines between importing packages/libraries/modules and the actual code
- Creating test documentation
  - Minimize logic (ex) list comprehension) for readability 

    

- Run program in pipevn 

```python
pipenv run pytest tests.py
```



## Analysis of Shop Data 상권 분석

* Pandas exercise : 

https://medium.com/dunder-data/selecting-subsets-of-data-in-pandas-6fcd0170be9c



* 분석 단계

  * 목표 정하기

* 1. - 우리나라 전체의 스타벅스와 이디야를 지도로 시각화해보자.

  * 데이터 가져오고 살펴보기
    * Csv 데이터 로드. 
      * encoding issue - 한글 encoding : utf-8 or cp949
      * shape, head, tail, describe 이용해서 데이터 살펴보기 (data exploration)
  * 데이터 정제하기
    * loc이용해서 스타벅스, 이디야가 들어있는 값들만 추출하기
  * 지도 데이터로 표현하기
    * import folium
    * Parameter 설정해주기