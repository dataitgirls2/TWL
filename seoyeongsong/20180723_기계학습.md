20180723



### conda vs pip

- 패키지 관리 도구
- conda 는 가상환경을 제공합니다. pip를 사용해 독립된 공간에서 패키지를 설치



### Pandas

- Wikipedia : In computer programming, **pandas** is a software library written for the Python programming language for data manipulation and analysis. In particular, it offers data structures and operations for manipulating numerical tables and time series. 
- The name is derived from the term "panel data", an [econometrics](https://en.wikipedia.org/wiki/Econometrics) term for data sets that include observations over multiple time periods for the same individuals .



### Numpy

- Wikipedia : Numpy is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of [high-level](https://en.wikipedia.org/wiki/High-level_programming_language) [mathematical](https://en.wikipedia.org/wiki/Mathematics) functions to operate on these arrays. 

  

### Scikit-learn

- Wikipedia : is a [free software](https://en.wikipedia.org/wiki/Free_software) [machine learning](https://en.wikipedia.org/wiki/Machine_learning)[library](https://en.wikipedia.org/wiki/Library_(computing)) for the [Python](https://en.wikipedia.org/wiki/Python_(programming_language))programming language. It features various [classification](https://en.wikipedia.org/wiki/Statistical_classification), [regression](https://en.wikipedia.org/wiki/Regression_analysis)and [clustering](https://en.wikipedia.org/wiki/Cluster_analysis) algorithms including [support vector machines](https://en.wikipedia.org/wiki/Support_vector_machine), [random forests](https://en.wikipedia.org/wiki/Random_forests), [gradient boosting](https://en.wikipedia.org/wiki/Gradient_boosting), [*k*-means](https://en.wikipedia.org/wiki/K-means_clustering) and [DBSCAN](https://en.wikipedia.org/wiki/DBSCAN), and is designed to interoperate with the Python numerical and scientific libraries [NumPy](https://en.wikipedia.org/wiki/NumPy)and [SciPy](https://en.wikipedia.org/wiki/SciPy). 



Classification 

ex. mail filtering service



Regression

ex. 수요예측



Clustering : 유사한 자료끼리 군집화

ex. mailing



Dimensionality reduction : 차원의 저주에서 알 수 있듯이, 고차원의 데이터는 의미를 제대로 표현하기 어렵기 때문에 데이터의 의미를 제대로 표현하는 특징을 추려내는 것을 의미한다.





### 복습

remove_stopwords(text) : stopwords란 조사와 같이 반복되는 불용어로 이를 제거한다. 



**token**

: Meaningful elements in a text such as words or phrases or symbols.

데이터의 전처리과정을 살펴보면,

1. Load text
2. Tokenize text (ex: stemming, morph analyzing)
3. Tag tokens (ex: POS, NER)
4. Token(Feature) selection and/or filter/rank tokens (ex: stopword removal, TF-IDF)
5. ...and so on (ex: calculate word/document similarities, cluster documents)



##### 토큰화 : 문자열에서 단어로 분리시키는 단계

##### 불용어 제거 : 전치사, 관사 등 너무 많이 등장하는 단어, 문장이나 문서의 특징을 표현하는데 불필요한 단어를 삭제하는 단계

##### 어간추출 : 단어의 기본 형태를 추출하는 단계

##### 문서표현 : 주어진 문서나 문장을 하나의 벡터로 표현하는 단계, 단어를 모두 indexing 하고 단어의 빈도수를 사용하여 문서를 표현





## 기계학습

- **Machine learning** is a subset of [artificial intelligence](https://en.wikipedia.org/wiki/Artificial_intelligence) in the field of [computer science](https://en.wikipedia.org/wiki/Computer_science) that often uses statistical techniques to give [computers](https://en.wikipedia.org/wiki/Computer) the ability to "learn" with [data](https://en.wikipedia.org/wiki/Data), without being explicitly programmed. 



Unsupervised ML (비지도학습)  : label이 없음

[1] **Supervised learning** : the [machine learning](https://en.wikipedia.org/wiki/Machine_learning) task of learning a function that maps an input to an output based on example input-output pairs. It infers a function from *labeled training data* consisting of a set of *training examples*.  A supervised learning algorithm analyzes the training data and produces an inferred function, which can be used for mapping new examples. 

[2] **Unsupervised machine learning** : the [machine learning](https://en.wikipedia.org/wiki/Machine_learning) task of inferring a function that describes the structure of "unlabeled" data (i.e. data that has not been classified or categorized). Since the examples given to the learning algorithm are unlabeled, there is no straightforward way to evaluate the accuracy of the structure that is produced by the algorithm—one feature that distinguishes unsupervised learning from supervised learning and reinforcement learning. 



#### label

Feature (몸무게, 길이) - label(고양이, 개)에 따라 분류

label을 초기에 지정해준다면 지도학습

label이 없다면 비지도학습 이라고 할 수 있다.



#### Bag of Word

Tfid - 단어에 가중치를 두어 자주 등장하지만 필요없는 단어를 따로 분류

순서를 무시하기 때문에 의미의 보존이 힘들다.

n-gram을 사용해 두 단어씩 묶어주면 의미의 보존에 용이하다.





over-fitting(결측치가 많아 영향을 많이 받거나, outlier까지 분석하는 경우) / under-fitting(모수가 적어 학습이 제대로 되지 않음)

over와 under 간의 균형을 이루는 지점을 sweet spot이라고 한다. 이것을 찾는 것이 머신러닝의 목표이다.



각 단어가 column이 되고 만약 존재하면 matrix에서 1을 표시하게 하여 vector화 할 수 있다. 

