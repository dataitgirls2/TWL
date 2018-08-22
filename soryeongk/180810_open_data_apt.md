
# 전국 신규 민간 아파트 분양가격 동향
* 2015년 10월부터 2018년 4월까지
* 주택분양보증을 받아 분양한 전체 민간 신규아파트 분양가격 동향
* https://www.data.go.kr/dataset/3035522/fileData.do


```python
import warnings
warnings.filterwarnings('ignore')
```


```python
import pandas as pd
import numpy as np
import re
from plotnine import *
```


```python
%ls Data
```

     C 드라이브의 볼륨: Windows
     볼륨 일련 번호: 44EC-5869

     C:\Users\rlath\dataitgirls\projects\open_data_apt\Data 디렉터리

    2018-08-10  오전 10:37    <DIR>          .
    2018-08-10  오전 10:37    <DIR>          ..
    2018-08-10  오전 10:35             4,509 180810_open_data_apt_2013_2015.csv
    2018-08-10  오전 10:35           105,350 180810_open_data_apt_2015_2018.csv
                   2개 파일             109,859 바이트
                   2개 디렉터리  199,776,309,248 바이트 남음



```python
pre_sale = pd.read_csv('Data/180810_open_data_apt_2015_2018.csv', encoding='euc-kr')
pre_sale.shape
```




    (2805, 5)




```python
pre_sale.head()
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
      <th>지역명</th>
      <th>규모구분</th>
      <th>연도</th>
      <th>월</th>
      <th>분양가격(㎡)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>서울</td>
      <td>전체</td>
      <td>2015</td>
      <td>10</td>
      <td>5841</td>
    </tr>
    <tr>
      <th>1</th>
      <td>서울</td>
      <td>전용면적 60㎡이하</td>
      <td>2015</td>
      <td>10</td>
      <td>5652</td>
    </tr>
    <tr>
      <th>2</th>
      <td>서울</td>
      <td>전용면적 60㎡초과 85㎡이하</td>
      <td>2015</td>
      <td>10</td>
      <td>5882</td>
    </tr>
    <tr>
      <th>3</th>
      <td>서울</td>
      <td>전용면적 85㎡초과 102㎡이하</td>
      <td>2015</td>
      <td>10</td>
      <td>5721</td>
    </tr>
    <tr>
      <th>4</th>
      <td>서울</td>
      <td>전용면적 102㎡초과</td>
      <td>2015</td>
      <td>10</td>
      <td>5879</td>
    </tr>
  </tbody>
</table>
</div>




```python
pre_sale.tail()
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
      <th>지역명</th>
      <th>규모구분</th>
      <th>연도</th>
      <th>월</th>
      <th>분양가격(㎡)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2800</th>
      <td>제주</td>
      <td>전체</td>
      <td>2018</td>
      <td>6</td>
      <td>3925</td>
    </tr>
    <tr>
      <th>2801</th>
      <td>제주</td>
      <td>전용면적 60㎡이하</td>
      <td>2018</td>
      <td>6</td>
      <td>5462</td>
    </tr>
    <tr>
      <th>2802</th>
      <td>제주</td>
      <td>전용면적 60㎡초과 85㎡이하</td>
      <td>2018</td>
      <td>6</td>
      <td>3639</td>
    </tr>
    <tr>
      <th>2803</th>
      <td>제주</td>
      <td>전용면적 85㎡초과 102㎡이하</td>
      <td>2018</td>
      <td>6</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2804</th>
      <td>제주</td>
      <td>전용면적 102㎡초과</td>
      <td>2018</td>
      <td>6</td>
      <td>3029</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 분양가격이 숫자 타입이 아닙니다. 숫자 타입으로 변경해줄 필요가 있겠어요.
pre_sale.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 2805 entries, 0 to 2804
    Data columns (total 5 columns):
    지역명        2805 non-null object
    규모구분       2805 non-null object
    연도         2805 non-null int64
    월          2805 non-null int64
    분양가격(㎡)    2658 non-null object
    dtypes: int64(2), object(3)
    memory usage: 109.6+ KB



```python
pre_sale_price = pre_sale['분양가격(㎡)']
```


```python
# 연도와 월은 카테고리 형태의 데이터이기 때문에 스트링 형태로 변경
pre_sale['연도'] = pre_sale['연도'].astype(str)
pre_sale['월'] = pre_sale['월'].astype(str)
```


```python
# 분양가격의 타입을 숫자로 변경해 줍니다.
pre_sale['분양가격'] = pd.to_numeric(pre_sale_price, errors='coerce')
# 평당 분양가격을 구해볼까요.
pre_sale['평당분양가격'] = pre_sale['분양가격'] * 3.3
```


```python
pre_sale.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 2805 entries, 0 to 2804
    Data columns (total 7 columns):
    지역명        2805 non-null object
    규모구분       2805 non-null object
    연도         2805 non-null object
    월          2805 non-null object
    분양가격(㎡)    2658 non-null object
    분양가격       2582 non-null float64
    평당분양가격     2582 non-null float64
    dtypes: float64(2), object(5)
    memory usage: 153.5+ KB



```python
# 분양가격에 결측치가 많이 있어요.
pre_sale.isnull().sum()
```




    지역명          0
    규모구분         0
    연도           0
    월            0
    분양가격(㎡)    147
    분양가격       223
    평당분양가격     223
    dtype: int64




```python
pre_sale.describe()
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
      <th>분양가격</th>
      <th>평당분양가격</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>2,582</td>
      <td>2,582</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>3,057</td>
      <td>10,087</td>
    </tr>
    <tr>
      <th>std</th>
      <td>1,110</td>
      <td>3,663</td>
    </tr>
    <tr>
      <th>min</th>
      <td>1,868</td>
      <td>6,164</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>2,339</td>
      <td>7,719</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>2,738</td>
      <td>9,037</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>3,289</td>
      <td>10,854</td>
    </tr>
    <tr>
      <th>max</th>
      <td>8,098</td>
      <td>26,723</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 2017년 데이터만 봅니다.
pre_sale_2017 = pre_sale.loc[pre_sale['연도'] == 2017]
pre_sale_2017.shape
```




    (0, 7)




```python
# 같은 값을 갖고 있는 걸로 시도별로 동일하게 데이터가 들어 있는 것을 확인할 수 있습니다.
pre_sale['규모구분'].value_counts()
```




    전용면적 102㎡초과          561
    전용면적 85㎡초과 102㎡이하    561
    전용면적 60㎡초과 85㎡이하     561
    전체                   561
    전용면적 60㎡이하           561
    Name: 규모구분, dtype: int64



# 전국평균 분양가격


```python
# 분양가격만 봤을 때 2015년에서 2018년으로 갈수록 오른 것을 확인할 수 있습니다.
pd.options.display.float_format = '{:,.0f}'.format
pre_sale.groupby(pre_sale.연도).describe().T
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
      <th>연도</th>
      <th>2015</th>
      <th>2016</th>
      <th>2017</th>
      <th>2018</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="8" valign="top">분양가격</th>
      <th>count</th>
      <td>243</td>
      <td>984</td>
      <td>899</td>
      <td>456</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>2,789</td>
      <td>2,934</td>
      <td>3,140</td>
      <td>3,299</td>
    </tr>
    <tr>
      <th>std</th>
      <td>977</td>
      <td>1,071</td>
      <td>1,108</td>
      <td>1,199</td>
    </tr>
    <tr>
      <th>min</th>
      <td>1,868</td>
      <td>1,900</td>
      <td>1,976</td>
      <td>2,076</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>2,225</td>
      <td>2,282</td>
      <td>2,365</td>
      <td>2,470</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>2,516</td>
      <td>2,672</td>
      <td>2,849</td>
      <td>2,912</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>3,026</td>
      <td>3,148</td>
      <td>3,456</td>
      <td>3,647</td>
    </tr>
    <tr>
      <th>max</th>
      <td>7,092</td>
      <td>8,096</td>
      <td>7,887</td>
      <td>8,098</td>
    </tr>
    <tr>
      <th rowspan="8" valign="top">평당분양가격</th>
      <th>count</th>
      <td>243</td>
      <td>984</td>
      <td>899</td>
      <td>456</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>9,203</td>
      <td>9,683</td>
      <td>10,360</td>
      <td>10,888</td>
    </tr>
    <tr>
      <th>std</th>
      <td>3,224</td>
      <td>3,536</td>
      <td>3,655</td>
      <td>3,958</td>
    </tr>
    <tr>
      <th>min</th>
      <td>6,164</td>
      <td>6,270</td>
      <td>6,521</td>
      <td>6,851</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>7,342</td>
      <td>7,531</td>
      <td>7,804</td>
      <td>8,153</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>8,303</td>
      <td>8,818</td>
      <td>9,402</td>
      <td>9,611</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>9,984</td>
      <td>10,390</td>
      <td>11,405</td>
      <td>12,036</td>
    </tr>
    <tr>
      <th>max</th>
      <td>23,404</td>
      <td>26,717</td>
      <td>26,027</td>
      <td>26,723</td>
    </tr>
  </tbody>
</table>
</div>



## 규모별 전국 평균 분양가격


```python
pre_sale.pivot_table('평당분양가격', '규모구분', '연도')
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
      <th>연도</th>
      <th>2015</th>
      <th>2016</th>
      <th>2017</th>
      <th>2018</th>
    </tr>
    <tr>
      <th>규모구분</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>전용면적 102㎡초과</th>
      <td>9,837</td>
      <td>10,389</td>
      <td>11,334</td>
      <td>11,260</td>
    </tr>
    <tr>
      <th>전용면적 60㎡이하</th>
      <td>8,952</td>
      <td>9,399</td>
      <td>10,246</td>
      <td>10,957</td>
    </tr>
    <tr>
      <th>전용면적 60㎡초과 85㎡이하</th>
      <td>8,892</td>
      <td>9,296</td>
      <td>9,825</td>
      <td>10,438</td>
    </tr>
    <tr>
      <th>전용면적 85㎡초과 102㎡이하</th>
      <td>9,519</td>
      <td>10,122</td>
      <td>10,540</td>
      <td>11,457</td>
    </tr>
    <tr>
      <th>전체</th>
      <td>8,893</td>
      <td>9,293</td>
      <td>9,901</td>
      <td>10,560</td>
    </tr>
  </tbody>
</table>
</div>



# 전국 분양가 변동금액
규모구분이 전체로 되어있는 금액으로 연도별 변동금액을 살펴봅니다.


```python
# 규모구분에서 전체로 되어있는 데이터만 가져온다.
region_year_all = pre_sale.loc[pre_sale['규모구분'] == '전체']
region_year = region_year_all.pivot_table('평당분양가격', '지역명', '연도').reset_index()

