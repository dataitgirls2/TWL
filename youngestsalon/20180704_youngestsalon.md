####  20180704 TIL : 파이썬 자습서 3-5장 요약



- 파이썬 자습서 주소

  ~~~
  https://docs.python.org/ko/3/tutorial/index.html
  ~~~

  

- 숫자

  - 사칙연산(+, -, *, -), 몫(//), 나머지(%), 제곱(**)

  - 나눗셈(/) : 무조건 실수형으로 결과값을 출력

  - ''-'보다 '**'의 우선순위가 높음

    ~~~
    -3 ** 2 = -(3 ** 2) = -9
    (-3) ** 2 = 9	#우선순위 조정을 위해 괄호를 사용
    ~~~

  - 대화형 모드 : 마지막 인쇄된 표현식은 변수 _에 대입됨

    → 변수 _ 에는 직접 값 대입 금지 : 내장 변수의 작동을 방해함.

    ~~~
    tax = 12.5 / 100
    price = 100.50
    price * tax = 12.5625
    price + _ = 113.0625	#변수 _ = 12.5625
    round(_, 2) = 113.06	#변수 _ = 113.0625
    ~~~

    

- 문자열 

  - 작은따옴표('')나 큰따옴표("")로 둘러쌈

  - 이스케이핑 코드 : \

  - 줄 바꿈 : \n

  - print() 함수 : 따옴표 자동 생략, 이스케이핑 코드 자동 반영

  - 역슬래시 뒤 문자가 특수문자가 아닌 경우 : 따옴표 앞에 'r' 추가

  - 여러 줄 문자열 : 삼중 따옴표 (''' 내용 ''' 또는 """ 내용 """)

  - 삼중 따옴표 안에서 줄바꾸기 방지 : 역슬래시

    ~~~
    #입력 코드
    print("""\
    Usage : thingy [options]
    	-h
    	-H Hostname
    """)
    
    #출력 결과 : 첫 줄에 빈 줄이 생성되지 않음
    Usage : thingy [options]
    	-h
    	-H Hostname
    ~~~

  - 문자열 이어붙이기(+), 반복(*)도 가능

  - 문자열 리터럴 + 문자열 리터럴 : + 사용 불필요 (자동으로 붙임)

  - '변수 + 변수 ' 또는 '변수 + 문자열 리터럴' : + 사용 필요

  - 문자열 인덱스 : 첫 번째 문자 = 인덱스 0

  - 음수 문자열 인덱스 : 끝에서부터 카운트, -1부터 시작.

  - 슬라이싱 : 부분 문자열을 얻을 때 사용

    ~~~
    word = 'Python'
    word[:2] + word[2:]
    #'Python'이 출력됨 = Py + thon이기 때문
    # s[:i] + s[i:] = s : 종료 위치의 문자는 포함되지 않음
    ~~~

  - len() 함수 : 문자열의 길이를 돌려줌



- 리스트

  - 다른 값들을 덩어리로 묶는데 사용

  - 서로 다른 형의 항목들을 포함 가능

  - 인덱싱 가능

  - 슬라이싱 가능 : 새 리스트로 돌려줌

  - 이어 붙이기 연산 지원 : + 연산자 사용

  - 가변(mutable) : 내용 변경 가능

    - 항목 추가 : append() 메소드
    - 항목 변경 / 삭제 : 슬라이싱 활용
    - 전체 항목 삭제 (빈 리스트가 됨) : 리스트명[:] = []

  - 길이 확인 : len() 함수

  - 중첩 가능

    


- print() 함수
  - 주어진 인자들의 값을 인쇄
  - 문자열 : 따옴표 없이 출력
  - 인자들 간에 빈칸 삽입



- 제어 흐름문

  1. while 문

     - 조건이 참인 동안 실행
     - 루프의 바디 : 들여쓰기 필요. 복합문 입력 시 끝에 빈 줄 필요.

  2. if 문

     - if 문 단독, if - else - 문, if - elif - else - 문 모두 가능

  3. for 루프

     - 시퀀스(리스트, 문자열)의 항목들을 순서대로 이터레이션
     - 루프 안에서 시퀀스를 수정할 시 : 사본을 먼저 만들 것

  4. break

     - for 문, 혹은 while 문을 빠져나가게 만듦
     - 루프가 break 문으로 종료할 시 else 문은 실행되지 않음

  5. continue 문

     - 루프의 다음 단계가 계속 실행되도록 함

  6. pass 문

     - 아무것도 하지 않음
     - 문법적으로 문장은 필요하지만, 프로그램은 할일이 없을 때
     - 최소한의 클래스(빈 클래스)를 만들때 흔히 사용
     - 함수/조건부 바디의 자리만 채워 놓을 때 (= '추후 작업 예정')

     

- range() 함수
  - 숫자들을 반복할 때 사용
  - 수열을 만듦 (단, 끝 값은 만들어지는 수열에서 제외)
  - 형식 : range(시작점, 끝점, 증가분) 
  - 음수도 사용 가능



- enumerate() 함수
  - 문자열로 구성된 리스트를 루핑할 때 사용
  - 위치 인덱스와 대응하는 값이 동시에 출력됨



- 함수

  - 정의할 때 : def 함수이름(형식 매개변수들의 목록)

    ~~~
    def 함수이름 (형식 매개변수들의 목록)
        바디
    
    def prt_list(n):
        """ 0부터 n까지의 수열을 리스트로 출력합니다 """
    	print(list(range(0, n)))
    	
    prt_list(10)	#prt_list 함수를 호출하여 사용
    ~~~

  - Docstring (독스트링)

    - 함수 바디의 첫 번째 문장에 위치한 문자열 리터럴
    - 함수의 기능을 설명 : 사용하는 습관을 들이자.

  - 전역 변수

    - 함수 내에서 참조는 가능
    - 함수 내에서 직접 값이 대입될 수는 없음
    - 함수 내에서 직접 값을 대입하려면 global 문 사용

  - 함수의 이름 변경 : 새로운 이름에 기존 함수를 대입

    ~~~
    p_l = prt_list
    p_l(10)		#prt_list(10)과 동일한 결과 출력
    ~~~

  - 함수의 결과로 출력할 값이 없다면, 아무것도 출력하지 않음

    - 굳이 'None'이라는 값을 봐야 한다면, print() 를 사용 

  - 인자 목록 언 패킹 

    - 리스트/튜플의 경우 : *리스트명 (또는 *튜플명)

    - 딕셔너리의 경우 : **딕셔너리명

      ~~~
      # 딕셔너리 언 패킹 & 다중 키워드 인자의 예시
      
      def parrot(voltage, state='a stiff', action='voom'):
          print("-- This parrot wouldn't", action, end=' ')
          print("if you put", voltage, "volts through it.", end=' ')
          print("E's", state, "!")
      
      d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
      parrot(**d)
      
      # 결과값
      -- This parrot wouldn't VOOM if you put four million volts through it. E's bleedin' demised !
      ~~~

  - lambda 함수

    - 한 줄짜리 간단한 익명의 함수를 지정 (Ex. lambda a, b: a+b)

  - 함수 어노테이션

    - 사용자 정의 함수가 사용하는 형들에 대한 선택적 메타데이터 정보

    - 함수의 \__annotations__ 어트리뷰트에 딕셔너리로 저장

    - 함수의 다른 부분에는 아무런 영향을 미치지 않음

    - 값을 구할 때 : 매개변수 목록과 콜론 사이에 "-> 표현식" 추가

      ~~~
      def f(ham: str, eggs: str = "eggs") -> str:
          print("Annotations:", f.__annotations__)
          print("Arguments:", ham, eggs)
          return ham + ' and ' + eggs
      
      f('spam')
      
      #결과값은?
      Annotations: {'ham': <class 'str'>, 'return': <class 'str'>, 'eggs': <class 'str'>}
      Arguments: spam eggs
      'spam and eggs'
      ~~~




- 리스트의 메소드
  - list.append(x) 
    - 리스트에 끝에 항목을 더함
  - list.extend(iterable)
    - 리스트의 끝에 이터러블의 모든 항목을 덧붙여서 확장
  - list.insert(i, x)
    - 주어진 위치(i)에 항목(x)을 삽입
  - list.remove(x)
    - 리스트에서 값이 x와 같은 첫 번째 항목을 삭제
    - 해당 항목이 없으면 에러
  - list.pop(i)
    - 리스트에서 주어진 위치에 있는 항목을 삭제하고, 돌려줌
    - a.pop() : 인덱스 미 지정 → 마지막 항목을 삭제하고 돌려줌
  - list.clear()
    - 리스트의 모든 항목을 삭제
  - list.index(x[, start[, end]])
    - 리스트의 항목 중 값이 x와 같은 첫 번째의 것의 0부터 시작하는 인덱스를 돌려줌
    - 해당 항목이 없으면 ValueError
  - list.count(x)
    - 리스트에서 x가 등장하는 횟수를 돌려줌
  - list.sort(key=None, reverse=False)
    - 리스트의 항목들을 제자리에서 정렬
  - list.reverse()
    - 리스트의 요소들을 제자리에서 뒤집음
  - list.copy()
    - 리스트의 (얕은) 사본을 돌려줌.



- 리스트를 스택 / 큐로 사용하기

  - 스택으로 사용하기 (Last-in, First-out)

    - 상대적으로 용이함
    - 마지막에 값 추가(append()), 값 꺼내기(pop())

  - 큐로 사용하기 (First-in, First-out)

    - 상대적으로 다소 불편함 (느림)

    - collections.depue 사용을 추천

      ~~~
      from collections import deque
      queue = deque(["Eric", "John", "Michael"])
      queue.append("Terry")
      queue.append("Graham")
      gueue.popleft()		#Eric : The first to arrive now leaves
      gueue.popleft()		#John : The second to arrive now leaves
      queue		#deque(['Michael', 'Terry', 'Graham']) : Remaining queue
      ~~~



- 리스트 컴프리헨션

  - 리스트를 만드는 간결한 방법을 제공

  - 표현식 + for 절 (+ for 절 혹은 if 절을 감싸는 대괄호들)

  - 결과는 리스트로 반환

    ~~~
    squares = []
    for x in range(10):
        squares.append(x**2)
    
    squares = list(map(lambda x: x**2, range(10)))
    squares = [x**2 for x in range(10)]
    
    #세 가지 모두 결과는 동일함 : 0~9의 제곱값 리스트를 반환.
    squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
    ~~~

  - 복잡한 표현식과 중첩된 함수들을 포함할 수 있음

    ~~~
    from math import pi
    [str(round(pi, i)) for i in range(1, 6)]
    #결과 : ['3.1', '3.14', '3.142', '3.1416', '3.14159']
    ~~~

  - 리스트 컴프리헨션의 중첩도 가능

    ~~~
    Ex. [[row[i] for row in matrix] for i in range(4)]
    ~~~



- del 문

  - 리스트에서 인덱스를 사용해서 항목을 삭제하는 방법

  - 리스트에서 슬라이스를 삭제할 때도 사용 가능

  - 리스트에서 전체를 삭제할 때도 사용 가능

  - 변수 자체를 삭제할 때도 사용 가능

    ~~~
    a = [1, 2, 3, 4, 5]
    del a[0]	#항목 삭제
    del a[1:2]	#슬라이스 삭제
    del a[:]	#전체 항목을 전부 삭제
    del a		#변수 자체를 삭제
    
    #변수 삭제 후에 이름 a를 참조하면 에러 발생
    ~~~

    

- 튜플

  - 시퀀스 자료 형 중 한 가지
  - 쉼표로 구분되는 여러 값으로 구성됨
  - 출력되는 튜플은 항상 괄호로 둘러싸임
  - 튜플의 개별 항목을 변경(대입)하는 것은 불가능
  - 리스트와 같은 가변 객체가 포함된 튜플 생성은 가능
  - 일반적으로 이질적인 요소들의 시퀀스를 포함
  - 패킹, 언 패킹, 인덱싱 가능
  - 빈 튜플 생성 가능 : 튜플명 = ()
  - 튜플 항목이 하나 뿐인 경우 쉼표 필요 : 튜플명 = (항목명**,** )



- 집합

  - 중복되는 요소가 없는 순서 없는 컬렉션

  - 중괄호(단, 빈 중괄호는 사용 불가) 혹은 set() 함수를 사용하여 생성

  - 용도 : 멤버십 검사 (in 사용), 중복 엔트리 제거 (print() 사용)

  - 집합 객체에 대한 수학적인 연산도 가능 : 합집합, 교집합, 차집합 등

    ~~~
    차집합 : - 사용
    합집합 : | 사용
    교집합 : & 사용
    대칭 차집합 (= 합집합 - 교집합) : ^ 사용
    ~~~

  - 집합 컴프리헨션도 가능 (리스트 컴프리헨션과 비슷)

    ~~~
    a = {x for x in 'abracadabra' if x not in 'abc'}
    #결과값 a = {'r', 'd'}
    ~~~



- 딕셔너리

  - 값을 키와 함께 저장하기 때문에 키로 인덱싱되는 시퀀스

  - {키: 값, 키2: 값2, 키3: 값3, ...} 형태로 입력/출력

  - 키에는 모든 불변형을 사용 가능 : 문자열, 숫자 등

  - ''키: 값'' 쌍의 집합. 동일 딕셔너리 내에서 키는 중복되지 않아야 함.

  - {} : 빈 딕셔너리를 생성

  - 값을 추출할 때 : 주어진 키를 사용

  - 값을 삭제할 때 : del (키: 값 쌍을 모두 삭제 가능)

  - 이미 사용 중인 키로 저장 : 해당 키의 예전 값은 잊혀짐

  - 존재하지 않는 키로 값을 추출 : 에러 발생

  - list(d) : 딕셔너리 내의 모든 키의 리스트를 삽입 순서대로 돌려줌

  - sorted(d) : 딕셔너리 내의 모든 키를 정렬해서 돌려줌 

  - in / not in 키워드 : 키가 딕셔너리 내에 있는지/없는지 검사

  - 키-값 쌍들의 시퀀스(Ex. 키-값 쌍의 튜플 모음인 리스트)인 경우

    ~~~
    #dict() 생성자를 사용
    dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
    # 결과값 : {'sape': 4139, 'guido': 4127, 'jack': 4098}
    ~~~

  - 딕셔너리 컴프리헨션 

    - 임의의 키와 값 표현식들로 딕셔너리를 만드는데 사용 가능

      ~~~
      {x: x**2 for x in (2, 4, 6)}
      #결과값 : {2: 4, 4: 16, 6: 36}
      ~~~

  - 키가 간단한 문자열인 경우, 키워드 인자로 딕셔너리 생성 가능

    ~~~
    dict(a=12, b=24, c=36)
    #결과값 : {'a': 12, 'b': 24, 'c': 36}
    ~~~

    

- 루프 테크닉

  - 딕셔너리로 루핑할 때 : item() 메소드 사용

    - 키, 값을 동시에 얻을 수 있음

      ~~~
      knights = {1: 'A', 2: 'B'}
      for int, str in knights.items():
          print (int, str)
          
      1 A
      2 B
      ~~~

  - 시퀀스를 루핑할 때 : enumerate() 함수 사용

    - 위치 인덱스와 대응하는 값을 동시에 얻을 수 있음

      ~~~
      for i, v in enumerate(['A', 'B', 'C']):
          print (i, v)
          
      0 A
      1 B
      2 C
      ~~~

  - 둘, 또는 그 이상의 시퀀스를 동시에 루핑할 때

    - zip() 함수로 엔트리들의 쌍을 만들기

      ~~~
      questions = ['name', 'quest', 'favorite color']
      answers = ['lancelot', 'the holy grail', 'blue']
      for q, a in zip(questions, answers):
          print('What is your {0}? It is {1}.'.format(q, a))
      
      What is your name? It is lancelot.
      What is your quest? It is the holy grail.
      What is your favorite color? It is blue.
      ~~~

  - 시퀀스를 거꾸로 루핑하고 싶을 때

    - 정방향으로 시퀀스를 지정한 다음 reversed() 함수 호출

      ~~~
      for i in reversed(range(1, 10, 2)):
          print (i)
          
      9
      7
      5
      3
      1
      ~~~

  - 정렬된 순서로 시퀀스를 루핑하고 싶을 때

    - sorted() 함수 사용 : 소스를 변경하지 않을 수 있음

      ~~~
      basket = [1, 6, 7, 3, 10]
      for n in sorted(set(basket)):
          print(n)
      
      1
      3
      6
      7
      10
      ~~~

  - 루프를 돌고 있는 리스트는 변경하지 말 것

    - 대신, 새 리스트를 생성 : 더 간단하고 안전함



- 조건 더 보기

  - 비교 연산자 in : 값이 시퀀스에 있는지 검사

  - 비교 연산자 not in : 값이 시퀀스에 없는지 검사

  - 연산자 is : 두 객체가 같은 객체인지 비교

  - 연산자 is not : 두 객체가 다른 객체인지 비교

  - 모든 비교 연산자들은 우선 순위가 같음

  - 모든 비교 연산자들은 모든 산술 연산자보다 우선순위가 낮음

  - 비교는 연쇄할 수 있음 (Ex. a < b == c)

  - 비교는 결합 가능 : 논리 연산자 and와 or를 사용

  - 비교의 결과(& 모든 논리 표현식)는 not으로 부정될 수 있음

  - not, and, or의 우선 순위 : not > and > or

    ~~~
    A and not B or C == (A and (not B)) or C
    ~~~

  - 비교의 결과(& 다른 논리 표현식의 결과) : 변수에 대입 가능

