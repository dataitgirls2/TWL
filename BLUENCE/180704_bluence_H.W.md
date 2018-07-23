# 180704_Homework_Python3 

## 03장 프로그램의 구조를 쌓는다!

**참고사이트 :  https://wikidocs.net/20**



### 03 - 1. if문 

* if 문의 기본 구조 

~~~
if 조건문:
    수행할 문장1
    수행할 문장2
    ...
else:
    수행할 문장A
    수행할 문장B
    ...
    
~~~



* 들여쓰기 

if문을 만들 때는 if조건문: 바로 아래 문장부터 if문에 속하는 모든 문장에 들여쓰기(indentation)를 해주어야 한다. 

들여쓰기는 Spacebar 와 Tab을 혼용해서 쓰지 말자. 

요즘 파이썬 커뮤니티에서는 들여쓰기를 할 때 공백( Spacebar ) 4개를 사용하는 것을 권장한다.

* 조건문 다음에 콜론(:) 을 잊지 말자!

* 조건문이란 ? : 참과 거짓을 판단하는 문장을 말한다. 자료형의 참과 거짓에 대해서 살펴보자

  숫자 : 참 (0이 아닌 숫자) / 거짓 ( 0 )

  문자열 : 참 ("abc") / 거짓 ("")

  리스트 : 참 ( [1.2.3] ) / 거짓( [] )

  튜플 : 참( (1,2,3) ) / 거짓 ( () )

  딕셔너리 : ( {"a":"b"} ) / 거짓 ( {} )

  ~~~
  money = 1
  if money :
  ~~~

   여기서 money는 '참' 이므로 if 문 이 수행된다.



* 비교연산자 : 조건문을 판달할때 ( 참인지 거짓인지 ) 비교연산자를 쓰는 경우가 훨씬 많다. 

  ( < , > , == , != , >= , <= )

  

* and , or , not : 조건문을 판단할때 연산자로 쓰인다. 

  * not x : x가 거짓이면 참이다 

* x in s , x not in s : 파이썬에서 제공되는 조건문  **<- 처음본다 !**

  x in 리스트 , 튜플 , 문자열 

~~~
>>> 1 in [1,2,3]
True 
>>> 1 not in [1,2,3]
Flase

>>> pocket = ['paper', 'cellphton' , 'money']
>>> if 'money' in pocket:
        print("택시를 타고 가라")
    else :
        print("걸어가라")
택시를 타고 가라 
~~~

* 조건문에서 아무 일도 하지 않게 설정하고 싶다면? = **'pass' 를 쓴다** 

  ( 조건문의 참, 거짓에 따라 실행할 행동을 정의할 때, ''아무런 일도 하지 않도록'' 설정하고 싶다면 )

~~~
>>> pocket = ['paper', 'cellphton' , 'money']
>>> if 'money' in pocket:
        pass
    else :
        print("걸어가라")
        
~~~

**pocket 이라는 리스트 안에 money라는 문자열이 있기 때문에 if문 다음 문장인 pass가 수행되고**

**아무론 결과 값도 보여 주지 않는다.**



* 다양한 조건을 판단하는 elif  : 조건문 2번 이상 판단해야 하는 경우사용

   **' elif ' 는 이전 조건문이 '거짓'일 때 수행된다**

  **' elif ' 는 개수에 제한 없이 사용할 수 있다.**

  ~~~
  >>> pocket = ['paper', 'cellphone']
  >>> card = 1
  >>> if 'money' in pocket:
  ...      print("택시를 타고가라")
  ... elif card: 
  ...      print("택시를 타고가라")
  ... else:
  ...      print("걸어가라")
  ...
  택시를 타고가라
  ~~~

  

* [응용] if문을 한 줄로 작성하기 

~~~
>>> pocket = ['paper' , 'money' , 'cellphone' ]
>>> if 'money' in pocket : pass 
    else: print("카드를 꺼내라")
    
~~~

 **if문 다음의 수행할 문장을 콜론(:) 뒤에 바로 적어 주었다. else문 역시 마찬가지이다.**

**때때로 이렇게 작성하 는 것이 보기 편할 수 있다.**



* 조건부 표현식 (conditional expression).  **< = 처음본다 ! **

  파이썬의 조건부 표현식을 이용하면 다음과 같이 간단히 표현할 수 있다. 

~~~
조건문이참인경우 if 조건문 else 조건문이거짓인경우

message = "success" if score >= 60 else "failure"

( score 가 60 이상인겨우 success가 출력되고 아니면  failure를 출력한다. )
~~~



## 연습문제 - if문 사용

**[문제1] 조건문 1**

홍길동씨는 5,000원의 돈을 가지고 있고 카드는 없다. 

~~~
money = 5000
card = False
~~~

홍길동씨는 택시를 타고 목적지까지 가려고 한다. 목적지까지 가기 위해서는 카드를 소유하거나, 4000원의 택시요금이 필요하다. 홍길동씨가 택시를 탈 수 있는지 판별하는 조건식을 작성하고 그 결과를 출력하라.

[풀이]

~~~
monet = 5000
card = False 
if money >= 4000 or card = True:
    "택시를 타자"
else:
    "걸어가자"
~~~



**[문제2] 조건문 2**

홍길동씨의 행운권 번호는 23번 이라고 한다. 다음은 행운권 당첨번호 리스트이다. 

~~~
lucky_list = [1, 9 ,23 , 46]
~~~

홍길동씨가 당첨되었다면 " 야호 " 하는 문자열을 출력하는 프로그램을 작성하라

[풀이]

