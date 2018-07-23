# 180703_6일차 

## 오전 수업 파이썬 - 애란쌤 

- 파이썬 공부 참고 사이트 : https://wikidocs.net/5

### 1. 지난수업 피드백

“컴퓨터는 임의로 하는걸 못한다"에 대한 부연 → 진정 임의로 하는걸 못한다는 의미, 사람을 속일 정도의 임의적 패턴을 만드는 것은 사람보다 컴퓨터가 잘해요 :)

“직관 보다는 데이터” → 직관과 데이터의 조화.

***마크다운* 문법** 

문자 드래그 => 커맨드 + B = 진하게 

문자 드래그 => 커맨드 + I = 이탤릭체 



## 2. 파이썬소개

* 파이썬 : 1991년에 Guido van Rossum이 개발한 프로그래밍 언어의 한 종류. 데이터 분석, 과학 계산, 웹 프로그래밍 등에 주로 쓰임.



**수 많은 언어들...몇 개인지 세어보려면? 자바스크립트로 구현 **

~~~
// Javascript

let selector = '.div-col.columns.column-width ul li a';

let links = document.querySelectorAll(selector);

for(let i = 0; i < links.length; i++) { 

 console.log(links[i].textContent);

}
~~~

**파이썬의 장점**

1. 데이터 수집, 분석, 실제 웹 서비스에 적용하기 까지의 모든 과정을 한 언어에서 끝낼 수 있음. 
2. 파이썬은 glow language 역할도 한다. (접착제언어) <= 핵심언어들은 다른언어로 짜고 이어붙이기 좋다.(인간과 가까운 언어이다.)



**Scratch에서 파이썬으로:**

* [Blockly](https://blockly-demo.appspot.com/static/demos/code/index.html)
  * “Hello World” 만들어보기
  * 블럭이 각 언어로 어떻게 변환되는지 살펴보기. 특히 파이썬과 다른 언어들을 비교해보기
  * [페어] Blockly로 1부터 100까지 모두 더한 값 출력하기
  * [페어] Blockly로 1부터 100사이에 존재하는 모든 3의 배수의 평균을 출력하시오.
    * a.1부터 100사이에 존재하는 모든 3의 배수의 '합'을구한다.
    * b.1부터 100사이에 존재하는 모든 3의 배수의 ''개수''를 구한다
    * c. a와 b를 나눈다 (평균구하기)






## 오후 수업 파이썬 - 애란쌤

## [PythonTutor](http://www.pythontutor.com/live.html#mode=edit)

shift + enter : 실행

Sum (range(100)) : 0~99 까지 만들고 더해라 1. PythonTutor → 파이썬 코드 단계적으로 실행해보기 

### (화면 하단 옵션에서 "render all objects on the heap" 선택)

ㄴ 코드를 한 줄씩 써가면서 어떻게 내부적으로 작동하는지를 볼 수있는 사이트



녹색화살표 : 실행된 코드

빨간화살표 : 이번에 실행될 



설정 바꿔주기 : objects 나오도록




**'=' : asignment = 대입연산**

**'n = 0'  대입문(asignment satatement)**

**' 0 '<- 정수 literer , literer 은 '수식'으로 본다.**

**literer 0과 object 0 은 다른개념임**

**모든 expression(수식)은 제대로 쓰였는지 평가되고 평가값이 메모리에 담긴다. **



평가해서 결과를 15라고 평가값을 내고 메모리(변수)에 담는다!

ex) 메모리에 15 라는 정수를 넣기 위해서 파이썬으로 표현할 수 있는 방법은 여러가지가 있다.

그냥 정수 literer 15 를 써도 15가 담기고, 10 + 5 라고 써도 object에는 15가 담기고

0xF 라고 써도 16진법으로 15가 담긴다. 


진한 파란색 글자 : literer / 파란색 글자 : 키워드(예약어) , 변수이름으로 써서는 안된다. Ex) for, in ... 

~~~
n = 0

total = 0

for i in range(100):

    total = total + i

    n = n + 1

average = total / n

print(average)

