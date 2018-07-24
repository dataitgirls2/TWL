
# 예스24 베스트셀러 목록 추출하기

## 필요한 패키지 설치하기

엉망으로 만들어진 HTML 문서도 대체로 잘 분석해서 DOM 구조로 만들어주는 `html5lib`와 CSS Selector를 이용하여 DOM 구조에서 원하는 엘리먼트들을 뽑아내는 기능을 제공하는 `beautifulsoup4`를 설치합니다.

이 두 패키지는 파이썬 표준 라이브러리에 포함되어 있지 않아서 별도로 설치해주어야 합니다. 다만 Google Colab에는 표준 라이브러리 이외에도 자주 쓰이는 몇몇 외부 패키지들이 미리 설치되어 있어서 이 두 패키지를 별도로 설치할 필요가 없습니다. 그래도 혹시 모르니 설치하는 명령을 한 번 실행하겠습니다.


```python
!pip install html5lib beautifulsoup4
```

    Requirement already satisfied: html5lib in /usr/local/lib/python3.6/dist-packages (1.0.1)
    Requirement already satisfied: beautifulsoup4 in /usr/local/lib/python3.6/dist-packages (4.6.0)
    Requirement already satisfied: webencodings in /usr/local/lib/python3.6/dist-packages (from html5lib) (0.5.1)
    Requirement already satisfied: six>=1.9 in /usr/local/lib/python3.6/dist-packages (from html5lib) (1.11.0)


## HTML 받아오기

예스24 서버로 HTTP 요청을 보내서 HTML을 받아온 후 파이썬 문자열(str)로 변환해보겠습니다.


```python
from urllib import request

url = "http://www.yes24.com/24/category/bestseller"
with request.urlopen(url) as f:
  html = f.read().decode('utf-8')
```

HTTP 응답으로 받아온 본문을 `utf-8` 코덱을 이용하여 파이썬 문자열로 변환하려고 했으나 에러가 발생했습니다. 소스 코드를 살펴보니 아래와 같은 부분이 있습니다.

```
<meta http-equiv="Content-Type" content="text/html;charset=euc-kr" />
```

`utf-8`이 아닌 `euc-kr`을 써야합니다. `euc-kr`은 오래 전에 한국에서만 쓰이던 낡은 방식이지만 아직도 상당수 한국 웹사이트에서 이 방식을 사용합니다.


```python
url = "http://www.yes24.com/24/category/bestseller"
with request.urlopen(url) as f:
  html = f.read().decode('euc-kr')
```

이번에는 오류가 발생하지 않았습니다.

사이트에 따라  `utf-8` 또는 `euc-kr`로 코드를 바꿔주는 반복 작업을 하고 싶지 않습니다. 구글 검색을 해보니 이렇게 쓰면 된다고 합니다.


```python
url = "http://www.yes24.com/24/category/bestseller"
with request.urlopen(url) as f:
  charset = f.headers.get_content_charset()
  html = f.read().decode(charset)
```

## HTML 문자열을 분석하여 DOM 구성하기

`html5lib`를 이용하여 DOM을 구성한 후 DOM 트리 구조를 탐색하여 원하는 정보를 추출하는 코드를 만들어도 되지만 번거롭습니다. `beautifulsoup`을 이용하면 CSS 셀렉터를 써서 원하는 정보를 쉽게 추출해낼 수 있습니다.

`beautifulsoup`은 내부적으로 DOM 트리를 구성하는데, 이 때 어떤 분석기(parser)를 사용할지 지정해줄 수 있습니다. 우리는 `html5lib`를 쓰도록 하겠습니다.


```python
from bs4 import BeautifulSoup

bs = BeautifulSoup(html, 'html5lib')
```

bs 객체에는 `select_one()` 함수와 `select()` 함수가 있습니다. 두 함수 모두 CSS 셀렉터로 원하는 엘리먼트를 찾아주는 기능을 한다는 점은 같지만, `select_one()` 함수는 처음으로 발견한 하나의 엘리먼트만 반환하고 `select()` 함수는 발견한 모든 엘리먼트를 반환한다는 점이 다릅니다.