~~~
홍길동 = 23 
lucky_list = [1, 9 ,23 , 46]
if 홍길동 in lucky_lisst print("야호") 
~~~



**[문제3] 홀수 짝수 판별** 

주어진 수가 짝수인지 홀수인지 판별하는 프로그램을 작성하시오.

~~~
a = input()

if a%2 == 0:
	print("짝수")
else:
    print("홀수")
   
  
~~~

----

## 03 - 2. while문

### 기본구조

~~~
while <조건문>:
    <수행할 문장1>
    <수행할 문장2>
    <수행할 문장3>
~~~



* " 열 번 찍어 안 넘어 가는 나무 없다 " 라는 속담을 파이썬 프로그램으로 만든다면 다음과 같이 될 것이다. 

~~~
>>> treeHIT = 0
>>> while treeHit < 10:
        treeHit = treeHit + 1 
        print("나무를%d번 찍었습니다." %treeHit)
        if treeHit == 10:
            print("나무 넘어갑니다.")
            나무를 1번 찍었습니다.
            
나무를 2번 찍었습니다.
나무를 3번 찍었습니다.
나무를 4번 찍었습니다.
나무를 5번 찍었습니다.
나무를 6번 찍었습니다.
나무를 7번 찍었습니다.
나무를 8번 찍었습니다.
나무를 9번 찍었습니다.
나무를 10번 찍었습니다.
나무 넘어갑니다.
~~~



## while문의 기본 구조

반복해서 문장을 수행해야 할 경우 while문을 사용한다. 그래서 while문을 반복문이라고도 부른다.

다음은 while문의 기본 구조이다.

```
while <조건문>:
    <수행할 문장1>
    <수행할 문장2>
    <수행할 문장3>
    ...
```

while문은 조건문이 참인 동안에 while문 아래에 속하는 문장들이 반복해서 수행된다.

"열 번 찍어 안 넘어 가는 나무 없다" 라는 속담을 파이썬 프로그램으로 만든다면 다음과 같이 될 것이다.

```
>>> treeHit = 0
>>> while treeHit < 10:
...     treeHit = treeHit +1
...     print("나무를 %d번 찍었습니다." % treeHit)
...     if treeHit == 10:
...         print("나무 넘어갑니다.")
...
나무를 1번 찍었습니다.
나무를 2번 찍었습니다.
나무를 3번 찍었습니다.
나무를 4번 찍었습니다.
나무를 5번 찍었습니다.
나무를 6번 찍었습니다.
나무를 7번 찍었습니다.
나무를 8번 찍었습니다.
나무를 9번 찍었습니다.
나무를 10번 찍었습니다.
나무 넘어갑니다.
```

> treeHit = treeHit + 1    <=>  treeHit += 1



* While 문 강제로 빠져나가기 = **break문**

while문은 조건문이 참인 동안 계속해서 while문 안의 내용을 반복적으로 수행한다. 하지만 강제로 while문을 빠져나가고 싶을 때가 있다. 예를 들어 커피 자판기를 생각해 보자. 자판기 안에 커피가 충분히 있을 때에는 동전을 넣으면 커피가 나온다. 그런데 자판기가 제대로 작동하려면 커피가 얼마나 남았는지 항상 검사해야 한다. 만약 커피가 떨어졌다면 판매를 중단하고 "판매 중지"라는 문구를 사용자에게 보여주어야 한다. 이렇게 판매를 강제로 멈추게 하는 것이 바로 break문이다.



>  커피 자판기를 파이썬 프로그램으로 표현하기 

~~~
coffee = 10
money = 300
while money:
     print("돈을 받았으니 커피를 줍니다.")
     coffee -= 1
     print("남은 커피의 양은 %d개 입니다." %coffee)
     if not coffee:
         print(" 커피가 다 떨어졌습니다. 판매를 중지합니다.")
         break
~~~

커피의 개수가 0이 되면 if not coffee: 문이 실행되고  break를 만나면 빠져나간다. 



> break문 이용해 자판기 작동 과정 만들기 

money = int(input("돈을 넣어 주세요:")) 라는 문장은

이 문장은 사용자로부터 입력을 받는 부분이고 입력받은 숫자를 money라는 변수에 대입하는 것이라고 알아두자.

~~~
coffee = 10
while True:
    money = int(input("돈을 넣어주세요: "))
    if money == 300:
        print("get a coffee")
        coffee -= 1
    elif money > 300:
        print("%d을 거슬러드리고 get a coffee" % (money-300))
        coffee -= 1
        
    else :
        print("you can't get a coffee")
        print("커피는 %d잔 남았습니다." %coffee)
    if not coffee:
        print("sold out")
        break
~~~



* 조건에 맞지 않는 경우 맨 처음으로 돌아가기  : **continue문**

while문 안의 문장을 수행할 때 입력된 조건을 검사해서 조건에 맞지 않으면 while문을 빠져나간다. 그런데 프로그래밍을 하다 보면 while문을 빠져나가지 않고 while문의 맨 처음(조건문)으로 다시 돌아가게 만들고 싶은 경우가 생기게 된다. 이때 사용하는 것이 바로 continue문이다.

만약 1부터 10까지의 숫자 중에서 홀수만 출력하는 것을 while문을 이용해서 작성한다고 생각해 보자. 어떤 방법이 좋을까?

~~~
a = 0
while a < 10:
    a += 1
    if a % 2 == 0: continue
    print(a)
~~~

>  continue를 만나면 while문 처음으로 돌아갈 수 있다. 
>
> 그러다가 a = 10 이 되면 while 문이 종료된다. 



* 무한 루프

~~~
while True: 
    수행할 문장1 
    수행할 문장2
