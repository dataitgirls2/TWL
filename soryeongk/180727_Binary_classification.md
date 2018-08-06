
# 국민청원 데이터로 이진 분류하기

* 예제로 응답여부를 0과 1로 예측합니다.
* 응답여부 외에도 청원의 카테고리를 예측하는 분류를 해볼 수도 있을것 같아요. 
* 이 예제를 참고하여 응답여부외에 청원내용으로 평균 이상의 투표를 받을 것인지 여부를 예측해 보면 좋겠습니다.


```python
import pandas as pd
import numpy as np
import re
print(pd.__version__)
print(np.__version__)
```

    0.23.0
    1.14.3
    

# 데이터 로드하기


```python
# 크롤링해 온 국민청원 데이터를 판다스를 통해 읽어옵니다.
petitions = pd.read_csv('https://s3.ap-northeast-2.amazonaws.com/data10902/petition/petition.csv',
                        parse_dates=['start', 'end'])
# 데이터의 크기가 어느정도인지 봅니다.
petitions.shape
```




    (219855, 8)




```python
petitions.describe()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>article_id</th>
      <th>answered</th>
      <th>votes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>219855.000000</td>
      <td>219855.000000</td>
      <td>219855.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>132868.594624</td>
      <td>0.000123</td>
      <td>149.437711</td>
    </tr>
    <tr>
      <th>std</th>
      <td>83296.535870</td>
      <td>0.011081</td>
      <td>4635.027514</td>
    </tr>
    <tr>
      <th>min</th>
      <td>21.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>57208.500000</td>
      <td>0.000000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>131803.000000</td>
      <td>0.000000</td>
      <td>3.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>204034.500000</td>
      <td>0.000000</td>
      <td>11.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>284841.000000</td>
      <td>1.000000</td>
      <td>714875.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 전체 데이터 중 투표가 1000건 이상인 데이터를 기준으로 가져옵니다. 아웃라이어 데이터 제거를 위해 10만건 이상 데이터도 제거합니다.
df = petitions.loc[(petitions['votes'] > 100) & (petitions['votes'] < 1000)]
# 500건 이상으로 바꾸어서 해보아도 좋음
# 개수가 많으면 학습을 잘 하는 것은 맞지만, outline데이터가 많으면 의미없을 수도.
df.shape
```




    (7963, 8)




```python
df.describe()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>article_id</th>
      <th>answered</th>
      <th>votes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>7963.000000</td>
      <td>7963.0</td>
      <td>7963.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>169588.050735</td>
      <td>0.0</td>
      <td>273.799950</td>
    </tr>
    <tr>
      <th>std</th>
      <td>72330.812603</td>
      <td>0.0</td>
      <td>195.966223</td>
    </tr>
    <tr>
      <th>min</th>
      <td>34.000000</td>
      <td>0.0</td>
      <td>101.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>121414.000000</td>
      <td>0.0</td>
      <td>137.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>184251.000000</td>
      <td>0.0</td>
      <td>196.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>221999.000000</td>
      <td>0.0</td>
      <td>333.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>284841.000000</td>
      <td>0.0</td>
      <td>998.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 1000건 이상 투표를 받은 데이터의 평군은 7483 입니다. 
df.loc[df['answered'] == 1].shape
```




    (0, 8)




```python
%matplotlib inline 
df['votes'].plot.hist()
```




    <matplotlib.axes._subplots.AxesSubplot at 0x29517ddea58>




![png](output_9_1.png)



```python
# 기본값을 0으로 세팅
df['votes_pos_neg'] = 0
```

    C:\Users\rlath\Anaconda3\lib\site-packages\ipykernel_launcher.py:2: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
      
    


```python
# 투표수가 평균을 넘으면 1로 다시 세팅
df['votes_pos_neg'] = (df['votes'] > 273) == 1
```

    C:\Users\rlath\Anaconda3\lib\site-packages\ipykernel_launcher.py:2: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
      
    


```python
# 타입을 boolean 에서 int로 변경해 줍니다.
df['votes_pos_neg'] = df['votes_pos_neg'].astype(int)
```

    C:\Users\rlath\Anaconda3\lib\site-packages\ipykernel_launcher.py:2: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
      
    


