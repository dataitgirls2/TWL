## 20180723 TWL  

* **지난 시간 복습**

  불용어 제거하기

```
def preprocessing(text):
    text = re.sub('- ', ' ', text)
    text = re.sub('같습니다', ' ', text)  # 의미 없는 텍스트 제거
    text = re.sub('좋았습니다', '좋았어요', text)  # 같은 의미 텍스트 합치기
    return text
```

```
def remove_stopwords(text):
    stops = ['수', '있는', '있습니다', '그', '년도', '에', '합니다', '하는', '및', '제', '할', '하고', '더', '대한', '한', '그리고', '월', '저는', '없는', '것입니다', '등', '일', '많은', '이런', '것은', '왜', '같은', '없습니다', '위해', '한다']
    # Stopwords 불용어 제거
    meaningful_words = [word for word in text if not word in stops]
    return ' '.join(meaningful_words)

%time tokens_remove_stopwords = 토큰으로만든단어들.apply(remove_stopwords)

def preprocessing(text):
    # 개행문자 제거
    text = re.sub('\\\\n', ' ', text)
    # 특수문자 제거
    # 특수문자나 이모티콘 등은 때로는 의미를 갖기도 하지만 여기에서는 제거했습니다.
    # text = re.sub('[?.,;:|\)*~`’!^\-_+<>@\#$%&-=#}※]', '', text)
    # text = re.sub('[0-9]', '', text)
    # 한글, 영문, 숫자만 남기고 모두 제거하도록 합니다.
    # text = re.sub('[^가-힣ㄱ-ㅎㅏ-ㅣa-zA-Z0-9]', ' ', text)
    # 한글, 영문만 남기고 모두 제거하도록 합니다.
    text = re.sub('[^가-힣ㄱ-ㅎㅏ-ㅣa-zA-Z]', ' ', text)
    return text

```

**virtualenv는?**

*우리가 보는 파이썬으로 데이터 길들이기의 데이터를 클론받으면 파이썬의 버전이 달라 실행이 안된다. 이때 이 소스코드 실행을 위한 가상환경을 따로 만들어 주면 우리가 수업에 사용하는 파이썬 버전과 충돌이 일어나지 않는다.*

https://www.python.org/dev/peps/pep-0486/

ELK??

* Classification(분류)
  * gmail - 소셜, 광고 메일 분류 +스팸메일 분류

* Regression

  * 수요 예측

* Clustering

  * 비슷한 것들끼리 묶어주는 것

* dimensionality reduction(차원축소)



http://scikit-learn.org/stable/tutorial/machine_learning_map/index.html

->튜토리얼 있음! 독학하기 좋음



* 영어는 불용어 데이터셋이 있음

* 트위터에서 만든 한국어 처리기 https://github.com/twitter/twitter-korean-text


* 벡터화 - 텍스트 데이터를 수치로 바꿔주는 것

  (이미지/음성 데이터 또한 수치로 바꿔줘야 한다)



* **Word2Vec**

   * 영화 추천 시스템
   * 팔로우 추천 시스템



https://www.kaggle.com/c/spooky-author-identification/kernels

-> 작가별 단어 사용 캐글 (글을 작가별로 분류)



```
# 샘플로 보고 싶은 인덱스의 번호를 넣어주세요.
sample_index = 214636
```

-> 여기서 인덱스 번호는 article_id 가 아니고 맨 왼쪽의 번호!



```
# 벡터화 된 피처를 확인해 봄
# Bag of words 에 몇 개의 단어가 들어있는지 확인
dist = np.sum(feature_vector, axis=0)
    
for tag, count in zip(vocab, dist):
    print(count, tag)
    
pd.DataFrame(dist, columns=vocab).T  #.T 붙여주면 데이터프레임 가로 세로 바뀜
```



* 내적 이해하기!!
* 주피터 노트북으로 할 때는 soynlp등 설치 한번만 하면 됨!
* 주피터 노트북으로 실습 --> ipynb 파일로!!(수업자료 폴더에 있음)