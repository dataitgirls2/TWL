# 판다스 기초 2

### 판다스와 NumPy의 개념

#### Pandas

- 파이썬 라이브러리

#### NumPy

- 수치계산할때 쓰임
- 행렬계산에 최적화되어있다.
- 파이썬으로 numpy를 쓸 수 있지만 내부는 C로 되어있어서 빠르다.
- 대규모 다차원배열을 처리하는데 쓰인다. 이미지 프로세싱, 블록체인, 머신러닝, 딥러닝 등

### 10minutes to Pandas

데이터타입이 어떤 것인지에 따라서 요약된 값을 다르게 보여주기 때문에 데이터타입 지정이 중요하다.

- `df.describe()`에 대해 궁금할때 `df.describe?` 하게되면 도움말이 나온다.
- `sort_index()`의 arguments
  - `axis=`  `0` : 행 ,  `1` : 열
  - `ascending=` `True` : 오름차순 (true 가 기본값) ,  `False` : 내림차순
- 스칼라값 = 각각의 값을 뜻함



## 국민청원 판다스로 분석하기

- seaborn : matplotlib을 더 쉽게 사용하도록 만든것  <https://seaborn.pydata.org/>

- plotnine으로 국민청원을 분석할 예정

  **과제 : plotnine 설치하기**, 워드클라우드도 설치하기