region_year['변동액'] = (region_year['2018'] - region_year['2015']).astype(int)
max_delta_price = np.max(region_year['변동액'])*1000
min_delta_price = np.min(region_year['변동액'])*1000
mean_delta_price = np.mean(region_year['변동액'])*1000

print('2015년부터 2018년까지 분양가는 계속 상승했으며, 상승액이 가장 큰 지역은 제주이며 상승액은 평당 {:,.0f}원이다.'.format(max_delta_price))
print('상승액이 가장 작은 지역은 울산이며 평당 {:,.0f}원이다.'.format(min_delta_price))
print('전국 평균 변동액은 평당 {:,.0f}원이다.'.format(mean_delta_price))

region_year
```

    2015년부터 2018년까지 분양가는 계속 상승했으며, 상승액이 가장 큰 지역은 제주이며 상승액은 평당 5,335,000원이다.
    상승액이 가장 작은 지역은 울산이며 평당 387,000원이다.
    전국 평균 변동액은 평당 1,666,647원이다.





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
      <th>연도</th>
      <th>지역명</th>
      <th>2015</th>
      <th>2016</th>
      <th>2017</th>
      <th>2018</th>
      <th>변동액</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>강원</td>
      <td>7,160</td>
      <td>7,011</td>
      <td>7,127</td>
      <td>7,643</td>
      <td>482</td>
    </tr>
    <tr>
      <th>1</th>
      <td>경기</td>
      <td>10,377</td>
      <td>11,220</td>
      <td>11,850</td>
      <td>12,854</td>
      <td>2476</td>
    </tr>
    <tr>
      <th>2</th>
      <td>경남</td>
      <td>7,586</td>
      <td>7,848</td>
      <td>8,120</td>
      <td>8,894</td>
      <td>1308</td>
    </tr>
    <tr>
      <th>3</th>
      <td>경북</td>
      <td>7,171</td>
      <td>7,361</td>
      <td>7,795</td>
      <td>8,262</td>
      <td>1090</td>
    </tr>
    <tr>
      <th>4</th>
      <td>광주</td>
      <td>8,052</td>
      <td>8,899</td>
      <td>9,464</td>
      <td>9,630</td>
      <td>1577</td>
    </tr>
    <tr>
      <th>5</th>
      <td>대구</td>
      <td>9,232</td>
      <td>10,310</td>
      <td>11,456</td>
      <td>11,652</td>
      <td>2419</td>
    </tr>
    <tr>
      <th>6</th>
      <td>대전</td>
      <td>8,098</td>
      <td>8,502</td>
      <td>9,045</td>
      <td>9,589</td>
      <td>1490</td>
    </tr>
    <tr>
      <th>7</th>
      <td>부산</td>
      <td>10,307</td>
      <td>10,430</td>
      <td>11,578</td>
      <td>12,710</td>
      <td>2402</td>
    </tr>
    <tr>
      <th>8</th>
      <td>서울</td>
      <td>19,725</td>
      <td>20,663</td>
      <td>21,376</td>
      <td>22,299</td>
      <td>2574</td>
    </tr>
    <tr>
      <th>9</th>
      <td>세종</td>
      <td>8,750</td>
      <td>8,860</td>
      <td>9,135</td>
      <td>10,382</td>
      <td>1631</td>
    </tr>
    <tr>
      <th>10</th>
      <td>울산</td>
      <td>10,053</td>
      <td>10,209</td>
      <td>11,345</td>
      <td>10,441</td>
      <td>387</td>
    </tr>
    <tr>
      <th>11</th>
      <td>인천</td>
      <td>10,484</td>
      <td>10,532</td>
      <td>10,737</td>
      <td>11,218</td>
      <td>734</td>
    </tr>
    <tr>
      <th>12</th>
      <td>전남</td>
      <td>6,317</td>
      <td>6,489</td>
      <td>7,188</td>
      <td>7,794</td>
      <td>1476</td>
    </tr>
    <tr>
      <th>13</th>
      <td>전북</td>
      <td>6,703</td>
      <td>6,418</td>
      <td>7,058</td>
      <td>7,552</td>
      <td>848</td>
    </tr>
    <tr>
      <th>14</th>
      <td>제주</td>
      <td>7,405</td>
      <td>9,129</td>
      <td>10,831</td>
      <td>12,741</td>
      <td>5335</td>
    </tr>
    <tr>
      <th>15</th>
      <td>충남</td>
      <td>7,115</td>
      <td>7,331</td>
      <td>7,456</td>
      <td>7,973</td>
      <td>857</td>
    </tr>
    <tr>
      <th>16</th>
      <td>충북</td>
      <td>6,645</td>
      <td>6,770</td>
      <td>6,763</td>
      <td>7,893</td>
      <td>1247</td>
    </tr>
  </tbody>
</table>
</div>



# 연도별 변동 그래프


```python
(ggplot(region_year_all, aes(x='지역명', y='평당분양가격', fill='연도'))
 + geom_bar(stat='identity', position='dodge')
 + theme(text=element_text(family='NanumBarunGothic'))
)
```

    C:\Users\rlath\Anaconda3\lib\site-packages\plotnine\layer.py:450: UserWarning: geom_bar : Removed 17 rows containing missing values.
      self.data = self.geom.handle_na(self.data)



![png](./Photo/output_\d\d_\d\d?\.png)





    <ggplot: (96008302428)>



## 지역별 평당 분양가격 합계
* 아래 데이터로 어느정도 규모로 분양사업이 이루어졌는지를 봅니다.
* 전체 데이터로 봤을 때 서울, 경기, 부산, 제주에 분양 사업이 다른 지역에 비해 규모가 큰 것으로 보여지지만 분양가격대비로 나눠볼 필요가 있습니다.


```python
pre_sale.pivot_table('평당분양가격', '규모구분', '지역명')
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
      <th>지역명</th>
      <th>강원</th>
      <th>경기</th>
      <th>경남</th>
      <th>경북</th>
      <th>광주</th>
      <th>대구</th>
      <th>대전</th>
      <th>부산</th>
      <th>서울</th>
      <th>세종</th>
      <th>울산</th>
      <th>인천</th>
      <th>전남</th>
      <th>전북</th>
      <th>제주</th>
      <th>충남</th>
      <th>충북</th>
    </tr>
    <tr>
      <th>규모구분</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>전용면적 102㎡초과</th>
      <td>7,871</td>
      <td>13,601</td>
      <td>9,222</td>
      <td>8,586</td>
      <td>10,381</td>
      <td>12,303</td>
      <td>14,282</td>
      <td>12,584</td>
      <td>22,035</td>
      <td>9,259</td>
      <td>9,974</td>
      <td>13,836</td>
      <td>7,550</td>
      <td>7,793</td>
      <td>10,435</td>
      <td>8,477</td>
      <td>7,900</td>
    </tr>
    <tr>
      <th>전용면적 60㎡이하</th>
      <td>7,185</td>
      <td>12,300</td>
      <td>8,320</td>
      <td>7,646</td>
      <td>8,494</td>
      <td>11,254</td>
      <td>8,816</td>
      <td>10,656</td>
      <td>21,976</td>
      <td>9,071</td>
      <td>8,965</td>
      <td>10,853</td>
      <td>6,980</td>
      <td>7,184</td>
      <td>14,700</td>
      <td>7,772</td>
      <td>6,951</td>
    </tr>
    <tr>
      <th>전용면적 60㎡초과 85㎡이하</th>
      <td>7,216</td>
      <td>11,650</td>
      <td>8,088</td>
      <td>7,657</td>
      <td>9,159</td>
      <td>10,889</td>
      <td>8,779</td>
      <td>11,135</td>
      <td>20,718</td>
      <td>9,237</td>
      <td>10,651</td>
      <td>10,719</td>
      <td>6,943</td>
      <td>6,868</td>
      <td>9,908</td>
      <td>7,484</td>
      <td>7,019</td>
    </tr>
    <tr>
      <th>전용면적 85㎡초과 102㎡이하</th>
      <td>7,612</td>
      <td>12,029</td>
      <td>9,834</td>
      <td>8,776</td>
      <td>9,296</td>
      <td>9,497</td>
      <td>9,037</td>
      <td>10,971</td>
      <td>23,714</td>
      <td>9,210</td>
      <td>8,861</td>
      <td>11,286</td>
      <td>7,858</td>
      <td>7,739</td>
      <td>10,744</td>
      <td>9,102</td>
      <td>8,145</td>
    </tr>
    <tr>
      <th>전체</th>
      <td>7,183</td>
      <td>11,664</td>
      <td>8,113</td>
      <td>7,661</td>
      <td>9,151</td>
      <td>10,854</td>
      <td>8,854</td>
      <td>11,241</td>
      <td>21,127</td>
      <td>9,230</td>
      <td>10,628</td>
      <td>10,727</td>
      <td>6,958</td>
      <td>6,877</td>
      <td>10,230</td>
      <td>7,474</td>
      <td>6,966</td>
    </tr>
  </tbody>
</table>
</div>



## 규모별


```python
# 서울의 경우 전용면적 85㎡초과 102㎡이하가 분양가격이 가장 비싸게 나옵니다.
(ggplot(pre_sale, aes(x='지역명', y='평당분양가격', fill='규모구분'))
 + geom_bar(stat='identity', position='dodge')
 + theme(text=element_text(family='NanumBarunGothic'))
)
```

    C:\Users\rlath\Anaconda3\lib\site-packages\plotnine\layer.py:450: UserWarning: geom_bar : Removed 223 rows containing missing values.
      self.data = self.geom.handle_na(self.data)



![png](./Photo/output_\d\d_\d\d?\.png)





    <ggplot: (-9223371940846455110)>




```python
# 위에 그린 그래프를 지역별로 나눠 봅니다.
(ggplot(pre_sale)
 + aes(x='연도', y='평당분양가격', fill='규모구분')
 + geom_bar(stat='identity', position='dodge')
 + facet_wrap('지역명')
 + theme(text=element_text(family='NanumBarunGothic'),
         axis_text_x=element_text(rotation=70),
         figure_size=(12, 6))
)
```

    C:\Users\rlath\Anaconda3\lib\site-packages\plotnine\layer.py:450: UserWarning: geom_bar : Removed 223 rows containing missing values.
      self.data = self.geom.handle_na(self.data)



![png](./Photo/output_\d\d_\d\d?\.png)





    <ggplot: (-9223371940846290586)>




```python
# 박스플롯을 그려봅니다.
(ggplot(pre_sale, aes(x='지역명', y='평당분양가격', fill='규모구분'))
 + geom_boxplot()
 + theme(text=element_text(family='NanumBarunGothic'),
         figure_size=(12, 6))
)
```

    C:\Users\rlath\Anaconda3\lib\site-packages\plotnine\layer.py:363: UserWarning: stat_boxplot : Removed 223 rows containing non-finite values.
      data = self.stat.compute_layer(data, params, layout)