```python
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>article_id</th>
      <th>start</th>
      <th>end</th>
      <th>answered</th>
      <th>votes</th>
      <th>category</th>
      <th>title</th>
      <th>content</th>
      <th>votes_pos_neg</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>13</th>
      <td>34</td>
      <td>2017-08-19</td>
      <td>2017-09-18</td>
      <td>0</td>
      <td>679</td>
      <td>기타</td>
      <td>『국가유공자 등 예우 및 지원에 관한법률』상「6.25전몰군경 자녀수당」의 불합리한 ...</td>
      <td>(현황)\n우리들 아버지께서는 67여년전 북의 남침으로 조국이 위기에 처했을 때 젊...</td>
      <td>1</td>
    </tr>
    <tr>
      <th>16</th>
      <td>37</td>
      <td>2017-08-19</td>
      <td>2017-09-18</td>
      <td>0</td>
      <td>415</td>
      <td>기타</td>
      <td>황우석박사님 연구재개 허용 촉구합니다.</td>
      <td>국민의 70% 이상이 황우석박사님을 응원하고 지지하고 있습니다.\n*2007년 1월...</td>
      <td>1</td>
    </tr>
    <tr>
      <th>18</th>
      <td>40</td>
      <td>2017-08-19</td>
      <td>2017-09-18</td>
      <td>0</td>
      <td>218</td>
      <td>외교/통일/국방</td>
      <td>국가유공자등 예우및 지우너에 관한 법률 시행령 개정</td>
      <td>지금부터 67년전 1950년 6.25전쟁때 조국 대한민국이 위태로운 시점에 우리들 ...</td>
      <td>0</td>
    </tr>
    <tr>
      <th>19</th>
      <td>41</td>
      <td>2017-08-19</td>
      <td>2017-09-18</td>
      <td>0</td>
      <td>227</td>
      <td>외교/통일/국방</td>
      <td>국가유공자등 예우및 지우너에 관한 법률 시행령 개정</td>
      <td>지금부터 67년전 1950년 6.25전쟁때 조국 대한민국이 위태로운 시점에 우리들 ...</td>
      <td>0</td>
    </tr>
    <tr>
      <th>20</th>
      <td>42</td>
      <td>2017-08-19</td>
      <td>2017-09-18</td>
      <td>0</td>
      <td>173</td>
      <td>육아/교육</td>
      <td>기간제 교사의 정규직화를 반대합니다.</td>
      <td>대통령님, 안녕하세요. 저는 임용을 준비하고 수험생입니다. 처음 기간제 정규직화 된...</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>



# 전처리 하기 


```python
def preprocessing(text):
    # 개행문자 제거
    text = re.sub('\\\\n', ' ', text)
    # 특수문자 제거
    # 특수문자나 이모티콘 등은 때로는 의미를 갖기도 하지만 여기에서는 제거했습니다.
    # text = re.sub('[?.,;:|\)*~`’!^\-_+<>@\#$%&-=#}※]', '', text)
    # 한글, 영문, 숫자만 남기고 모두 제거하도록 합니다.
    # text = re.sub('[^가-힣ㄱ-ㅎㅏ-ㅣa-zA-Z0-9]', ' ', text)
    # 한글, 영문만 남기고 모두 제거하도록 합니다.
    text = re.sub('[^가-힣ㄱ-ㅎㅏ-ㅣa-zA-Z]', ' ', text)
    return text
```


```python
# 불용어 제거에 따라서 정확도가 달라질 수 있음
def remove_stopwords(text):
    tokens = text.split(' ')
    stops = ['수', '현', '있는', '있습니다', '그', '년도', '합니다', '하는', '및', '제', '할', '하고', '더', '대한', '한', '그리고', '월', '저는', '없는', '입니다', '등', '일', '많은', '이런', '것은', '왜','같은', '같습니다', '없습니다', '위해', '한다']
    meaningful_words = [w for w in tokens if not w in stops]
    return ' '.join(meaningful_words)
