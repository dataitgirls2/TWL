
# [A Grammar of Graphics for Python — plotnine](http://plotnine.readthedocs.io/en/stable/index.html)
* [tutorial](http://plotnine.readthedocs.io/en/stable/tutorials.html)
* [ggplot2-cheatsheet](https://www.rstudio.com/wp-content/uploads/2015/03/ggplot2-cheatsheet.pdf)


```python
!pip install -q 'plotnine[all]'
```


```python
!pip show plotnine
```

    Name: plotnine
    Version: 0.3.0
    Summary: A grammar of graphics for python
    Home-page: https://github.com/has2k1/plotnine
    Author: Hassan Kibirige
    Author-email: has2k1@gmail.com
    License: GPL-2
    Location: /usr/local/lib/python3.6/dist-packages
    Requires: pandas, statsmodels, six, numpy, mizani, scipy, patsy, matplotlib
    Required-by: 



```python
import pandas as pd
import numpy as np
print(pd.__version__)
print(np.__version__)
```

    0.22.0
    1.14.5
    


```python
# 불필요한 warnings을 찍지 않기 위해 import 해왔습니다. 
import warnings
warnings.filterwarnings('ignore')

%config InlineBackend.figure_format = 'retina'

!apt -qq -y install fonts-nanum > /dev/null
import matplotlib.font_manager as fm
fontpath = '/usr/share/fonts/truetype/nanum/NanumBarunGothic.ttf'
font = fm.FontProperties(fname=fontpath, size=9)

from plotnine import *
import plotnine
```

    
    WARNING: apt does not have a stable CLI interface. Use with caution in scripts.
    



```python
# 크롤링해 온 국민청원 데이터를 판다스를 통해 읽어온다.
df = pd.read_csv('https://s3.ap-northeast-2.amazonaws.com/data10902/petition/petition.csv', 
                 parse_dates=['start', 'end'])

# 데이터의 크기가 어느정도인지 본다.
df.shape
```




    (211690, 8)




```python
# 전체 데이터로 보면 너무 느리기 때문에 본인의 관심사에 맞는 데이터를 가져옵니다.
aversion = df.loc[(df.title.str.contains('공인인증서|공인 인증서|액티브X|ActiveX|Active X', regex=True)) & \
                  (df.content.str.contains('공인인증서|공인 인증서|액티브X|ActiveX|Active X', regex=True))] 
aversion.shape
```




    (59, 8)




```python
aversion.head(3)
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
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>747</th>
      <td>775</td>
      <td>2017-08-28</td>
      <td>2017-09-12</td>
      <td>0</td>
      <td>4</td>
      <td>미래</td>
      <td>관공서 마다 다른 Active X 설치 시대를 역행하는 행정 서비스</td>
      <td>안녕하세요. 저는 세금을 내고 어쩌다 교통 범칙금도 내는 일반 시민 입니다.\n지금...</td>
    </tr>
    <tr>
      <th>1319</th>
      <td>1348</td>
      <td>2017-09-01</td>
      <td>2017-11-30</td>
      <td>0</td>
      <td>7</td>
      <td>미래</td>
      <td>암티브엑스(암+ActiveX)를 폐지해주세요.</td>
      <td>한국에서 금융권 사이트와 정부 사이트를 이용하려면 끝도 없이 깔아야 하는 Activ...</td>
    </tr>
    <tr>
      <th>12394</th>
      <td>12454</td>
      <td>2017-09-08</td>
      <td>2017-12-07</td>
      <td>0</td>
      <td>1</td>
      <td>기타</td>
      <td>공인인증서 폐지해주세요</td>
      <td>공인인증서 때문에 특히 예비군들이 피해를 많이 봅니다.\n훈련 하나 확인하는데 공인...</td>
    </tr>
  </tbody>
</table>
</div>




```python
aversion.tail(3)
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
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>207567</th>
      <td>268275</td>
      <td>2018-06-11</td>
      <td>2018-07-11</td>
      <td>0</td>
      <td>4</td>
      <td>경제민주화</td>
      <td>공인인증서 폐기해주세요! 제발!</td>
      <td>적폐중의 적폐인 공인인증서 사용을 완전히 없애주세요.\n모바일로 실시간 비밀번호 넣...</td>
    </tr>
    <tr>
      <th>207670</th>
      <td>268399</td>
      <td>2018-06-11</td>
      <td>2018-07-11</td>
      <td>0</td>
      <td>5</td>
      <td>행정</td>
      <td>공인인증서의 제도의 깔끔한 폐지를 원합니다.</td>
      <td>지난 수년간 공인인증서 제도는 발급절차의 까다로움과 사용의 불편함 때문에 대다수의 ...</td>
    </tr>
    <tr>
      <th>207673</th>
      <td>268402</td>
      <td>2018-06-11</td>
      <td>2018-07-11</td>
      <td>0</td>
      <td>21</td>
      <td>행정</td>
      <td>공인인증서의 제도의 깔끔한 폐지를 원합니다.</td>
      <td>지난 수년간 공인인증서 제도는 발급절차의 까다로움과 사용의 불편함 때문에 대다수의 ...</td>
    </tr>
  </tbody>
</table>
</div>




```python
aversion.info()
```

    <class 'pandas.core.frame.DataFrame'>
    Int64Index: 59 entries, 747 to 207673
    Data columns (total 8 columns):
    article_id    59 non-null int64
    start         59 non-null datetime64[ns]
    end           59 non-null datetime64[ns]
    answered      59 non-null int64
    votes         59 non-null int64
    category      59 non-null object
    title         59 non-null object
    content       59 non-null object
    dtypes: datetime64[ns](2), int64(3), object(3)
    memory usage: 4.1+ KB
    


```python
aversion.describe(include=np.object)
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
      <th>category</th>
      <th>title</th>
      <th>content</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>59</td>
      <td>59</td>
      <td>59</td>
    </tr>
    <tr>
      <th>unique</th>
      <td>9</td>
      <td>56</td>
      <td>59</td>
    </tr>
    <tr>
      <th>top</th>
      <td>행정</td>
      <td>공인인증서 폐지</td>
      <td>공인인증서 지역에 씨티은행,하나은행,국민은행,신한은행,우체국은행,농협은행,우리은행등...</td>
    </tr>
    <tr>
      <th>freq</th>
      <td>21</td>
      <td>2</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>



## 시계열 데이터 보기


```python
aversion.dtypes
```




    article_id                  int64
    start              datetime64[ns]
    end                datetime64[ns]
    answered                    int64
    votes                       int64
    category                   object
    title                      object
    content                    object
    start_year                  int64
    start_month                 int64
    start_day                   int64
    start_hour                  int64
    start_dow                   int64
    start_wdn                  object
    start_dayofweek            object
    dtype: object




```python
aversion['start_year'] = aversion['start'].dt.year
aversion['start_month'] = aversion['start'].dt.month
aversion['start_day'] = aversion['start'].dt.day
aversion['start_hour'] = aversion['start'].dt.hour
aversion['start_dow'] = aversion['start'].dt.dayofweek
aversion['start_wdn'] = aversion['start'].dt.weekday_name

# 요일을 좀 더 간단하게 표현해 봅니다.
days = {0:'Mon',1:'Tues',2:'Weds',3:'Thurs',4:'Fri',5:'Sat',6:'Sun'}
aversion['start_dayofweek'] = aversion['start_dow'].apply(lambda x: days[x])
aversion.shape
```




    (1231, 15)




```python
days = {0:'월',1:'화',2:'수',3:'목',4:'금',5:'토',6:'일'}
aversion['start_dayofweek'] = aversion['start_dow'].apply(lambda x: days[x])
# apply는 매 행마다 괄호 안의 내용을 반영해줌
aversion['start_dayofweek'].value_counts()
```




    화    206
    일    184
    수    177
    월    177
    토    167
    금    161
    목    159
    Name: start_dayofweek, dtype: int64




```python
# 월별 데이터 보기
aversion['start_month'].value_counts()
```




    5     246
    2     199
    6     177
    1     142
    11    120
    3     108
    12     92
    4      74
    10     43
    9      27
    8       3
    Name: start_month, dtype: int64




```python
# 요일별 데이터 보기
aversion['start_dayofweek'].value_counts()
```




    화    206
    일    184
    수    177
    월    177
    토    167
    금    161
    목    159
    Name: start_dayofweek, dtype: int64




```python
# 요일별 데이터 보기
# 육아, 보육과 관련된 청원을 내는 사람들은 보통 수요일에 청원을 많이 내고 주말에는 적게 내는 것을 알수 있습니다.
aversion['start_wdn'].value_counts()
```




    Tuesday      206
    Sunday       184
    Monday       177
    Wednesday    177
    Saturday     167
    Friday       161
    Thursday     159
    Name: start_wdn, dtype: int64



## 한글폰트 사용하기
* 한글이 깨져보이는 것을 해결하기 위해 한글폰트를 사용해야 합니다.
* 여기에서는 나눔바른고딕을 사용하도록 합니다.
    * 이때 폰트가 로컬 컴퓨터에 설치되어 있어야해요.
    * 나눔고딕은 무료로 사용할 수 있는 폰트입니다.
    * 참고 : [네이버 나눔글꼴 라이선스](https://help.naver.com/support/contents/contents.nhn?serviceNo=1074&categoryNo=3497)
* 한글을 사용하기 위해서는 ggplot에서 theme에 폰트를 지정해 주면됩니다.
* 아래의 문서를 참고하면 **element_text**와 관련된 옵션을 볼 수 있습니다.
* 참고 : [plotnine.themes.element_text — plotnine 0.3.0 documentation](http://plotnine.readthedocs.io/en/stable/generated/plotnine.themes.element_text.html)


```python
# 카테고리별 청원 수
(ggplot(aversion)
 + aes('category')
 + geom_bar(fill='#FF0080')
 + ggtitle('카테고리별 청원 수')
 + theme(text=element_text(fontproperties=font),
        axis_text_x=element_text(rotation=60))
)
```


![png](output_19_0.png)





    <ggplot: (-9223363278799454271)>




```python
# 카테고리별 투표수
(ggplot(aversion)
 + aes(x='category', y='votes')
 + geom_col(fill='pink')
 + ggtitle('카테고리별 투표수')
 + theme(text=element_text(fontproperties=font),
        axis_text_x=element_text(rotation=70))
)
```


![png](output_20_0.png)





    <ggplot: (8758057713377)>




```python
# coord_flip을 사용해서 x축과 y축을 바꿔본다.
(ggplot(aversion)
 + aes(x='category', y='votes')
 + geom_col(fill='pink')
 + ggtitle('카테고리별 투표수')
 + coord_flip()  # 가로 세로를 바꾸어서 보여줌
 + theme(text=element_text(fontproperties=font))
)
```


![png](output_21_0.png)





    <ggplot: (8758051031567)>




```python
(ggplot(aversion) 
 + aes(x='category', y='votes', fill='answered')
 + geom_point()
 + ggtitle('카테고리별 답변 대상 청원')
 + theme(text=element_text(fontproperties=font),
        axis_text_x=element_text(rotation=70))
)
```


![png](output_22_0.png)





    <ggplot: (8758051468131)>




```python
(ggplot(aversion, aes(x='category', y='votes', fill='answered'))
 + geom_col()
 + ggtitle('카테고리별 답변 대상 청원')
 + theme(text=element_text(fontproperties=font),
        axis_text_x=element_text(rotation=70))
)
```


![png](output_23_0.png)





    <ggplot: (8758051360057)>




```python
# 연도별 청원수는 크게 의미가 없다.
(ggplot(aversion)
 + aes('start_year')
 + geom_bar(fill='green')
 + labs(y='청원수', x='연도', title='연도별 청원수')
 + theme(text=element_text(fontproperties=font))
)
```


![png](output_24_0.png)





    <ggplot: (-9223363278803254261)>




```python
(ggplot(aversion)
 + aes('start_month')
 + geom_bar(fill='green')
 + labs(y='청원수', x='월', title='월별 청원수')
 + theme(text=element_text(fontproperties=font))
)
```


![png](output_25_0.png)





    <ggplot: (8758055301398)>




```python
# 9월에 청원이 특히 많은데 상위 3개 날짜만 뽑아보자
child_9 = child.loc[child['start_month'] == 9]
child_9['start_day'].value_counts()[:3]
```




    26    75
    20    68
    21    44
    Name: start_day, dtype: int64




```python
child_9_sample = child_9.loc[(child_9['start_day'] == 26) | (child_9['start_day'] == 20)]
child_9_sample[['title', 'content', 'votes']].sort_values(by='votes', ascending=False)[:20]
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
      <th>title</th>
      <th>content</th>
      <th>votes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>17052</th>
      <td>초등돌봄교실 지자체 이관을 반대합니다</td>
      <td>학부모들이 돌봄교실에 자녀를\n믿고 맡기는 것은 학교가 관리하기 때문인데 운영주체가...</td>
      <td>7</td>
    </tr>
    <tr>
      <th>15251</th>
      <td>초등돌봄교실 지자체 이관을 절대 반대합니다.</td>
      <td>초등돌봄교실은 학교 안에서 학부모와 학생으로부터 신뢰를 바탕으로 만족도가 1위인 정...</td>
      <td>6</td>
    </tr>
    <tr>
      <th>15254</th>
      <td>돌봄교실 지자체이관반대</td>
      <td>초등돌봄교실은 학교 안에서 학부모와 학생으로부터 신뢰를 바탕으로 만족도가 1위인 정...</td>
      <td>6</td>
    </tr>
    <tr>
      <th>15292</th>
      <td>초등돌봄교실 지자체 이관을 반대합니다</td>
      <td>초등돌봄교실 지자체 이관 반대입니다.\n돌봄전담사 의견을 들어봐 주세요....\n학...</td>
      <td>6</td>
    </tr>
    <tr>
      <th>16901</th>
      <td>울산초등학교(울산광역시 중구 소재) 수직증축 철회 강력히 요청합니다</td>
      <td>울산초등학교(울산광역시 중구 소재) 수직증축 철회 강력히 요청합니다</td>
      <td>6</td>
    </tr>
    <tr>
      <th>17054</th>
      <td>돌봄교실 지자체이관을 결사반대합니다!!!</td>
      <td>돌봄전담사가 가장 우려하는 점은 시설은 학교에 있고 그 운영주체는 지자체가 맡아 분...</td>
      <td>6</td>
    </tr>
    <tr>
      <th>17027</th>
      <td>돌봄교실의 지자체 이관 결사 반대한다.</td>
      <td>돌봄교실은 학교 안에서의 가정이고 엄마의 중요한 자리다.  가정교육의 중요성은 익히...</td>
      <td>6</td>
    </tr>
    <tr>
      <th>16956</th>
      <td>초등돌봄교실 지자체 이관을 절대 반대합니다</td>
      <td>돌봄전담사가 가장 우려하는 점은 시설은 학교에 있고 그 운영주체는 지자체가 맡아 분...</td>
      <td>5</td>
    </tr>
    <tr>
      <th>17067</th>
      <td>초등돌봄교실 지자체 이관 반대</td>
      <td>초등돌봄교실 이용 아동은 저학년입니다. 지역아동센터는 중학생까지 관리를 합니다. 어...</td>
      <td>5</td>
    </tr>
    <tr>
      <th>17049</th>
      <td>초등돌봄교실 지자체 이관반대</td>
      <td>돌봄교실은 학교 안에서 운영되어야 안정적으로 운영됩니다. 돌봄교실이 과연 무엇을 하...</td>
      <td>5</td>
    </tr>
    <tr>
      <th>17062</th>
      <td>초등돌봄교실 지자체 이관 반대</td>
      <td>초등저학년이 다니는 돌봄교실은 학교안에 잇어야 안전합니다. 지자체로 이관이 되면 안...</td>
      <td>5</td>
    </tr>
    <tr>
      <th>17069</th>
      <td>초등돌봄교실 지자체 이관 반대</td>
      <td>초등돌봄교실 이용 아동은 저학년입니다. 지역아동센터는 중학생까지 관리를 합니다. 어...</td>
      <td>5</td>
    </tr>
    <tr>
      <th>17026</th>
      <td>초등학교 돌봄교실 지체체 이관에 관하여 청원드립니다.</td>
      <td>난생 처음 저의 생각과 의견을 전하고 싶어 처음으로 청와대 홈페이지를 들어왔습니다....</td>
      <td>5</td>
    </tr>
    <tr>
      <th>17048</th>
      <td>초등돌봄교실 지자체 이관 반대건</td>
      <td>돌봄전담사가 가장 우려하는 점은 시설은 학교에 있고 그 운영주체는 지자체가 맡아 분...</td>
      <td>5</td>
    </tr>
    <tr>
      <th>15407</th>
      <td>초등돌봄교실 지자체이관과 사회서비스공단설립 절대반대</td>
      <td>예전 지자체에서 운영할 당시 문제점이 제기되어 교육청으로 통합한 사실이 있는데 실패...</td>
      <td>5</td>
    </tr>
    <tr>
      <th>15321</th>
      <td>돌봄교실 이관반대</td>
      <td>지자체로 이관하면 학교운영주체의 초등돌봄교실의 질이 향상되기는 어렵다. 지자체는 학...</td>
      <td>5</td>
    </tr>
    <tr>
      <th>15320</th>
      <td>초등돌봄교실 지자체 이관 반대합니다</td>
      <td>초등돌봄교실은 학교 안에서 학부모와 학생으로부터 신뢰를 바탕으로 만족도가 1위인 정...</td>
      <td>5</td>
    </tr>
    <tr>
      <th>15319</th>
      <td>돌봄교실 이관반대</td>
      <td>지자체로 이관하면 학교운영주체의 초등돌봄교실의 질이 향상되기는 어렵다. 지자체는 학...</td>
      <td>5</td>
    </tr>
    <tr>
      <th>15285</th>
      <td>돌봄교실 이관 반대</td>
      <td>지자체로 이관하면 학교운영주체의 초등돌봄교실의 질이 향상되기는 어렵다. 지자체는 학...</td>
      <td>5</td>
    </tr>
    <tr>
      <th>15304</th>
      <td>초등돌봄교실 지자체 이관을 절대 반대합니다.</td>
      <td>초등돌봄교실은 학교 안에서 학부모와 학생으로부터 신뢰를 바탕으로 만족도가 1위인 정...</td>
      <td>5</td>
    </tr>
  </tbody>
</table>
</div>




```python
(ggplot(child)
 + aes('start_day')
 + geom_bar(fill='green')
 + labs(y='청원수', x='일', title='일자별 청원수')
 + theme(text=element_text(fontproperties=font))
)
```


![png](output_28_0.png)





    <ggplot: (-9223363243667584070)>




```python
# 그래프를 그리다가 컬럼명이 떠오르지 않으면 위로 올라가지 않고 바로 컬럼명을 찍어 봅니다.
child.columns
```




    Index(['article_id', 'start', 'end', 'answered', 'votes', 'category', 'title',
           'content', 'start_year', 'start_month', 'start_day', 'start_hour',
           'start_dow', 'start_wdn', 'start_dayofweek'],
          dtype='object')




```python
(ggplot(child)
 + aes('start_dayofweek')
 + geom_bar(fill='green')
 + labs(y='청원수', x='요일', title='요일별 청원수')
 + theme(text=element_text(fontproperties=font))
)
```


![png](output_30_0.png)





    <ggplot: (8793186791039)>




```python
# 박스플롯을 그려볼까요?
(ggplot(child, aes(x='start_dayofweek', y='votes', fill='category'))
 + geom_boxplot()
 + labs(y='투표', x='요일', title='요일별 청원')
 + theme(text=element_text(fontproperties=font))
)
```


![png](output_31_0.png)





    <ggplot: (8793186753088)>




```python
# 그래프를 좀 더 자세하게 보기 위해 투표수가 특정 건 이하인 데이터만 모아본다.
child_votes_25000 = child.loc[child['votes'] < 1000]

(ggplot(child_votes_25000, aes(x='start_dayofweek', y='votes', fill='category'))
 + geom_boxplot()
 + labs(y='투표', x='요일', title='요일별 청원')
 + theme(text=element_text(fontproperties=font))
)
```


![png](output_32_0.png)





    <ggplot: (-9223363243667989297)>