![png](./Photo/output_\d\d_\d\d?\.png)





    <ggplot: (-9223371940848684533)>




```python
pre_sale_seoul = pre_sale.loc[pre_sale['지역명']=='서울']
(ggplot(pre_sale_seoul)
 + aes(x='연도', y='평당분양가격', fill='규모구분')
 + geom_boxplot()
 + theme(text=element_text(family='NanumBarunGothic'))
)
```

    C:\Users\rlath\Anaconda3\lib\site-packages\plotnine\layer.py:363: UserWarning: stat_boxplot : Removed 5 rows containing non-finite values.
      data = self.stat.compute_layer(data, params, layout)



![png](./Photo/output_\d\d_\d\d?\.png)





    <ggplot: (96006107684)>




```python
# 2015년에서 2018년까지 분양가 차이가 가장 컸던 제주를 봅니다.
(ggplot(pre_sale.loc[pre_sale['지역명']=='제주'])
 + aes(x='연도', y='평당분양가격', fill='규모구분')
 + geom_boxplot()
 + theme(text=element_text(family='NanumBarunGothic'))
)
```

    C:\Users\rlath\Anaconda3\lib\site-packages\plotnine\layer.py:363: UserWarning: stat_boxplot : Removed 24 rows containing non-finite values.
      data = self.stat.compute_layer(data, params, layout)



![png](./Photo/output_\d\d_\d\d?\.png)





    <ggplot: (-9223371940848667981)>




```python
# 2015년에서 2018년까지 분양가 차이가 가장 작았던 울산을 봅니다.
(ggplot(pre_sale.loc[pre_sale['지역명']=='울산'])
 + aes(x='연도', y='평당분양가격', fill='규모구분')
 + geom_boxplot()
 + theme(text=element_text(family='NanumBarunGothic'))
)
```

    C:\Users\rlath\Anaconda3\lib\site-packages\plotnine\layer.py:363: UserWarning: stat_boxplot : Removed 38 rows containing non-finite values.
      data = self.stat.compute_layer(data, params, layout)



![png](./Photo/output_\d\d_\d\d?\.png)





    <ggplot: (-9223371940846370430)>



# 2013년 12월~2015년 9월 3.3㎡당 분양가격
* 2015년 10월부터 2018년 4월까지 데이터는 평당 분양가로 조정을 해주었었는데 이 데이터는 평당 분양가가 들어가 있다.


```python
df = pd.read_csv('Data/180810_open_data_apt_2013_2015.csv', \
                 encoding='euc-kr', skiprows=1, header=0)
df.shape
```




    (23, 27)




