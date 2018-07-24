# 파이썬 자습서

## 3. 파이썬의 간략한 소개

주석은 # 로 시작하고 줄의 끝까지 이어지지만, 문자열 리터럴 (" ") 안에서는 주석이 아닌 문자 자체로 인식되어 적용되지 않음.

### 3.1. 파이썬을 계산기로 사용하기

#### 3.1.1. 숫자

정수는 int형 , 소수는 float형 (실수를 지원. 서로 다른 형의 피연산자를 갖는 연산에서는 실수로 변환함.)

-  **/** (float형), **//** (int형) : 나눗셈

- **%** : 나머지

-  ****** : 거듭제곱

-  **J** / **j** : 복소수    (eg) 3 + 5j

```python
>>> (50 - 5*6) / 4    # 사칙연산
5.0
>>> 17 / 3    # float형 나누기
5.666666666666667
>>> 17 // 3    # int형 나누기
5
>>> 17 % 3    # 나머지
2
>>> 5 ** 2    # 거듭제곱
25
>>> (-3)**2    # 음수의 거듭제곱
9
>>> -3**2
-9
```

대화형 모드에서 마지막에 인쇄된 표현식은 _에 대입됨.

```python
>>> tax = 12.5 / 100
>>> price = 100.50
>>> price * tax
12.5625

>>> price + _    # 바로 위의 문장인 price * tax ( = 12.5625) 가 대입됨.
113.0625

>>> round(_, 2)    # 소수점 두 자리까지 표시
113.06
```

#### 3.1.2. 문자열

- **문자열**:

  작은 따옴표(' ')나 큰 따옴표(" ")로 표현. 문자열이 작은 따옴표를 포함하고 있다면 큰 따옴표가 사용됨. print() 함수는 따옴표를 생략함.

- **\\** : 따옴표를 이스케이핑

- **\n** : 줄바꿈

- **r** : \뒤의 문자를 문법으로 인식하지 않게 하기

- **""" """** / **''' '''** (삼중 따옴표) : 여러 줄로 확장된 문자열 리터럴

```python
>>> 'spam eggs'
'spam eggs'

>>> "doesn't"    'doesn\'t'
"doesn't"

>>> '"Yes," they said.'    "\"Yes,\" they said."
'"Yes," they said.'

>>> print('"Isn\'t," they said.')
"Isn't," they said.

>>> s = 'First line. \nSecond line.'
'First line. \nSecond line.'

>>> print(s)
First line.
Second line.

>>> print(r 'C:\some\name')
C:\some\name

>>> print(""" \
Usage: thingy [OPTIONS]
	-h						Display this usage message
	-H hostname				 Hostname to connect to
""")
Usage: thingy [OPTIONS]
	-h						Display this usage message
	-H hostname				 Hostname to connect to
```

- 문자열 **+** 문자열 : 이어붙이기 (두 개 이상의 문자열리터럴이 연속으로 나타나면 자동으로 이어 붙임)

- 문자열 ***** 문자열 :  반복시키기

```python
>>> 3 * 'un' + 'ium'
'unununium'

>>> 'py''thon'
'phython'

>>> prefix = 'py'
>>> prefix 'thon'
>>> ('un' *3)'ium'
SyntaxError: invalid syntax

>>> prefix + 'thon'
'python'
```

- 문자열 인덱스 :

  인덱스가 양수인 경우 맨 앞자리부터 0, 1, 2, ... 할당되지만, 음수 인덱스인 경우 -0은 0 이므로, 첫번째 자리가 -1로 할당됨.

  **시작** 위치는 항상 **포함**되는 반면, **종료** 위치의 문자는 항상 **미포함**.

  너무 큰 인덱스 값을 사용하는 것은 에러지만, 범위 사용할 때 입력된 큰 인덱스는 부드럽게 처리됨.

  문자열의 인덱스로 참조한 위치에 새로운 값을 대입하여 변경할 수 **없음**.

- **len( )** : 문자열의 길이 반환

```python
>>> word = 'Python'
>>> word[0]
'P'
>>> word[5]
'n'
>>> word[-2]
'o'
>>> word[2:5]    # 2 ~ 4번자리까지
'tho'
>>> word[:2] + word[2:]    # 0 ~ 1번자리까지 + 2 ~ 마지막까지
'Python'
>>> word[:4]    # 0 ~ 3번자리까지
'Pyth'
>>> word[-2:]    # 뒤에서부터 2번자리까지
'on'
>>> 'j' + word[1:]
'Jython'
```

#### 3.1.3. 리스트

- **[ ]** : 리스트(compound 자료형), 서로 다른 형의 항목 포함 가능.

이어붙이기 등의 연산도 지원함.

```python
>>> squares = [1, 4, 9, 16, 25]
>>> squares    squares[:]
[1, 4, 9, 16, 25]
>>> squares[0]
1
>>> squares[-1]
25
>>> squares[-3:]
[9, 16, 25]
>>> squares + [36, 49]
[1, 4, 9, 16, 25, 36, 49]
```

단지 지칭하는 것 뿐인 문자열과는 달리 참조하여 값을 변경할 수 있음.

```python
>>> cubes = [1,8,27,65,125]
>>> cubes[3] = 64
>>> cubes
[1, 8, 27, 64, 125]
>>> cubes.append(216)    # 요소를 리스트 끝에 덧붙임
>>> cubes.append(7 ** 3)
>>> cubes
[1, 8, 27, 125, 216, 343]
```

슬라이스에 대입, 길이 변경, 모든 항목을 삭제, 중첩 가능.

```python
>>> letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>> letters[2:5] = ['C', 'D', 'E']
>>> letters
['a', 'b', 'C', 'D', 'E', 'f', 'g']
>>> letters[2:5] = []
>>> letters
['a', 'b', 'f', 'g']
>>> letters[:] = []
>>> letters
[]
```

```python
>>> a = ['a', 'b', 'c']
>>> n = [1, 2, 3]
>>> x = [a, n]
>>> x
[['a', 'b', 'c'], [1, 2, 3]]
>>> x[0]
['a', 'b', 'c']
>>> x[0][1]
'b'
```



### 3.2. 프로그래밍으로의 첫걸음

- 비교 연산자들: 

  **>** (크다), **<** (작다), **==** (같다), **<=** (작거나 같다), **>=** (크거나 같다), **!=** (다르다)

- **print( )** : 주어진 인자들의 값을 인쇄. 인자들 사이에 빈 칸이 삽입됨.

```python
>>> i = 256*256
>>> print('The value of i is', i)
The value of i is 65536
```

```python
>>> a, b = 0, 1			#다중대입 a = 0, b = 1 동시에 대입됨. 
while a < 10:		# a < 10 이 참인 동안 실행됨.
    print(a)
    a, b = b, a+b	 # b, a+b가 계산되어 a, b에 대입됨.
...
0
1
1
2
3
5
8

>>> while a < 1000:
...		print(a, end=', ')
...		a, b = b, a+b
...
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 
```



***

***



## 4. 기타 제어 흐름 도구

### 4.1. if 문

```python
>>> x = int(input("Please enter an integer: "))
Please enter an integer: 42
>>> if x < 0:
        x = 0
        print('Negative changed to zero')
    elif x == 0:
        print('Zero')
    elif x == 1:
        print('Single')
    else:
        print('More')
....
 More
```

### 4.2. for 문

파이썬의 for문은 임의의 시퀀스(리스트나 문자열)의 항목들을 그 시퀀스에 들어있는 순서대로 이터레이션 함.

```python
>>> words = ['cat', 'window', 'defenestrate']
	for w in words:
        print(w, len(w))
...
cat 3
window 6
defenestrate 12

>>> for w in words[:]:		
    	if len(w) > 6:
            words.insert(0,w)
>>> words
['defenestrate', 'cat', 'window', 'defenestrate']
# for w in words: 를 쓰게되면 defenestrate를 반복해서 넣고 또 넣음으로써, 무한한 리스트를 만들려고 시도하게 됨.
```

### 4.3. range( ) 함수

숫자들의 시퀀스로 이터레이트 할 필요가 있을 경우 사용. 수열을 만듬.

```python
>>> for i in range(5):		# 끝값은 만들어지는 수열에 포함X
    	print(i)		# range(5): 5개의 값을 만드는 것.
...
0
1
2
3
4
```

```python
range(5, 10)    # 5, 6, 7, 8, 9
range(0, 10, 3)    # 0, 3, 6, 9
range(-10, -100, -30)    #-10, -40, -70
```

```python
>>> a = ['Mary', 'had', 'a', 'little', 'lamb']
>>> for i in range(len(a)):
	 	print(i, a[i])
...
0 Mary
1 had
2 a
3 little
4 lamb
```

**이터러블** : range( )가 돌려준 객체는 리스트처럼 동작하지만 리스트는 아님. 그냥 순서대로 돌려주는 객체이고, 실제 리스트를 만들지 않아 공간을 절약.

```python
>>> list(range(5))
[0, 1, 2, 3, 4]
```

### 4.4. 루프의 break 와 continue 문, 그리고 else 절

break : for나 while 루프로부터 빠져나감.

```python
>>> for n in range(2,10):
    	for x in range(2,n):
            if n % x == 0:
                print(n, 'equals', x, '*', n//x)
                break
            else:	#루프의 else절은 break가 발생하지 않을 때 실행됨.
                print(n, 'is a prime number')
...
2 is a prime number
3 is a prime number
4 equals 2 * 2
5 is a prime number
6 equals 2 * 3
7 is a prime number
8 equals 2 * 4
9 equals 3 * 3
```

- **continue** : 루프의 다음 이터레이션에서 계속 하도록 만듬.

```python
>>> for num in range(2, 10):
    	if num % 2 == 0:
            print("Found an even number", num)
            continue
        print("Found a number", num)
...
Found an even number 2
Found a number 3
Found an even number 4
Found a number 5
Found an even number 6
Found a number 7
Found an even number 8
Found a number 9
```

### 4.5. pass 문

pass문은 아무것도 하지 않음.

```python
>>> while True:    # 문법적으로 문장이 필요한 경우
    	pass
>>> class MyEmptyClass:    # 최소한의 클래스를 만들 때 사용
    	pass
>>> def initlog(*args):
    	pass
```

### 4.6. 함수 정의하기

```python
>>> def fib(n):    #피보나치 수열을 임의의 한도까지 출력하는 함수
    	""" Print a Fibonacci series up to n """    # 함수의 도큐멘테이션 문자열(docstring)
    	a, b = 0, 1
        while a < n:
            print(a, end=' ')
            a, b = b, a+b
        print()
...
>>> fib(2000)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597
```

전역 변수들은 함수 내에서 (global 문으로 명시하지 않는 이상) 직접 값이 대입될 수 없음. 함수 호출로 전달되는 실제 매개변수들(인자들)은 호출될 때 *값에 의한 호출 (call by value)* 로 전달됨.

```python
>>> fib
<function fib at 10042ed0>
>>> f = fib
>>> f(100)
0 1 1 2 3 5 8 21 34 55 89

>>> fib(0)    # return 문이 없는 함수도 None 값을 돌려줌
>>> print(fib(0))
None

>>> def fib2(n):
        """Return a list containing the Fibonacci series up to n."""
        result = []
        a, b = 0, 1
        while a < n:
            result.append(a)    # result = result + [a] 와 동일
            a, b = b, a+b
            return result    # 함수로부터 값을 갖고 복귀하게 만듬.
...
>>> f100 = fib2(100)
>>> f100
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
```



## 4.7. 함수 정의 더보기

### 4.7.1. 기본 인자 값

```python
>>>> def ask_ok(prompt, retries=4, reminder='Please try again!'):
        while True:
            ok = input(prompt)
            if ok in ('y', 'ye', 'yes'):
                return True
            if ok in ('n', 'no', 'nop', 'nope'):
                return False
            retries = retries - 1
            if retries < 0:
                raise ValueError('invalid user response')
            print(reminder)
....
```

여러가지 방법으로 함수 호출하기

- ask_ok( ' 정말 끝내길 원하세요? ' )
- ask_ok( ' 파일을 덮어써도 좋습니까? ', 2)
- ask_ok( ' 파일을 덮어써도 좋습니까? ', 2, ' 자, 예나 아니요로만 답하세요! ' )



```python
>>> i = 5
    def f(arg=i):
    	print(arg)
...
>>> i = 6
>>> f()
5

>>> def f(a, L=[]):
        L.append(a)
        return L
>>> print(f(1))    # 기본값은 오직 한 번만 값이 구해짐.
>>> print(f(2))    # 계속되는 호출로 전달된 인자들을 누적함.
>>> print(f(3))
[1]
[1, 2]
[1, 2, 3]

>>> def f(a, L=None):    # 연속된 호출 간에 기본값이 공유되지 않음.
        if L is None:
            L = []
        L.append(a)
        return L
```



### 4.7.2. 키워드 인자

함수는 kwarg=value 형식의 키워드 인자를 사용해서 호출 될 수 있음. 키워드 인자는 위치인자 뒤에 와야 하며, 두 개 이상의 값을 받을 순 없음. 순서는 중요하지 않음.

```python
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

parrot(1000)    # 1 positional argument
parrot(voltage=1000)    # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')    # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)    # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')
# 3 positional arguments
parrot('a thousand', state='pushing up the daisies')
# 1 positional, 1 keyword
```

```python
def cheeseshop(kind, *arguments, **keywords):    # 함수 정의하기
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

# 함수 호출하기
cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

# 출력 결과
Do you have any Limburger ?
I'm sorry, we're all out of Limburger
It's very runny, sir.
It's really very, VERY runny, sir.
----------------------------------------
shopkeeper : Michael Palin
client : John Cleese
sketch : Cheese Shop Sketch
```

### 4.7.3. 임의의 인자 목록

가장 덜 사용되는 옵션은 함수가 임의의 개수 인자로 호출될 수 있도록 지정하는 것.

```python
>>> def concat(*args, sep="/"):
...     return sep.join(args)
...

>>> concat("earth", "mars", "venus")
'earth/mars/venus'
>>> concat("earth", "mars", "venus", sep=".")
'earth.mars.venus'
```

### 4.7.4. 인자 목록 언 패킹

인자들이 이미 리스트나 튜플에 있지만, 분리된 위치인자들을 요구하는 함수 호출을 위해 언 패킹 해야 하는 경우.

예를 들어, 내장 range() 함수는 별도의 start 와 stop 인자를 기대함. 그것들이 따로 있지 않으면, 리스트와 튜플로부터 인자를 언 패킹하기 위해 *- 연산자를 이용하여 함수를 호출하면 됨.

딕셔너리도 **- 연산자를 써서 키워드 인자를 전달할 수 있음.

```python
>>> list(range(3, 6))    # 분리된 argument를 normal call
[3, 4, 5]
>>> args = [3, 6]
>>> list(range(*args))    # 리스트로부터 언 패킹 한 후 call argument
[3, 4, 5]
```

```python
>>> def parrot(voltage, state='a stiff', action='voom'):
...     print("-- This parrot wouldn't", action, end=' ')
...     print("if you put", voltage, "volts through it.", end=' ')
...     print("E's", state, "!")
...
>>> d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
>>> parrot(**d)
-- This parrot wouldn't VOOM if you put four million volts through it. E's bleedin' demised !
```



### 4.7.5. 람다 표현식

- **lambda** : 사용해서 작고 이름없는 함수를 만들 수 있음. 두 인자의 합을 돌려줌. 함수 객체가 있어야 하는 곳이면 어디나 사용 가능. 문법적으로는 하나의 표현식으로 제한됨.

```python
>>> def make_incrementor(n):
...     return lambda x: x + n    # 함수를 돌려주기 위해 람다 사용
...
>>> f = make_incrementor(42)
>>> f(0)
42
>>> f(1)
43
```

```python
>>> pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
>>> pairs.sort(key=lambda pair: pair[1])    # 작은 함수로 인자 전달
>>> pairs
[(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]
```



### 4.7.6. 도큐멘테이션 문자열

- 첫 줄은 짧고 간결하게.
- 대문자로 시작, 마침표로 끝.
- 줄과 줄 사이 간격을 띰.
- 뒷문장으로는 객체의 호출규약, 부작용 등을 설명



### 4.7.7. 함수 어노테이션

어노테이션은 함수의 _ _annotations_ _ 어트리뷰트에 딕셔너리로 저장됨. 다른 부분에는 아무런 영향을 미치지 않음. 매개변수의 이름 뒤에 오는 콜론으로 정의.

```python
>>> def f(ham: str, eggs: str = 'eggs') -> str:
...     print("Annotations:", f.__annotations__)
...     print("Arguments:", ham, eggs)
...     return ham + ' and ' + eggs
...
>>> f('spam')
Annotations: {'ham': <class 'str'>, 'return': <class 'str'>, 'eggs': <class 'str'>}
Arguments: spam eggs
'spam and eggs'
```

## 4.8. 막간극: 코딩 스타일

- 들려 쓰기에 4-스페이스를 사용, 탭 사용X

- 79자를 넘지 않도록 줄 넘김 하기

  이것은 작은 화면을 가진 사용자를 돕고 큰 화면에서는 여러 코드 파일들을 나란히 볼 수 있게 함.

- 함수, 클래스, 함수 내의 큰 코드 블록 사이에 빈 줄을 넣어 분리

- 가능하다면, 주석은 별도의 줄로 넣기

- 독스트링 사용하기

- 연산자들 주변과 콤마 뒤에 스페이스를 넣고,

  괄호 바로 안쪽에는 스페이스 X : `a = f(1, 2) + g(3, 4)`.

- 클래스와 함수들에 일관성 있는 이름을 붙이기

  관례는 클래스의 경우 `CamelCase`,

  함수와 메서드의 경우 `lower_case_with_underscores` 

  첫 번째 메서드 인자의 이름으로는 항상 `self` 를 사용.

- 국제적 환경에서 사용을 위해 특별한 인코딩 사용 하지 않기

- 식별자에 ASCII 이외의 문자를 사용하지 않기



# 5. 자료 구조

## 5.1. 리스트 더 보기

- list . append(x) : 리스트의 끝에 항목 더하기; a[len(a) : ] = [x]
- list . extend(iterable) : 리스트의 끝에 이터러블의 모든 항목을 덧붙여 확장; a[len(a) : ] = iterable
- list . insert(i, x) : 주어진 위치 i (0 부터 시작) 에 항목 x 를 삽입; a . insert(len(a), x) 는 a . append(x) 와 동일
- list . remove(x) : 리스트에서 값이 x와 같은 첫 번째 항목을 삭제. 없으면 에러
- list . pop( [i] ) : 리스트에서 [i] 위치에 있는 항목을 삭제하고 그 항목을 돌려줌. 인덱스를 지정하지 않으면( a.pop() ) 리스트의 마지막 항목을 삭제하고 돌려줌.
- list . clear() : 리스트의 모든 항목을 삭제; del a[ : ] 
- list . index(x[, start[, end]]) : 리스트의 항목 값이 처음으로 x가 되는 인덱스를 돌려줌(0부터 시작), 그런 항목이 없으면 value error
- list . count(x) : 리스트에서 x가 등장하는 횟수
- list . sort(key=None, reverse=False) : 리스트의 항목들을 제자리에서 정렬
- list . reverse() : 리스트의 요소들을 제자리에서 뒤집음
- list . copy() : 리스트의 얕은 사본을 돌려줌; a[ : ]

```python
>>> fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
>>> fruits.count('apple')
2
>>> fruits.index('banana')
3
>>> fruits.index('banana', 4)  # Find next banana starting a position 4
6
>>> fruits.append('grape')
>>> fruits
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']
>>> fruits.sort()
>>> fruits
['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']
>>> fruits.pop()
'pear'
```

### 5.1.1. 리스트를 스택으로 사용하기

마지막에 넣은 요소가 처음으로 꺼내지는 요소가 됨. (last-in, first-out)

스택의 꼭대기에 항목을 넣으려면 append() 사용.

스택의 꼭대기에서 값을 다시 꺼내려면 명시적 인덱스 없이 pop() 사용.

### 5.1.2. 리스트를 큐로 사용하기

처음으로 넣은 요소가 처음으로 꺼내지는 요소가 됨. (first-in, first-out)

하지만 다른 요소들을 앞으로 모두 이동시켜야 하기 때문에 효율적이지 않음.

```python
>>> from collections import deque
>>> queue = deque(["Eric", "John", "Michael"])
>>> queue.append("Terry")    # Terry arrives
>>> queue.append("Graham")    # Graham arrives
>>> queue.popleft()    # The first to arrive now leaves
'Eric'
>>> queue.popleft()    # The second to arrive now leaves
'John'
>>> queue    # Remaining queue in order of arrival
deque(['Michael', 'Terry', 'Graham'])
```

### 5.1.3. 리스트 컴프리헨션

리스트를 만드는 간결한 방법 제공.

```python
>>> squares = []
>>> for x in range(10):    # x 변수를 만들고(덮어쓰고) 루프 종료 후에도 남아있음
...     squares.append(x**2)
...
>>> squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

```python
squares = list(map(lambda x: x**2, range(10)))
```

```
squares = [x**2 for x in range(10)]
```

리스트 컴프리헨션은 표현식과 그 뒤를 따르는 for 절과 for, if 절들을 감싸는 [] 로 구성됨.

```python
>>> [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
```

```python
>>> combs = []    # 위의 코드와 for, if 문 순서가 같음
>>> for x in [1,2,3]:
...     for y in [3,1,4]:
...         if x != y:
...             combs.append((x, y))
...
>>> combs
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
```

복잡한 표현식과 중첩된 함수들을 포함할 수 있음.

```python
>>> from math import pi
>>> [str(round(pi, i)) for i in range(1, 6)]
['3.1', '3.14', '3.142', '3.1416', '3.14159']
```

### 5.1.4. 중첩된 리스트 컴프리헨션

```python
>>> matrix = [
...     [1, 2, 3, 4],
...     [5, 6, 7, 8],
...     [9, 10, 11, 12],
... ]

# 다음은 모두 같은 결과 (전치행렬 만들기)
>>> transposed = []
>>> for i in range(4):
...     # the following 3 lines implement the nested listcomp
...     transposed_row = []
...     for row in matrix:
...         transposed_row.append(row[i])
...     transposed.append(transposed_row)
...
>>> transposed
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]


>>> transposed = []
>>> for i in range(4):
...     transposed.append([row[i] for row in matrix])
...
>>> transposed
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]


>>> [[row[i] for row in matrix] for i in range(4)]
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

>>> list(zip(*matrix))
[(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]
```



## 5.2. del 문

리스트에서 값 대신 인덱스를 사용하여 항목 삭제.

리스트에서 슬라이스를 삭제하거나, 전체 리스트를 비우는 데도 사용.

변수 자체 삭제도 가능. (eg) del a    이후에 변수 a 를 참조할 수 없음

```python
>>> a = [-1, 1, 66.25, 333, 333, 1234.5]
>>> del a[2:4]
>>> a
[1, 66.25, 1234.5]
```