문서 내의 모든 하이퍼링크를 찾으려면 `select("a")`라고 씁니다. HTML에서는 a 엘리먼트가 링크를 뜻하기 때문입니다. 모든 링크를 찾은 후 처음 다섯개만 출력해보겠습니다.


```python
links = bs.select('a')
links[:5]
```




    [<a href="#wrapperContent">본문 바로가기</a>,
     <a href="http://www.yes24.com/eWorld/EventWorld/Event?eventno=157265" onclick="setWcode('001');"><img alt="7월혜택" height="50" src="http://image.yes24.com/images/01_Banner/welcome/topBanner/2018/0711_m3_480x50_1.gif?180504" width="480"/></a>,
     <a href="http://www.yes24.com/campaign/01_book/yesPresent/yesPresent.aspx?EventNo=157880&amp;CategoryNumber=001" onclick="setWcode('001');"><img alt="여행파우치" height="50" src="http://image.yes24.com/images/01_Banner/welcome/topBanner/2018/0711_m3_480x50_2.gif" width="480"/></a>,
     <a href="http://www.yes24.com/campaign/00_corp/2018/youngAuthor.aspx" onclick="setWcode('001');"><img alt="젊은작가" height="50" src="http://image.yes24.com/momo/TopCate1911/MidCate008/191073254.gif" width="480"/></a>,
     <a href="http://www.yes24.com/campaign/01_book/yesPresent/yesPresent.aspx?EventNo=157880&amp;CategoryNumber=001" onclick="setWcode('001');"><img alt="투명파우치" height="50" src="http://image.yes24.com/images/01_Banner/welcome/topBanner/2018/0711_m2_480x50_2.gif" width="480"/></a>]



`select_one()` 함수는 첫 엘리먼트만 반환합니다. 따라서 `select("a")[0]`와 `select_one("a")`는 같습니다.


```python
bs.select("a")[0] == bs.select_one("a")
```




    True



##CSS 주로 사용하는 용어설명


- 여는 태그 안에 들어간 것들을  'attribute' 라고 한다.
  <p class="hightlight">

- id :   이 문서 전체에서 유일한 '식별자'를 부여 할 수 있다. welcome이라는 id를 유일하게 주는 것 
  ㄴ id를 찾을때는 # 으로 찾습니다.
- 강조하고 싶은것을 highlight 주고 싶으면 class를 여러개 부여해줄 수 있습니다. 
  ㄴ 클래스를 해놓으면 해당 클래스 관련된것을 모두 다 가져올 수 있습니다. 
  ㄴ 클래스는 . (점) 을 써서 찾습니다.
  ㄴ 뛰어쓰기는 그 안에 있는 모든걸 찾습니다. 
  - ul .highlight : 중간에 공백이 있으면 ul 엘리먼트를 우선 싹 찾고 그 밑에 highlight(클래스)를 찾습니다. ul 의 자식들 중에!
  - ul.highligth : 뛰어쓰기 안하면 ul이면서 hightlight인것을 찾는다! (And)
  - p > span : p에 직계자식중에서 span인것을 찾는다
  - p span : p에 자식의자식의자식까지 모든 span 을 찾는것 
  - p .span : p 의 모든자식들중에서 span에 해당하는 클래스를 찾는다.

---






## 선택자의 조합:

- p.highlight -> 태그이름이 p이면서 class속성이 하이라이트인 엘리먼트
- body .highlight -> 태그이름이 body인 엘리먼트의 자손 중 class속성이 하이라이트인 엘리먼트
- body > .highlight -> 태그이름이 body 인 엘리먼트의 직계자식!! 중 class속성이 highlight인 엘리먼트


## 베스트셀러 목록 추출하기

크롬의 개발자 도구를 통해 문서를 살펴보니 베스트셀러를 담고 있는 영역은 id가 "bestList"인 div 엘리먼트의 자식인 ol 엘리먼트입니다. ol 엘리먼트에 속한 li 엘리먼트 하나하나가 각 책에 대한 정보를 담고 있습니다. 따라서 아래와 같이 쓰면 책 40권에 해당하는 li 엘리먼트 40개가 나와야 합니다.


```python
len(bs.select('#bestList > ol > li'))
```




    40



