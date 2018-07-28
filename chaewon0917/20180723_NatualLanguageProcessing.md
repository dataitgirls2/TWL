#### 01. 관련 개념 정리

**(1) 싸이킷 런 (Scikit-learn)**

- 파이썬에 있는 대표적인 Machine Learning Library. 
- data mining, data analysis를 위한 간결하고 효과적인 툴.
- Numpy, scipy, matplotlib으로 쓰여졌다.
-  오픈 소스이자 상업적으로 사용 가능하다. (BSD license)

**(2) 차원 축소 (dimensionally reduction)**

- 압축해서 본다.
- wordcloud로 단어의 유사도를 체크하고, 유사도에 기초하여 군집화한다. 
- 3차원의 경우 2차원으로 줄인다. 

**(3) 회귀 (regression)**

- 수요 분석할 때 많이 쓰인다.

**(4) 군집화 (clustering)**

- 비슷한 아이들끼리 묶어준다 

**(5) 분류 (classification)**

- 속성에 따라 분류해 준다.   

  

#### 02. 자연어 처리 실습

**(1) 정규표현식을 사용해서 지난 시간 soynlp 실습 결과 wordcloud 개선하기**

- 불용어 제거하기 

  - preprocessing (전처리)

    ```python
    def preprocessing(text):
        text = re.sub('- ', ' ', text)
        text = re.sub('같습니다', ' ', text)
        text = re.sub('좋았습니다', '좋았어요', text)
        text = re.sub('지영님의', '지영님', text)
        return text
    ```

  - remove_stopwords (불용어 제거)

    ```python
    def remove_stopwords(text):
        stops = ['수', '있는', '있습니다', '그', '년도', '에', '합니다', '하는', '및', '제', '할', '하고', '더', '대한', '한', '그리고', '월', '저는', '없는', '것입니다', '등', '일', '많은', '이런', '것은', '왜', '같은', '없습니다', '위해', '한다']
        # Stopwords 불용어 제거
        meaningful_words = [word for word in text if not word in stops]
        return ' '.join(meaningful_words)
    
    %time tokens_remove_stopwords = 토큰으로만든단어들.apply(remove_stopwords)
    ```

**(2) 정규표현식 불러오기**

-  `import re` 
- 정규표현식은 모든 언어에 다 있다. 
- 데이터 전처리 preprocessing에 필수 요소이다. 



#### 03. 기계학습 기초

- **Andread Muller's Machine Learning with Scikit-Learn** 

  Classification, Regression, Clustering, Semi-Supervised Learning, Feature Selection, Feature Extraction, Manifold Learning, Dimensionality Reduction, Kernel Approximation, Hyperparameter Optimization, Evaluation Metrics, Out-of-core learning, ...

- **Supervised Machine Learning (지도 학습, 교사 학습, 교수 학습(?))** 

  - Traning data를 넣어서 어떤 모델을 만들고, Test Data에 있는 Training Labels를 예측하는 것이 Supervised Machine Learning이다. Coursera에서 강의를 들어볼 수 있다. 보스턴의 집 값을 예측하는 머신 러닝 알고리즘. 통계 시간에 측정 기법들을 배우게 될 것이다. 

  - Traning (훈련)과 Generalization (일반화). 특정 데이터에만 맞는 데이터가 아니라, 어떤 데이터도 예측 가능하도록 결측치를 제거하거나, 하는 등의 과정을 Traning. 이후 테스트하고 평가하는 과정을 Generalization이라고 한다. 

  - `clf.fit(X_train, y_train)` : 대문자와 소문자의 차이는 행렬과 벡터의 차이이다. 

  - `clf.score(X_test, y_test)` : 예측 결과가 얼마나 정확한지 평가(Evaluation) 하는 단계. 

    ```python
    clf = RandomForestClassifier()
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    clf.score(X_test, y_texst )
    ```

    단 네 줄로 기계학습을 실행할 수 있다! 

  - 분류와 회귀의 경우 거의 지도학습에 해당한다. 비지도 학습으로도 수행할 수 있으나, labels를 가지고 분류하는 경우 supervised. 회귀의 경우 집 값 예측이나 배송 물건 예측, 배송 시간 예측 등은 기존의 데이터를 기계에게 알려주어 그것을 바탕으로 예측하도록 한다. 

- **Unsupervised Machine Learning (비지도 학습, 비교사 학습)**

  - Training Data를 넣고, 바로 Test 한다. Unsupervised 같은 경우는, labels가 없다. 

    ```python
    pca = PCA()
    pca.fit(X_train)
    X_new = pca.transform(X_test)
    ```

- **Labels, Features ?**

  - e.g.) Labels에 고양이와 개. 몸무게, 키 등의 기준(속성)들이 Features. 지도 학습에서는 Labels를 주고 이것을 바탕으로 Classify 한다. 비지도 학습에서는 Labels가 없음. 분류가 아니라 회귀의 경우, Labels에 집 값이 들어간다.

- **TfidVertorizer**

  - 검색 엔진에서 자주 사용하는 알고리즘. 단어에 가중치를 준다. Bag of Word의 단점을 보완하는 도구로 사용되고 있다. 

- **Overfitting / Underfitting** 

  - Overfitting : 정확도가 높을 수록.
  - Underfittinf : 정확도가 낮을 수록.
    - Training과 Heneralization의 격차가 적은 구간이 정확도의 측면에서 최적화된 지점(Sweet spot)이다. Underfitting의 경우 모수가 적은 경우. 데이터를 적게 부여하고 학습을 시킨 경우, 제대로 학습되어 있지 않다고 하여 underfitting 이라고 한다. 반대로 너무 학습이 잘 되어 Outlier나 결측치에 대해서도 학습을 하는 경우를 overfitting이라고 한다. 
      - e.g.) 어떤 학습 결과가 육아 관련 데이터를 잘 예측하지만 반려동물 데이터에 대해서는 잘 예측하지 못한다면, 이 학습 결과는 육아 관련 데이터에 overfitting 되었다고 한다.