```


```python
# 샘플데이터에 적용
pre_sample_content = preprocessing(sample_content)
```


```python
pre_sample_content = remove_stopwords(pre_sample_content)
```


```python
%time df['content_preprocessing'] = df['content'].apply(preprocessing)
```

    Wall time: 908 ms
    

    C:\Users\rlath\Anaconda3\lib\site-packages\ipykernel_launcher.py:1: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
      """Entry point for launching an IPython kernel.
    


```python
%time df['content_preprocessing2'] = df['content_preprocessing'].apply(remove_stopwords)
```

    Wall time: 1.23 s
    

    C:\Users\rlath\Anaconda3\lib\site-packages\ipykernel_launcher.py:1: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
      """Entry point for launching an IPython kernel.
    

# 학습세트와 테스트세트 만들기
* 학습세트와 테스트세트를 7:3의 비율로 나눠 줍니다.


```python
df = df.reindex()  # 인덱스를 새로 생성
```


```python
df.shape
```




    (2922, 11)




```python
split_count = int(df.shape[0] * 0.7)
split_count
```




    2045




```python
df_train = df[:split_count]
df_train.shape
# 70%의 데이터를 학습데이터로 담아둠
# 70%의 데이터(학습데이터)로 30%의 데이터(실헙데이터)를 예측
```




    (2045, 11)




```python
df_train.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>article_id</th>
      <th>start</th>
      <th>end</th>
      <th>answered</th>
      <th>votes</th>
      <th>category</th>
      <th>title</th>
      <th>content</th>
      <th>votes_pos_neg</th>
      <th>content_preprocessing</th>
      <th>content_preprocessing2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>7</th>
      <td>28</td>
      <td>2017-08-19</td>
      <td>2017-08-26</td>
      <td>0</td>
      <td>2137</td>
      <td>경제민주화</td>
      <td>소액주주를 보호해주십시오</td>
      <td>**  존경하옵는 문재인대통령님께\n저는 중국원양자원이라는 KOSPI상장사의 소액 ...</td>
      <td>0</td>
      <td>존경하옵는 문재인대통령님께 저는 중국원양자원이라는 KOSPI상장사의 소액 주...</td>
      <td>존경하옵는 문재인대통령님께 중국원양자원이라는 KOSPI상장사의 소액 주주입니...</td>
    </tr>
    <tr>
      <th>13</th>
      <td>34</td>
      <td>2017-08-19</td>
      <td>2017-09-18</td>
      <td>0</td>
      <td>679</td>
      <td>기타</td>
      <td>『국가유공자 등 예우 및 지원에 관한법률』상「6.25전몰군경 자녀수당」의 불합리한 ...</td>
      <td>(현황)\n우리들 아버지께서는 67여년전 북의 남침으로 조국이 위기에 처했을 때 젊...</td>
      <td>0</td>
      <td>현황  우리들 아버지께서는   여년전 북의 남침으로 조국이 위기에 처했을 때 젊은...</td>
      <td>현황  우리들 아버지께서는   여년전 북의 남침으로 조국이 위기에 처했을 때 젊은...</td>
    </tr>
    <tr>
      <th>21</th>
      <td>43</td>
      <td>2017-08-19</td>
      <td>2017-09-18</td>
      <td>0</td>
      <td>11293</td>
      <td>육아/교육</td>
      <td>기간제 교사의 정규직화를 반대합니다.</td>
      <td>대통령님, 안녕하세요. 저는 임용을 준비하고 수험생입니다. 처음 기간제 정규직화 된...</td>
      <td>1</td>
      <td>대통령님  안녕하세요  저는 임용을 준비하고 수험생입니다  처음 기간제 정규직화 된...</td>
      <td>대통령님  안녕하세요  임용을 준비하고 수험생입니다  처음 기간제 정규직화 된다고 ...</td>
    </tr>
    <tr>
      <th>24</th>
      <td>46</td>
      <td>2017-08-19</td>
      <td>2017-09-18</td>
      <td>0</td>
      <td>1933</td>
      <td>육아/교육</td>
      <td>기간제교사의 정규직화를 반대합니다.</td>
      <td>대통령님, 안녕하세요. 저는 임용을 준비하고 수험생입니다. 처음 기간제 정규직화 된...</td>
      <td>0</td>
      <td>대통령님  안녕하세요  저는 임용을 준비하고 수험생입니다  처음 기간제 정규직화 된...</td>
      <td>대통령님  안녕하세요  임용을 준비하고 수험생입니다  처음 기간제 정규직화 된다고 ...</td>
    </tr>
    <tr>
      <th>28</th>
      <td>50</td>
      <td>2017-08-19</td>
      <td>2017-10-18</td>
      <td>0</td>
      <td>1251</td>
      <td>일자리</td>
      <td>치과위생사 국가고시 날짜 변경 억울합니다</td>
      <td>안녕하십니까? 대통령님 간단하게 제소개 부터 하겠습니다. 저는 치위생과 3학년 학생...</td>
      <td>0</td>
      <td>안녕하십니까  대통령님 간단하게 제소개 부터 하겠습니다  저는 치위생과  학년 학생...</td>
      <td>안녕하십니까  대통령님 간단하게 제소개 부터 하겠습니다  치위생과  학년 학생입니다...</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 학습 세트에서 투표수가 평균보다 많은 건
