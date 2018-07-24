# 180703

## 애란선생님(오전)

패턴이 존재하는 환경에서 정량적이고 빈번한 feedback을 받기
어떤 데이터를 어디에서 수집할 것인가? 는 문제는 인간의 직관과 더 관련이 있음.
직관과 데이터의 조화가 중요*

#### 파이썬(1991)

- 활용분야: 데이터 분석, 과학 계산, 웹 프로그래밍, 게임 서버 등
- 장점
  - 분석부터 웹서비스 적용까지 한 번에 가능
  - 한국/미국 개발자 커뮤니티가 훌륭함
  - 참고자료가 제법 풍부함
  - 제법 괜찮은 문법 -> 쓰고 익히기가 간결한가의 balance가 중요
    - 이 언어의 문법을 설명하기 위한 매뉴얼이 간결할수록 꽤나 괜찮은 편 (eg) io language는 문법이 A4 반 페이지가 전부.
  - 제법 괜찮은 성능 -> 같은 실행결과를 얻기 위한 실행시간이 꽤 빠름
  - 다양한 패러다임? 동일한 결과물을 만들기 위한 여러가지 방식이 존재(eg) 1부터 10까지 더하는 여러가지 방법
- “컴퓨터랑 멀다” = ”인간과 가깝다”  trade-off 존재
- 컴퓨터 입장에서는 비효율적으로 동작할 수 있다
- 성능과 배터리의 절약 VS 인간의 사고로 쉽게 사용
- IDC(Internet Dater Center)





### 오후수업

```python
m = 0xF
n = 0
total = 0

for i in range(5):
    total = total + i
    n = n + 1
average = total / n
print(average)

```


Frame: 변수 틀
objects: int 0 이 담겨있음.
=: 대입연산자(operator)

`0=n`
> syntax error(문법오류): can’t assign to literal

`n=0`
> 대입문
> 변수=수식
> 수식(expression)을 평가 후 변수 memory에 담음
수식>>literal
*n에 어떤 수를 넣기 위하여 쓸 수 있는 코딩이 여러가지임.
(eg) n=15 (10진수) n=0xF (16진수) n=10+5

짙은 파란색: literal
쨍한 파란색: python문법

`range(100)` > 0~99까지 100개의 원소
`for i in [0,1,2,3,4,5]` > [원소 리스트] 5개의 정수가 들어있는 리스트 object 만들어짐.

리스트 안에 리스트를 담을 수도 있음.
(eg) [[3,1],2,4,3]

대입문의 오른쪽에는 무조건 expression이 와야 함.
expression 자리에 올 수 있는 것들:

- literal+literal
- 변수+변수
- 변수+literal
- expression+expression

for등의 반복문 쓸 때 block하는 방법: 들여쓰기(tab써도 되긴 하는데 웬만하면 4 space로 구분)

reference가 사라지면 hip에 있는 object는 garbage로 보냄.

float(부동소수점): 소수점이 떠다님.
수학에서의 소수점은 무한함. 하지만 프로그램에서는 integer를 흉내 내어 -21억~21억까지로 지정하고, 자릿수를 제한하거나 정밀도를 제한함.
(eg) 2와 2.0의 차이
정수/정수는 floating point로 자동 변환됨

n에 0.0을 넣으면 정수 0이 아니라, 실수로 처리됨.

- STEM(Science Technology Engineering Mathematics)

\<font color=brown> 마크다운 문법 폰트 색 바꾸기

#### 라이브러리와 함수

http://www.pythontutor.com
함수 이름을 지을 때는 보통 동사 형태로, 변수는 명사 형태로 지음
print : 출력 장치에 결과물을 찍어라
return : memory 상에 실행 결과를 저장해라.

m = 0xF
n = 0
total = 0
lists = [[3,1],2,4,3]
nums=[0,1,2,3,4]
x=nums[0]
for i in nums:
    total = total + i
    n = n + 1
average = total / n
print(average)

함수 정의하기(합, 길이, 평균)
### sum function: sum()
def calc_sum(numbs):
    result = 0
    for num in numbs:
        result = result + num
    return result

### length function: len()

```
def calc_len(numbs):
    result = 0
    for num in numbs:
        result = result + 1
    return result
```

### average function

```python
def calc_average(numbs):
    total = calc_sum(numbs)
    length = calc_len(numbs)
    return total / length
```

### executing function

```python
scores = [50, 60, 70]
avg = calc_average(scores)    #calling function
print(avg)
```

stack overflow 스택이 너무 많이 쌓임(함수 내의 함수를 너무 많이 호출하는 경우)
object는 아무도 가리키는 대상이 없을 때 사라짐
함수 내의 변수는 지역변수여서 함수 내에서만 영향을 미침. 외 변수는 global 변수.