~~~



## 연습문제 - while문 사용 

**[문제1] 1부터 100까지 더하고 결과를 출력하기**

[풀이]

~~~
a = 0
sum = 0
while a < 100:
    a += 1
    sum = sum + a
    
print("sum")
~~~



**[문제2] 1부터 1000까지의 자연수 중 3의 배수의 합 구하기** 

[풀이]

~~~
a = 1
sum = 0
while a < 1000:
    if a % 3 == 0:
        sum = sum + a 
    a += 1 
    
print(sum)
~~~



**[문제3] 50점 이상의 총합** 

다음은 A학급 학생의 점수를 나타내는 리스트이다. 다음 리스트에서 50점 이상의 점수들의 총합을 구하시오.

A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]

~~~
A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
~~~

[풀이]

```
첫 작성 => 오류 난 코드임 (TypeError: '>=' not supported between instances of 'list' and 'int')

A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
sum = 0
while A:
    if A >= 50:
        sum = sum + A 
        
print(sum)
```

리스트 : 참 ( [1.2.3] ) / 거짓( [ ] ) 

리스트는 참 , 거짓을 1과 0으로만 평가한다. 따라서 50 이상인지는 따질 수 없다. 

A 안에 있는 원소인  20을 뽑아내야  50보다 큰지를 판별 할 수 있을 것이다.

> A.pop()     :  A리스트 안에 있는 원소를 뒤에서부터 하나씩 뽑아낸다. 

~~~
A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]

result = 0
while A:  # A 리스트에 값이 있는 동안
    mark = A.pop()  # A리스트의 가장 마지막 항목을 하나씩 뽑아냄
    if mark >= 50:  # 50점 이상의 점수만 더함
        result += mark

print(result)  # 481 출력
~~~



**[문제4] 별 표시하기1**

while문을 이용하여 아래와 같이 별(`*`)을 표시하는 프로그램을 작성해 보자.

1번째 줄에는 별 1개를 찍고 , 2번째 줄에는 별 2개를 찍고... 4번째 줄에 별 4개 찍기 

~~~
i = 0
while True:
    i += 1  # while문 수행 시 1씩 증가
    if i > 5: break  # i 값이 5보다 크면 while문을 벗어난다.
    print ('*' * i)  # i 값 개수만큼 *를 출력한다.
~~~



**[문제5] 별 표시하기2**

while문을 이용하여 아래와 같이 별(`*`)을 표시하는 프로그램을 작성해 보자.

~~~
출력되는 별의 갯수는 7, 5, 3, 1 이고 앞에 포함되어야 할 공백 갯수는 0, 1, 2 , 3 임을 알 수 있다. 이러한 아이디어를 기반으로 작성한 파이썬 코드는 다음과 같다.

star = 7  # 별의 갯수
space = 0  # 공백의 갯수
while star > 0:
    print(' ' * space + '*' * star)  # 공백 + 별 출력
    star -= 2  # 별의 갯수는 2씩 감소
    space += 1 # 공백의 갯수는 1씩 증가
~~~





## 03 - 2. for문



* for문의 기본구조 

~~~
for 변수 in 리스트(또는 튜플, 문자열):
    수행할 문장1
    수행할 문장2
~~~

* 전형적인 for문 

~~~r
test_list = ['one','two','tree']
for i in test_list:
	print(i)
one , two , tree
~~~

* 다양한 for문의 사용

~~~
>>> a = [(1,2), (3,4), (5,6)]
>>> for (first, last) in a:
...     print(first + last)
...
3
7
11
~~~

a 리스트의 요소값이 튜플이기 때문에 각각의 요소들이 자동으로 (first 와 last)라는 변수에 대입된다.

* for문의 응용

>  "총 5명의 학생이 시험을 보았는데 시험 점수가 60점이 넘으면 합격이고 그렇지 않으면 불합격이다. 합격인지 불합격인지 결과를 보여주시오."

각각의 학생에게 번호를 붙여 주기 위해 number라는 변수를 이용하였다. 

점수 리스트인 marks에서 차례로 점수를 꺼내어 mark라는 변수에 대입하고 for문 안의 문장들을 수행하게 된다. 

우선 for문이 한 번씩 수행될 때마다 number는 1씩 증가한다.

~~~
marks = [90, 25, 67, 45, 80]
number = 0

for mark in marks:
    number += 1
    if mark >= 60:
        print("%d번 학생은 합격" %number)
        
    else:
        print("%d번 학생은 불합격" %number)
~~~



* for문과 continue

while문에서 살펴보았던 continue를 for문에서도 사용할 수 있다. 

**즉, for문 안의 문장을 수행하는 도중에 continue문을 만나면 for문의 처음으로 돌아가게 된다.**

앞서 for문 응용 예제를 그대로 이용해서 60점 이상인 사람에게는 축하 메시지를 보내고 나머지 사람에게는 아무런 메시지도 전하지 않는 프로그램을 에디터를 이용해 작성해 보자.

~~~
marks = [90, 25, 67, 45, 80]

number = 0 
for mark in marks: 
    number = number +1 
    if mark < 60: continue 
    print("%d번 학생 축하합니다. 합격입니다. " % number)
~~~

점수가 60 이하인 학생은 : continue 를 만나면서 for문의 처음으로 돌아간다. 따라서 print문이 수행되지 않는다.



* for문과 range  함수 

> range 함수 : 숫자 '리스트'를 자동으로 만들어 준다. 

~~~
a = range(10)
range(0,10)
~~~

0부터 9까지의 10개의 숫자리스트를 만들어준다. 