df_train.loc[df_train['votes_pos_neg'] == 1].shape
```




    (439, 11)




```python
df_test = df[split_count:]
df_test.shape
```




    (877, 11)




```python
df_test.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>article_id</th>
      <th>start</th>
      <th>end</th>
      <th>answered</th>
      <th>votes</th>
      <th>category</th>
      <th>title</th>
      <th>content</th>
      <th>votes_pos_neg</th>
      <th>content_preprocessing</th>
      <th>content_preprocessing2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>167743</th>
      <td>207826</td>
      <td>2018-04-21</td>
      <td>2018-05-21</td>
      <td>0</td>
      <td>1825</td>
      <td>인권/성평등</td>
      <td>경찰 성평등교육, 인성교육의무화</td>
      <td>뺑소니사고를 당해서 경찰에 신고를 했습니다.\n도착한 경위님과 대화중 계속 아가씨 ...</td>
      <td>0</td>
      <td>뺑소니사고를 당해서 경찰에 신고를 했습니다  도착한 경위님과 대화중 계속 아가씨 아...</td>
      <td>뺑소니사고를 당해서 경찰에 신고를 했습니다  도착한 경위님과 대화중 계속 아가씨 아...</td>
    </tr>
    <tr>
      <th>167766</th>
      <td>207852</td>
      <td>2018-04-21</td>
      <td>2018-05-21</td>
      <td>0</td>
      <td>752</td>
      <td>인권/성평등</td>
      <td>법무부 검찰과장 권순정의 파면을 요구합니다.</td>
      <td>서지현 검사의 검찰과장과 면담내용이 법무부 발표와 전혀 다르다는것을 알게 되었습니다...</td>
      <td>0</td>
      <td>서지현 검사의 검찰과장과 면담내용이 법무부 발표와 전혀 다르다는것을 알게 되었습니다...</td>
      <td>서지현 검사의 검찰과장과 면담내용이 법무부 발표와 전혀 다르다는것을 알게 되었습니다...</td>
    </tr>
    <tr>
      <th>167784</th>
      <td>207870</td>
      <td>2018-04-21</td>
      <td>2018-05-21</td>
      <td>0</td>
      <td>1089</td>
      <td>행정</td>
      <td>강원도 고성군 거진앞바다 2.5마일 해역에 승조원 17명(경찰관 9명, 의무전투경찰...</td>
      <td>존경하는 국민여러분! 존경하는 대통령님!\n강원도 고성군 거진앞바다 2.5마일 해역...</td>
      <td>0</td>
      <td>존경하는 국민여러분  존경하는 대통령님  강원도 고성군 거진앞바다    마일 해역에...</td>
      <td>존경하는 국민여러분  존경하는 대통령님  강원도 고성군 거진앞바다    마일 해역에...</td>
    </tr>
    <tr>
      <th>167818</th>
      <td>207906</td>
      <td>2018-04-21</td>
      <td>2018-05-21</td>
      <td>0</td>
      <td>1965</td>
      <td>기타</td>
      <td>[묻재] 황x미 경찰의 파면을 청원합니다</td>
      <td>밀양 집단 강간 사건을 기억하십니까?\n이때 평생 잊을 수 없는 상처를 받는 피해자...</td>
      <td>0</td>
      <td>밀양 집단 강간 사건을 기억하십니까  이때 평생 잊을 수 없는 상처를 받는 피해자를...</td>
      <td>밀양 집단 강간 사건을 기억하십니까  이때 평생 잊을 상처를 받는 피해자를 우롱하고...</td>
    </tr>
    <tr>
      <th>168141</th>
      <td>208316</td>
      <td>2018-04-21</td>
      <td>2018-05-21</td>
      <td>0</td>
      <td>673</td>
      <td>외교/통일/국방</td>
      <td>일본 자위대 행사와 천황 생일기념식 한국행사 차단</td>
      <td>◼일본 자위대 행사와 천황 생일기념식 한국행사 차단\n군국주의로 물든 일본, 반성없...</td>
      <td>0</td>
      <td>일본 자위대 행사와 천황 생일기념식 한국행사 차단 군국주의로 물든 일본  반성없는...</td>
      <td>일본 자위대 행사와 천황 생일기념식 한국행사 차단 군국주의로 물든 일본  반성없는...</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 테스트 세트에서 투표수가 평균보다 많은 건
df_test.loc[df_test['votes_pos_neg'] == 1].shape
```




    (172, 11)



# 단어 벡터화 하기


```python
from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer(analyzer = 'word', # 캐릭터 단위로 벡터화 할 수도 있습니다.
                             tokenizer = None, # 토크나이저를 따로 지정해 줄 수도 있습니다.
                             preprocessor = None, # 전처리 도구
                             stop_words = None, # 불용어 nltk등의 도구를 사용할 수도 있습니다.
                             min_df = 3, # 토큰이 나타날 최소 문서 개수로 오타나 자주 나오지 않는 특수한 전문용어 제거에 좋다. 
                             ngram_range=(1, 5), # BOW의 단위를 1~3개로 지정합니다.
                             max_features = 3000 # 만들 피처의 수, 단어의 수가 된다. (많을수록 좋지만, 많다고 다 좋은건 ㄴㄴ)
                             # ngram과 max_features의 수 등에 따라서도 정확도가 달라짐
                            )
vectorizer
```




    CountVectorizer(analyzer='word', binary=False, decode_error='strict',
            dtype=<class 'numpy.int64'>, encoding='utf-8', input='content',
            lowercase=True, max_df=1.0, max_features=3000, min_df=3,
            ngram_range=(1, 5), preprocessor=None, stop_words=None,
            strip_accents=None, token_pattern='(?u)\\b\\w\\w+\\b',
            tokenizer=None, vocabulary=None)




```python
%%time 
train_feature_vector = vectorizer.fit_transform(df_train['content_preprocessing2'])
train_feature_vector.shape
```

    Wall time: 15.9 s
    


```python
%%time 
test_feature_vector = vectorizer.fit_transform(df_test['content_preprocessing2'])
test_feature_vector.shape
```

    Wall time: 7.66 s
    


```python
vocab = vectorizer.get_feature_names()
print(len(vocab))
vocab[:10]
# 왜 20개의 feature인가? 우리가 최대 feature를 지정해줬기 때문
# 학습/테스트 데이터의 feature가 같아야 함. 일정 수로 맞춰주어야 함
```

    3000
    




    ['aid',
     'article',
     'articleview',
     'articleview html',
     'articleview html idxno',
     'a씨는',
     'bbk',
     'be',
     'blog',
     'blog naver']




```python
dist = np.sum(train_feature_vector, axis=0)

pd.DataFrame(dist, columns=vocab)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>aid</th>
      <th>article</th>
      <th>articleview</th>
      <th>articleview html</th>
      <th>articleview html idxno</th>
      <th>a씨는</th>
      <th>bbk</th>
      <th>be</th>
      <th>blog</th>
      <th>blog naver</th>
      <th>...</th>
      <th>휴게시간을</th>
      <th>희망을</th>
      <th>힘든</th>
      <th>힘들게</th>
      <th>힘들고</th>
      <th>힘들어</th>
      <th>힘듭니다</th>
      <th>힘없는</th>
      <th>힘을</th>
      <th>힘이</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>62</td>
      <td>96</td>
      <td>41</td>
      <td>70</td>
      <td>54</td>
      <td>54</td>
      <td>23</td>
      <td>21</td>
      <td>146</td>
      <td>140</td>
      <td>...</td>
      <td>51</td>
      <td>21</td>
      <td>106</td>
      <td>62</td>
      <td>27</td>
      <td>28</td>
      <td>33</td>
      <td>30</td>
      <td>67</td>
      <td>50</td>
    </tr>
  </tbody>
</table>
<p>1 rows × 3000 columns</p>
</div>




```python
from sklearn.feature_extraction.text import TfidfTransformer
# 가중치를 적용; Tfidf는 문서에 아주 자주 등장하는 단어 중 큰 의미가 없는 단어
# 전체 청원에서는 자주 등장하지 않지만, 특정 청원에서 아주 많이 등장하는 단어는 중요한 단어라고 여기는 방식
transformer = TfidfTransformer(smooth_idf=False)
transformer
```




    TfidfTransformer(norm='l2', smooth_idf=False, sublinear_tf=False,
             use_idf=True)




```python
%%time 
train_feature_tfidf = transformer.fit_transform(train_feature_vector)
train_feature_tfidf.shape
```

    Wall time: 16.5 ms
    


```python
%%time 
test_feature_tfidf = transformer.fit_transform(test_feature_vector)
test_feature_tfidf.shape
```

    Wall time: 6.94 ms
    


```python
test_feature_tfidf.shape
```




    (877, 3000)



# 랜덤 포레스트로 학습시키기
* 공식문서 : http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html


```python
from sklearn.ensemble import RandomForestClassifier

# 랜덤포레스트 분류기를 사용
forest = RandomForestClassifier(
    n_estimators = 200, n_jobs = -1, random_state=2018)
forest
# max_leaf_nodes는 오버피팅을 방지할 때 사용함
# n_jobs는 몇 개의 CPU 코어를 사용하는 것인지 이야기하는 것 (-1은 걔가 가진 최대의 코어를 사용하도록 함)
```




    RandomForestClassifier(bootstrap=True, class_weight=None, criterion='gini',
                max_depth=None, max_features='auto', max_leaf_nodes=None,
                min_impurity_decrease=0.0, min_impurity_split=None,
                min_samples_leaf=1, min_samples_split=2,
                min_weight_fraction_leaf=0.0, n_estimators=100, n_jobs=-1,
                oob_score=False, random_state=2018, verbose=0,
                warm_start=False)




```python
# 학습에 사용할 y_label 을 넣어준다.
y_label = df_train['votes_pos_neg']
%time forest = forest.fit(train_feature_tfidf, y_label)
```

    Wall time: 1.74 s
    

# 평가하기


```python
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
k_fold = KFold(n_splits=10, shuffle=True, random_state=0)
# 학습 데이터를 'n_splits=10'은 10개로 쪼개어서 확인하라
scoring = 'accuracy'
score = cross_val_score(forest, train_feature_tfidf, y_label, cv=k_fold, n_jobs=-1, scoring=scoring)
score
```




    array([0.82439024, 0.74634146, 0.77073171, 0.7902439 , 0.75609756,
           0.79901961, 0.83333333, 0.75490196, 0.76960784, 0.78431373])




```python
round(np.mean(score)*100,2)
```




    78.29



# 예측


```python
# 테스트 데이터를 넣고 예측한다.
y_pred = forest.predict(test_feature_tfidf)
y_pred[:10]
```




    array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])




