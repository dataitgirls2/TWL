%matplotlib inline : notebook을 실행한 브라우저에서 바로 그림을 볼 수 있게 해주는 역할
python에서 제공하는 rich output에 대한 표현 방식

<초보자를 위한 Kaggle 추천 Competition>
    * 분류 : https://www.kaggle.com/c/titanic
    * 회귀 : https://www.kaggle.com/c/bike-sharing-demand
    * NLP : https://www.kaggle.com/c/word2vec-nlp-tutorial
바이크와 word2vec은 이미 끝났지만 커널이 공유되고 데이터 공유 약관이 없으므로 끝난 경진대회 참가를 권장
    * 해당 경진대회에 대한 온라인 강좌 :
        - https://programmers.co.kr/learn/courses/21
        - https://www.inflearn.com/course/nlp-imdb-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%90%EC%97%B0%EC%96%B4-%EC%B2%98%EB%A6%AC/

scalar : 숫자 하나

변수 = get_df(데이터프레임)
변수.shape
변수.head()
변수.info()
변수.describe() -> unique : 속한 값, top : 최빈값, freq : 최빈값 빈도수
df_titanic['Class'].value_counts() : 각각의 value가 몇 개 있는지

#데이터 타입을 int로 변경하면 수치형 데이터. count, mean, std, min/max, 사분위수를 보여준다.
df_king['life'] = df_king['life'].astype(int)
df_king['period'] = df_king['period'].astype(int)
df_king.describe()

# 결측치를 보고 싶을 때 널값을 구해 본다.
df_king.isnull().sum()
df_king.sum()

# 가장 오래 집권한 왕순으로 정렬해 보고 상위 5개의 데이터만 본다.
df_king.sort_values(by='period', ascending=False).head(5)

# 평균, 표준 편차
df_king.mean()
df_king.std()
df_king.max()

df_king['life'].plot()
df_king['life'].hist()

#어떤 칼럼이 있는지 보여줌
df_titanic.columns

#도심&외곽 컨텐츠에 따라 describe하기
house.groupby('도심&외각').describe()

