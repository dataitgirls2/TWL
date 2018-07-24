# 180723

## 오전수업 배로님

### 지난수업 회고

pip선호 > conda?

#### 우리가 사용하는 라이브러리(패키지)들

##### pandas?

엑셀보다 더 많은 데이터를 다룰 수 있고, 파이썬으로 코딩을 하여 조금 더 많은 것을 다루어 볼 수 있는 툴.

##### Matplotlib

plotnine, seaborn 등의 시각화 툴

##### numpy

(속도가 빠른) 수치 계산용 라이브러리

#### 머신러닝

scikit-learn 튜토리얼 참고하기

##### dimensionality reduction

차원을 축소시켜 압축해 보는 것과 같음.

##### classification

(eg) 개와 고양이 이미지, 사진 속 인물, gmail에서 메일 자동분류

##### regression

수요예측

##### clustering

군집화(비슷한 애들끼리 묶어 주는 것), classification과 같이 쓰일 수 있음.

#### soynlp

- stopwords : 워드클라우드를 조금 더 의미있게 그려보기 위해 토큰화한다음 빼내야 함. 의미없는 조사 등.
- meaningful_words

### soynlp 토큰화, 불용어 제거 실습

`import re` : 정규 표현식. 데이터 전처리 할 때 필수. 정규표현식 배우는 사이트 有.

`str.match(p) ` : string에 담겨져 있는 단어와 관련한 함수. "정규표현식과 매치되는 단어들을 가져오겠다."

`re.` : 붙은것들은 정규표현식에 있는 기능들.

`df['title'].str?` : 판다스 문서에서도 도움말 볼 수 있음.

##### 토큰화

어절 단위 띄어쓰기 기준으로 토큰화 시켜 줌.

##### 텍스트 데이터 전처리

의미없는 개행문자나 000원 등의 문자를 공백으로 바꾸어 주는 이유는 안그럼 토큰(띄어쓰기 단위)들이 붙어벌임~

- [ ] 국민청원 soynlp 저번 시간거 복습
- [ ] bull 용어 제거하고 실행해보기

#### Machine learning - Scikit Learn

Classification, Regression, Clustering, Feature Selection/Extraction 등에 사용.

##### Supervised Machine Learning - 지도학습

분류와 회귀는 주로 지도학습.

특성에 따른 모델을 만들어 준 후, test data를 가지고 예측.

측정 기법들을 가지고 평가함.

Generalization(일반화)

X (대문자) : 행렬(데이터프레임)

y (소문자) : 벡터(하나의 레이블 된 데이터)

`y_pred = clf.predict(X_test)` :집값이 없는 데이터에 예측한 데이터를 넣어줌.

`clf.score(X_test, y_test)` : 스코어를 내고 평가함.

- 전처리된 데이터가 있다면 코드 네 줄만으로로 예측된 데이터가 나옴.

배송데이터 등을 가지고 시간이 걸렸던 데이터를 알려주면, 다음 시간을 비유해서 예측해 준다.

- label data : 내가 예측한 데이터와 실제 데이터의 차이를 구하는 것. 표준편차가 얼마나 작아지느냐에 초점.

###### classification

(몸무게, 키)를 개/고양이(label)로 분류 (지도학습)

(몸무게, 키)를 분류했더니 두 개로 분류 (비지도학습)

##### Unsupervised Machine Learning - 비지도학습

training data 를 넣고 모델을 만듬.

test data를 넣고 view를 만들어줌

Label이 없는 것이 지도학습과의 차이.

차원 축소 : 계산해서 압축해준다(?) 3차원을 2차원으로 줄여주는 것. 예를들어 내부의 계산

clustering : 비슷한 것들을 묶어준다(?)

#### Bag of Word Representations

- Tfidf : 검색 엔진에서 많이 사용하는 알고리즘. 단어 별 가중치를 다르게 둠.

#### Overfitting and Underfitting

- Underfitting : 머신러닝에서 데이터를 적게 넣어 제대로 학습되지 않은 형태
- Overfitting : 아웃라이어들까지도 러닝되어 다른 측정값들까지 영향을 받거나, missing 데이터가 많은 경우.
- overfitting과 underfitting 그 사이 어딘가

#### Decision Trees

- 부동산 데이터에서 (depth 1) 강남/강북을 yes/no 나눔. (depth 2) 몇 년이상 된 아파트인지 아닌지 yes/no , ...
- 시각화 하기 좋음.
- 생각보다 정확도가 떨어짐
- 단점을 보완하기 위해 Random Forests 개발됨.

#### Random Forests

- depth를 너무 깊게 내려가도 overfitting되어 정확도가 떨어지고
- depth를 너무 얕게 내려가도 underfitting되어 정확도가 떨어짐.



### 오후수업

- TF-IDF

  얼마나 많이 등장하는가가 중요함. 특정 문서에서는 특정 단어가 등장하는데 그것이 중요하다는 것을 의미함.

#### Word2Vec

- 추천 시스템에도 많이 쓰임.

  특정 배우나 함께 등장했던 배우의 영화를 추천해 줌.

  following한 사람과 follower들을 추천해서 추출 가능.

##### 텍스트 데이터를 시각화 할 수 있는 몇 가지 방법

- wordcloud

#### 사이킷런

캐릭터 단위의 벡터화

속도느리고 시간오래걸림, 영어같은 경우엔 할만 함.