```python
y_pred.shape
```




    (877,)




```python
# 예측 결과를 저장하기 위해 데이터프레임에 담아 준다.
output = pd.DataFrame(data={'votes_pos_neg_pred':y_pred})
output.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>votes_pos_neg_pred</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 0과 1이 어떻게 집계 되었는지 확인한다.
# 실제 데이터에는 답변 대상 건이 있는데 없는 것으로 예측되었다.
output['votes_pos_neg_pred'].value_counts()
```




    0    866
    1     11
    Name: votes_pos_neg_pred, dtype: int64




```python
df_test['votes_pos_neg_pred'] = y_pred
```

    C:\Users\rlath\Anaconda3\lib\site-packages\ipykernel_launcher.py:1: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
      """Entry point for launching an IPython kernel.
    


```python
df_test['pred_diff'] = df_test['votes_pos_neg'] - df_test['votes_pos_neg_pred']
df_test.head()
# 실제 데이터에서 예측한 내용을 뺌
```

    C:\Users\rlath\Anaconda3\lib\site-packages\ipykernel_launcher.py:1: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
      """Entry point for launching an IPython kernel.
    




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>article_id</th>
      <th>start</th>
      <th>end</th>
      <th>answered</th>
      <th>votes</th>
      <th>category</th>
      <th>title</th>
      <th>content</th>
      <th>votes_pos_neg</th>
      <th>content_preprocessing</th>
      <th>content_preprocessing2</th>
      <th>votes_pos_neg_pred</th>
      <th>pred_diff</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>167743</th>
      <td>207826</td>
      <td>2018-04-21</td>
      <td>2018-05-21</td>
      <td>0</td>
      <td>1825</td>
      <td>인권/성평등</td>
      <td>경찰 성평등교육, 인성교육의무화</td>
      <td>뺑소니사고를 당해서 경찰에 신고를 했습니다.\n도착한 경위님과 대화중 계속 아가씨 ...</td>
      <td>0</td>
      <td>뺑소니사고를 당해서 경찰에 신고를 했습니다  도착한 경위님과 대화중 계속 아가씨 아...</td>
      <td>뺑소니사고를 당해서 경찰에 신고를 했습니다  도착한 경위님과 대화중 계속 아가씨 아...</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>167766</th>
      <td>207852</td>
      <td>2018-04-21</td>
      <td>2018-05-21</td>
      <td>0</td>
      <td>752</td>
      <td>인권/성평등</td>
      <td>법무부 검찰과장 권순정의 파면을 요구합니다.</td>
      <td>서지현 검사의 검찰과장과 면담내용이 법무부 발표와 전혀 다르다는것을 알게 되었습니다...</td>
      <td>0</td>
      <td>서지현 검사의 검찰과장과 면담내용이 법무부 발표와 전혀 다르다는것을 알게 되었습니다...</td>
      <td>서지현 검사의 검찰과장과 면담내용이 법무부 발표와 전혀 다르다는것을 알게 되었습니다...</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>167784</th>
      <td>207870</td>
      <td>2018-04-21</td>
      <td>2018-05-21</td>
      <td>0</td>
      <td>1089</td>
      <td>행정</td>
      <td>강원도 고성군 거진앞바다 2.5마일 해역에 승조원 17명(경찰관 9명, 의무전투경찰...</td>
      <td>존경하는 국민여러분! 존경하는 대통령님!\n강원도 고성군 거진앞바다 2.5마일 해역...</td>
      <td>0</td>
      <td>존경하는 국민여러분  존경하는 대통령님  강원도 고성군 거진앞바다    마일 해역에...</td>
      <td>존경하는 국민여러분  존경하는 대통령님  강원도 고성군 거진앞바다    마일 해역에...</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>167818</th>
      <td>207906</td>
      <td>2018-04-21</td>
      <td>2018-05-21</td>
      <td>0</td>
      <td>1965</td>
      <td>기타</td>
      <td>[묻재] 황x미 경찰의 파면을 청원합니다</td>
      <td>밀양 집단 강간 사건을 기억하십니까?\n이때 평생 잊을 수 없는 상처를 받는 피해자...</td>
      <td>0</td>
      <td>밀양 집단 강간 사건을 기억하십니까  이때 평생 잊을 수 없는 상처를 받는 피해자를...</td>
      <td>밀양 집단 강간 사건을 기억하십니까  이때 평생 잊을 상처를 받는 피해자를 우롱하고...</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>168141</th>
      <td>208316</td>
      <td>2018-04-21</td>
      <td>2018-05-21</td>
      <td>0</td>
      <td>673</td>
      <td>외교/통일/국방</td>
      <td>일본 자위대 행사와 천황 생일기념식 한국행사 차단</td>
      <td>◼일본 자위대 행사와 천황 생일기념식 한국행사 차단\n군국주의로 물든 일본, 반성없...</td>
      <td>0</td>
      <td>일본 자위대 행사와 천황 생일기념식 한국행사 차단 군국주의로 물든 일본  반성없는...</td>
      <td>일본 자위대 행사와 천황 생일기념식 한국행사 차단 군국주의로 물든 일본  반성없는...</td>
      <td>0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>




```python
pred_diff = df_test['pred_diff'].value_counts()
pred_diff
# 0이라는 것은 예측했다는 이야기
```




     0    700
     1    169
    -1      8
    Name: pred_diff, dtype: int64




```python
print('전체 {}건의 데이터 중 {}건 예측'.format(y_pred.shape[0], pred_diff[0]))
```

    전체 877건의 데이터 중 700건 예측
    


```python
acc = ( pred_diff[0] / y_pred.shape[0] ) *100 
print('예측 비율 {}'.format(acc))
```

    예측 비율 79.81755986316989
    