```python
# pandas에서 보기 쉽게 컬럼을 변경해 줄 필요가 있다.
df
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
      <th>Unnamed: 0</th>
      <th>Unnamed: 1</th>
      <th>Unnamed: 2</th>
      <th>Unnamed: 3</th>
      <th>Unnamed: 4</th>
      <th>Unnamed: 5</th>
      <th>Unnamed: 6</th>
      <th>Unnamed: 7</th>
      <th>Unnamed: 8</th>
      <th>Unnamed: 9</th>
      <th>...</th>
      <th>Unnamed: 17</th>
      <th>Unnamed: 18</th>
      <th>Unnamed: 19</th>
      <th>Unnamed: 20</th>
      <th>Unnamed: 21</th>
      <th>Unnamed: 22</th>
      <th>Unnamed: 23</th>
      <th>Unnamed: 24</th>
      <th>Unnamed: 25</th>
      <th>Unnamed: 26</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>구분</td>
      <td>NaN</td>
      <td>2013년</td>
      <td>2014년</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>(단위: 천원/3.3㎡)</td>
    </tr>
    <tr>
      <th>1</th>
      <td>시도</td>
      <td>시군구</td>
      <td>12월</td>
      <td>1월</td>
      <td>2월</td>
      <td>3월</td>
      <td>4월</td>
      <td>5월</td>
      <td>6월</td>
      <td>7월</td>
      <td>...</td>
      <td>3월</td>
      <td>4월</td>
      <td>5월</td>
      <td>6월</td>
      <td>7월</td>
      <td>8월</td>
      <td>9월</td>
      <td>전월비</td>
      <td>전년말비</td>
      <td>전년동월비</td>
    </tr>
    <tr>
      <th>2</th>
      <td>전국</td>
      <td>NaN</td>
      <td>8,059</td>
      <td>8,130</td>
      <td>8,195</td>
      <td>8,204</td>
      <td>8,289</td>
      <td>8,358</td>
      <td>8,344</td>
      <td>8,333</td>
      <td>...</td>
      <td>8,563</td>
      <td>8,613</td>
      <td>8,624</td>
      <td>8,627</td>
      <td>8,643</td>
      <td>8,678</td>
      <td>8,665</td>
      <td>-13</td>
      <td>82</td>
      <td>207</td>
    </tr>
    <tr>
      <th>3</th>
      <td>서울</td>
      <td>NaN</td>
      <td>18,189</td>
      <td>17,925</td>
      <td>17,925</td>
      <td>18,016</td>
      <td>18,098</td>
      <td>19,446</td>
      <td>18,867</td>
      <td>18,742</td>
      <td>...</td>
      <td>19,415</td>
      <td>18,842</td>
      <td>18,367</td>
      <td>18,374</td>
      <td>18,152</td>
      <td>18,443</td>
      <td>17,969</td>
      <td>-474</td>
      <td>-2,300</td>
      <td>-1,434</td>
    </tr>
    <tr>
      <th>4</th>
      <td>6대광역시</td>
      <td>부산</td>
      <td>8,111</td>
      <td>8,111</td>
      <td>9,078</td>
      <td>8,965</td>
      <td>9,402</td>
      <td>9,501</td>
      <td>9,453</td>
      <td>9,457</td>
      <td>...</td>
      <td>9,279</td>
      <td>9,327</td>
      <td>9,345</td>
      <td>9,515</td>
      <td>9,559</td>
      <td>9,581</td>
      <td>9,608</td>
      <td>1</td>
      <td>430</td>
      <td>477</td>
    </tr>
    <tr>
      <th>5</th>
      <td>NaN</td>
      <td>대구</td>
      <td>8,080</td>
      <td>8,080</td>
      <td>8,077</td>
      <td>8,101</td>
      <td>8,267</td>
      <td>8,274</td>
      <td>8,360</td>
      <td>8,360</td>
      <td>...</td>
      <td>8,441</td>
      <td>8,446</td>
      <td>8,568</td>
      <td>8,542</td>
      <td>8,542</td>
      <td>8,795</td>
      <td>8,863</td>
      <td>27</td>
      <td>400</td>
      <td>350</td>
    </tr>
    <tr>
      <th>6</th>
      <td>NaN</td>
      <td>인천</td>
      <td>10,204</td>
      <td>10,204</td>
      <td>10,408</td>
      <td>10,408</td>
      <td>10,000</td>
      <td>9,844</td>
      <td>10,058</td>
      <td>9,974</td>
      <td>...</td>
      <td>9,876</td>
      <td>9,938</td>
      <td>10,551</td>
      <td>10,443</td>
      <td>10,443</td>
      <td>10,449</td>
      <td>10,450</td>
      <td>-162</td>
      <td>-150</td>
      <td>-131</td>
    </tr>
    <tr>
      <th>7</th>
      <td>NaN</td>
      <td>광주</td>
      <td>6,098</td>
      <td>7,326</td>
      <td>7,611</td>
      <td>7,346</td>
      <td>7,346</td>
      <td>7,523</td>
      <td>7,659</td>
      <td>7,612</td>
      <td>...</td>
      <td>7,861</td>
      <td>7,914</td>
      <td>7,877</td>
      <td>7,881</td>
      <td>8,089</td>
      <td>8,231</td>
      <td>8,083</td>
      <td>-148</td>
      <td>334</td>
      <td>281</td>
    </tr>
    <tr>
      <th>8</th>
      <td>NaN</td>
      <td>대전</td>
      <td>8,321</td>
      <td>8,321</td>
      <td>8,321</td>
      <td>8,341</td>
      <td>8,341</td>
      <td>8,341</td>
      <td>8,333</td>
      <td>8,333</td>
      <td>...</td>
      <td>8,067</td>
      <td>8,145</td>
      <td>8,272</td>
      <td>8,079</td>
      <td>8,079</td>
      <td>8,079</td>
      <td>7,917</td>
      <td>68</td>
      <td>610</td>
      <td>414</td>
    </tr>
    <tr>
      <th>9</th>
      <td>NaN</td>
      <td>울산</td>
      <td>8,090</td>
      <td>8,090</td>
      <td>8,090</td>
      <td>8,153</td>
      <td>8,153</td>
      <td>8,153</td>
      <td>8,153</td>
      <td>8,153</td>
      <td>...</td>
      <td>8,629</td>
      <td>9,380</td>
      <td>9,192</td>
      <td>9,190</td>
      <td>9,190</td>
      <td>9,215</td>
      <td>9,215</td>
      <td>0</td>
      <td>324</td>
      <td>722</td>
    </tr>
    <tr>
      <th>10</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>8,151</td>
      <td>8,355</td>
      <td>8,597</td>
      <td>8,552</td>
      <td>8,585</td>
      <td>8,606</td>
      <td>8,669</td>
      <td>8,648</td>
      <td>...</td>
      <td>8,692</td>
      <td>8,858</td>
      <td>8,967</td>
      <td>8,942</td>
      <td>8,984</td>
      <td>9,058</td>
      <td>9,023</td>
      <td>-36</td>
      <td>325</td>
      <td>352</td>
    </tr>
    <tr>
      <th>11</th>
      <td>경기</td>
      <td>NaN</td>
      <td>10,855</td>
      <td>10,855</td>
      <td>10,791</td>
      <td>10,784</td>
      <td>10,876</td>
      <td>10,646</td>
      <td>10,266</td>
      <td>10,124</td>
      <td>...</td>
      <td>10,469</td>
      <td>10,684</td>
      <td>10,685</td>
      <td>10,573</td>
      <td>10,518</td>
      <td>10,573</td>
      <td>10,341</td>
      <td>-232</td>
      <td>-38</td>
      <td>-160</td>
    </tr>
    <tr>
      <th>12</th>
      <td>수도권</td>
      <td>NaN</td>
      <td>13,083</td>
      <td>12,995</td>
      <td>13,041</td>
      <td>13,069</td>
      <td>12,991</td>
      <td>13,312</td>
      <td>13,064</td>
      <td>12,947</td>
      <td>...</td>
      <td>13,253</td>
      <td>13,155</td>
      <td>13,201</td>
      <td>13,130</td>
      <td>13,038</td>
      <td>13,155</td>
      <td>12,920</td>
      <td>-235</td>
      <td>-636</td>
      <td>-373</td>
    </tr>
    <tr>
      <th>13</th>
      <td>세종</td>
      <td>NaN</td>
      <td>7,601</td>
      <td>7,600</td>
      <td>7,532</td>
      <td>7,814</td>
      <td>7,908</td>
      <td>7,934</td>
      <td>8,067</td>
      <td>8,067</td>
      <td>...</td>
      <td>8,555</td>
      <td>8,546</td>
      <td>8,546</td>
      <td>8,671</td>
      <td>8,669</td>
      <td>8,695</td>
      <td>8,715</td>
      <td>20</td>
      <td>155</td>
      <td>434</td>
    </tr>
    <tr>
      <th>14</th>
      <td>지방</td>
      <td>강원</td>
      <td>6,230</td>
      <td>6,230</td>
      <td>6,230</td>
      <td>6,141</td>
      <td>6,373</td>
      <td>6,350</td>
      <td>6,350</td>
      <td>6,268</td>
      <td>...</td>
      <td>6,182</td>
      <td>6,924</td>
      <td>6,846</td>
      <td>6,986</td>
      <td>7,019</td>
      <td>7,008</td>
      <td>7,121</td>
      <td>113</td>
      <td>756</td>
      <td>702</td>
    </tr>
    <tr>
      <th>15</th>
      <td>NaN</td>
      <td>충북</td>
      <td>6,589</td>
      <td>6,589</td>
      <td>6,611</td>
      <td>6,625</td>
      <td>6,678</td>
      <td>6,598</td>
      <td>6,587</td>
      <td>6,586</td>
      <td>...</td>
      <td>6,783</td>
      <td>6,790</td>
      <td>6,805</td>
      <td>6,682</td>
      <td>6,601</td>
      <td>6,603</td>
      <td>6,606</td>
      <td>3</td>
      <td>-137</td>
      <td>22</td>
    </tr>
    <tr>
      <th>16</th>
      <td>NaN</td>
      <td>충남</td>
      <td>6,365</td>
      <td>6,365</td>
      <td>6,379</td>
      <td>6,287</td>
      <td>6,552</td>
      <td>6,591</td>
      <td>6,644</td>
      <td>6,805</td>
      <td>...</td>
      <td>7,161</td>
      <td>7,017</td>
      <td>6,975</td>
      <td>6,939</td>
      <td>6,935</td>
      <td>6,942</td>
      <td>6,939</td>
      <td>-3</td>
      <td>-50</td>
      <td>57</td>
    </tr>
    <tr>
      <th>17</th>
      <td>NaN</td>
      <td>전북</td>
      <td>6,282</td>
      <td>6,281</td>
      <td>5,946</td>
      <td>5,966</td>
      <td>6,277</td>
      <td>6,306</td>
      <td>6,351</td>
      <td>6,319</td>
      <td>...</td>
      <td>6,542</td>
      <td>6,551</td>
      <td>6,556</td>
      <td>6,601</td>
      <td>6,750</td>
      <td>6,580</td>
      <td>6,885</td>
      <td>304</td>
      <td>301</td>
      <td>165</td>
    </tr>
    <tr>
      <th>18</th>
      <td>NaN</td>
      <td>전남</td>
      <td>5,678</td>
      <td>5,678</td>
      <td>5,678</td>
      <td>5,696</td>
      <td>5,736</td>
      <td>5,656</td>
      <td>5,609</td>
      <td>5,780</td>
      <td>...</td>
      <td>5,825</td>
      <td>5,940</td>
      <td>6,050</td>
      <td>6,243</td>
      <td>6,286</td>
      <td>6,289</td>
      <td>6,245</td>
      <td>-43</td>
      <td>461</td>
      <td>441</td>
    </tr>
    <tr>
      <th>19</th>
      <td>NaN</td>
      <td>경북</td>
      <td>6,168</td>
      <td>6,168</td>
      <td>6,234</td>
      <td>6,317</td>
      <td>6,412</td>
      <td>6,409</td>
      <td>6,554</td>
      <td>6,556</td>
      <td>...</td>
      <td>6,997</td>
      <td>7,006</td>
      <td>6,966</td>
      <td>6,887</td>
      <td>7,035</td>
      <td>7,037</td>
      <td>7,029</td>
      <td>-9</td>
      <td>39</td>
      <td>451</td>
    </tr>
    <tr>
      <th>20</th>
      <td>NaN</td>
      <td>경남</td>
      <td>6,473</td>
      <td>6,485</td>
      <td>6,502</td>
      <td>6,610</td>
      <td>6,599</td>
      <td>6,610</td>
      <td>6,615</td>
      <td>6,613</td>
      <td>...</td>
      <td>7,668</td>
      <td>7,683</td>
      <td>7,717</td>
      <td>7,715</td>
      <td>7,723</td>
      <td>7,665</td>
      <td>7,947</td>
      <td>282</td>
      <td>615</td>
      <td>1,179</td>
    </tr>
    <tr>
      <th>21</th>
      <td>NaN</td>
      <td>제주</td>
      <td>7,674</td>
      <td>7,900</td>
      <td>7,900</td>
      <td>7,900</td>
      <td>7,900</td>
      <td>7,900</td>
      <td>7,914</td>
      <td>7,914</td>
      <td>...</td>
      <td>7,826</td>
      <td>7,285</td>
      <td>7,285</td>
      <td>7,343</td>
      <td>7,343</td>
      <td>7,343</td>
      <td>7,379</td>
      <td>36</td>
      <td>-360</td>
      <td>-453</td>
    </tr>
    <tr>
      <th>22</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>6,432</td>
      <td>6,462</td>
      <td>6,435</td>
      <td>6,443</td>
      <td>6,566</td>
      <td>6,552</td>
      <td>6,578</td>
      <td>6,605</td>
      <td>...</td>
      <td>6,873</td>
      <td>6,899</td>
      <td>6,900</td>
      <td>6,925</td>
      <td>6,961</td>
      <td>6,933</td>
      <td>7,019</td>
      <td>85</td>
      <td>203</td>
      <td>321</td>
    </tr>
  </tbody>
</table>
<p>23 rows × 27 columns</p>
</div>




```python
year = df.iloc[0]
month = df.iloc[1]
```


```python
# 결측치를 채워준다.
year
```




    Unnamed: 0                구분
    Unnamed: 1               NaN
    Unnamed: 2             2013년
    Unnamed: 3             2014년
    Unnamed: 4               NaN
    Unnamed: 5               NaN
    Unnamed: 6               NaN
    Unnamed: 7               NaN
    Unnamed: 8               NaN
    Unnamed: 9               NaN
    Unnamed: 10              NaN
    Unnamed: 11              NaN
    Unnamed: 12              NaN
    Unnamed: 13              NaN
    Unnamed: 14              NaN
    Unnamed: 15            2015년
    Unnamed: 16              NaN
    Unnamed: 17              NaN
    Unnamed: 18              NaN
    Unnamed: 19              NaN
    Unnamed: 20              NaN
    Unnamed: 21              NaN
    Unnamed: 22              NaN
    Unnamed: 23              NaN
    Unnamed: 24              NaN
    Unnamed: 25              NaN
    Unnamed: 26    (단위: 천원/3.3㎡)
    Name: 0, dtype: object




```python
df
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
      <th>Unnamed: 0</th>
      <th>Unnamed: 1</th>
      <th>Unnamed: 2</th>
      <th>Unnamed: 3</th>
      <th>Unnamed: 4</th>
      <th>Unnamed: 5</th>
      <th>Unnamed: 6</th>
      <th>Unnamed: 7</th>
      <th>Unnamed: 8</th>
      <th>Unnamed: 9</th>
      <th>...</th>
      <th>Unnamed: 17</th>
      <th>Unnamed: 18</th>
      <th>Unnamed: 19</th>
      <th>Unnamed: 20</th>
      <th>Unnamed: 21</th>
      <th>Unnamed: 22</th>
      <th>Unnamed: 23</th>
      <th>Unnamed: 24</th>
      <th>Unnamed: 25</th>
      <th>Unnamed: 26</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>구분</td>
      <td>NaN</td>
      <td>2013년</td>
      <td>2014년</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>(단위: 천원/3.3㎡)</td>
    </tr>
    <tr>
      <th>1</th>
      <td>시도</td>
      <td>시군구</td>
      <td>12월</td>
      <td>1월</td>
      <td>2월</td>
      <td>3월</td>
      <td>4월</td>
      <td>5월</td>
      <td>6월</td>
      <td>7월</td>
      <td>...</td>
      <td>3월</td>
      <td>4월</td>
      <td>5월</td>
      <td>6월</td>
      <td>7월</td>
      <td>8월</td>
      <td>9월</td>
      <td>전월비</td>
      <td>전년말비</td>
      <td>전년동월비</td>
    </tr>
    <tr>
      <th>2</th>
      <td>전국</td>
      <td>NaN</td>
      <td>8,059</td>
      <td>8,130</td>
      <td>8,195</td>
      <td>8,204</td>
      <td>8,289</td>
      <td>8,358</td>
      <td>8,344</td>
      <td>8,333</td>
      <td>...</td>
      <td>8,563</td>
      <td>8,613</td>
      <td>8,624</td>
      <td>8,627</td>
      <td>8,643</td>
      <td>8,678</td>
      <td>8,665</td>
      <td>-13</td>
      <td>82</td>
      <td>207</td>
    </tr>
    <tr>
      <th>3</th>
      <td>서울</td>
      <td>NaN</td>
      <td>18,189</td>
      <td>17,925</td>
      <td>17,925</td>
      <td>18,016</td>
      <td>18,098</td>
      <td>19,446</td>
      <td>18,867</td>
      <td>18,742</td>
      <td>...</td>
      <td>19,415</td>
      <td>18,842</td>
      <td>18,367</td>
      <td>18,374</td>
      <td>18,152</td>
      <td>18,443</td>
      <td>17,969</td>
      <td>-474</td>
      <td>-2,300</td>
      <td>-1,434</td>
    </tr>
    <tr>
      <th>4</th>
      <td>6대광역시</td>
      <td>부산</td>
      <td>8,111</td>
      <td>8,111</td>
      <td>9,078</td>
      <td>8,965</td>
      <td>9,402</td>
      <td>9,501</td>
      <td>9,453</td>
      <td>9,457</td>
      <td>...</td>
      <td>9,279</td>
      <td>9,327</td>
      <td>9,345</td>
      <td>9,515</td>
      <td>9,559</td>
      <td>9,581</td>
      <td>9,608</td>
      <td>1</td>
      <td>430</td>
      <td>477</td>
    </tr>
    <tr>
      <th>5</th>
      <td>NaN</td>
      <td>대구</td>
      <td>8,080</td>
      <td>8,080</td>
      <td>8,077</td>
      <td>8,101</td>
      <td>8,267</td>
      <td>8,274</td>
      <td>8,360</td>
      <td>8,360</td>
      <td>...</td>
      <td>8,441</td>
      <td>8,446</td>
      <td>8,568</td>
      <td>8,542</td>
      <td>8,542</td>
      <td>8,795</td>
      <td>8,863</td>
      <td>27</td>
      <td>400</td>
      <td>350</td>
    </tr>
    <tr>
      <th>6</th>
      <td>NaN</td>
      <td>인천</td>
      <td>10,204</td>
      <td>10,204</td>
      <td>10,408</td>
      <td>10,408</td>
      <td>10,000</td>
      <td>9,844</td>
      <td>10,058</td>
      <td>9,974</td>
      <td>...</td>
      <td>9,876</td>
      <td>9,938</td>
      <td>10,551</td>
      <td>10,443</td>
      <td>10,443</td>
      <td>10,449</td>
      <td>10,450</td>
      <td>-162</td>
      <td>-150</td>
      <td>-131</td>
    </tr>
    <tr>
      <th>7</th>
      <td>NaN</td>
      <td>광주</td>
      <td>6,098</td>
      <td>7,326</td>
      <td>7,611</td>
      <td>7,346</td>
      <td>7,346</td>
      <td>7,523</td>
      <td>7,659</td>
      <td>7,612</td>
      <td>...</td>
      <td>7,861</td>
      <td>7,914</td>
      <td>7,877</td>
      <td>7,881</td>
      <td>8,089</td>
      <td>8,231</td>
      <td>8,083</td>
      <td>-148</td>
      <td>334</td>
      <td>281</td>
    </tr>
    <tr>
      <th>8</th>
      <td>NaN</td>
      <td>대전</td>
      <td>8,321</td>
      <td>8,321</td>
      <td>8,321</td>
      <td>8,341</td>
      <td>8,341</td>
      <td>8,341</td>
      <td>8,333</td>
      <td>8,333</td>
      <td>...</td>
      <td>8,067</td>
      <td>8,145</td>
      <td>8,272</td>
      <td>8,079</td>
      <td>8,079</td>
      <td>8,079</td>
      <td>7,917</td>
      <td>68</td>
      <td>610</td>
      <td>414</td>
    </tr>
    <tr>
      <th>9</th>
      <td>NaN</td>
      <td>울산</td>
      <td>8,090</td>
      <td>8,090</td>
      <td>8,090</td>
      <td>8,153</td>
      <td>8,153</td>
      <td>8,153</td>
      <td>8,153</td>
      <td>8,153</td>
      <td>...</td>
      <td>8,629</td>
      <td>9,380</td>
      <td>9,192</td>
      <td>9,190</td>
      <td>9,190</td>
      <td>9,215</td>
      <td>9,215</td>
      <td>0</td>
      <td>324</td>
      <td>722</td>
    </tr>
    <tr>
      <th>10</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>8,151</td>
      <td>8,355</td>
      <td>8,597</td>
      <td>8,552</td>
      <td>8,585</td>
      <td>8,606</td>
      <td>8,669</td>
      <td>8,648</td>
      <td>...</td>
      <td>8,692</td>
      <td>8,858</td>
      <td>8,967</td>
      <td>8,942</td>
      <td>8,984</td>
      <td>9,058</td>
      <td>9,023</td>
      <td>-36</td>
      <td>325</td>
      <td>352</td>
    </tr>
    <tr>
      <th>11</th>
      <td>경기</td>
      <td>NaN</td>
      <td>10,855</td>
      <td>10,855</td>
      <td>10,791</td>
      <td>10,784</td>
      <td>10,876</td>
      <td>10,646</td>
      <td>10,266</td>
      <td>10,124</td>
      <td>...</td>
      <td>10,469</td>
      <td>10,684</td>
      <td>10,685</td>
      <td>10,573</td>
      <td>10,518</td>
      <td>10,573</td>
      <td>10,341</td>
      <td>-232</td>
      <td>-38</td>
      <td>-160</td>
    </tr>
    <tr>
      <th>12</th>
      <td>수도권</td>
      <td>NaN</td>
      <td>13,083</td>
      <td>12,995</td>
      <td>13,041</td>
      <td>13,069</td>
      <td>12,991</td>
      <td>13,312</td>
      <td>13,064</td>
      <td>12,947</td>
      <td>...</td>
      <td>13,253</td>
      <td>13,155</td>
      <td>13,201</td>
      <td>13,130</td>
      <td>13,038</td>
      <td>13,155</td>
      <td>12,920</td>
      <td>-235</td>
      <td>-636</td>
      <td>-373</td>
    </tr>
    <tr>
      <th>13</th>
      <td>세종</td>
      <td>NaN</td>
      <td>7,601</td>
      <td>7,600</td>
      <td>7,532</td>
      <td>7,814</td>
      <td>7,908</td>
      <td>7,934</td>
      <td>8,067</td>
      <td>8,067</td>
      <td>...</td>
      <td>8,555</td>
      <td>8,546</td>
      <td>8,546</td>
      <td>8,671</td>
      <td>8,669</td>
      <td>8,695</td>
      <td>8,715</td>
      <td>20</td>
      <td>155</td>
      <td>434</td>
    </tr>
    <tr>
      <th>14</th>
      <td>지방</td>
      <td>강원</td>
      <td>6,230</td>
      <td>6,230</td>
      <td>6,230</td>
      <td>6,141</td>
      <td>6,373</td>
      <td>6,350</td>
      <td>6,350</td>
      <td>6,268</td>
      <td>...</td>
      <td>6,182</td>
      <td>6,924</td>
      <td>6,846</td>
      <td>6,986</td>
      <td>7,019</td>
      <td>7,008</td>
      <td>7,121</td>
      <td>113</td>
      <td>756</td>
      <td>702</td>
    </tr>
    <tr>
      <th>15</th>
      <td>NaN</td>
      <td>충북</td>
      <td>6,589</td>
      <td>6,589</td>
      <td>6,611</td>
      <td>6,625</td>
      <td>6,678</td>
      <td>6,598</td>
      <td>6,587</td>
      <td>6,586</td>
      <td>...</td>
      <td>6,783</td>
      <td>6,790</td>
      <td>6,805</td>
      <td>6,682</td>
      <td>6,601</td>
      <td>6,603</td>
      <td>6,606</td>
      <td>3</td>
      <td>-137</td>
      <td>22</td>
    </tr>
    <tr>
      <th>16</th>
      <td>NaN</td>
      <td>충남</td>
      <td>6,365</td>
      <td>6,365</td>
      <td>6,379</td>
      <td>6,287</td>
      <td>6,552</td>
      <td>6,591</td>
      <td>6,644</td>
      <td>6,805</td>
      <td>...</td>
      <td>7,161</td>
      <td>7,017</td>
      <td>6,975</td>
      <td>6,939</td>
      <td>6,935</td>
      <td>6,942</td>
      <td>6,939</td>
      <td>-3</td>
      <td>-50</td>
      <td>57</td>
    </tr>
    <tr>
      <th>17</th>
      <td>NaN</td>
      <td>전북</td>
      <td>6,282</td>
      <td>6,281</td>
      <td>5,946</td>
      <td>5,966</td>
      <td>6,277</td>
      <td>6,306</td>
      <td>6,351</td>
      <td>6,319</td>
      <td>...</td>
      <td>6,542</td>
      <td>6,551</td>
      <td>6,556</td>
      <td>6,601</td>
      <td>6,750</td>
      <td>6,580</td>
      <td>6,885</td>
      <td>304</td>
      <td>301</td>
      <td>165</td>
    </tr>
    <tr>
      <th>18</th>
      <td>NaN</td>
      <td>전남</td>
      <td>5,678</td>
      <td>5,678</td>
      <td>5,678</td>
      <td>5,696</td>
      <td>5,736</td>
      <td>5,656</td>
      <td>5,609</td>
      <td>5,780</td>
      <td>...</td>
      <td>5,825</td>
      <td>5,940</td>
      <td>6,050</td>
      <td>6,243</td>
      <td>6,286</td>
      <td>6,289</td>
      <td>6,245</td>
      <td>-43</td>
      <td>461</td>
      <td>441</td>
    </tr>
    <tr>
      <th>19</th>
      <td>NaN</td>
      <td>경북</td>
      <td>6,168</td>
      <td>6,168</td>
      <td>6,234</td>
      <td>6,317</td>
      <td>6,412</td>
      <td>6,409</td>
      <td>6,554</td>
      <td>6,556</td>
      <td>...</td>
      <td>6,997</td>
      <td>7,006</td>
      <td>6,966</td>
      <td>6,887</td>
      <td>7,035</td>
      <td>7,037</td>
      <td>7,029</td>
      <td>-9</td>
      <td>39</td>
      <td>451</td>
    </tr>
    <tr>
      <th>20</th>
      <td>NaN</td>
      <td>경남</td>
      <td>6,473</td>
      <td>6,485</td>
      <td>6,502</td>
      <td>6,610</td>
      <td>6,599</td>
      <td>6,610</td>
      <td>6,615</td>
      <td>6,613</td>
      <td>...</td>
      <td>7,668</td>
      <td>7,683</td>
      <td>7,717</td>
      <td>7,715</td>
      <td>7,723</td>
      <td>7,665</td>
      <td>7,947</td>
      <td>282</td>
      <td>615</td>
      <td>1,179</td>
    </tr>
    <tr>
      <th>21</th>
      <td>NaN</td>
      <td>제주</td>
      <td>7,674</td>
      <td>7,900</td>
      <td>7,900</td>
      <td>7,900</td>
      <td>7,900</td>
      <td>7,900</td>
      <td>7,914</td>
      <td>7,914</td>
      <td>...</td>
      <td>7,826</td>
      <td>7,285</td>
      <td>7,285</td>
      <td>7,343</td>
      <td>7,343</td>
      <td>7,343</td>
      <td>7,379</td>
      <td>36</td>
      <td>-360</td>
      <td>-453</td>
    </tr>
    <tr>
      <th>22</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>6,432</td>
      <td>6,462</td>
      <td>6,435</td>
      <td>6,443</td>
      <td>6,566</td>
      <td>6,552</td>
      <td>6,578</td>
      <td>6,605</td>
      <td>...</td>
      <td>6,873</td>
      <td>6,899</td>
      <td>6,900</td>
      <td>6,925</td>
      <td>6,961</td>
      <td>6,933</td>
      <td>7,019</td>
      <td>85</td>
      <td>203</td>
      <td>321</td>
    </tr>
  </tbody>
