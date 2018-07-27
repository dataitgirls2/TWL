# 국민청원 투표 결과 예측하기

국민청원 투표 수가 평균을 넘을 것인지를 예측해본다. 

#### 1.  전처리

1. `votes_pos_neg` 칼럼에 투표 수가 평균을 넘으면 1, 넘지 않으면 0을 할당
2. 개행문자, 특수문자, 불용어 제거 (`df['content_processing2']`)
3. 아웃라이어 제거



#### 2. 학습 세트와 테스트 세트 만들기

- DataFrame을 7:3으로 나누어서 담기



#### 3. 단어 벡터화 하기

`train_feature_tfidf`와 `test_feature_tfidf`에 벡터화 된 단어 담아두기



#### 4. 랜덤 포레스트로 학습시키기

1. 랜덤 포레스트 분류기 만들기

```python
from sklearn.ensemble import RandomForestClassifier

forest = RandomForestClassifier(
    n_estimators = 100, n_jobs = -1, random_state=2018)
```



2. Training

- 학습할 데이터 : 전처리되고 벡터화된 국민청원의 내용(`df['content_processing2']`을 벡터화한 `train_feature_tfidf`)
- 분류할 라벨 : 평균보다 높은 투표수(`df['votes_pos_neg'`의 값-1/0으로 판별)

```python
forest = forest.fit(train_feature_tfidf, y_label)
```



3. Predict

- label(평균보다 높은 투표수)을 기준으로 예측하기

```python
y_pred = forest.predict(test_feature_tfidf)
```



4. Evaluate

- 