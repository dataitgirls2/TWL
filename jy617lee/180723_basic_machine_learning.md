# 기계학습 기초

## Supervised Machine Learning (지도학습)

1. 트레이닝 데이터로 모델을 만들고 (training)

``` 
​```python
clf = RandomForestClassifier() 
clf.fit(X_train, y_train) 
```

1. 테스트 데이터를 모델을 이용해 예측하고 

``` 
​```python
y_pred = clf.predict(X_test)
```

1. 테스트 레이블을 통해서 평가를 할 수 있는 과정 (generalization)

```
​```python
clf.score(X_test, y_test)
```

--> 레이블을(데이터를 구분하는 기분) 사람이 지정하여 학습시켜 학습/예측/평가하는 방법

## Unsupervised Machine Learning (비지도학습)

컴퓨터에게 feature를 주면 나름의 방법으로 분류/예측/평가하는 방법



## 참고자료

http://research.sualab.com/machine-learning/2017/09/04/what-is-machine-learning.html

https://datascienceschool.net/view-notebook/3e7aadbf88ed4f0d87a76f9ddc925d69/



# 단어를 벡터화 하기

- 컴퓨터에게 단어를 알려주기 위해서는 벡터화 해야 한다. 

  - 전처리

  1. 정규화  : 입니닼ㅋㅋ -> 입니다 ㅋㅋ, 샤릉해 -> 사랑해
  2. 토큰화 : 한국어 예시입니다 ㅋㅋ -> 한국어, 예시, 입니다
  3. 어근화 : 입니다 --> 이다
  4. 어구 추출 : 명사 추출 등

  - 정규화 --> 토큰화 --> 불용어 처리 --> 어구추출의 과정을 거치는 실습을 진행함

## 사이킷런을 이용한 벡터화

```python
from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer(analyzer = 'word', # 캐릭터 단위로 벡터화 할 수도 있습니다.
                             tokenizer = None, # 토크나이저를 따로 지정해 줄 수도 있습니다.
                             preprocessor = None, # 전처리 도구
                             stop_words = None, # 불용어 nltk등의 도구를 사용할 수도 있습니다.
                             min_df = 2, # 토큰이 나타날 최소 문서 개수로 오타나 자주 나오지 않는 특수한 전문용어 제거에 좋다. 
                             ngram_range=(1, 3), # BOW의 단위를 1~3개로 지정합니다.
                             max_features = 1000 # 만들 피처의 수, 단어의 수가 된다.
                            )
feature_vector = vectorizer.fit_transform(air['content_preprocessing'])
feature_vector.shape
```



## word2vec을 이용한 벡터화

```python

# 초기화 및 모델 학습
from gensim.models import word2vec

# 모델 학습
model = word2vec.Word2Vec(tokens, min_count=1)

# 모델 이름을 지정하고 저장한다.
model_name = '1minwords'
model.save(model_name)
vocab = model.wv.vocab

# 가장 적게 등장하는 단어
min(vocab, key=vocab.get)

# 유사도 보기
model.wv.most_similar('주식')

# 가장 유사한 단어를 추출
model.wv.most_similar('공매도')
```



# TF-IDF

#### 정의 

- TF (Term Frequency) : 문서 내의 특정 단어의 등장 빈도수
- DF (Document frequency) : 전체 문서 내에서 특정 문서에 나타나는 단어의 등장 빈도수 (해당 단어가 나타난 문서 수 / 전체 문서 수)
- IDF (Inverse Document Frequency) : DF의 역수
- TF-IDF : TF * IDF로 높을 수록 해당 단어가 중요하게 이 문서에서 자주 나왔다는 의미를 가짐

``` python
from sklearn.feature_extraction.text import TfidfTransformer

transformer = TfidfTransformer(smooth_idf=False)
feature_tfidf = transformer.fit_transform(feature_vector)
```



#### 