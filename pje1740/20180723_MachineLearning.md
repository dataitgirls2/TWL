# 2018년 7월 23일

## pip and Conda

**pip**

pip 는 패키지 관리 도구입니다.모듈을 설치하거나 모듈간 디펜던시를 관리하거나 할 때 사용합니다. 예를 들면 특정버전의 패키지나 라이브러리를 설치하고 삭제하는 역할을 한다고 볼수 있습니다.

**conda** 

conda 라는 도구는 virtualenv 와 같이 가상 환경을 제공하는 도구 입니다.즉 conda 를 사용해서 별도의 가상 환경을 만들어 격리(독립공간)시키고 해당 공간에서 pip를 사용해서 패키지들을 설치합니다.



## 데이터 전처리

https://colab.research.google.com/drive/1h1zXedeYzPbcMb1_ORklbe8vZwI2tGwf#scrollTo=Av3neKddlvmy



지난 주에 Syonlp를 이용하여 만든 워드 클라우드를 불용어를 조금 더 정리해서 새롭게 찍어보는 과정을 실습해보았습니다. 



~~~
def preprocessing(text):
    # 개행문자 제거
    text = re.sub('\\\\n', ' ', text) #공백으로 대체해야 띄어쓰기가 된다 (아니면 뒷 단어랑 붙어버린다~)
    text = re.sub('000원', ' ', text)
    text = re.sub('스포츠', ' ', text)
    text = re.sub('[^가-힣ㄱ-ㅎㅏ-ㅣa-zA-Z]', ' ', text)
    return text
    
def remove_stopwords(text):
    stops = ['수', '있는', '있습니다', '그', '년도', '에', '합니다', '하는', '및', '제', '할', '하고', '더', '대한', '한', '그리고', '월', '저는', '없는', '것입니다', '등', '일', '많은', '이런', '것은', '왜', '같은', '없습니다', '위해', '한다', '월']
    # Stopwords 불용어 제거
    meaningful_words = [word for word in text if not word in stops]
    return ' '.join(meaningful_words)
~~~



~~~
tokens_remove_stopwords = tokens.apply(remove_stopwords)

tokens_remove_stopwords
~~~



위와 같이 불용어를 제거하고 토큰에 적용해준다. 



#### 관련용어



**불용어** Stopword

학습이나 예측 프로세스에 불필요한 용어



**어간추출 **Stemming

단어를 축약형으로 바꾸는 과정



**음소표기법** Lemmatization

품사정보가 보존된 형태의 기본형으로 변환하는 과정



## 기계학습

인공 지능의 한 분야로, 컴퓨터가 **학습**할 수 있도록 하는 알고리즘과 기술을 개발하는 분야 (위키백과)



![Related image](http://inspirauk.wpengine.com/wp-content/uploads/2018/02/Artificial-Intelligence-Machine-Learning-Deep-Learning.jpg) 

**기계학습의 목적**

Classification: 분류. 개와 고양이 구분이 대표적.

Regression: 회귀. 주로 수요예측에 이용된다.

Clustering: 군집화. 비슷한 것을 모으는 것.



등이 존재한다.



### 기계학습의 종류



#### Supervised Machine Learning(지도학습)

지도 학습은 미리 레이블을 지정해두고 컴퓨터에게 학습을 명령한다.

~~~
clf = RandomForestClassifier()
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
clf.score(X_test, y_test)
~~~



#### Unsupervised Machine Learning(비지도학습)

비지도학습은 지도학습과는 반대로 레이블을 지정하지 않는다. 

~~~
pca = PCA()
pca.fit(X_train)
X_new = pca.transform(X_test)
~~~



#### Feature & Label의 예시

| Feature 01 몸무게 | Feature 02 키 | Label  |
| :---------------: | :-----------: | :----: |
|        3kg        |     20cm      | 고양이 |
|        1kg        |     15cm      | 강아지 |



#### Bag of Word

단어를 토크나이즈 해서 bag에 담는다는 개념



• 가장 간단하지만 효과적이라 널리쓰이는 방법

• 장, 문단, 문장, 서식과 같은 입력 텍스트의 구조를 제외하고 각 단어가이 말뭉치에 얼마나 많이 나타나는지만 헤아림

• 구조와 상관없이 단어의 출현횟수만 세기 때문에 텍스트를 담는 가방(bag)으로 생각할 수 있음

• BOW는 단어의 순서가 완전히 무시 된다는 단점• 예를 들어 의미가 완전히 반대인 두 문장을 보자

~~~ 
it's bad, not good at all.

it's good, not bad at all.
~~~

• 위 두 문장은 의미가 전혀 반대지만 완전히 동일하게 반환

• 이를 보완하기 위해 n-gram을 사용하는 데 BOW는 하나의 토큰을 사용하지만 n-gram은 n개의 토큰을 사용



즉, 존재하는 무수히 많은 한글 단어를 하나하나 토큰화한다고 보면 됨. (엄청나게 방대한 표가 나오게 된다)

TF-IDF는 bag of word가 갖는 단점을 보완하여 특정 언어가 특정 구간에서 많이 등장한다면 중요성에 가중치를 준다.



#### Word2Vec(Word Embedding to Vector)

one hot encoding(예 [0000001000]) 혹은 Bag of Words에서vector size가 매우 크고 sparse 하므로 neural net 성능이 잘 나오지 않음.

•주위 단어가 비슷하면 해당 단어의 의미는 유사하다 라는 아이디어
•단어를 트레이닝 시킬 때 주변 단어를 label로 매치하여 최적화
•단어를 의미를 내포한 dense vector로 매칭 시키는 것

Word2Vec은 분산 된 텍스트 표현을 사용하여 개념 간 유사성을 봄.
예를 들어, 베이징과 중국이 서울과 한국이 (수도와 나라) 같은 방식으로 관련되어 있음을 이해.



**실습**

https://colab.research.google.com/drive/1QsfupG8gbg530DhVsVi-YsbPN3Zs9-Pj#scrollTo=2mHW2sbWbN-u