# 20180717

## <오전수업>

### 1. Pandas

```
- 엑셀은 파일 사이즈가 제한적이고, 많은 양의 데이터를 불러와도 속도가 느리고 사용할 수 있는 플러그인이 제한되어 있다. 
  Pandas나 Numpy를 사용하면 간편하고 확장이 용이하다.
```

### 2. Numpy

```
Q. 파이썬 표준 라이브러리 만으로도 수치계산이 대부분 가능한데 왜 Numpy를 사용할까?
-> A. Numpy는 행렬이나 일반적으로 대규모 다차원 배열을 쉽게 처리 할 수 있게 해주는 파이썬의 라이브러리이다. 
      데이터 구조 외에도 수치 계산을 위해 효율적으로 구현 된 기능을 제공한다. 
```



### 3. 10 Minutes to pandas

```
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
```

#### 1) s = pd.Series([1, 3, 5, np.nan,6 , 8])

```
0    1.0
1    3.0
2    5.0
3    NaN
4    6.0
5    8.0
dtype: float64
```

#### 2) Datafame 결과의 데이터타입을 확인해보는것은 중요!

```
 => 다양한 데이터 타입으로 구성되기 때문
```

#### 3) df2."TAB키를 누르면"    ->  사용가능한 함수가 나온다.  

```
df2.A                  df2.bool
df2.abs                df2.boxplot
df2.add                df2.C
df2.add_prefix         df2.clip
df2.add_suffix         df2.clip_lower
df2.align              df2.clip_upper
df2.all                df2.columns
df2.any                df2.combine
df2.append             df2.combine_first
df2.apply              df2.compound
df2.applymap           df2.consolidate
df2.D
```

#### 4) head()와 tail()

```
head는 데이터의 앞  /  tail은 데이터의 뒤
```

#### 5) 데이터의 세부정보 확인하기

```
- index
- columns
- values
```

#### 6) 데이터의 대략적인 통계적 정보 확인하기

```
- describe()를 사용한다.
```

#### 7) 데이터 전치

##### - 행과 열 바꾸기

```
> df.T
```

##### - 축 별로 정렬

```
> df.sort_index(axis=1, ascending = False)  # axis가 1=열(colums), 0=행(raw)이다.
                                            # 항상 행이 먼저고 열이 다음이다.
                                            # ascending가 True면 순서대로, False면 역순으로(=descending)
```

##### - 값 별로 정렬

```
> df.sort_values(by='B')     # B컬럼을 기준으로 정렬
```

#### 8) 데이터얻기

##### 특정 열만 추출하기

```
> df['A']
> df['A', 'B']]
```

```
# 0부터 3전짜기 추출
> df[0:3]
	            A	        B	        C         	D
2013-01-01	0.395799	1.324341	0.153554	-0.672920
2013-01-02	-0.303496	-1.596556	-0.920610	-0.840386
2013-01-03	0.677687	0.204407	0.256671	-1.094652
```

```
# 원하는 날짜
> df['20130102':'20130104']
	            A	        B	       C	        D
2013-01-02	-0.303496	-1.596556	-0.920610	-0.840386
2013-01-03	0.677687	0.204407	0.256671	-1.094652
2013-01-04	-1.109111	-0.770913	-0.330677	-0.570009
```



-----





# <오후 수업>

# 실습해보기 :checkered_flag:

### 1. Pandas와 Numpy를 import하기

```
import pandas as pd
import numpy as np
print(pd.__version__)
print(np.__version__)
```



### 2. plotnine 실행

```
from plotnine import *   # R의 ggplot과 유사
```



 ### 3. csv 데이터 불러오기

```
df = pd.read_csv('https://s3.ap-northeast-2.amazonaws.com/data10902/petition/petition.csv',
                  parse_dates=['start', 'end'])
```



### 4.  읽어온 데이터가 몇 행 몇 열인지

```
df.shape
```



### 5. 일부 데이터 미리 보기

#### 1) 상단 5개 데이터

```
df.head(5)
```

#### 2) 하단 3개 데이터

```
df.tail(3)
```



### 6. 정규표현식 사용을 위해 import

```
import re
# 원하는 검색어 넣고, 몇건이 나오는지 확인
p = r '.*(문화|예술|공연).*'
art = df[df['title'].str.match(p) |
           df['content'].str.match(p, flags=re.MULTILINE)]
art.shape
```

```
# 커피를 검색했을 때 투표수가 0인 것은 제외하는 방법
coffee = df[( df.title.str.find('커피') != -1 ) & ( df.content.str.find('커피') != -1  ) & ( df.votes > 0 ) ]
coffee[['title','content', 'votes']].sort_values(by='votes', ascending=False)
```

```
df['title']과 df.title은 같은 것이다.
```

```
drop(colums['answer']) -> drop은 사용하지 않는 컬럼을 삭제
```



### 7. 결측치 확인하는방법

```
df. isnull().sum()
```



### 8. 데이터 요약하기

#### 1) 어떤 컬럼이있고 어떤 타입인지 출력

```
df.info()
```

#### 2) 데이터 타입만 따로 뽑아보기

```
df. dtypes
```

#### 3) 컬럼명만 따로 추출해보기

```
df.columns     # df['columns']와 같은 뜻
```
#### 4) 수치형 데이터 요약

```
df.describe()
```

#### 5) 카테고리(object) 형태의 데이터 요약

```
df.describe(include=np.object)
```





-----

:gift_heart: 함수사용법과 정규표현식 공부하기!

💝  오늘 배운거 복습하고, 여러번 반복하기!