</table>
<p>23 rows × 27 columns</p>
</div>




```python
# 컬럼을 새로 만들어 주기 위해 0번째와 1번째 행을 합쳐준다.
for i, y in enumerate(year):
    if i > 2 and i < 15:
        year[i] = '2014년 ' + month[i]
    elif i >= 15:
        year[i] = '2015년 ' + month[i]
    elif i == 2 :
        year[i] =  year[i] + ' ' + month[i]
    elif i == 1:
        year[i] = '시군구'

print(year)
```

    Unnamed: 0              구분
    Unnamed: 1             시군구
    Unnamed: 2       2013년 12월
    Unnamed: 3        2014년 1월
    Unnamed: 4        2014년 2월
    Unnamed: 5        2014년 3월
    Unnamed: 6        2014년 4월
    Unnamed: 7        2014년 5월
    Unnamed: 8        2014년 6월
    Unnamed: 9        2014년 7월
    Unnamed: 10       2014년 8월
    Unnamed: 11       2014년 9월
    Unnamed: 12      2014년 10월
    Unnamed: 13      2014년 11월
    Unnamed: 14      2014년 12월
    Unnamed: 15       2015년 1월
    Unnamed: 16       2015년 2월
    Unnamed: 17       2015년 3월
    Unnamed: 18       2015년 4월
    Unnamed: 19       2015년 5월
    Unnamed: 20       2015년 6월
    Unnamed: 21       2015년 7월
    Unnamed: 22       2015년 8월
    Unnamed: 23       2015년 9월
    Unnamed: 24      2015년 전월비
    Unnamed: 25     2015년 전년말비
    Unnamed: 26    2015년 전년동월비
    Name: 0, dtype: object



