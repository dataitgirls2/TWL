### 7월 5일 목요일, 파이썬 활용 실습 복습  

#### 01. 파이썬 활용 실습
``` python
def get_sum(data): # get_sum이라는 함수를 정의한다. 이 함수의 인자로 data를 받는다.
  result = 0 # result라는 변수에 0을 대입하여 초기값을 설정한다.
  for datum in data: # data라는 리스트 안에 있는 이름이 datum인 값들을 하나씩 다 꺼낼 때 까지 반복한다.
    result = result + datum # 초기값 0이었던 result에 datum을 차례대로 합한 값을 누적하여 result에 대입한다.
  return result # result의 값을 반환한다. 
```

이렇게 정의한 함수를 호출하면서, 인자로 어떤 list를 넣어주면 그 리스트의 값을 전부 합한 결과를 반환한다.  

```python
def get_lan(data):
  result = 0
  for datum in data:
    result = result + 1 # data안의 값들을 하나씩 꺼낼 때 마다 1씩 누적하여 result에 대입한다. 
  return result 
```

이렇게 정의한 함수를 호출하면서 어떤 list를 넘겨주면, list에 담겨있는 element의 개수를 반환한다.  

```python
  total = get_sum(data) # total 이라는 변수에 처음 작성한 get_sum(data)의 값을 담는다.

  n = get_lan(data) # n 이라는 변수에 두번 째로 작성한 get_lan(data)의 값을 담는다.

  result = total / n # result 라는 변수에 total을 n으로 나눈 결과를 담는다.

  return result # result의 값을 반환한다.

score = [50, 60, 70] # 50, 60, 70 3개의 elements를 가진 score라는 리스트를 정의한다.

average = get_average(score) # get_average에 인자로 score을 넘겨준 결과값을 average에 담는다.

print(average) # average를 출력한다.

```

**Python 코드는 위에서 아래로 실행되며, 블럭 별로 독립적이다.**

- INCEPTION 영화를 생각해 보자. 영화 안에서 꿈을 설계하는 설계자는 꿈 안에서 또 꿈 안으로 들어가는 구조를 만들어낸다. 이런 시스템을 recursion(재귀)라고 볼 수 있다.
  이는 파이썬 프로그램 안에서 파이썬 프로그램을 실행하는 것과 마찬가지다. 전체 코드에서, 각각의 코드 블럭은 하나의 꿈과 같다. 코드 블럭들이 전부 실행되면, 꿈에서 깬다.