잘되는 것을 확인하였습니다. 각 li 안에는 p 태그가 여러개 있는데 이 중 세번째 p 엘리먼트 안에 책 이름이 담겨 있고, 가격을 담고 있는 p 엘리먼트에는 `price` 클래스가 붙어 있습니다.

```
<li>
   <p>...</p>
   <p>...</p>
   <p><a href="...">책이름</a></p>
   ...
   <p class="price"><strong>가격</strong></p>
</li>
```

책 이름을 뽑아내볼까요?


```python
bs.select('#bestList > ol > li p:nth-child(3) a')
```


    ---------------------------------------------------------------------------
    
    NotImplementedError                       Traceback (most recent call last)
    
    <ipython-input-9-4dcaccc7a75f> in <module>()
    ----> 1 bs.select('#bestList > ol > li p:nth-child(3) a')


    /usr/local/lib/python3.6/dist-packages/bs4/element.py in select(self, selector, _candidate_generator, limit)
       1449                 else:
       1450                     raise NotImplementedError(
    -> 1451                         'Only the following pseudo-classes are implemented: nth-of-type.')
       1452 
       1453             elif token == '*':


    NotImplementedError: Only the following pseudo-classes are implemented: nth-of-type.


각 li의 자식 중 세번째 자식인 p를 찾으려고 했으나 해당 셀렉터 문법은 beautifulsoup4에서 아직 구현하지 않았다며 에러가 발생합니다.

아쉽지만 각 책에 해당하는 li 엘리먼트들까지만 찾아서 변수에 담은 후 각 li 엘리먼트에서 원하는 정보를 뽑아내는 코드를 따로 만들어야합니다.


```python
books = bs.select('#bestList > ol > li')
titles = []
for book in books:
  # "p:nth-of-type(3)"은 li의 자식 중 세번째 p 엘리먼트를 찾아줍니다.
  title = book.select_one('p:nth-of-type(3) a').text
  titles.append(title)
titles
```




    ['역사의 역사',
     '열두 발자국',
     '죽고 싶지만 떡볶이는 먹고 싶어',
     '모든 순간이 너였다',
     '설민석의 한국사 대모험 7',
     '사피엔스',
     '언어의 온도 (100만부 돌파 기념 양장 특별판)',
     '개인주의자 선언',
     '2019 전한길 한국사 필기노트+빵꾸노트',
     '고양이 1',
     '곰돌이 푸, 행복한 일은 매일 있어',
     '원피스 ONE PIECE 89',
     '행복해지는 연습을 해요',
     '고양이 2',
     '나는 나로 살기로 했다',
     '에듀윌 한국사능력검정시험 2주끝장 고급 개정판 3.0',
     '돌이킬 수 없는 약속',
     '하마터면 열심히 살 뻔했다',
     '설민석의 한국사 대모험 6',
     '해커스 토익 기출 보카',
     '해커스 토익 실전 1000제 READING 1 문제집',
     '어디서 살 것인가',
     'Go Go 카카오프렌즈 3',
     '해커스 토익 Reading (2018)',
     '한때 소중했던 것들',
     '곰돌이 푸, 서두르지 않아도 괜찮아',
     '나는 오늘도 경제적 자유를 꿈꾼다',
     '82년생 김지영',
     '해커스 토익 실전 1000제 1 LC 리스닝 (Hackers Toeic Listening) 문제집 2...',
     '27년 동안 영어 공부에 실패했던 39세 김과장은 어떻게 3개월 만에 영어 천...',
     '호모 데우스',
     '설민석의 한국사 대모험 1',
     '굿 라이프',
     '대한민국 아파트 부의 지도',
     '김 비서가 왜 그럴까 3',
     '나미야 잡화점의 기적',
     '어떻게 살 것인가',
     '큰별쌤 최태성의 별★별 한국사 한국사능력검정시험 고급(1·2급) 상',
     '[예약판매] 나는 유튜브 크리에이터를 꿈꾼다(사인 인쇄본)',
     '마법천자문 42']



비슷한 방법으로 가격도 뽑아냅시다.


