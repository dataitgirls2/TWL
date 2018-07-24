![1531962444289](C:\Users\wolever\Desktop\데잇걸즈2\1531962444289.png)

# 180719

## 오전수업

### crawling 과제 feedback

#### 이은지님,박진영님,김희영님 과제 짱짱맨

`df = pd.read_html(url, flavor='html5lib')` : url의 표를 불러와서 데이터프레임으로 만들어 줌.

**beautifulsoup** : for 루프 안돌리고 원하는 부분을 뽑아낼 수 있음. 하지만 결과 앞뒤에 빈줄이나 공백이 있음.

`text.strip()` : text 의 앞뒤 공백 없어지는 함수.

`text.replace('\n', ' ')` : 줄바꿈 문자를 공백으로 바꾸어 줌.

`text.replace('\n', ' ').replace('\r', ' ' )` : \n과 \r을 공백으로 바꿈.

#### 함수로 나누기

코딩하다가 복붙을 많이 사용하게 된 순간이 함수를 만들어야 하는 시점(?)

#### TO DO 리스트 만들고 작업하기, 중간 결과물 공유하기

잘 망하는 방법? 특정 기능에 대한 데이터베이스씩 조금씩 나누어서 기능 구현. 실제 사용자들이 써봐야 진짜 피드백을 받을 수 있음. 데이터베이스만 구성하다 끝나버리면 잘 된 프로젝트인지 아닌지 1도 모름.

**경제학의 게임이론 :** 
non-zerosum game : 내가 잘되고 다른 사람도 잘될수있음. 혹은 둘 다 질 수도 있음(win-win)
zerosum game : 상대평가를 하는 수업 - 내가 잘하면 다른 사람은 떨어짐.

#### 서로 다른 웹 문서의 내용을 하나로 합치기

#### 시각화

데이터 클렌징

#### 질문에서 시작하기

탐색적 데이터 분석 : 하나의 질문을 상정한 후 시작함.



### 수업의 목표 - 여긴어디 나는누구

매번 웹사이트를 방문하여 데이터 수집이 귀찮다. urllib패키지의 request모듕릐 urlopen함수를 쓰면 주소를 읽어와서 파이썬 문서로 만들어줌.
그중 제목에 해당하는 글자 수를 세어서 뽑아낼 수도 있긴 한데 X

우리는 children의 두번 째 행의 두 번째 text를 뽑아내고 싶다. 이렇게 한 것.

dom의 children > 루프 후 title찾고 등.. 이렇게 했음. > 나무구조를 만들었음.

###### 크롤링을 어디에 사용할 수 있을까용?

원하는 정보를 실시간으로 얻기, 원격 서버를 만들어서 원하는 정보를 볼 수 있음.

##### 실습

beautifulsoup이 안깔려 있을 경우`!pip install beautifulsoup4` 해주기

```python
from urllib import request
from bs4 import BeautifulSoup

url = "https://www.naver.com"
with request.urlopen(url) as f:
  html = f.read().decode('utf-8')

bs = BeautifulSoup(html, 'html5lib')
title = bs.select_one('title').text
print(title)

title_element = bs.select_one('title')
title_text = title_element.text
print(title_text)
```

#### CSS선택자(selector)로 원하는 정보 뽑아내기

##### CSS란?

- 스타일이 바뀜
- 전산학(컴퓨터 과학)에서 '관심사의 분리' 분야. 큰 덩어리를 작은 덩어리들로 나누고, 각각의 덩어리들이 자기가 맡은 일만 열심히 할 수 있도록 함.
- CSS만으로도 사이트를 간단히 바꿀 수 있게 됨.
- 글자색, 배경색 등을 줄줄이 써준다면, 셀렉터로 선택됨 엘리먼트들에 적용.
- `h1, h2, h3, h4, h5, h6 { font-weight: bold; } `모든 제목들한테는 글자를 굵게 써줘라. `h1, h2, ..., h6` 부분이 셀렉터라고 함.
- CSS에서는 스타일을 바꾸어 주었지만 우리는 그걸로 크롤링을 할거임.

##### 애란이네 책방 실습

- <여는태그> element </닫는태그>

- element안에는 또다른 node나 text node가 들어갈 수 있음.

- 노드에는 항상 헤드와 바디가 잇음.

- 몇몇 엘리먼트에는 여는 태그 안에 다른 정보가 들어잇는데 attribute라고 부름. 항상 key = 'value' 형식으로 쓰여짐.

  (eg) `<p class="highlight">`

  유일한 식별자를 부여할 때 id= 속성을 사용.

  강조하고 싶은 것을 class="highlight"로 정해주었음.

  한 문서 안에 같은 클래스를 갖는 애들은을 여러개 만들 수 잇ㅇ므.

  선생님 코드에서는 강조하고싶은 것에 "highlight"써준 것을 볼수있음.

