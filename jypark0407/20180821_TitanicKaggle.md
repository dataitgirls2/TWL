## 결측치 처리 방법

* 결측치는 왜 생길까?

* 결측치 처리 방법 (수동)

  * 제거

    * ```python
      df.dropna()
      df.dropna(how='all')
      df.dropna(axis=1, how='all')
      df.dropna(thresh=x) #thresh : threshold
      ```

  * 대체 (Imputation)

    * 통계적 방법 : 평균, 중앙값, 최빈값, 확률분포

      * 평균 : 단점 - 아웃라이어의 영향을 크게 받을 수 있음.

        --> 그런 경우, 중앙값을 써줌

      ```python
      dataset['Age'].fillna(dataset['Age'].mean(), inplace=True)
      ```



* 결측치 처리 방법 (자동)

  머신 러닝을 이용해서 결측치 예측하기

  * Scit-Learn의 Imputer

    

**범주형 데이터 <--> 수치형 데이터 변환**

One-Hot(Vector|Encoding) --> binning(Bucketing)

* Categorical Data 범주형 데이터 --> Numerical Data 수치형 데이터
  * 머신러닝이나 딥러닝 알고리즘은 수치화된 데이터만 이해
  * 하나의 데이터만 1로 변경해주고 나머지는 0으로 
  * 단점 : 벡터 사이즈가 커져서 분포가 넓어짐 (sparse)

```python
from sklearn.preprocessing import LableEncoder
# 자동으로 범주형 데이터를 수치형 데이터로 변환
```



* 수치형 데이터 --> 범주형 데이터

  * 나누는 기준을 임의로 정함 (interval)

  ```python
  ggplot(df)
  +aes(x='age')
  +geom_histogram(binwidth=1)
  # binwidth로 bin의 크기를 정함
  ```




## 타이타닉 캐글 score 올리기

https://ahmedbesbes.com/how-to-score-08134-in-titanic-kaggle-challenge.html

**Feature Selection **

* 어떤 Feature가 중요한지 보고, Overfitting방지를 위해서 몇 개만 골라줄 수 있다. 
* Graphviz를 이용해서 Tree를 시각화하여 각 Feature의 특징들을 분석한다.
  * Gini Impurity (지니 불순도 ) : 집합에 이질적인 것이 얼마나 섞였는지를 측정하는 지표. CART알고리즘에서 사용.
  * CART Algorithm : Classification and Regression Tree Algorithm



결정 트리 (Decision Tree)에 대한 참고자료: https://tensorflow.blog/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%A8%B8%EC%8B%A0%EB%9F%AC%EB%8B%9D/2-3-5-%EA%B2%B0%EC%A0%95-%ED%8A%B8%EB%A6%AC/

참고 : Local에서 나오는 점수와 실제 Kaggle에서 매겨지는 점수에는 차이가 있다.