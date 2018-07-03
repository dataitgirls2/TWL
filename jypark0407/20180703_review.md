# Python
* 넓은 분야에 쓰임.
* '괜찮은' 문법: 문법에 대한 설명이 간결함
* '괜찮은' 성능 : 수업에서 다룰 Python Library는 C언어로 쓰여져서 (Python보다 더 빠름) 성능이 좋음.

**Trade Off**
* 컴퓨터에 사고하는 방식에 가까움 - 컴퓨터를 극도로 사용할 수 있어서 성능이 빨라짐
* 인간이 사고하는 방식에 가까움 - 다루기는 쉬울 수 있지만 효율이 떨어짐

요즘은 컴퓨터의 속도가 빨라져서 인간이 다루기 쉬운 언어들이 더 선호되는 편임. 

## Pair Programming using Blockly

1. Blockly로 1부터 100까지 모두 더한 값 출력하기

```python
sum2 = None
i = None


sum2 = 0
for i in range(1, 101):
  sum2 = sum2 + i
print(sum2)
```

2. Blockly로 1부터 100 사이에 존재하는 모든 3의 배수의 평균을 출력하시오.

```python
number = None
sum2 = None
i = None


number = 0
sum2 = 0
for i in range(1, 101):
  if i % 3 == 0:
    sum2 = sum2 + i
    number = number + 1
print(sum2 / number)
```

### Live Programming
http://www.pythontutor.com/live.html#mode=edit


## Python Programming using Colab
https://colab.research.google.com/drive/119qBunjvT0nojgbZftuDIJTHuBf4xN2y#scrollTo=bhjVLVsQOZnn

Shift + Enter to compile

```python
n = 0  # n (variable) 0 (expression, literal) # assign literal integer 
total = 0
for i in range(100):
    total = total + i
    n = n + 1
average = total/n
print (average)
```

1. Object vs Literal
0xF(16진법) | 15(10진법) --> 둘다 15를 의미함. 더 정확하게 말하자면, '15'인 object에 대응하는 값들임.

메모리에 있는 '15'이라는 진수를 위해서 표현할 수 있는 방법이 여러 개 있음.

Expression is evaluated to derive evaluated value, which is stored in memory.

Frame/Object - stored in separate memories

List is an object.

```python
n = 0
total = 0
for i in range(100):
    total = total + i
    n = n + 1
average = total/n
print (average)
```

2. 문법의 일부
짙은 파랑색

연한 파랑색 



(색깔은 변경 가능)


* Python Documentation 
https://docs.python.org/3/reference/index.html

**총점과 평균 구하기. 데이터 = 70점, 55점, 90점, 85점**
```python
scores = [70, 55, 90, 85, 100, 77]
total = 0
number = 0
for i in scores:
  total = total + i
  number = number + 1
average = total/number
print(average)
print(total)
```

## Defining Function 
```python
def calc_sum(numbs):
    result = 0 
    for i in numbs:
        result = result + i
    return result 
    
scores = [50, 60, 70]
total = calc_sum(scores)
print (total)
```