- 영화에서는 Totem을 가지고 꿈으로 들어간다. 이와 같이, 파이썬 코드 안에서도 분리된 코드 블럭 안을 자유롭게 넘나드는 무언가를 가질 수 있는데, 이를 함수에 적용되는 parameter(인자)라고 한다.
- 마지막 코드 블럭에서, score라는 이름으로 정의한 list가 이 전체 파이썬 코드에서 Totem의 역할을 한다. 그리고 꿈에서 깨면서, 꿈 안에 있던 무언가를 가지고 현실로 돌아올 수 있다고 한다면, 그것이 바로 return(결과값)이다. 이러한 return(결과값) 말고는 독립적인 파이썬 블록은 전체 코드 구조에 영향을 주지 않는다.
- 그렇기 때문에 '이름 공간'이라는 측면에 있어서 경제적이다.
- 꿈을 너무 많이 꾸면 영화에서 미쳐버리듯, 함수도 너무 많은 구조의 재귀를 반복하면 Stack overflow error가 발생한다. Stack이 너무 많이 쌓여 과부하가 걸리는 것이다.
- [Stack Overflow](https://colab.research.google.com/drive/www.stackoverflow.com) 사이트를 애용하자.  



#### 02. Lambda 보충설명 

``` python
# 이름과 나이를 담고 있는 리스트를 만든다.
names = ['Alan', 'Dave', 'Brad', 'Cate'] # string list를 만든다. 
ages = [50, 60, 30, 40] 

# 이름 순으로 정렬한다.
# sorted는 Python안에 기본적으로 내장되어 있는 정렬 함수이다. 인자를 오름차순으로 정렬한다. 
sorted(names) 
sorted(ages)

# 자료형에 따라 어떤 함수를 이용할 수 있는지 궁금하다면, 아래와 같은 방식으로 도움을 구해 보자.
# type(이름)은 자료형이 무엇인지 알려 준다.  
type(names)

# list 자료형에 사용할 수 있는 함수들을 알아보려면, dir(자료형)을 입력한다. 
dir(list)

students = list(zip(names, ages)) 
# names라는 이름의 list와 ages라는 이름의 list를 한 쌍으로 묶는다. zip(list1, list2) 
# 이 하나하나의 인자를 tuple이라고 한다. 
# 이 tuple, 즉 각각의 쌍을 원소로 갖는 list를 만들어 주고, 이 것을 students에 담는다. 
students

# students 라는 리스트를 정렬하고 싶은데, 이름 순으로 할지 나이 순으로 할지 기준을 정해 줘야 한다.
# 이름 순으로 정렬해 보자.

def by_name(student): # by_name이라는 함수를 정의한다. 인자는 student로 받는다. 
  return student[0] # student 안의 0번 Index의 인자, 즉 첫번 째 인덱스의 인자를 반환한다. 

sorted(students, key=by_name) # sorted 함수를 사용하여, students 를 by_name의 결과값을 key로 갖게 sorted 한다. 
# sorted 함수에 key라는 parameter을 추가하여, 첫번 째 인자를 무엇을 기준으로 정렬할건지 알려줄 수 있다. 
# sorted 는 정렬할 때만 사용된다. 

# Lambda는 students라는 리스트를 student라는 리스트의 첫 번째 인덱스를 기준으로 정렬하겠다는 뜻이다.
# 즉, students는 tuple을 원소로 갖는 list이다. tuple은 인덱스가 [0], [1]이다. 
sorted(students, key=lambda student: student[0])

# lambda를 쓰고, 수행되어야 할 표현식을 적어준다. 
# students라는 인자 이름을 무작위로 지어주고, 그 인자의[?]번째 element를 기준으로 정렬하겠다는 것을 선언한다. 
# 즉, 아래 코드는 students라는 리스트의 각각의 원소(tuple)를 뽑아서, 그 원소(tuple)안의 [?]번째 인자를 기준으로 정렬하라는 뜻이다. 
sorted(students, key=lambda student: student[1]) 
```

- Lambda는 이러한 과정을 단순화시키는 기능을 한다. Lambda를 사용하면 함수 이름을 지을 필요가 없고, 코드를 두 줄이나 입력해야 할 필요가 없어진다. 즉, 한 줄 짜리 짧은 함수를, 이름을 짓지 않고 순식간에 쓰고 버리게끔 하는 문법이라고 생각하면 된다.
- Lambda는 어떠한 표현식도 사용 가능하다.
- Lambda 라는 이름의 유래는, Lambda Calculus 에서 유래하였다. 계산기가 없던 시절, 앨런 튜링은 튜링 머신이라는 가상의 기계가 수행할 수 있는 모든 것을 '연산(계산)'이라고 정의한다. 앨런은 람다 캘큘러스라는 함수에 기반한 체계를 만들었는데, 이 체계로 수행할 수 있는 것을 계산이라고 정의한다. 어쨌든 '계산'이란 무엇인가를 정의하려고 시도한 모든 체계들이, 튜링 머신과 람다 캘큘러스로 수행될 수 있는 것들과 비슷한 결과를 냈다. 즉, 전산학계의 하나의 가설이다.
- Lambda Calculus에서 중요한 개념은, Abstraction(추상화, definition; 정의)와 Application(실행, call; 적용)이다. Abstraction이라 함은 추상화인데, 복잡한 수식을 추상화하고, 그것을 호출하여 적용하면 수행된 결과가 나오는 것.
- 함수의 인자로 함수를 받는 프로그래밍에서의 '이차 함수'는 Second order function이라고 한다. 우리가 알고 있는 'Second degree polynomial function'과는 다르다.



#### 03. dictionary 란?

``` python
dic = {'name' : 'Chaewon Kang', 'phone' : '01012341234', 'birth' : '0917' }
```

위에서 key는 각각 'name', 'phone', 'birth'이고, 각각의 key에 해당하는 value는 'pey', '01012341234', '0917'이다.

```python
dic = {1: 'hi'}
```

위의 예 처럼 key에 int(정수)를, value에 string(문자열)을 사용할 수 있다.

```python
dic = {'a' : [1, 2, 3]}
```

위의 예 처럼 value에 list도 사용할 수 있다.  



**Dictionary에서 Key를 사용해 Value 얻기**

Dictionary는 key를 사용하여 value를 얻어내는 방법으로만 요소값을 얻어낼 수 있다. 즉, 어떤 key의 value를 얻기 위해서는 "딕셔너리 변수[key]' 를 사용한다.

```python
dict = {1 : 'a', 2 : 'b'}
a[1]
```

` 'a'`

``` python
a[2]
```

 `'b'`

이처럼, 딕셔너리 변수에서 []안의 숫자 1은 두번 째 element(요소)를 뜻하는 것이 아니라, key에 해당하는 1을 나타낸다. dictonary는 list나 tuple에 있는 indexing 방법을 적용할 수 없다. 즉, 딕셔너리 dict는 dict[key]로 입력하여 해당 key에 해당하는 value를 얻는다.  



#### 04. 실습 (code review, 점진적 개선)

당신은 농구팀 코치이며, 네 명의 지원자 중 한 명을 추가로 선발하고자 합니다. 다음은 각 지원자 별 최근 열 번 경기에서의 득점 기록입니다. **평균 득점이 가장 높은** 선수를 선발하고자 합니다. 어떤 선수를 선발해야 하는지, 그 이유는 무엇인지 설명하는 보고서를 작성하세요.  

```python
 candidates = {
  'alan': [8, 14, 6, 8, 14, 9, 14, 9, 15, 5],
  'brad': [11, 4, 11, 7, 9, 7, 8, 7, 10, 6],
  'cate': [16, 22, 13, 15, 12, 3, 20, 17, 13, 23],
  'dave': [24, 15, 18, 12, 9, 19, 23, 13, 14, 18],
}
# 주어진 candidates의 자료형을 알아보자. 
type(candidates)

averages = {} # 선수별 평균 점수를 담기 위한 빈 dictionary를 하나 만든다.

for name in candidates.keys(): # candidates의 key값을 구하고, 그 dict_keys 안에서 차례대로 반복한다. 그 반복할 변수의 이름은 name으로 한다. 
  scores = candidates[name] # candidates 안의 각각의 key 값의 결과를 scores라는 변수에 담는다
  total = 0 # 총점을 구하기 위하여 total 이라는 변수에 0을 할당하여 초기화 한다
  for score in scores: # scores 안에서 다시 반복한다 
    total = total + score # 0으로 설정되어있었던 total에 score의 값을 누적하여 더한다 
  average = total / 10 # 모든 점수를 게임의 횟수로 나눈 값(평균)을 average에 저장한다 
  averages[name] = average # 평균 점수를 dictionary에 저장한다   
averages # 결과를 확인한다 

```

**(1) items() 함수를 이용하여 dictionary의 key, value 쌍 얻기**

items 함수는 어떤 dictionary의 key와 value의 쌍을 튜플로 묶은 값을 dict_items 객체로 돌려준다.  

```python
candidates = {
  'alan': [8, 14, 6, 8, 14, 9, 14, 9, 15, 5],
  'brad': [11, 4, 11, 7, 9, 7, 8, 7, 10, 6],
  'cate': [16, 22, 13, 15, 12, 3, 20, 17, 13, 23],
  'dave': [24, 15, 18, 12, 9, 19, 23, 13, 14, 18],
}

averages = {} # 평균'들'을 담을 빈 딕셔너리를 하나 만들어 준다. 

for name, scores in candidates.items(): 
# candidates의 key, value 값을 튜플로 묶은 dict.items 안에서
# for 구문 안에서 정의한 함수들의 결과를 name, scores 라는 함수에 순차적으로 저장하며 
# dic.items 안의 elements 들이 다 소진될 때까지 반복하고 끝낸다 
  total = 0 # total이라는 변수에 나중에 값을 담아야 하므로 total 을 0으로 초기화하여 선언
  for score in scores: 
  # candidates의 value 값 안에서 value 값이 다 소진될 때 까지
  # total = total + score 의 결과값을 차례로 score 이라는 변수에 저장한 뒤 블럭을 벗어난다 
    total = total + score
    
  average = total / 10
  
  averages[name] = average # dictionary 쌍 추가하기. dictionary[key] = value  
  
print(averages)
```

**(2) 총점을 구하는 함수를 따로 정의하고, 좀 더 짧게 줄여보기**

```python
candidates = {
  'alan': [8, 14, 6, 8, 14, 9, 14, 9, 15, 5],
  'brad': [11, 4, 11, 7, 9, 7, 8, 7, 10, 6],
  'cate': [16, 22, 13, 15, 12, 3, 20, 17, 13, 23],
  'dave': [24, 15, 18, 12, 9, 19, 23, 13, 14, 18],
}

def calc_total(data):
  total = 0
  for d in data:
    total = total + d
  return total 

averages = {} # 선수별 평균 점수를 담기 위한 빈 딕셔너리를 만들어 준다. 

for name, scores in candidates.items():
  # candidates의 key, value 값을 튜플로 묶은 dict.items 안에서
  # for 구문 안에서 정의한 함수들의 결과를 name, scores 라는 함수에 순차적으로 저장하며 
  # dic.items 안의 elements 들이 다 소진될 때까지 반복하고 끝낸다 
  average = calc_total(scores) / 10
  # calc_total의 결과를 10으로 나눈 뒤 average에 저장한다 

  # average의 결과를 순차적으로 averages에 저장한다 
  averages[name] = average

print(averages)
```

**(3) average 변수 제거하고, 평균을 averages dictionary에 바로 담아보기**

```python
candidates = {
  'alan': [8, 14, 6, 8, 14, 9, 14, 9, 15, 5],
  'brad': [11, 4, 11, 7, 9, 7, 8, 7, 10, 6],
  'cate': [16, 22, 13, 15, 12, 3, 20, 17, 13, 23],
  'dave': [24, 15, 18, 12, 9, 19, 23, 13, 14, 18],
}

def calc_total(data): # calc_total이라는 함수를 선언한다. 인자 이름은 data이다. 
  total = 0 # total 은 0으로 초기화 해 준다.
  for d in data: # 인자 안에서 순차적으로 for 구문 안의 식을 반복하고 그 값을 d에 담는다. 모든 인자를 다룬 뒤 빠져나온다. 
    total = total + d # total + d 한 뒤 그 값을 total 에 누적한다. 
  return total  # total 값을 return 한다. 


averages = {} # 평균들을 담을 빈 dictionary를 선언한다.

for name, scores in candidates.items():
    averages[name] = calc_total(scores) / 10

print(averages)
```

**(4) dictionary comprehension 문법을 써서 좀 더 간결하게 만들어 보기**

```python
candidates = {
  'alan': [8, 14, 6, 8, 14, 9, 14, 9, 15, 5],
  'brad': [11, 4, 11, 7, 9, 7, 8, 7, 10, 6],
  'cate': [16, 22, 13, 15, 12, 3, 20, 17, 13, 23],
  'dave': [24, 15, 18, 12, 9, 19, 23, 13, 14, 18],
}

def calc_total(data): # calc_data 라는 함수를 정의한다. 
  total = 0 # total 변수를 0으로 초기화한다. 
  for d in data: # 인자 안의 요소들을 차례로 반복하여 d 에 대입한다. 
    total = total + d
  return total
  
averages = { # averages 라는 딕셔너리를 선언한다. 
    name: calc_total(scores) / 10 # name 은 calc_total 
    for name, scores in candidates.items()
}

print(averages)
```

dictionary 는 정렬을 하기에 적합한 자료구조가 아니므로, dictionary comprehension 대신 list comprehension 문법을 사용하여 리스트를 만들어 정렬을 해 보기. 점수가 낮은 선수부터 높은 순서로 정렬이 되었으므로, 리스트의 맨 마지막 요소를 뽑아내면 점수가 가장 높은 선수를 알 수 있다.

즉, 리스트 인덱스를 -1로 지정하면 마지막 요소를 가져올 수 있다.  

```python
candidates = {
  'alan': [8, 14, 6, 8, 14, 9, 14, 9, 15, 5],
  'brad': [11, 4, 11, 7, 9, 7, 8, 7, 10, 6],
  'cate': [16, 22, 13, 15, 12, 3, 20, 17, 13, 23],
  'dave': [24, 15, 18, 12, 9, 19, 23, 13, 14, 18],
}

def calc_total(data):
  total = 0
  for d in data:
    total = total + d
  return total 

averages = [
    (name, calc_total(scores) / 10)
    for name, scores in candidates.items()
]
sorted_averages = sorted(averages, key=lambda x:x[1])
sorted_averages[-1]
```

**(5) 파이썬 내장 함수 sum()을 사용하여 간결하게 알아내기 + 게임 횟수가 변하더라도 코드를 변경할 필요가 없게끔, 상수를 scores의 length로 바꾸어 주기**

```python
candidates = {
  'alan': [8, 14, 6, 8, 14, 9, 14, 9, 15, 5],
  'brad': [11, 4, 11, 7, 9, 7, 8, 7, 10, 6],
  'cate': [16, 22, 13, 15, 12, 3, 20, 17, 13, 23],
  'dave': [24, 15, 18, 12, 9, 19, 23, 13, 14, 18],
}

averages = [
    (name, sum(scores) / len(scores))
    for name, scores in candidates.items()
]

sorted_averages = sorted(averages, key=lambda x:x[1])
sorted_averages[-1]
```

