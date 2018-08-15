## 프로젝트

프로젝트 : 거창한 거 아님. 더 자주해서 부담감을 줄이는 것이 더 중요하니까 프로젝트는 자주 해보자!



## (Test-Driven development로 진행한) 자판기 프로젝트 

1. 준비하기
   1. git init을 사용해서 로컬에 git 생성
   2. test.py 생성
   3. pipenv의 pytest설치 및 테스트
2. 테스트 코드 추가 및 테스트 실행
3. 테스트 실행에 기반해서 프로그램 짜기
4. 2,3번을 반복하면서 테스트 프로그램을 간결하고, 의도가 더 잘 드러나게 만들기

사용자들의 편의를 생각해서 코드를 디자인할 수 있음. 



**로컬에 git 생성하는 이점**

- version control system이로서 코드 변경 이력을 쉽게 확인하고, 전 상태로 되돌릴 수도 있다. 
- 

**TD와 QA와 차이**

test-driven development이지, software test가 아니다.

여기서 테스트는 간결한 알고리즘을 짜기 위한 도구로 볼 수 있다.

TDD를 한다고 QA가 필요없는 것은 아니다. 



**Clean Code?**

"Do The Simplest Thing That Could Possibly Work"

"You Ain't Gonna Need It"

코드를 읽을 때 평범한 문장처럼 읽히는 코드

쓸 수 있는 가장 단순한 기술을 씀. (기술 낭비 X)



**Creating Test**

* 하나의 테스트에 assertion이 많으면 에러가 났을때 체크하기 어려움. 다른 테스트를 만들어서 assertion을 만드는 것이 더 나음.
* 각각의 테스트는 격리되어야 함. (test isolation) 하나의 테스트는 다른 테스트의 간섭을 받으면 안 됨.



## Class& Object

https://en.wikipedia.org/wiki/Object-oriented_programming

Object : Class + Instance를 통칭해서 부름

​	Class : Category라고 생각하면 됨.  Class 자체에는 실체가 없음.

​		Instance : Class의 예시. 실체가 있음.

​	Method : Object 내부의 함수. 첫번째 인자로 self를 무조건 받아야 			

​			한다.



Class를 쓰는 이유 : 연산을 쉽게 하기 편함. 있어야 할 것이 없으면 코드가 복잡해짐.

Object-Oriented Programming : 객체 (Receiver)에게 메세지를 보내는 (호출) 형식으로 프로그래밍.



```python
class VendingMachine
	def __init__(self):    # 첫 번째 인자로 self를 받음
        self._change = 0  # change라는 변수에 0이라는 integer literal object를 assign함. 
        # 함수 (여기서는 method) 밖에서 쓰지 말하는 의미로 change앞에 "_" (underscore)를 붙여줌.
```



## Others

CLI (Command Line Interface) : 익숙해지면 유용함. 

예시들

```text
atom .  # atom 프로그램을 열기
```

```text
touch (파일이름)  # 파일 생성
echo (내용)      # print 내용
echo (내용) > (파일이름)  # insert 내용 into 파일이름 - 파일에 들어가 있던 내용은 지워짐!
echo (내용) >> (파일이름) #  파일이름의 내용에 (내용)을 append
cat   # explore the file content
```



Python 코드 간결하게 만들기 

```python
cmd = token[0]
params = token[1:]
    
cmd,params = token[0], token[1:]
```



Add+Commit 같이 하기

```python
git commit -am "(message)"
```