~~~

* 문법 1 : ( )안에 담겨있는 원소의 개수만큼 for문 안에있는 블럭을 반복한다. 

​		for i in ragne(5):

​		for i in rage[0,1,2,3,4]:	

​		(5) = [0,1,2,3,4] : 0부터 4까지의 원소를 배열로 갖는다.

* total 의 평가값 = 0 / range(100)의 평가값 = [0,1,2,3,4, ... , 99]
* 관습적으로 들여쓰기는 스페이스바 4개 씀 (Tab과 섞어스면 에러난다.)
* 참조(화살표)가 없는 objecet는 없앤다. (garbage collector) <= 메모리를 자동으로 정리해줌 
* integer: 정수 '2' / floting : 부동소수점 '2.0'
* 정수 / 정수 = 부동소수점 (자동으로 파이썬이 해줌)



## 2. Colab 가지고 놀아보기

**범죄통계 데이터 살펴보기**

https://colab.research.google.com/drive/1SDpv8E4Wx2En5C9zF9xsAWRqZbqKX9Hf#scrollTo=nASastysYwq_&forceEdit=true&offline=true&sandboxMode=true



1. 텍스트추가 하면 마크다운언어로 쓸 수있습니다. 


2. 데이터 불러오기

   ~~~
   import pandas as pd
   
   import numpy as np
   
   df = pd.read_csv('https://s3.ap-northeast-2.amazonaws.com/data10902/messy/crime_clean.csv')
   
   df.tail()
   
   ~~~

   df.tail()   

   Df 는 거대한 데이터테이블 만듬

   데이터 테이블의 마지막 5줄만 출력하는것

## 3. 파이썬으로 총점과 평균 구해보기. 

**총점과 평균 구하기. 데이터 = 70점, 55점, 90점, 85점, 100점, 77점**

* [페어] 총점과 평균을 구하는 프로그램을 Colab에 작성하세요. 파이썬 문법을 모르겠거나 막히는 부분이 있으면 Blockly와 PythonTutor를 활용해보세요

https://colab.research.google.com/drive/1iPZgKZ4_FBOV-iTiXGW4ogSGgAztU2rI



~~~
scores = [70 ,55 ,90 ,85 ,100 ,77]

n = len(scores)

total = 0 

for i in scores:

    total = total + i

print(total)

print(total/n)

~~~

--------

~~~
scores = [70 ,55 ,90 ,85 ,100 ,77]

n = 0

total = 0 

for i in scores:

    total = total + i

    n = n + 1 

    

print(total)

print(total/n)

~~~



## 4. 표본분산과 표본표준편차 계산하기 

* [시연] 총점과 평균을 **함수**로 분리하기

  * 재귀적 결합 : 한번 부품으로 만들어놨으면 가져다가 바로 쓸 수 있게 하기 = 라이브러리 만들기 

    * 1. sum함수(function)만들기 => **def calc_sum()**

      함수이름은 보통 '동사' 형태로 한다.

      반복되어야 하는 명령문이면 뒤에 : 찍기 

      ​     def calc_sum(numbs):

      ​      result = 0 
            for num in numbs:
                result = result + num
            return result 

      ​    scores = [50,60,70]
          total = calc_sum(scores)
          print(total)

      

      ( Clac_sum(scores) : 함수 호출하고 평가한값(return)이 나온다. ) 
      

      ( 회색은 사실 이미 사라진 frame 이다.)

      2. 길이 함수 만들기 

      3. 평균만드는 함수 만들기 

         ~~~
         def calc_sum(numbs):
         
           result = 0 
         
           for num in numbs:
         
               result = result + num
         
           return result 
         
         def calc_len(numbs):
         
           result = 0 
         
           for num in numbs:
         
               result = result + 1
         
           return result 
         
         def calc_average(numbs):
         
           total = calc_sum(numbs)
         
           lengh = calc_len(numbs)
         
           return total/lengh
         
         scores = [50 ,60 ,70 ]
         
         total = calc_average(scores)
         
         print(total)
         
         ~~~

         

         

  