앞서 살펴보았던 60점 이상이면 합격이라는 문장을 출력하는 예를 range함수를 사용하여 만들어보자.

>  len 함수 : 리스트 내 ''요소의 개수''를 돌려주는 함수이다

~~~
marks = [90, 25, 67, 45, 80]

for number in range(len(marks)):
    if marks[number] < 60: continue
    print(" %d번 축하" % (number+1))
~~~

 len 함수는 리스트 내 요소의 개수를 돌려주는 함수이다. 따라서 len(marks)는 5가 될 것이고 range(len(marks))는 range(5)가 될 것이다. number 변수에는 차례로 0부터 4까지의 숫자가 대입될 것이고, marks[number]는 차례대로 90, 25, 67, 45, 80이라는 값을 갖게 된다. 



* for와 range를 이용한 구구단 만들기 

~~~
for i in range(2,10): 
     for j in range(1, 10): 
         print(i*j, end=" ") 
     print('') 
~~~

①번 for문에서 2부터 9까지의 숫자(range(2, 10))가 차례로 i에 대입된다.

 i가 처음 2일 때 ②번 for문을 만나게 된다. 

②번 for문에서 1부터 9까지의 숫자(range(1, 10))가 j에 대입된다.

그 다음 문장인 `print(i*j)`를 수행한다.



> end=" "        : 다음줄로 넘어가지 말고 그 줄에 계속해서 출력하기 위해서 사용
>
> print(' ')     : 다음줄로 넘겨서 출력하기 위해 사용 



* 리스트 안에 for문 포함하기 (List comprehension)

리스트 안에 for문을 포함하는 리스트 내포(List comprehension)를 이용하면 좀 더 편리하고 직관적인 프로그램을 만든다.

~~~
a = [1.2.3.4]
result = []

for num in a:
    result.appent(num*3)
    
    print(result)
[3, 6, 9, 12]
~~~

위의 예제를 **List comprehension** 을 이용해서 간단히 할 수 있다.

~~~
a = [1,2,3,4]
result = []

result = [num * 3 for num in a]
print(result)
~~~



* List comprehension (리스트내포) 의 일반적인 문법구조  **<- 처음본다!**

~~~
[표현식 for 항목 in 반복가능객체 if 조건]
~~~



> 만약 구구단의 모든 결과를 리스트에 담고 싶다면 for문 2개를 사용하는 리스트 내포를 이용하여
>
>  아래와 같이 간단히 구현가능하다. (생각보다 직관적으로 이해가지 않는다)

~~~
result = [x*y for x in range(2,10)
               for y in range(1,10)]
print(result)

[2, 4, 6, 8, 10, 12, 14, 16, 18, 3, 6, 9, 12, 15, 18, 21, 24, 27, 4, 8, 12, 16,
20, 24, 28, 32, 36, 5, 10, 15, 20, 25, 30, 35, 40, 45, 6, 12, 18, 24, 30, 36, 42
, 48, 54, 7, 14, 21, 28, 35, 42, 49, 56, 63, 8, 16, 24, 32, 40, 48, 56, 64, 72,
9, 18, 27, 36, 45, 54, 63, 72, 81]
~~~

x에 2가 담기고 y 에는 1이 담긴다.  y에 2이 담긴다. ~~~ y에 9가 담긴다.

x에 3이 담기고 y에는 1이 담긴다. ~~~                            y에 9가 담긴다.

… 무한반복

다 담긴다음에 x*y를 한값을 result 라는 [] 리스트안에 넣는다.

result 라는 리스트를 쫙 출력한다. 



## 연습문제 - for문

**[문제4] 혈액형 ** **< = 딕셔너리에 값을 입력하는것은 잘 이해 안간다…ㅎ..**

다음은 학생들의 혈액형(A, B, AB, O)에 대한 데이터이다.

```
['A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A', 'B', 'O', 'B', 'AB']
```

for 문을 이용하여 각 혈액형 별 학생수의 합계를 구하시오.



혈액형 별로 합계를 구해야 하므로 **딕셔너리** 를 이용하는 것이 유리하다. 

>  딕셔너리를 사용할 때는 ''키 값의 유무'' 에 주의하여 코딩해야 한다.
>
> if 문을 사용해서 키 값이 존재하는 경우에는 result 딕셔너리에 해당 키를 만들고 1을 더한다.
>
> 만약 키 값이 존재하지 않는 경우에는 해당 키값이 1을 갖는 딕셔너리를 새로 생성한다.

~~~
data = ['A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A', 'B', 'O', 'B', 'AB']
result = {}
for blood_type in data:
    if blood_type in result:  # 키 값이 존재하는 경우에는 기존 값에 더함
        result[blood_type] += 1
    else:  # 키 값이 없는 경우에는 새로운 키 생성
        result[blood_type] = 1

print(result)  # {'A': 3, 'B': 3, 'O': 3, 'AB': 3} 출력
~~~





**[문제5] 리스트 내포1**

" 리스트 중에서 홀수에만 2를 곱하여 저장 " 하는 다음과 같은 코드가 있다.

```
numbers = [1, 2, 3, 4, 5]

result = []
for n in numbers:
    if n % 2 == 1:
        result.append(n*2)
```

위 코드를 리스트 내포(list comprehension)를 이용하여 표현하시오.

~~~
result = [x*2 for x in numbers if x%2 == 1]
print(result)
~~~



**[문제6] 리스트 내포2**

리스트 내포를 이용하여 다음 문장에서 모음('aeiou')을 제거하시오.

```
Life is too short, you need python
```