```python
books = bs.select('#bestList > ol > li')

titles = []
prices = []
for book in books:
  # "p:nth-of-type(3)"은 li의 자식 중 세번째 p 엘리먼트를 찾아줍니다.
  title = book.select_one('p:nth-of-type(3) a').text
  titles.append(title)

  price = book.select_one('p.price').text
  prices.append(price)

prices
```




    ['14,400원(10%+5%)',
     '15,120원(10%+5%)',
     '12,420원(10%+5%)',
     '12,420원(10%+5%)',
     '9,450원(10%+5%)',
     '19,800원(10%+5%)',
     '12,420원(10%+5%)',
     '12,150원(10%+5%)',
     '18,900원(10%)',
     '11,520원(10%+5%)',
     '10,800원(10%+5%)',
     '4,500원(10%+5%)',
     '13,050원(10%+5%)',
     '11,520원(10%+5%)',
     '12,420원(10%+5%)',
     '18,900원(10%+5%)',
     '13,500원(10%+5%)',
     '13,500원(10%+5%)',
     '9,450원(10%+5%)',
     '11,610원(10%+5%)',
     '10,710원(10%+5%)',
     '14,400원(10%+5%)',
     '10,800원(10%+5%)',
     '16,920원(10%+5%)',
     '12,600원(10%+5%)',
     '12,420원(10%+5%)',
     '15,120원(10%+5%)',
     '11,700원(10%+5%)',
     '10,710원(10%+5%)',
     '12,600원(10%+5%)',
     '19,800원(10%+5%)',
     '8,820원(10%+5%)',
     '15,300원(10%+5%)',
     '15,120원(10%+5%)',
     '11,700원(10%+5%)',
     '13,320원(10%+5%)',
     '13,500원(10%+5%)',
     '12,150원(10%+5%)',
     '13,320원(10%+5%)',
     '8,820원(10%+5%)']



가격을 정수로 바꿔주면 좋겠습니다. 우선 괄호 안에 담긴 내용을 제거해볼까요? 파이썬 문자열 객체에는 `split()` 함수가 있습니다. 이 함수를 써서 여는 괄호 "(" 문자를 기준으로 문자열을 둘로 나눈 뒤 앞 부분(0번째 조각)을 취하면 괄호 뒷 부분을 제거할 수 있습니다.


```python
"14,000원(10%+5%)".split("(")
```




    ['14,000원', '10%+5%)']




```python
"14,000원(10%+5%)".split("(")[0]
```




    '14,000원'



"원"이라는 글자와 쉼표를 제거하면 숫자만 남습니다.


```python
"14,000원(10%+5%)".split("(")[0].replace('원', '').replace(',', '')
```




    '14000'



이제 숫자만 남은 문자열들을 정수로 바꿔줍시다.


```python
int("14,000원(10%+5%)".split("(")[0].replace('원', '').replace(',', ''))
```




    14000



해당 코드를 함수로 만들어볼까요?


```python
def to_int(raw):
  nums = raw.split("(")[0].replace('원', '').replace(',', '')
  return int(nums)

to_int("14,000원(10%+5%)")
```




    14000



이제 원래 코드에 적용해봅시다.


```python
books = bs.select('#bestList > ol > li')

titles = []
prices = []
for book in books:
  # "p:nth-of-type(3)"은 li의 자식 중 세번째 p 엘리먼트를 찾아줍니다.
  title = book.select_one('p:nth-of-type(3) a').text
  titles.append(title)
  price = book.select_one('p.price').text
  prices.append(to_int(price))

prices
```




    [14400,
     15120,
     12420,
     12420,
     9450,
     19800,
     12420,
     12150,
     18900,
     11520,
     10800,
     4500,
     13050,
     11520,
     12420,
     18900,
     13500,
     13500,
     9450,
     11610,
     10710,
     14400,
     10800,
     16920,
     12600,
     12420,
     15120,
     11700,
     10710,
     12600,
     19800,
     8820,
     15300,
     15120,
     11700,
     13320,
     13500,
     12150,
     13320,
     8820]



리스트 컴프리헨션을 써서 코드를 줄여볼까요?


