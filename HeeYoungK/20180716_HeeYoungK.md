API(Application programming Interface)
인간이 얼마나 쉽게 쓸 수 있는가
인간의 attention과 memory의 한계 측면

Pythontutor 파란 글씨 : 예약어
Built-in함수

* Shuffle 과제 review

1. import random

def shuffle(data):
    copied = data[:]
    random.shuffle(copied)
    return copied

data = [1, 2, 3, 4, 5]
copied = shuffle(data)
copied


2. 비복원 임의추출(random sampling without replacement)
import random

data = [1, 2, 3, 4]
random.sample(data, 4)

Magic number 4는 len(data)로 바꿔주기!


3. def Sortbylen(d): \# 인자의 길이 순으로 리스트를 출력
    e = sorted(d, key=len)
    return e
        
d= ["chicken", "bentto", "pizza", "chinese", "icecream", "milk", "pretzel"]
print(Sortbylen(d)) 


 이름 수정
def Sortbylen(data):
    result = sorted(d, key=len)
    return result
        
data= ["chicken", "bentto", "pizza", "chinese", "icecream", "milk", "pretzel"]
print(Sortbylen(data)) 


\# Sortbylen -> sort_by_len
\# SortByLen : camal case (대문자로 시작하는것 파스칼 케이싱)
\# sortByLen : camal casing 
\# sort-by-len (케밥 케이싱)
Uppercase, undercase. 줄간격=레딧(납)
파이썬은 Case sensitive 언어

언어마다 다른데
파이썬은 함수 이름 소문자로 시작, 언더바 사용
def sort_by_len(data):
    Return sorted(d, key=len)
        
data= ["chicken", "bentto", "pizza", "chinese", "icecream", "milk", "pretzel"]
print(Sortbylen(data)) 


3. 카드 셔플 방식
import random

a = [1, 2, 3, 4, 5]

def shuffle2(data):
  n = len(data)
  
  shuffled_data = data[:]
  
  for i in range(20): # 매직 넘버 설정 중요!
    random_index = random.randint(0,n-1)  
    random_index2 = random.randint(0,n-1)
    value = shuffled_data.pop(random_index)
    shuffled_data.insert(random_index2,value)
  
  return shuffled_data

print(a)
print(shuffle2(a))



4. 
import random                                        \# Random 모듈 호출

data = ["Heroes", "Bears", "Eagles", "Twins", "Wyverns", "Lions", "Giants", "Dinos", "Tigers", "Wiz"]
data4 = []                                           \# 결과값 입력을 위한 리스트 생성

def shuffle2(data):
    while True:                                      \# 무한 반복. 이 부분을 for 문으로 처리하면 결과값 리스트가 모두 채워지지 않아도 함수가 끝나는 오류가 발생.
        if len(data) == len(data4)):        \# 원본 리스트(data)와 결과값 리스트(data4)의 인덱스가 동일해지면...
            break                                    \# 함수 종료
        else:                                        \# 원본 리스트(data)와 결과값 리스트(data4)의 인덱스가 동일하지 않으면...
            choice = random.choice(data)             \# 원본 리스트(data)의 요소 중 하나를 random하게 선택
            if choice in data4:                      \# 선택된 요소(choice)가 결과값 리스트(data4)에 이미 존재한다면...
                pass                                 \# 아무 변화 없이 pass
            else:                                    \# 선택된 요소가 결과값 리스트에 없다면...
                data4.append(choice)                 \# 결과값 리스트에 선택된 요소를 추가
    return data4

data_4th = shuffle2(data)
print(data_4th)
print(data)

\*  Information hiding

선생님이 코딩하시는 방식. 주석 먼저!
def shuffle():
  \# 어쩌고를 한다
  asdasdasf
  \# 저쩌고인동안
  asdasd
  \# 이거를 하고
    asdasd
  \# 저거를 한다
    asdasd
  
5. data.copy() = data[:]

from random import randint

def shuffle3(data):
  new_list = data.copy()
  result = []
  x = 0
  for x in range(len(data)):
    index = (randint(0, len(new_list) - 1))
    result.append(new_list[index])
    del new_list[index]
  print(result)
  
shuffle3([1, 2, 3, 4, 5])

피셔-예이츠 셔플링(Fisher-Yates shuffling) 알고리즘 소개

* Ronald Fisher와 Frank Yates가 1938에 <Statistical tables for biological, agricultural and medical research>에서 소개한 절차. “난수표"랑 종이와 연필이 필요.
* 알고리즘 시각화, 알고리즘 수행 결과의 시각화 (데이터 시각화의 또다른 활용 사례)

# 인터넷, 웹, 웹브라우저
 https://www.youtube.com/watch?v=J8hzJxb0rpc

인터넷(The Internet):
* 컴퓨터 네트워크들의 네트워크(inter-network)
웹(web) 또는 월드 와이드 웹(World Wide Web; WWW)
* HTTP(HyperText Transfer Protocol)로 통신하는 컴퓨터들의 네트워크.
* 프로토콜? 양방향 라디오 통신 프로토콜 사례: Over, Roger, Affirmative, Negative, Out
* HTTP는 인터넷 프로토콜 “위에" 구현되어 있음. 웹은 인터넷의 일부
* URL(Uniform Resource Locator):
    * protocol://user@host:port/path?query#fragment
    * https://www.google.com/search?q=test