> join 함수를 쓰면 **리스트를 문자열로 변환** 할 수 있다. 
>
> * 리스트(배열) 정의
>
>   food = [ "123", "자장면", "짬뽕", "탕수육", "물만두", "팔보채" ]
>
> * 요소들 사이에 공백 넣기 (구분자는 공백)
>
>   print " ".join(food)
>
>   출력 결과: 123 자장면 짬뽕 탕수육 물만두 팔보채
>
> * 모든 요소들을 하나로 연결하여 출력 (구분자 없음)
>
>   print "".join(food)
>
>   출력결과 : 123자장면짬뽕탕수육물만두팔보채 
>
> * 줄바꿈 문자를 구분자로 하여 출력
>
> ​	print "\n".join(food)
>
> ​	출력 결과:
> 	123
> 	자장면
> 	짬뽕
> 	탕수육
> 	물만두
> 	팔보채
> 	
>
> (출저: http://mwultong.blogspot.com/2006/12/python-join-list-array.html)

 ~~~
vowels = 'aeiou'
sentence = 'Life is too short, you need python'
sentence = ''.join([a for a in sentence if a not in vowels])
print(sentence)

Lf s t shrt, y nd pythn
 ~~~

sentence 를 돌면서 해당 번째의 요소(문자)가 vowels안에 없으면 (문자가 aeiou가 아니면) 

해당 a번째 요소(문자)를 연결(join)해서 ''문자열''로  sentence에 저장해라. 출력하면 문자열로 나옴 



# 04장 프로그램의 입력과 출력은 어떻게 해야 할까?

지금껏 공부한 내용을 바탕으로 함수, 입력과 출력, 파일 처리 방법 등에 대해서 알아보기로 하자.

입출력은 프로그래밍 설계와 관련이 있다. 프로그래머는 프로그램을 만들기 전에 어떤 식으로 동작하게 할 것인지 설계 부터 하게 되는데 그때 가장 중요한 부분이 바로 입출력의 설계이다. 특정 프로그램만이 사용하는 함수를 만들 것인지 아니면 모든 프로그램이 공통으로 사용하는 함수를 만들 것인지, 더 나아가 오픈 API로 공개하여 외부 프로그램들도 사용할 수 있게 만들 것인지 그 모든 것이 입출력과 관련이 있다.



## 04 - 1. 함수

* 파이썬 함수의 구조

~~~
def 함수명(매개변수):
    <수행할 문장1>
    <수행할 문장2>
    ...
~~~

```
def sum(a, b): 
    return a + b
```

위 함수는 다음과 같이 풀이된다.

> "이 함수의 이름(함수명)은 sum이고 입력으로 2개의 값을 받으며 결과값은 2개의 입력값을 더한 값이다."

 

* 매개변수와 인수 

매개변수(parameter)와 인수(arguments)는 혼용해서 사용되는 헷갈리는 용어이므로 잘 기억해 두기로 하자. 

매개변수는 함수에 입력으로 전달된 값을 받는 변수를 의미하고 인수는 함수를 호출할 때 전달하는 입력값을 의미한다.

~~~
def sum(a, b):  # a, b는 매개변수
    return a+b

print(sum(3, 4))  # 3, 4는 인수
~~~



* 입력값이 없는 함수 

~~~
def say():
    return 'hi'
   
~~~

say라는 이름의 함수를 만들었다. 그런데 매개변수 부분을 나타내는 함수명 뒤의 괄호 안이 비어 있다.

~~~
a = say()
print(a)
hi
~~~

인수에 값을 주지 않아야 실행된다. a에 hi라는 문자열이 대입되는 것이다. 



* 결과값이 없는 함수 

~~~
def sum(a,b):
    print("%d, %d의 합은 %d 입니다." % (a, b, a+b))
   
sum(3, 4)
3, 4의 합은 7입니다.
~~~

return 값으로 a변수에  None을 돌려준다. 

따라서 print(a) 를 하면 None이 나온다.



* 입력값도 결과값도 없는 함수 

~~~
def say():
    print('hi')
    
say()

hi
~~~



* 매개변수를 지정하고 호출하기 

  매개변수를 지정하면 다음과 같이 순서에 상관없이 사용할 수 있다는 장점이 있다.

~~~
def sum(a, b):
    return a+b

sum(b=5, a=3) # b에 5를 넣고 a에 3을 넣는다.
8
~~~



* 입력값이 몇 개가 될지 모를 때는?

입력값이 여러 개일 때 그 입력값들을 모두 더해 주는 함수를 생각해 보자. 하지만 몇 개가 입력될지 모를 때는 어떻게 해야 할까? 아마도 난감할 것이다. 파이썬은 이런 문제를 해결하기 위해 다음과 같은 방법을 제공한다.

여러개의 입력값을 모두 더하는 함수를 만들어보자.

~~~
def sum_many(*args):
    sum = 0
    for i in args:
        sum = sum + 1
    return sum
~~~

 `*args`처럼 매개변수명 앞에 `*`을 붙이면 입력값들을 전부 모아서 튜플로 만들어 주기 때문이다. 만약 sum_many(1, 2, 3)처럼 이 함수를 쓰면 args는 (1, 2, 3)이 되고, sum_many(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)처럼 쓰면 args는 (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)이 된다. 여기서 `*args`라는 것은 임의로정한 변수명이다. `*pey`, `*python`처럼 아무 이름이나 써도 된다.

> ※ args는 입력 ''인수''를 뜻하는 영어 단어인 arguments의 약자이며 관례적으로 자주 사용한다.

~~~
>>> def sum_mul(choice, *args): 
...     if choice == "sum": 
...         result = 0 
...         for i in args: 
...             result = result + i 
...     elif choice == "mul": 
...         result = 1 
...         for i in args: 
...             result = result * i 
...     return result 
... 
이렇게 만들어놓고 choice가 어떤것인지에 따라서 인수를 여러개의 튜플로 입력받아 쓸 수 있다. 
~~~



* 키워드 파라미터 kwargs

이번에는 키워드 파라미터인 `**kwargs`에 대해서 알아보자. kwargs는 keyword arguments의 약어이다. `**kwargs`는 `*args`와는 달리 별표시(`*`)가 두 개 사용된다. 



먼저 다음과 같은 함수를 작성 해 보자.

```
>>> def func(**kwargs):
...     print(kwargs)
...
```

```
>>> func(a=1)
{'a': 1}
>>> func(name='foo', age=3)
{'age': 3, 'name': 'foo'}
```

func 함수의 인수로 key=value 형태를 주었을 때 입력 값 전체가 kwargs라는 딕셔너리에 저장된다는 것을 알 수 있다.

즉, `**kwargs`는 모든 key=value 형태의 입력인수가 저장되는 딕셔너리 변수이다.



* return의 또 다른 쓰임새

어떤 특별한 상황이 되면 함수를 빠져나가고자 할 때는 return을 단독으로 써서 함수를 즉시 빠져나갈 수 있다. 다음 예를 보자.

```
>>> def say_nick(nick): 
...     if nick == "바보": 
...         return 
...     print("나의 별명은 %s 입니다." % nick)
... 
>>>
```

위의 함수는 "별명"을 입력으로 전달받아 출력하는 함수이다. 이 함수 역시 리턴값은 없다(문자열을 출력한다는 것과 리턴값이 있다는 것은 전혀 다른 말이다. 혼동하지 말자. 함수의 리턴값은 오로지 return문에 의해서만 생성된다).

만약에 입력값으로 '바보'라는 값이 들어오면 문자열을 출력하지 않고 함수를 즉시 빠져나간다.

```
>>> say_nick('야호')
나의 별명은 야호입니다.
>>> say_nick('바보')
>>>
```

이처럼 return으로 함수를 빠져나가는 방법은 실제 프로그래밍에서 자주 사용된다.

## lambda

lambda는 함수를 생성할 때 사용하는 예약어로, def와 동일한 역할을 한다. 보통 함수를 한줄로 간결하게 만들 때 사용한다. 우리말로는 "람다"라고 읽고 def를 사용해야 할 정도로 복잡하지 않거나 def를 사용할 수 없는 곳에 주로 쓰인다. 사용법은 다음과 같다.

> lambda 매개변수1, 매개변수2, ... : 매개변수를 이용한 표현식

한번 직접 만들어 보자.

```
>>> sum = lambda a, b: a+b
>>> sum(3,4)
7
```

그렇다면 def가 있는데 왜 lambda라는 것이 나오게 되었을까? 이유는 간단하다.

 lambda는 def 보다 간결하게 사용할 수 있기 때문이다. 또한 lambda는 def를 사용할 수 없는 곳에도 사용할 수 있다. 

다음 예제에서 " 리스트 내에 lambda가 들어간 경우 " 를 살펴보자.

```
>>> myList = [lambda a,b:a+b, lambda a,b:a*b]
>>> myList
[at 0x811eb2c>, at 0x811eb64>]
```

즉, 리스트 각각의 요소에 lambda 함수를 만들어 바로 사용할 수 있다. 첫 번째 요소 myList[0]은 2개의 입력값을 받아 두 값의 합을 돌려주는 lambda 함수이다.

```
>>> myList[0]
at 0x811eb2c>
>>> myList[0](3,4)
7
```

두 번째 요소 myList[1]은 2개의 입력값을 받아 두 값의 곱을 돌려주는 lambda 함수이다.

```
>>> myList[1](3,4)
12
```

파이썬에 익숙해질수록 lambda 함수가 굉장히 편리하다는 사실을 알게 될 것이다.



## 04-2. 사용자 입력과 출력 

### input의 사용

```
>>> a = input()
Life is too short, you need python
>>> a
'Life is too short, you need python'
>>>
```

input은 입력되는 모든 것을 문자열로 취급한다.



### 프롬프트를 띄워서 사용자 입력 받기

사용자에게 입력을 받을 때 "숫자를 입력하세요"라든지 "이름을 입력하세요"라는 안내 문구 또는 질문이 나오도록 하고 싶을 때가 있다. 그럴 때는 input()의 괄호 안에 질문을 입력하여 프롬프트를 띄워주면 된다.

> input("질문 내용")

다음의 예를 직접 입력해 보자.

```
>>> number = input("숫자를 입력하세요: ")
숫자를 입력하세요:
```

### 문자열 띄어쓰기는 콤마로 한다

```
>>> print("life", "is", "too short")
life is too short
```

콤마(,)를 이용하면 문자열 간에 띄어쓰기를 할 수 있다.

### 한 줄에 결과값 출력하기

03-3절에서 for문을 배울 때 만들었던 구구단 프로그램에서 보았듯이 한 줄에 결과값을 계속 이어서 출력하려면 입력 인수 end를 이용해 끝 문자를 지정해야 한다.

```
>>> for i in range(10):
...     print(i, end=' ')
...
0 1 2 3 4 5 6 7 8 9
```



## 04-3.  파일 읽고 쓰기

파일을 통한 입출력 방법에 대해서 알아보자. 

먼저 파일을 새로 만든 다음 프로그램에 의해서 만들어진 결과값을 새 파일에 한번 적어 보고, 또 파일에 적은 내용을 읽어 보는 프로그램을 만드는 것으로 시작해 보자.

 파일 생성하기

다음 소스 코드를 에디터로 작성해서 저장한 후 실행해 보자. 프로그램을 실행한 디렉터리에 새로운 파일이 하나 생성된 것을 확인할 수 있을 것이다

```
f = open("새파일.txt", 'w')
f.close()
```

파일을 생성하기 위해 우리는 open이라는 파이썬 내장 함수를 사용했다. open 함수는 다음과 같이 "파일 이름"과 "파일 열기 모드"를 입력값으로 받고 결과값으로 파일 객체를 돌려준다.

> 파일 객체 = open(파일 이름, 파일 열기 모드)

파일 열기 모드에는 다음과 같은 것들이 있다.

| 파일열기모드 | 설명                                                       |
| ------------ | ---------------------------------------------------------- |
| r            | 읽기모드 - 파일을 읽기만 할 때 사용                        |
| w            | 쓰기모드 - 파일에 내용을 쓸 때 사용                        |
| a            | 추가모드 - 파일의 마지막에 새로운 내용을 추가 시킬 때 사용 |

 파일을 쓰기 모드로 열게 되면 해당 파일이 이미 존재할 경우 원래 있던 내용이 모두 사라지고, 해당 파일이 존재하지 않으면 새로운 파일이 생성된다. 위의 예에서는 디렉터리에 파일이 없는 상태에서 새파일.txt를 쓰기 모드인 'w'로 열었기 때문에 새파일.txt라는 이름의 새로운 파일이 현재 디렉터리에 생성되는 것이다.

만약 새파일.txt라는 파일을 `C:/doit`이라는 디렉터리에 생성하고 싶다면 다음과 같이 작성해야 한다.

```
f = open("C:/doit/새파일.txt", 'w')
f.close()
```

위의 예에서 f.close()는 열려 있는 파일 객체를 닫아 주는 역할을 한다. 사실 이 문장은 생략해도 된다. 

프로그램을 종료할 때 파이썬 프로그램이 열려 있는 파일의 객체를 자동으로 닫아주기 때문이다. 하지만 close()를 사용해서 열려 있는 파일을 직접 닫아 주는 것이 좋다. 

쓰기모드로 열었던 파일을 닫지 않고 다시 사용하려고 하면 오류가 발생하기 때문이다.



## 파일을 쓰기 모드로 열어 출력값 적기

위의 예에서는 파일을 쓰기 모드로 열기만 했지 정작 아무것도 쓰지는 않았다. 

이번에는 에디터를 열고 프로그램의 출력값을 파일에 직접 써 보자.

```
# writedata.py
f = open("C:/doit/새파일.txt", 'w')
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()
```

## 프로그램의 외부에 저장된 파일을 읽는 여러 가지 방법

* readline() 함수 : txt의 가장 첫 번째 줄이 화면에 출력될 것이다.

  * 만약 모든 라인을 읽어서 화면에 출력하고 싶다면 다음과 같이 작성하면 된다.

  ```
  # readline_all.py
  f = open("C:/doit/새파일.txt", 'r')
  while True:
      line = f.readline()
      if not line: break
      print(line)
  f.close()
  ```

  즉, while True:라는 무한 루프 안에서 f.readline()을 이용해 파일을 계속해서 한 줄씩 읽어들이도록 한다. 만약 더 이상 읽을 라인이 없으면 break를 수행한다(readline()은 더 이상 읽을 라인이 없을 경우 None을 출력한다).

* readlines() 함수 : 파일의 모든 라인을 읽어서 각각의 줄을 요소로 갖는 리스트로 리턴한다

* read() 함수  : f.read()는 파일의 내용 전체를 문자열로 리턴한다. 



## 파일에 새로운 내용 추가하기

쓰기 모드('w')로 파일을 열 때 이미 존재하는 파일을 열 경우 그 파일의 내용이 모두 사라지게 된다고 했다. 

하지만 원래 있던 값을 유지하면서 단지 새로운 값만 추가해야 할 경우도 있다. 

이런 경우에는 파일을 추가 모드('a')로 열면 된다. 에디터를 켜고 다음 소스 코드를 작성해 보자.

```
# adddata.py
f = open("C:/doit/새파일.txt",'a')
for i in range(11, 20):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()
```

위 예는 새파일.txt라는 파일을 추가 모드('a')로 열고 write를 이용해서 결과값을 기존 파일에 추가해 적는 예이다. 

여기서 추가 모드로 파일을 열었기 때문에 새파일.txt라는 파일이 원래 가지고 있던 내용 바로 다음부터 결과값을 적기 시작한다.

새파일.txt 파일을 확인해 보면 원래 있던 파일 뒷부분에 새로운 내용이 추가되었음을 볼 수 있다.



## with문과 함께 사용하기( with open( ) as x: )

지금까지 살펴본 예제를 보면 항상 다음과 같은 방식으로 파일을 열고 닫아 왔다.

```
f = open("foo.txt", 'w')
f.write("Life is too short, you need python")
f.close()
```

파일을 열면 위와 같이 항상 close해 주는 것이 좋다. 

하지만 이렇게 파일을 열고 닫는 것을 자동으로 처리할 수 있다면 편리하지 않을까?

파이썬의 with문이 바로 이런 역할을 해준다. 다음의 예는 with문을 이용해서 위 예제를 다시 작성한 모습이다.

```
with open("foo.txt", "w") as f:
    f.write("Life is too short, you need python")
```

**위와 같이 with문을 이용하면 with 블록을 벗어나는 순간 열린 파일 객체 f가 자동으로 close되어 편리하다.**



## sys 모듈로 입력 인수 주기 <- 진짜 잘 모르겠다. (pass)

> 도스 명령어 [인수1 인수2 ...]

파이썬에서는 sys라는 모듈을 이용하여 입력 인수를 직접 줄수 있다. sys 모듈을 이용하려면 아래 예의 import sys처럼 import라는 명령어를 사용해야 한다.

> ※ 모듈을 이용하고 만드는 방법에 대해서는 뒤에서 자세히 다룰 것이다.

```
#sys1.py
import sys

args = sys.argv[1:]
for i in args:
    print(i)
```

위의 예는 입력받은 인수들을 for문을 이용해 차례대로 하나씩 출력하는 예이다. sys 모듈의 argv는 명령창에서 입력한 인수들을 의미한다. 즉, 아래와 같이 입력했다면 argv[0]는 파일 이름인 sys1.py가 되고 argv[1]부터는 뒤에 따라오는 인수들이 차례로 argv의 요소가 된다.

![img](https://wikidocs.net/images/page/26/04_005.png)

이 프로그램을 C:/doit 디렉터리에 저장한 후 입력 인수를 함께 주어 실행시키면 다음과 같은 결과값을 얻을 수 있다.

```
C:\doit>python sys1.py aaa bbb ccc
aaa
bbb
ccc
```

위의 예를 이용해서 간단한 스크립트를 하나 만들어 보자.

```
#sys2.py
import sys
args = sys.argv[1:]
for i in args:
    print(i.upper(), end=' ')
```

문자열 관련 함수인 upper()를 이용하여 명령 행에 입력된 소문자를 대문자로 바꾸어 주는 간단한 프로그램이다. 명령 프롬프트 창에서 다음과 같이 입력해 보자.

> ※ sys2.py 파일이 `C:\doit` 디렉터리 안에있어야만 한다.

```
C:\doit>python sys2.py life is too short, you need python
```

결과는 다음과 같다.

```
LIFE IS TOO SHORT, YOU NEED PYTHON
```



## 연습문제 - 파일 읽고 쓰기

**[풀이3] 역순 저장**

파일 객체의 readlines를 이용하여 모든 라인을 읽은 후에 reversed를 이용하여 역순으로 정렬한 후에 다시 파일에 저장한다.

```
f = open('abc.txt', 'r')
lines = f.readlines()  # 모든 라인을 읽음
f.close()

rlines = reversed(lines)  # 읽은 라인을 역순으로 정렬

f = open('abc.txt', 'w')
for line in rlines:
    line = line.strip()  # 포함되어 있는 줄바꿈 문자 제거
    f.write(line)
    f.write('\n')  # 줄바꿈 문자 삽입
f.close()
```

**[풀이4] 파일 수정**

파일을 모두 읽은 후에 문자열의 replace를 이용하여 java라는 문자열을 python으로 변경하여 저장한다.

```
f = open('test.txt', 'r')
body = f.read()
f.close()

body = body.replace('java', 'python')

f = open('test.txt', 'w')
f.write(body)
f.close()
```

**[풀이5] 평균값 구하기**

```
f = open("sample.txt")
lines = f.readlines( )  # sample.txt를 줄단위로 모두 읽는다.
f.close( )

total = 0
for line in lines:
    score = int(line)  # 줄에 적힌 점수를 숫자형으로 변환한다.
    total += score
average = total / len(lines)

f = open("result.txt", "w")
f.write(str(average))
f.close()
```

sample.txt의 점수를 모두 읽기 위해 파일을 열고 readlines를 이용하여 각 줄의 점수 값을 모두 읽어 들여 총 점수를 구한다. 

총 점수를 sample.txt 파일의 라인(Line) 수로 나누어 평균값을 구한 후 그 결과를 result.txt 파일에 쓴다. 

**숫자 값은 result.txt 파일에 바로 쓸 수 없으므로 str함수를 이용하여 문자열로 변경한 후 파일에 쓴다.**



 

## 05장 클래스 부터는  내일 다시 공부해보도록 하자. 이미 다 갈렸다...ㅎ 

---


## homework ver.2   범죄예방 데이터로 공부한것 적용해보기 

```

# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np


df = pd.read_csv('https://s3.ap-northeast-2.amazonaws.com/data10902/messy/crime_clean.csv') # 데이터프레임 형태로 저장한다.

print(df.tail()) # 데이터의 마지막 5줄만 가져온다.

# 1. 데이터에서 '명'만 가져오기 위해 우선 열의 이름을 알아본다.

print(df.columns)

# 2. '명' 열을 가져온다.

df.loc[np.isnan(df['명']),'명'] = 0 # NaN 값은 0으로 바꿔줘야 에러가 안난다.

num = df['명']

# 3. 평균 구하기

sum = 0

for i in num:
	sum += i

print(sum) # 총합
print(len(num)) # 데이터 총 개수


average = int(sum/len(num))

print("평균은 %d 입니다." % average)


# 4. 중앙값 구하기 / 데이터의 개수가 짝수(4060) 이므로 4060/2 번째 관측값과 4060/2 + 1 번째 관측값의 평균으로 구한다.

num2 = num.sort_values()  # 우선 num 이라는 df의 값을 크기순으로 나열해줍니다.

value1 = num2.values[2030] # 2030번째의 관측값

value2 = num2.values[2031] # 2031번째의 관측값

print("중앙값은 %d 입니다." %(value1+value2/2))

```

ValueError: cannot convert float NaN to integer

= = … NaN값은 제거 해줘야 겠다. 