```python
books = bs.select('#bestList > ol > li')
titles = [b.select_one('p:nth-of-type(3) a').text for b in books]
prices = [to_int(b.select_one('p.price').text) for b in books]
```

DataFrame에 넣어봅시다.


```python
import pandas as pd

df = pd.DataFrame(
    {'title': titles, 'price': prices},
    columns=['title', 'price']
)
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
      <th>title</th>
      <th>price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>역사의 역사</td>
      <td>14400</td>
    </tr>
    <tr>
      <th>1</th>
      <td>열두 발자국</td>
      <td>15120</td>
    </tr>
    <tr>
      <th>2</th>
      <td>죽고 싶지만 떡볶이는 먹고 싶어</td>
      <td>12420</td>
    </tr>
    <tr>
      <th>3</th>
      <td>모든 순간이 너였다</td>
      <td>12420</td>
    </tr>
    <tr>
      <th>4</th>
      <td>설민석의 한국사 대모험 7</td>
      <td>9450</td>
    </tr>
  </tbody>
</table>
</div>



전체 코드를 한 번에 모아볼까요?


```python
from urllib import request
import pandas as pd
from bs4 import BeautifulSoup

url = "http://www.yes24.com/24/category/bestseller"
with request.urlopen(url) as f:
  charset = f.headers.get_content_charset()
  html = f.read().decode(charset)

def to_int(raw):
  nums = raw.split("(")[0].replace('원', '').replace(',', '')
  return int(nums)

bs = BeautifulSoup(html, 'html5lib')
books = bs.select('#bestList > ol > li')
titles = [b.select_one('p:nth-of-type(3) a').text for b in books]
prices = [to_int(b.select_one('p.price').text) for b in books]

df = pd.DataFrame(
    {'title': titles, 'price': prices},
    columns=['title', 'price']
)
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
      <th>title</th>
      <th>price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>역사의 역사</td>
      <td>14400</td>
    </tr>
    <tr>
      <th>1</th>
      <td>열두 발자국</td>
      <td>15120</td>
    </tr>
    <tr>
      <th>2</th>
      <td>죽고 싶지만 떡볶이는 먹고 싶어</td>
      <td>12420</td>
    </tr>
    <tr>
      <th>3</th>
      <td>모든 순간이 너였다</td>
      <td>12420</td>
    </tr>
    <tr>
      <th>4</th>
      <td>설민석의 한국사 대모험 7</td>
      <td>9450</td>
    </tr>
  </tbody>
</table>
</div>



URL만 넣으면 BeautifulSoup 객체를 만들어주는 코드도 함수로 만들면 좋겠습니다.


```python
from urllib import request
import pandas as pd
from bs4 import BeautifulSoup

def load_url(url):
  """URL의 HTML 문서를 받아와서 BeautifulSoup 객체 생성"""
  with request.urlopen(url) as f:
    charset = f.headers.get_content_charset()
    html = f.read().decode(charset)
  return BeautifulSoup(html, 'html5lib')

def to_int(raw):
  """Yes24의 책 가격 문자열을 정수로 변환"""
  nums = raw.split("(")[0].replace('원', '').replace(',', '')
  return int(nums)

bestseller_url = "http://www.yes24.com/24/category/bestseller"
bs = load_url(bestseller_url)
books = bs.select('#bestList > ol > li')
titles = [b.select_one('p:nth-of-type(3) a').text for b in books]
prices = [to_int(b.select_one('p.price').text) for b in books]

df = pd.DataFrame(
    {'title': titles, 'price': prices},
    columns=['title', 'price']
)
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
      <th>title</th>
      <th>price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>역사의 역사</td>
      <td>14400</td>
    </tr>
    <tr>
      <th>1</th>
      <td>열두 발자국</td>
      <td>15120</td>
    </tr>
    <tr>
      <th>2</th>
      <td>죽고 싶지만 떡볶이는 먹고 싶어</td>
      <td>12420</td>
    </tr>
    <tr>
      <th>3</th>
      <td>모든 순간이 너였다</td>
      <td>12420</td>
    </tr>
    <tr>
      <th>4</th>
      <td>설민석의 한국사 대모험 7</td>
      <td>9450</td>
    </tr>
  </tbody>
</table>
</div>


