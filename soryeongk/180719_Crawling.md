

```python
!pip install beautifulsoup4
```

    Requirement already satisfied: beautifulsoup4 in /usr/local/lib/python3.6/dist-packages (4.6.0)



```python
from urllib import request
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.naver.com"
with request.urlopen(url) as f:
  html = f.read().decode('utf-8')

bs = BeautifulSoup(html, 'html5lib')  # 내부에서 html5lib를 사용해 dom을 만들어 줌
title = bs.select_one('title').text  # select로 시작하는 함수에서 'title'요소를 찾아줌
# .text로 text만 뽑아내는 것, select_one은 select로 뽑아낸 리스트의 첫 요소만을 return
# title은 사실 태그이름보다는 css selector의 이름이라고 보면 됨
print(title)
```

    NAVER
    


```python
from urllib import request
from bs4 import BeautifulSoup

url = "http://www.yes24.com/searchcorner/Search?keywordAd=&keyword=&domain=BOOK&qdomain=%B1%B9%B3%BB%B5%B5%BC%AD&query=%C6%C4%C0%CC%BD%E3"
with request.urlopen(url) as f:
  html = f.read().decode('euc-kr')

bs = BeautifulSoup(html, 'html5lib')  # 내부에서 html5lib를 사용해 dom을 만들어 줌

```


```python
title_elements = bs.select('div.goodsList p.goods_name a strong')
# title_elements는 제목만 있는 리스트
titles = [t.text for t in title_elements]  # 제목을 텍스트만 리스트에 담음

price_elements = bs.select('div.goodsList p.goods_price strong')
prices = [int(p.text[:-1].replace(',','')) for p in price_elements]
# 16,920원을 16920으로 변환
prices  # 할인가를 출력
```




    [16920,
     10800,
     21600,
     27000,
     22500,
     27000,
     24750,
     14400,
     31500,
     31500,
     25200,
     27000,
     13500,
     27000,
     36000,
     29700,
     27000,
     24300,
     18000,
     22500]




```python
books = pd.DataFrame(
    {'title' : titles, 'price' : prices},
    columns=['title', 'price'],
    index=[str(n+1)+'위' for n in range(20)]
)
books
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
      <th>price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1위</th>
      <td>Do it! 점프 투 파이썬</td>
      <td>16920</td>
    </tr>
    <tr>
      <th>2위</th>
      <td>모두의 파이썬</td>
      <td>10800</td>
    </tr>
    <tr>
      <th>3위</th>
      <td>밑바닥부터 시작하는 딥러닝</td>
      <td>21600</td>
    </tr>
    <tr>
      <th>4위</th>
      <td>파이썬을 이용한 머신러닝, 딥러닝 실전 개발 입문</td>
      <td>27000</td>
    </tr>
    <tr>
      <th>5위</th>
      <td>파이썬과 케라스를 이용한 딥러닝/강화학습 주식투자</td>
      <td>22500</td>
    </tr>
    <tr>
      <th>6위</th>
      <td>파이썬 라이브러리를 활용한 머신러닝</td>
      <td>27000</td>
    </tr>
    <tr>
      <th>7위</th>
      <td>파이썬으로 데이터 주무르기</td>
      <td>24750</td>
    </tr>
    <tr>
      <th>8위</th>
      <td>모두의 알고리즘 with 파이썬</td>
      <td>14400</td>
    </tr>
    <tr>
      <th>9위</th>
      <td>파이썬 자연어 처리의 이론과 실제</td>
      <td>31500</td>
    </tr>
    <tr>
      <th>10위</th>
      <td>파이썬 GUI 프로그래밍 쿡북 2/e</td>
      <td>31500</td>
    </tr>
    <tr>
      <th>11위</th>
      <td>파이썬을 활용한 금융공학 레시피</td>
      <td>25200</td>
    </tr>
    <tr>
      <th>12위</th>
      <td>처음 시작하는 파이썬</td>
      <td>27000</td>
    </tr>
    <tr>
      <th>13위</th>
      <td>Hello Coding 한입에 쏙 파이썬</td>
      <td>13500</td>
    </tr>
    <tr>
      <th>14위</th>
      <td>파이썬을 이용한 웹 크롤링과 스크레이핑</td>
      <td>27000</td>
    </tr>
    <tr>
      <th>15위</th>
      <td>파이썬으로 배우는 알고리즘 트레이딩</td>
      <td>36000</td>
    </tr>
    <tr>
      <th>16위</th>
      <td>파이썬 라이브러리를 활용한 데이터 분석</td>
      <td>29700</td>
    </tr>
    <tr>
      <th>17위</th>
      <td>한 권으로 배우는 파이썬 기초 &amp; 알고리즘 사고법</td>
      <td>27000</td>
    </tr>
    <tr>
      <th>18위</th>
      <td>파이썬과 케라스로 배우는 강화학습</td>
      <td>24300</td>
    </tr>
    <tr>
      <th>19위</th>
      <td>초보자를 위한 파이썬 200제</td>
      <td>18000</td>
    </tr>
    <tr>
      <th>20위</th>
      <td>파이썬으로 만드는 암호화폐 자동 거래 시스템</td>
      <td>22500</td>
    </tr>
  </tbody>
</table>
</div>