```python
df.columns = year
```


```python
df = df.drop(df.index[[0,1]])
df
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
      <th>구분</th>
      <th>시군구</th>
      <th>2013년 12월</th>
      <th>2014년 1월</th>
      <th>2014년 2월</th>
      <th>2014년 3월</th>
      <th>2014년 4월</th>
      <th>2014년 5월</th>
      <th>2014년 6월</th>
      <th>2014년 7월</th>
      <th>...</th>
      <th>2015년 3월</th>
      <th>2015년 4월</th>
      <th>2015년 5월</th>
      <th>2015년 6월</th>
      <th>2015년 7월</th>
      <th>2015년 8월</th>
      <th>2015년 9월</th>
      <th>2015년 전월비</th>
      <th>2015년 전년말비</th>
      <th>2015년 전년동월비</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2</th>
      <td>전국</td>
      <td>NaN</td>
      <td>8,059</td>
      <td>8,130</td>
      <td>8,195</td>
      <td>8,204</td>
      <td>8,289</td>
      <td>8,358</td>
      <td>8,344</td>
      <td>8,333</td>
      <td>...</td>
      <td>8,563</td>
      <td>8,613</td>
      <td>8,624</td>
      <td>8,627</td>
      <td>8,643</td>
      <td>8,678</td>
      <td>8,665</td>
      <td>-13</td>
      <td>82</td>
      <td>207</td>
    </tr>
    <tr>
      <th>3</th>
      <td>서울</td>
      <td>NaN</td>
      <td>18,189</td>
      <td>17,925</td>
      <td>17,925</td>
      <td>18,016</td>
      <td>18,098</td>
      <td>19,446</td>
      <td>18,867</td>
      <td>18,742</td>
      <td>...</td>
      <td>19,415</td>
      <td>18,842</td>
      <td>18,367</td>
      <td>18,374</td>
      <td>18,152</td>
      <td>18,443</td>
      <td>17,969</td>
      <td>-474</td>
      <td>-2,300</td>
      <td>-1,434</td>
    </tr>
    <tr>
      <th>4</th>
      <td>6대광역시</td>
      <td>부산</td>
      <td>8,111</td>
      <td>8,111</td>
      <td>9,078</td>
      <td>8,965</td>
      <td>9,402</td>
      <td>9,501</td>
      <td>9,453</td>
      <td>9,457</td>
      <td>...</td>
      <td>9,279</td>
      <td>9,327</td>
      <td>9,345</td>
      <td>9,515</td>
      <td>9,559</td>
      <td>9,581</td>
      <td>9,608</td>
      <td>1</td>
      <td>430</td>
      <td>477</td>
    </tr>
    <tr>
      <th>5</th>
      <td>NaN</td>
      <td>대구</td>
      <td>8,080</td>
      <td>8,080</td>
      <td>8,077</td>
      <td>8,101</td>
      <td>8,267</td>
      <td>8,274</td>
      <td>8,360</td>
      <td>8,360</td>
      <td>...</td>
      <td>8,441</td>
      <td>8,446</td>
      <td>8,568</td>
      <td>8,542</td>
      <td>8,542</td>
      <td>8,795</td>
      <td>8,863</td>
      <td>27</td>
      <td>400</td>
      <td>350</td>
    </tr>
    <tr>
      <th>6</th>
      <td>NaN</td>
      <td>인천</td>
      <td>10,204</td>
      <td>10,204</td>
      <td>10,408</td>
      <td>10,408</td>
      <td>10,000</td>
      <td>9,844</td>
      <td>10,058</td>
      <td>9,974</td>
      <td>...</td>
      <td>9,876</td>
      <td>9,938</td>
      <td>10,551</td>
      <td>10,443</td>
      <td>10,443</td>
      <td>10,449</td>
      <td>10,450</td>
      <td>-162</td>
      <td>-150</td>
      <td>-131</td>
    </tr>
    <tr>
      <th>7</th>
      <td>NaN</td>
      <td>광주</td>
      <td>6,098</td>
      <td>7,326</td>
      <td>7,611</td>
      <td>7,346</td>
      <td>7,346</td>
      <td>7,523</td>
      <td>7,659</td>
      <td>7,612</td>
      <td>...</td>
      <td>7,861</td>
      <td>7,914</td>
      <td>7,877</td>
      <td>7,881</td>
      <td>8,089</td>
      <td>8,231</td>
      <td>8,083</td>
      <td>-148</td>
      <td>334</td>
      <td>281</td>
    </tr>
    <tr>
      <th>8</th>
      <td>NaN</td>
      <td>대전</td>
      <td>8,321</td>
      <td>8,321</td>
      <td>8,321</td>
      <td>8,341</td>
      <td>8,341</td>
      <td>8,341</td>
      <td>8,333</td>
      <td>8,333</td>
      <td>...</td>
      <td>8,067</td>
      <td>8,145</td>
      <td>8,272</td>
      <td>8,079</td>
      <td>8,079</td>
      <td>8,079</td>
      <td>7,917</td>
      <td>68</td>
      <td>610</td>
      <td>414</td>
    </tr>
    <tr>
      <th>9</th>
      <td>NaN</td>
      <td>울산</td>
      <td>8,090</td>
      <td>8,090</td>
      <td>8,090</td>
      <td>8,153</td>
      <td>8,153</td>
      <td>8,153</td>
      <td>8,153</td>
      <td>8,153</td>
      <td>...</td>
      <td>8,629</td>
      <td>9,380</td>
      <td>9,192</td>
      <td>9,190</td>
      <td>9,190</td>
      <td>9,215</td>
      <td>9,215</td>
      <td>0</td>
      <td>324</td>
      <td>722</td>
    </tr>
    <tr>
      <th>10</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>8,151</td>
      <td>8,355</td>
      <td>8,597</td>
      <td>8,552</td>
      <td>8,585</td>
      <td>8,606</td>
      <td>8,669</td>
      <td>8,648</td>
      <td>...</td>
      <td>8,692</td>
      <td>8,858</td>
      <td>8,967</td>
      <td>8,942</td>
      <td>8,984</td>
      <td>9,058</td>
      <td>9,023</td>
      <td>-36</td>
      <td>325</td>
      <td>352</td>
    </tr>
    <tr>
      <th>11</th>
      <td>경기</td>
      <td>NaN</td>
      <td>10,855</td>
      <td>10,855</td>
      <td>10,791</td>
      <td>10,784</td>
      <td>10,876</td>
      <td>10,646</td>
      <td>10,266</td>
      <td>10,124</td>
      <td>...</td>
      <td>10,469</td>
      <td>10,684</td>
      <td>10,685</td>
      <td>10,573</td>
      <td>10,518</td>
      <td>10,573</td>
      <td>10,341</td>
      <td>-232</td>
      <td>-38</td>
      <td>-160</td>
    </tr>
    <tr>
      <th>12</th>
      <td>수도권</td>
      <td>NaN</td>
      <td>13,083</td>
      <td>12,995</td>
      <td>13,041</td>
      <td>13,069</td>
      <td>12,991</td>
      <td>13,312</td>
      <td>13,064</td>
      <td>12,947</td>
      <td>...</td>
      <td>13,253</td>
      <td>13,155</td>
      <td>13,201</td>
      <td>13,130</td>
      <td>13,038</td>
      <td>13,155</td>
      <td>12,920</td>
      <td>-235</td>
      <td>-636</td>
      <td>-373</td>
    </tr>
    <tr>
      <th>13</th>
      <td>세종</td>
      <td>NaN</td>
      <td>7,601</td>
      <td>7,600</td>
      <td>7,532</td>
      <td>7,814</td>
      <td>7,908</td>
      <td>7,934</td>
      <td>8,067</td>
      <td>8,067</td>
      <td>...</td>
      <td>8,555</td>
      <td>8,546</td>
      <td>8,546</td>
      <td>8,671</td>
      <td>8,669</td>
      <td>8,695</td>
      <td>8,715</td>
      <td>20</td>
      <td>155</td>
      <td>434</td>
    </tr>
    <tr>
      <th>14</th>
      <td>지방</td>
      <td>강원</td>
      <td>6,230</td>
      <td>6,230</td>
      <td>6,230</td>
      <td>6,141</td>
      <td>6,373</td>
      <td>6,350</td>
      <td>6,350</td>
      <td>6,268</td>
      <td>...</td>
      <td>6,182</td>
      <td>6,924</td>
      <td>6,846</td>
      <td>6,986</td>
      <td>7,019</td>
      <td>7,008</td>
      <td>7,121</td>
      <td>113</td>
      <td>756</td>
      <td>702</td>
    </tr>
    <tr>
      <th>15</th>
      <td>NaN</td>
      <td>충북</td>
      <td>6,589</td>
      <td>6,589</td>
      <td>6,611</td>
      <td>6,625</td>
      <td>6,678</td>
      <td>6,598</td>
      <td>6,587</td>
      <td>6,586</td>
      <td>...</td>
      <td>6,783</td>
      <td>6,790</td>
      <td>6,805</td>
      <td>6,682</td>
      <td>6,601</td>
      <td>6,603</td>
      <td>6,606</td>
      <td>3</td>
      <td>-137</td>
      <td>22</td>
    </tr>
    <tr>
      <th>16</th>
      <td>NaN</td>
      <td>충남</td>
      <td>6,365</td>
      <td>6,365</td>
      <td>6,379</td>
      <td>6,287</td>
      <td>6,552</td>
      <td>6,591</td>
      <td>6,644</td>
      <td>6,805</td>
      <td>...</td>
      <td>7,161</td>
      <td>7,017</td>
      <td>6,975</td>
      <td>6,939</td>
      <td>6,935</td>
      <td>6,942</td>
      <td>6,939</td>
      <td>-3</td>
      <td>-50</td>
      <td>57</td>
    </tr>
    <tr>
      <th>17</th>
      <td>NaN</td>
      <td>전북</td>
      <td>6,282</td>
      <td>6,281</td>
      <td>5,946</td>
      <td>5,966</td>
      <td>6,277</td>
      <td>6,306</td>
      <td>6,351</td>
      <td>6,319</td>
      <td>...</td>
      <td>6,542</td>
      <td>6,551</td>
      <td>6,556</td>
      <td>6,601</td>
      <td>6,750</td>
      <td>6,580</td>
      <td>6,885</td>
      <td>304</td>
      <td>301</td>
      <td>165</td>
    </tr>
    <tr>
      <th>18</th>
      <td>NaN</td>
      <td>전남</td>
      <td>5,678</td>
      <td>5,678</td>
      <td>5,678</td>
      <td>5,696</td>
      <td>5,736</td>
      <td>5,656</td>
      <td>5,609</td>
      <td>5,780</td>
      <td>...</td>
      <td>5,825</td>
      <td>5,940</td>
      <td>6,050</td>
      <td>6,243</td>
      <td>6,286</td>
      <td>6,289</td>
      <td>6,245</td>
      <td>-43</td>
      <td>461</td>
      <td>441</td>
    </tr>
    <tr>
      <th>19</th>
      <td>NaN</td>
      <td>경북</td>
      <td>6,168</td>
      <td>6,168</td>
      <td>6,234</td>
      <td>6,317</td>
      <td>6,412</td>
      <td>6,409</td>
      <td>6,554</td>
      <td>6,556</td>
      <td>...</td>
      <td>6,997</td>
      <td>7,006</td>
      <td>6,966</td>
      <td>6,887</td>
      <td>7,035</td>
      <td>7,037</td>
      <td>7,029</td>
      <td>-9</td>
      <td>39</td>
      <td>451</td>
    </tr>
    <tr>
      <th>20</th>
      <td>NaN</td>
      <td>경남</td>
      <td>6,473</td>
      <td>6,485</td>
      <td>6,502</td>
      <td>6,610</td>
      <td>6,599</td>
      <td>6,610</td>
      <td>6,615</td>
      <td>6,613</td>
      <td>...</td>
      <td>7,668</td>
      <td>7,683</td>
      <td>7,717</td>
      <td>7,715</td>
      <td>7,723</td>
      <td>7,665</td>
      <td>7,947</td>
      <td>282</td>
      <td>615</td>
      <td>1,179</td>
    </tr>
    <tr>
      <th>21</th>
      <td>NaN</td>
      <td>제주</td>
      <td>7,674</td>
      <td>7,900</td>
      <td>7,900</td>
      <td>7,900</td>
      <td>7,900</td>
      <td>7,900</td>
      <td>7,914</td>
      <td>7,914</td>
      <td>...</td>
      <td>7,826</td>
      <td>7,285</td>
      <td>7,285</td>
      <td>7,343</td>
      <td>7,343</td>
      <td>7,343</td>
      <td>7,379</td>
      <td>36</td>
      <td>-360</td>
      <td>-453</td>
    </tr>
    <tr>
      <th>22</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>6,432</td>
      <td>6,462</td>
      <td>6,435</td>
      <td>6,443</td>
      <td>6,566</td>
      <td>6,552</td>
      <td>6,578</td>
      <td>6,605</td>
      <td>...</td>
      <td>6,873</td>
      <td>6,899</td>
      <td>6,900</td>
      <td>6,925</td>
      <td>6,961</td>
      <td>6,933</td>
      <td>7,019</td>
      <td>85</td>
      <td>203</td>
      <td>321</td>
    </tr>
  </tbody>
</table>
<p>21 rows × 27 columns</p>
</div>




```python
# 지역 컬럼을 새로 만들어 시도와 시군구를 합쳐준다.
df['구분'] = df['구분'].fillna('')  #공백으로 만들어줌
df['시군구'] = df['시군구'].fillna('')
```


```python
df['지역'] = df['구분'] + df['시군구']
```


```python
df['지역']
```




    2          전국
    3          서울
    4     6대광역시부산
    5          대구
    6          인천
    7          광주
    8          대전
    9          울산
    10           
    11         경기
    12        수도권
    13         세종
    14       지방강원
    15         충북
    16         충남
    17         전북
    18         전남
    19         경북
    20         경남
    21         제주
    22           
    Name: 지역, dtype: object




```python
melt_columns = df.columns.copy()
melt_columns
```




    Index(['구분', '시군구', '2013년 12월', '2014년 1월', '2014년 2월', '2014년 3월',
           '2014년 4월', '2014년 5월', '2014년 6월', '2014년 7월', '2014년 8월', '2014년 9월',
           '2014년 10월', '2014년 11월', '2014년 12월', '2015년 1월', '2015년 2월',
           '2015년 3월', '2015년 4월', '2015년 5월', '2015년 6월', '2015년 7월', '2015년 8월',
           '2015년 9월', '2015년 전월비', '2015년 전년말비', '2015년 전년동월비', '지역'],
          dtype='object', name=0)




```python
df_2013_2015 = pd.melt(df, id_vars=['지역'], value_vars=melt_columns[2:-4])
df_2013_2015.head()
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
      <th>지역</th>
      <th>0</th>
      <th>value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>전국</td>
      <td>2013년 12월</td>
      <td>8,059</td>
    </tr>
    <tr>
      <th>1</th>
      <td>서울</td>
      <td>2013년 12월</td>
      <td>18,189</td>
    </tr>
    <tr>
      <th>2</th>
      <td>6대광역시부산</td>
      <td>2013년 12월</td>
      <td>8,111</td>
    </tr>
    <tr>
      <th>3</th>
      <td>대구</td>
      <td>2013년 12월</td>
      <td>8,080</td>
    </tr>
    <tr>
      <th>4</th>
      <td>인천</td>
      <td>2013년 12월</td>
      <td>10,204</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_2013_2015.columns = ['지역', '기간', '분양가']
