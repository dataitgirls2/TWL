# Python

- 범용적 프로그래밍 언어. 주로 데이터 분석, 과학 계산, 웹 프로그래밍 등에 사용
- a list of Programming languages : https://en.wikipedia.org/wiki/List_of_programming_languages
- Python? :  https://en.wikipedia.org/wiki/Python_(programming_language)
- 장점
  - 데이터 수집, 분석, 웹 서비스 적용까지 모든 과정을 한 언어로 끝낼 수 있음.
  - 문법, 성능도 not bad.
  - 다양한 패러다임 지원.
  - (한국도) 개발자 커뮤니티가 발달.
  - 참고자료 풍부.
  - 외워야하는 키워드 30개 정도. basic은 100개 정도. 영어 자연어를 닮게 만들기 위해 키워드가 많아짐. 문법이 너무 간소하면 비직관적. 사용할 때 짧은 문법들을 조합 해야함.
- 데이터 가공 -> 웹을 통해 데이터 제공 -> 앱 데이터 또한 웹으로 부터...

Beautiful is better than ugly

Explicit is better than implicit

Simple is better than complex

Complex is better than complicated

Readability counts


- 개발자를 미치게 하는 10가지 언어 : http://www.itworld.co.kr/slideshow/90954
- 스크래치에서 blockly로 파이썬 넘어가보자 : https://blockly-demo.appspot.com/static/demos/code/index.html?lang=ko
- 서버 호텔=ICT


# 파이썬 문법
'n = 0' : 대입문 assignment statement
왼쪽 변수 = 수식(expression)을 입력. 0 -> literal intiger정수도 수식.
Literal 0과 objects 0은 다름
파이썬에서 16진수 F=15
모든 Expression을 evaluation평가해서 나오는 0은 evaluated value=objects 0

짙은 파란색 : expression
옅은 파란색 : keyword

반복문 문법 : for i in range(100)-list,바구니
For I in range(5):
=for I in [0, 1, 2, 3, 4]:
:콜론은 실행의 의미!
block만들고 싶으면 관습상 spacebar 4번으로 함. tab해도 되지만 관습x

reference참조(화살표)가 사라지면 objects는 garbage가 됨
->garbage collector 프로그램(python runtime에 들어있음)이 garbage를 없애서 메모리를 확보 시켜줌.

- Kill : parent process가 child process를 만들고 삭제됨
- Demon : kill되지 않는 child
- Float : floating point 부동소수점 2.0은 int 2와는 다른 것.

컴퓨터 정수 바운더리 : -21억~+21억
자릿수나 정밀도를 제한해서 숫자를 표현함.

Nums = [0, 1, 2, 3, 4]
For I in nums:

colab
$$ 사이에 타입하면 수식 $$

Library : 블럭을 쌓아서 압축하는 개념
함수function를 정의하는 문법 def
Def calc_sum()
-> Define calculate_summation()
함수 이름은 주로 verb
변수 이름은 주로 noun
블럭이 시작되기 전에는 :을!

Print (표준 출력장치, 화면, 단말기로 내보낸다는 의미)
Print output (가상의 옛날 프린터기)

Return (박스에서 내보낸다는 의미. 메모리에 있음)

Stack : 함수를 쌓는것
이름 공간

과제 : 3,4,5장을 정독
