## 데잇걸즈 6일차 (2018.07.03.) TIL



#### 파이썬 개요

- 파이썬 : 데이터. 과학. 웹 프로그래밍에서 사용. 
- 장점 : 데이터 수집/분석 및 웹 적용에 모두 사용 가능. 문법/성능이 괜찮음. 다양한 패러다임 지원. 커뮤니티/참고자료 많음. 접착제 언어.
    * 괜찮은 문법 : 학습/사용이 간결하고 직관적. 문법에 대한 설명이 간결함.
    * 괜찮은 성능 : 명령 수행 속도가 느리지 않음.
    * 접착제 언어 : 다른 다양한 언어와 결합하여 사용 가능 (C, Java 등)



#### 파이썬 실습

- Scratch -> Python 실습 : Blockly (https://blockly-demo.appspot.com/static/demos/code/index.html)

- Python 실습 : Google Colaboratory 

    - https://colab.research.google.com/notebooks/welcome.ipynb#recent=true
    - 마크다운(.md) 문법 사용 가능
    - '범죄통계' 파일 @데잇걸즈2 수업자료 폴더 : 향후 데이터를 다루는 방법을 preview 

- Python 실습 2 : Pythontutor. 

    - 소스 코드를 단계별로 실행하면서 작동 원리/오류 원인을 확인 가능. 
    - http://www.pythontutor.com

    

#### 파이썬 문법
- 대입문 : '변수 = 수식' 형식. '='는 대입 연산자임. literal, integer, floating도 수식임.
- 키워드 : 언어 구현을 위해 개발 환경에서 기능이 예약된 문자열, 변수 이름으로 사용 불가
- for 변수 in 리스트 : 반복문. 리스트로 정의된 조건의 한도 내에서 작동을 반복함.

~~~
n = 0	#대입문
total = 0
nums = [90, 95, 92, 100]	#nums를 안 설정하고
for i in nums:		  	    #여기를 for i in range(5): 로 써도 됨
    total = total + i
    n = n + 1
average = total / n
print(average)
~~~

- 변수 등을 통해 호출될 수 있는 연결 관계가 모두 끊어진 object(메모리에 저장된 임시 값)는 자동 삭제됨
- 정수 : Integer (int) / 실수 : Floating point (float). 
- 실수 + 정수 = 실수로 출력됨.
- 파이썬에서 첫 번째 칸은 '0'번 칸임. 즉, 두 번째 칸이 '1'번 칸임.



#### 파이썬 실습 2

~~~
# Q. 70, 55, 90, 85, 100, 77의 합계와 평균 구하기

score = [70, 55, 90, 85, 100, 77]
sum_score = sum(score)
average = sum_score / 6
print(score, '의 합계와 평균 :', sum_score,',', average)
~~~

~~~
# 합계 구하기 실습

def calc_sum(numbs):			#함수 정의('def')는 동사형, 변수 정의는 명사형을 주로 사용
    result = 0				    #결과값을 저장하는 변수
    for num in numbs:
        result = result + num
    return result				#함수의 결과값을 반환
    
def calc_len(numbs):
    result = 0
    for num in nums:
        result = result + 1
    return result
    
def calc_average(numbs):
    total = calc_sum(numbs)
    length = calc_len(numbs)
    return total / length
    
scores = [50, 60, 70]
total = calc_sum(scores)		#함수를 호출
avg = calc_average(scores)
print(total, avg)
~~~

~~~
# 참고 : $$ 수학/공학 수식을 입력할 때에는 앞/뒤로 '$$'를 붙이면 됩니다. $$
~~~