- class 셀렉터 .

- id 셀렉터 #

- element는 그냥 쓰면 됨.

- `ul .highlight` ul의 자손들 중에 highlight클래스가 있는 애들을 고름.

  ul이면서 카테고리 클래스(공백을 써준 경우)

  ul의 모든 자손들을 선택.

  공백을 사용한다? : 자손 선택자 (descendant selector)

- body .highlight 와 달리 `body > .highlight` 를 넣어주면 직계자식만 찾음.

  body의 바로 밑에 있는 애들 중 highlight만 찾음.

##### yes 24 실습

![1531969831944](C:\Users\wolever\AppData\Local\Temp\1531969831944.png)

- 안변할것 같은 셀렉터를 적절히 골라서 크롤링에 사용해랏...

  예를들면 goods_list  등



## 오후수업 (배로선생님)

### 머신러닝, 시각화와 자연어처리

#### 지난 수업 회고

- 로컬에 다운로드 받아서 `git push -u upstream master` 로 마스터 브랜치에 push해주기

  이렇게 해야 컴플릭 X

- 10 minutes 2 pandas 혼자 공부하다가 뭔가 문제가 있으면 이슈로 등록해주고, 그 다음 조가 수정해주기

- 쥬피터 노트북에 마크다운으로 저장하는 기능이 있음.

  til이나 twl 바로 올리고 싶을 경우 사용하면 됨.



#### 데이터 시각화 실습(plotnine)

`!pip show plotnine` : plotnine의 경로 등 정보를 확인.

`pip install -q 'plotnine[all]'`

`regex` (regular expression) : 정규표현식

###### plotnine

`as` : 에스테틱 = 미학적 작용 

`geom` : 지오메트릭_포인트/박스플랏

`stats_smooth` `facet_wrap` : 관련된 여러 옵션들

###### 시계열 데이터 실습



#### 최지영님 자연어 처리 특강

https://github.com/jiyoung-choi/TIL/blob/master/%ED%95%9C%EA%B5%AD%EC%96%B4%20%EB%8B%A8%EC%9C%84.md

###### 형태소 / 어절 / 단어 / 음절 위주의 4. 5. 6. 7. 문항

단어와 형태소의 가장 큰 차이점 :  자립성(!)

오냐 > 는 하나의 형태소
웬걸 > 은 두 개의 형태소 ('웬', '걸')

형태소는 하-, -아(여), 아니-, -라 등 -(대시)를 써서 독립적으로 사용할 수 없다는 것을 나타내 줌.
단어의 경우 자립성이 있기 때문에 은, 는, 이, 가 는 -(대시)를 써주지 않음.

체언 : 體 몸 (체)

음운 : 음소와 운소가 합쳐진 내용.

- 음소 : 단순한 기호들.

- 운소 : 높낮이, 길이, 세기 등을 포함하여 뜻이 달라지는 소리의 단위.

복합명사 : 단일명사+단일명사 / 명사+명사 등 명사 여러개가 합쳐진 경우.

#### soynlp (자세한 실습은 다음 시간에)

##### KNLP

KoNLPy 패키지는 한국어 자연어 처리에 대하여 더 최적화 되어 있지만...(생략)
'미안하다 Java'
여러가지 형태소 분석기(트위터, 매캡, 한나눔 등)를 사용하고 있음.

다른 분석기들은 자바나 C++이 설치되어 있어야, 또 파이썬에서 자바를 설치하여 사용하게 해 주는 툴을 설치해 주어야 함. **!!설치 지옥!!**
하지만 KoNLPy는 순수 파이썬으로 작성되어있음.

##### soynlp

Summary: Unsupervised Korean Natural Language Processing Toolkits 

konlpy가 가지고 있는 단점들을 꽤나 보정하여 신조어 등도 비지도학습(Unsupervised Learning)으로 학습하게 했음.

로컬에서는 따로 설치 해주어야 함.

정규 표현식을 사용하는 패키지.

`soynlp.tokenizer` : 특정 문장을 '토큰화' 하는 것.
보통 어절 단위로 띄어쓰기를 하는 편. 문자들을 이해할 수 없어서 벡터화 시켜 주기 위하여 토큰화를 진행함.

역슬래시로 문자열로 인식시켜야 해서 \\\n 을 인식시키려고 역슬래시 네 개 적어줌.

###### 각자의 관심사로 워드클라우드 그리기 (과제)

있는, 이런, 그리고, 합니다 등의 단어는 필요없듬 > 함수가 만들어져 있음