df_2013_2015.head()
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
      <th>지역</th>
      <th>기간</th>
      <th>분양가</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>전국</td>
      <td>2013년 12월</td>
      <td>8,059</td>
    </tr>
    <tr>
      <th>1</th>
      <td>서울</td>
      <td>2013년 12월</td>
      <td>18,189</td>
    </tr>
    <tr>
      <th>2</th>
      <td>6대광역시부산</td>
      <td>2013년 12월</td>
      <td>8,111</td>
    </tr>
    <tr>
      <th>3</th>
      <td>대구</td>
      <td>2013년 12월</td>
      <td>8,080</td>
    </tr>
    <tr>
      <th>4</th>
      <td>인천</td>
      <td>2013년 12월</td>
      <td>10,204</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_2013_2015['연도'] = df_2013_2015['기간'].apply(lambda year_month : year_month.split('년')[0])
df_2013_2015['월'] = df_2013_2015['기간'].apply(lambda year_month : re.sub('월', '', year_month.split('년')[1]).strip())
```


```python
df_2013_2015.head()
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
      <th>지역</th>
      <th>기간</th>
      <th>분양가</th>
      <th>연도</th>
      <th>월</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>전국</td>
      <td>2013년 12월</td>
      <td>8,059</td>
      <td>2013</td>
      <td>12</td>
    </tr>
    <tr>
      <th>1</th>
      <td>서울</td>
      <td>2013년 12월</td>
      <td>18,189</td>
      <td>2013</td>
      <td>12</td>
    </tr>
    <tr>
      <th>2</th>
      <td>6대광역시부산</td>
      <td>2013년 12월</td>
      <td>8,111</td>
      <td>2013</td>
      <td>12</td>
    </tr>
    <tr>
      <th>3</th>
      <td>대구</td>
      <td>2013년 12월</td>
      <td>8,080</td>
      <td>2013</td>
      <td>12</td>
    </tr>
    <tr>
      <th>4</th>
      <td>인천</td>
      <td>2013년 12월</td>
      <td>10,204</td>
      <td>2013</td>
      <td>12</td>
    </tr>
  </tbody>
</table>
</div>



## 지역명 강원과 부산 정리


```python
df_2013_2015['지역'].value_counts()
```




               44
    서울         22
    울산         22
    전북         22
    충북         22
    제주         22
    경북         22
    수도권        22
    인천         22
    광주         22
    경남         22
    충남         22
    대구         22
    대전         22
    경기         22
    전남         22
    세종         22
    전국         22
    6대광역시부산    22
    지방강원       22
    Name: 지역, dtype: int64




```python
df_2013_2015['지역'] = df_2013_2015['지역'].apply(lambda x: re.sub('6대광역시부산','부산', x))
df_2013_2015['지역'] = df_2013_2015['지역'].apply(lambda x: re.sub('지방강원','강원', x))
df_2013_2015['지역'].value_counts()
```




           44
    강원     22
    울산     22
    전북     22
    충북     22
    제주     22
    경북     22
    수도권    22
    인천     22
    광주     22
    경남     22
    충남     22
    대구     22
    대전     22
    세종     22
    전국     22
    부산     22
    경기     22
    서울     22
    전남     22
    Name: 지역, dtype: int64




```python
df_2013_2015.describe()
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
      <th>지역</th>
      <th>기간</th>
      <th>분양가</th>
      <th>연도</th>
      <th>월</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>462</td>
      <td>462</td>
      <td>462</td>
      <td>462</td>
      <td>462</td>
    </tr>
    <tr>
      <th>unique</th>
      <td>20</td>
      <td>22</td>
      <td>371</td>
      <td>3</td>
      <td>12</td>
    </tr>
    <tr>
      <th>top</th>
      <td></td>
      <td>2015년 8월</td>
      <td>8,067</td>
      <td>2014</td>
      <td>2</td>
    </tr>
    <tr>
      <th>freq</th>
      <td>44</td>
      <td>21</td>
      <td>7</td>
      <td>252</td>
      <td>42</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_2013_2015['분양가격'] = df_2013_2015['분양가'].str.replace(',', '').astype(int)
```