* Hyperlink, Hypertext, HTML (HyperText Markup Language)
* 웹 문서(HTML)의 구조 3D로 보기 - Firefox version 46에서 가능
브라우저가 하는 일:

* 인간의 명령을 해석하여 원격 컴퓨터로 HTTP 요청을 보내기
* 원격 컴퓨터의 HTTP 응답을 해석하여 인간에게 보여주기
* 브라우저는 “사용자 대리인(user agent)”의 일종
from urllib import request #import:다른 사람이 만들어 놓은 파이썬 코드를 불러오는 것 , urllib 패키지(디렉토리)에서 request라는 모듈(파이 확장자 파일)을 호출

url = "https://www.naver.com” #url은 변수
with request.urlopen(url) as f: #f라는 변수에 with 뒤가 만든 자원을 담았다가(할당하고) 블럭이 끝나면 버리겠다(자원 사용을 해제)는 의미의 함수. F is for file. Request:모듈, urlopen:함수.

    html = f.read().decode('utf-8’) #아스키 코드. 라틴 계열이 아닌 문자를 쓸 때는 read()에 문자를 담아와서 utf-8이라는 방식으로 한글을 해석을 해주는 것.
    print(html)



from urllib import request as req
-> 이후에 req로 모듈이름을 줄여서 사용 가능



# 크롤링2
Xml : html과 비슷한 계열
HTML DOM
Css selector : 작은 요소들을 뽑아낼 수 있음

+ 저작권, 라이선스
CCL : Creative Commons lisence
CC BY : 출처 밝히기
NC : 판매금지 (비영리)
ND : 변경금지
SA : 동일조건라이선스로 변경허락

* 로봇 배제 프로토콜 robots.txt
https://www.daum.net/robots.txt
User-agent: *
Disallow: /


+ 마크업 언어
\> 인용
HTML(HyperText Markup Language)이란? 하이퍼텍스트에 대한 마크업을 표기하기 위한 인공 언어.
하이퍼텍스트 : 하이퍼링크가 담겨있는 문서

<!DOCTYPE html>
<html> <!-- <에서>사이는 태그라고 부름. <여는 태그> element(children) </닫는 태그> -->
<head>
  <meta charset="utf-8">
  <title>'돌아온' 오늘 MBC 뉴스의 첫 앵커 멘트는 '사과'였다</title>
  <style>
  h1 {
    color: red;
    transform: rotateY(30deg)
  }
  </style>
</head>

<body>
\<h1>2017년 12월 08일 15시 27분, <a href="https://herwan.com">허완 기자</a> <!-- 앵커 -->, 허핑턴포스트코리아</h1>

<blockquote>
<p>“저희 MBC는 신임 최승호 사장의 취임에 맞춰, 오늘(8일)부터 뉴스데스크 앵커를 교체하고 당분간 뉴스를 &amp;lt 임시 &lt; 체제로 진행합니다. 저희들은 재정비 기간 동안 MBC 보도가 시청자 여러분께 남긴 상처들을 거듭 되새기며, 철저히 반성하는 시간을 갖겠습니다.</p>
<p>치밀한 준비를 거쳐 빠른 시일 안에 정확하고 겸손하고 따뜻한 뉴스데스크로 시청자 여러분께 다시 인사드리겠습니다.”</p>
</blockquote>

<p>8일 저녁 8시, MBC 메인뉴스인 '뉴스데스크' 대신 'MBC뉴스'라는 타이틀로 방송된 뉴스에서 임시 앵커를 맡은 김수지 아나운서는 짤막한 사과문을 읽어내려갔다.<p>
</body>
</html>



HTML은 긴 문자열. 긴 문자열을 분석(parse)하여 나무구조(tree structure)로 만든 것이 HTML DOM(Document Object Model) 

import html5lib
document = html5lib.parse("<p>Hello World!")

dir(dom)
엘리먼트 태그 이름 얻어오기
Element의 text 얻어오기

!pip install html5lib #package installer, linux 명령어
from urllib import request
import html5lib

url = "https://www.naver.com"
with request.urlopen(url) as f:
  html = f.read().decode('utf-8')
  
dom = html5lib.parse(html) #html element
children = dom.getchildren() #head와 body가 담긴 list
head = children[0] #head는 [0], body는 [1]

head_children = head.getchildren()
for element in head_children:
  if element.tag[-5:] == 'title' :
    print(element.text)


Type() —> 어떤 유형인지 조회


과제 알림 5m 다음주 수요일까지

과제. 오늘 배운 내용을 참고하여 다음 요구사항을 구현하는 노트북 파일을 만들고 과제 폴더에 공유하세요.
* 내가 평소 자주 가는 사이트에서 원하는 정보만 추출하여 화면에 출력(print 함수)하세요.
* 반드시 robots.txt와 사이트 저작권 정책을 살펴보고 정책에 위반되지 않도록 주의해주세요.
선택과제. (과제1을 하고 시간이 남으면) 원하는 정보를 추출한 결과를 잘 정리하여 판다스 DataFrame에 담아보세요.