- **Decision Trees** 

  - True / False 로 구분되는 Data. 어떤 기준을 바탕으로 점점 True/False로 Depth를 더해가며 그래프를 그린다. 
  - 이것이 정확도가 떨어져서, 이 부분을 보완한 것이 RandomForests이다. 이러한 Decision Trees 를 Random하게 매우 많이 그린다. depth를 너무 깊게 내려가도 overfitting이 되어 정확도가 떨어지고, depth가 너무 낮아도 underfitting 되어 정확도가 떨어진다. 데이터에 맞게 적절한 지점을 찾는 것이 중요하다.  

  

#### 04. 텍스트 데이터 정제 및 전처리

- 기계가 텍스트를 이해할 수 있도록 텍스트를 정제하여, 신호와 소음을 구분하게 한다. 

- 아웃라이어데이터로 인한 overfitting을 방지하는 기능을 한다.

  - HTML Tag, 특수문자, 이모티콘
  - 정규표현식
  - 불용어 (stopword)
    - 일반적으로 코퍼스에서 자주 나타나는 단어로, 학습이나 예측 프로세스에 실제로 기여하지 않는 단어들. 
    - 영어는 불용어 Dataset 잘 되어 있지만 한국어에 쓸만한 건 없다… 
  - 어간추출 (stemming)
    - 단어를 축약형으로 바꿔준다. 의미가 통하도록 축약하여 어간을 추출한다. 
  - 음소표기법 (lemmatizing)
    - 품사 정보가 보존된 형태의 기본형으로 변환
    - 어간추출을 했을 때 의미가 부딪힐 위험이 있는 동음이의어 등의 단어들을 처리하는 방법 

- 정규화 normalization, 토큰화 tokenization, 어근화 stemming, 어구 추출 phrase extraction 등의 방법을 사용한다. 

  

#### 05. 텍스트 데이터 벡터화

- 머신러닝 알고리즘은, 0과 1밖에 모르는 기계에게 인간의 언어를 알려주기 위한 절차이다. 컴퓨터는 숫자만 인식할 수 있기 때문에 수치로 바꾸어 바이너리 코드로 처리해주어야 한다. 

- **One Hot Vector** 

  - 텍스트 데이터나 범주형 데이터를 수치형 데이터로 바꾸어 주어야 한다. 벡터에서 해당되는 하나의 데이터만 1로 변경해 주고, 나머지는 0으로 채워준다. 이 행렬을 Random Forests와 Decision Tree에 넣어준다. 

- **BOW (bag of words)**

  - 단어는 같지만 문장 구조나 순서가 달라 뜻이 완전히 달라지는 문장들을 완전히 동일하게 반환한다는 단점이 있다. 이를 보완하기 위해 n-gram을 사용하여 의미가 보존되도록 n개의 토큰을 사용한다. 
  - n-gram : uni-gram, bi-gram, tri-gram 등으로 구분. (묶어주는 토큰의 개수에 따라). bi-gram (1,2)나 tri-gram(2,3) 등을 사용하면 토큰 개수를 섞어서 사용할 수 있다. 

- **TF-IDF (Term frequency Inverse document frequency)**

  - TF (단어 빈도, term frequency)는 특정한 단어가 문서 내에서 얼마나 자주 등장하는지를 나타내는 값으로, 이 값이 높을 수록 문서에서 중요한 단어라고 생각할 수 있지만 단어 자체가 문서군 내에서 자주 사용되는 경우 이것은 그 단어가 흔하게 등장한다는 것을 의미한다. 이를 DF (문서 빈도, document frequency)라고 하며, 이 값의 역수를 IDF (역문서 빈도, inverse document frequency)라고 한다. 
    - 이를테면 전체 청원에서 '초등학교'라는 키워드는 자주 등장하지 않지만, 보육과 관련된 특정 청원에서는 이 단어가 자주 등장한다. 
    - TF-IDF는 TF와 IDF를 곱한 값이다. 

- **Word2Vec** 

  - 딥러닝 기반 알고리즘. 

  - 유사한 벡터를 근처에 배치하기 때문에, 추천 시스템에도 많이 쓰인다. 

  - CBOW (continuous bag-of-words), Skip-Gram

    - CBOW : 전체 텍스트로 하나의 단어를 예측하기 때문에, 작은 데이터셋일 수록 유리하다.
    - Skip-Gram : 타겟 단어들로부터 원본 단어를 역으로 예측하는 것으로, CBOW와는 반대로 컨텍스트-타겟 쌍을 새로운 발견으로 처리하고 큰 규모의 데이터셋일수록 유리하다.   

    

#### 06. 텍스트 데이터 시각화

- **(1) Word2Vec으로 벡터화하고, 일부 데이터를 차원축소 기법으로 줄여서 표현**
  - 비슷한 단어끼리 비슷한 위치에 분포
  - 조사와 불용어가 섞여 있어 데이터 정제 필요
- **(2) 작가별 품사 사용, 단어 개수, 소설에 자주 등장하는 단어**



#### 07. 자연어 처리로 할 수 있는 일

- 자동 요약, 맞춤법 수정, 스팸메일 검출, 분류, 자동답변, 고객센터, 챗봇, 기계번역, 추천, 감정분석 등 

- 자연어 처리에서 활용하기

  - Classification : 스팸메일 분류

  - Regression : 리뷰 평점 예측

  - Clustering : 비슷한 메일끼리 모으기

  - Dimensionality reduction : 차원 축소 기법으로 시각화 

    

    숙제 : for 문 응용으로 불용어 처리하기