```python
(ggplot(df_2013_2015, aes(x='지역', y='분양가격', fill='연도'))
 + geom_boxplot()
 + theme(text=element_text(family='NanumBarunGothic'),
         figure_size=(12, 6))
)
```


![png](./Photo/output_\d\d_\d\d?\.png)





    <ggplot: (96006890209)>




```python
(ggplot(df_2013_2015, aes(x='지역', y='분양가격', fill='연도'))
 + geom_bar(stat='identity', position='dodge')
 + theme(text=element_text(family='NanumBarunGothic'),
         figure_size=(12, 6))
)
```


![png](./Photo/output_\d\d_\d\d?\.png)





    <ggplot: (-9223371940848055997)>



## 이제 2013년부터 2018년 4월까지 데이터를 합칠 준비가 됨


```python
df_2015_2018 = pre_sale.loc[pre_sale['규모구분'] == '전체']
print(df_2015_2018.shape)
df_2015_2018.head()
```

    (561, 7)





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
      <th>지역명</th>
      <th>규모구분</th>
      <th>연도</th>
      <th>월</th>
      <th>분양가격(㎡)</th>
      <th>분양가격</th>
      <th>평당분양가격</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>서울</td>
      <td>전체</td>
      <td>2015</td>
      <td>10</td>
      <td>5841</td>
      <td>5,841</td>
      <td>19,275</td>
    </tr>
    <tr>
      <th>5</th>
      <td>인천</td>
      <td>전체</td>
      <td>2015</td>
      <td>10</td>
      <td>3163</td>
      <td>3,163</td>
      <td>10,438</td>
    </tr>
    <tr>
      <th>10</th>
      <td>경기</td>
      <td>전체</td>
      <td>2015</td>
      <td>10</td>
      <td>3138</td>
      <td>3,138</td>
      <td>10,355</td>
    </tr>
    <tr>
      <th>15</th>
      <td>부산</td>
      <td>전체</td>
      <td>2015</td>
      <td>10</td>
      <td>3112</td>
      <td>3,112</td>
      <td>10,270</td>
    </tr>
    <tr>
      <th>20</th>
      <td>대구</td>
      <td>전체</td>
      <td>2015</td>
      <td>10</td>
      <td>2682</td>
      <td>2,682</td>
      <td>8,851</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_2013_2015.columns
```




    Index(['지역', '기간', '분양가', '연도', '월', '분양가격'], dtype='object')




```python
df_2013_2015_prepare = df_2013_2015[['지역', '연도', '월', '분양가격']]
df_2013_2015_prepare.head()
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
      <th>지역</th>
      <th>연도</th>
      <th>월</th>
      <th>분양가격</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>전국</td>
      <td>2013</td>
      <td>12</td>
      <td>8059</td>
    </tr>
    <tr>
      <th>1</th>
      <td>서울</td>
      <td>2013</td>
      <td>12</td>
      <td>18189</td>
    </tr>
    <tr>
      <th>2</th>
      <td>부산</td>
      <td>2013</td>
      <td>12</td>
      <td>8111</td>
    </tr>
    <tr>
      <th>3</th>
      <td>대구</td>
      <td>2013</td>
      <td>12</td>
      <td>8080</td>
    </tr>
    <tr>
      <th>4</th>
      <td>인천</td>
      <td>2013</td>
      <td>12</td>
      <td>10204</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_2013_2015_prepare.columns = ['지역명', '연도', '월', '평당분양가격']
```


```python
df_2015_2018.columns
```




    Index(['지역명', '규모구분', '연도', '월', '분양가격(㎡)', '분양가격', '평당분양가격'], dtype='object')




```python
df_2015_2018_prepare = df_2015_2018[['지역명', '연도', '월', '평당분양가격']]
df_2015_2018_prepare.head()
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
      <th>지역명</th>
      <th>연도</th>
      <th>월</th>
      <th>평당분양가격</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>서울</td>
      <td>2015</td>
      <td>10</td>
      <td>19,275</td>
    </tr>
    <tr>
      <th>5</th>
      <td>인천</td>
      <td>2015</td>
      <td>10</td>
      <td>10,438</td>
    </tr>
    <tr>
      <th>10</th>
      <td>경기</td>
      <td>2015</td>
      <td>10</td>
      <td>10,355</td>
    </tr>
    <tr>
      <th>15</th>
      <td>부산</td>
      <td>2015</td>
      <td>10</td>
      <td>10,270</td>
    </tr>
    <tr>
      <th>20</th>
      <td>대구</td>
      <td>2015</td>
      <td>10</td>
      <td>8,851</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_2015_2018_prepare.describe()
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
      <th>평당분양가격</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>544</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>9,702</td>
    </tr>
    <tr>
      <th>std</th>
      <td>3,361</td>
    </tr>
    <tr>
      <th>min</th>
      <td>6,300</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>7,484</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>8,928</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>10,554</td>
    </tr>
    <tr>
      <th>max</th>
      <td>22,833</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_2013_2018 = pd.concat([df_2013_2015_prepare, df_2015_2018_prepare])
df_2013_2018.shape
```




    (1023, 4)




```python
df_2013_2018.head()
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
      <th>지역명</th>
      <th>연도</th>
      <th>월</th>
      <th>평당분양가격</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>전국</td>
      <td>2013</td>
      <td>12</td>
      <td>8,059</td>
    </tr>
    <tr>
      <th>1</th>
      <td>서울</td>
      <td>2013</td>
      <td>12</td>
      <td>18,189</td>
    </tr>
    <tr>
      <th>2</th>
      <td>부산</td>
      <td>2013</td>
      <td>12</td>
      <td>8,111</td>
    </tr>
    <tr>
      <th>3</th>
      <td>대구</td>
      <td>2013</td>
      <td>12</td>
      <td>8,080</td>
    </tr>
    <tr>
      <th>4</th>
      <td>인천</td>
      <td>2013</td>
      <td>12</td>
      <td>10,204</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_2013_2015_region= df_2013_2015_prepare['지역명'].unique()
df_2013_2015_region
```




    array(['전국', '서울', '부산', '대구', '인천', '광주', '대전', '울산', '', '경기', '수도권',
           '세종', '강원', '충북', '충남', '전북', '전남', '경북', '경남', '제주'], dtype=object)




```python
df_2015_2018_region = df_2015_2018_prepare['지역명'].unique()
df_2015_2018_region
```




    array(['서울', '인천', '경기', '부산', '대구', '광주', '대전', '울산', '세종', '강원', '충북',
           '충남', '전북', '전남', '경북', '경남', '제주'], dtype=object)




```python
exclude_region = [region for region in df_2013_2015_region if not region in df_2015_2018_region]
exclude_region
```




    ['전국', '', '수도권']




```python
df_2013_2018.shape
```




    (1023, 4)




```python
df_2013_2018.loc[df_2013_2018['지역명'].str.match('전국|수도권')].head()
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
      <th>지역명</th>
      <th>연도</th>
      <th>월</th>
      <th>평당분양가격</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>전국</td>
      <td>2013</td>
      <td>12</td>
      <td>8,059</td>
    </tr>
    <tr>
      <th>10</th>
      <td>수도권</td>
      <td>2013</td>
      <td>12</td>
      <td>13,083</td>
    </tr>
    <tr>
      <th>21</th>
      <td>전국</td>
      <td>2014</td>
      <td>1</td>
      <td>8,130</td>
    </tr>
    <tr>
      <th>31</th>
      <td>수도권</td>
      <td>2014</td>
      <td>1</td>
      <td>12,995</td>
    </tr>
    <tr>
      <th>42</th>
      <td>전국</td>
      <td>2014</td>
      <td>2</td>
      <td>8,195</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_2013_2018.drop(df_2013_2018.loc[df_2013_2018['지역명'].str.match('전국|수도권')].index, axis=0, inplace=True)
df_2013_2018.drop(df_2013_2018.loc[df_2013_2018['지역명'] == ''].index, axis=0, inplace=True)
```


```python
(ggplot(df_2013_2018, aes(x='연도', y='평당분양가격'))
 + geom_bar(stat='identity', position='dodge')
 + theme(text=element_text(family='NanumBarunGothic'))
)
```

    C:\Users\rlath\Anaconda3\lib\site-packages\plotnine\layer.py:450: UserWarning: geom_bar : Removed 17 rows containing missing values.
      self.data = self.geom.handle_na(self.data)



![png](./Photo/output_\d\d_\d\d?\.png)





    <ggplot: (96008316883)>




```python
(ggplot(df_2013_2018, aes(x='지역명', y='평당분양가격', fill='연도'))
 + geom_bar(stat='identity', position='dodge')
 + theme(text=element_text(family='NanumBarunGothic'),
         figure_size=(12, 6))
)
```

    C:\Users\rlath\Anaconda3\lib\site-packages\plotnine\layer.py:450: UserWarning: geom_bar : Removed 17 rows containing missing values.
      self.data = self.geom.handle_na(self.data)



![png](./Photo/output_\d\d_\d\d?\.png)





    <ggplot: (-9223371940848850793)>




```python
(ggplot(df_2013_2018)
 + aes(x='연도', y='평당분양가격')
 + geom_boxplot()
 + theme(text=element_text(family='NanumBarunGothic'))
)
```

    C:\Users\rlath\Anaconda3\lib\site-packages\plotnine\layer.py:363: UserWarning: stat_boxplot : Removed 17 rows containing non-finite values.
      data = self.stat.compute_layer(data, params, layout)



![png](./Photo/output_\d\d_\d\d?\.png)





    <ggplot: (96008348585)>




```python
df_2013_2018_jeju = df_2013_2018.loc[df_2013_2018['지역명'] == '제주']
(ggplot(df_2013_2018_jeju)
 + aes(x='연도', y='평당분양가격')
 + geom_boxplot()
 + theme(text=element_text(family='NanumBarunGothic'))
)
```

    C:\Users\rlath\Anaconda3\lib\site-packages\plotnine\layer.py:363: UserWarning: stat_boxplot : Removed 1 rows containing non-finite values.
      data = self.stat.compute_layer(data, params, layout)



![png](./Photo/output_\d\d_\d\d?\.png)





    <ggplot: (96006271780)>




```python
(ggplot(df_2013_2018)
 + aes(x='연도', y='평당분양가격')
 + geom_boxplot()
 + facet_wrap('지역명')
 + theme(text=element_text(family='NanumBarunGothic'),
         axis_text_x=element_text(rotation=70),
         figure_size=(12, 6))
)
```

    C:\Users\rlath\Anaconda3\lib\site-packages\plotnine\layer.py:363: UserWarning: stat_boxplot : Removed 17 rows containing non-finite values.
      data = self.stat.compute_layer(data, params, layout)



![png](./Photo/output_\d\d_\d\d?\.png)





    <ggplot: (-9223371940848503899)>
