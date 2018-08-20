### 20180814_The_VendingMachine_Project

새로운 개념: 클래스와 객체, 객체지향프로그래밍

오늘은 내 컴퓨터에서 작업을 하고 깃헙에 올릴 것이다. 

"자판기 프로젝트"

$ echo Hello
Hello

pytest는 자동으로 _test를 찾아서 자동으로 실행해주는 모듈이다. 테스트주도개발의 좋은 예 ; 오픈소스가 공개될때 테스트케이스가 공개되는게 관습이 되었다. 

      있어야할 것 : 
        Pipfile
        Pipfile.lock
        test_vm.py
git status를 해보고 위에 파일중에 git ignore에 넣어야할 것을 확인해본다. 

repo에 최소한의 깔끔한 파일만 나오게 해야한다. 

git ignore를 하고 한번에 할 수 있는 방법 : echo

```git commit -am``` : add와 commit을 한번에 한다. 

#### 클래스, 객체, 인스턴스?

```
import pandas as pd

# 1은 정수 리터럴 표현식, 평가값은 정수 인스턴스 1
x = 1
1은 메모리 어딘가에 담긴다. int 객체 1이 생긴다. 

# DataFrame은 클래스. 클래스를 호출하면 해당 클래스의 인스턴스가 만들어짐
df = pd.DataFrame(...)

# read_csv는 pd 모듈에 담긴 함수.
# 함수 내부에서 pd.DataFrame()을 호출하여 DataFrame 클래스의 인스턴스를 생성
df = pd.read_csv(...)
read_csv라는 모듈이다. dataframe이라는 클래스의 객체 instance가 생기는 것이고 이게 df에 담기는 것이다. 
\

# head는 df의 메서드.
df.head()

# 정수 연산 다시 생각하기
x = 1

# 클래스(class)는 범주, 인스턴스(instance)는 범주에 속한 사례. 인스턴스를 다른 말로 객체(object)라고 부름: “df 객체는 DataFrame 클래스의 인스턴스”

```

더하기를 객체지향방식으로 표현하면 1에 더하기를 시키는데 2라는 인자를 넘긴다고 보면된다.

1 add (2) 

메세지를 보낸다 = 메서드를 호출한다. 

누군가가 메세지를 받는 객체가 되어야한다.  메서드를 호출했을 때 메세지를 받는 사람이 리시버가 된다. 메서드는 어떤 리시버에 속해있는 것이다. 클래스는 개념이고 여기에 인스턴스를 만들어야 실체가 생긴다. 

인스턴스에 메세지를 보내는 것이다. 메세지는 인스턴스에만 보낸다. 밴딩머신에 클래스 이름을 괄호를 열고 닫으면 새로운 인스턴스(자판기!)가 생긴다. 

모든 메서드는 m에 대해서 self라고 한다. m과 같다. 

```
class VendingMachine: # 이렇게 하면 VendingMachine이라는 개념이 생기는 것이다. 
    def __init__(self): # __(언더바언더바)함수는 엄청난 약속임. 
        self. change = 0
         
    def run() : # run이란 method가 있다는 것이다. 
        pass # method가 된다. 벤딩머신에 인스턴스를 
        # 만들어야한다. 
        
실체는 VendingMachine() : 이때생기고 생기자마자 Class 가 호출된다. 
인스턴스안에는 change라는 변수가 생기고 run이라는 매서드(함수)가 생긴다. -- 유일한 호출체계. 변수는 각각의 벤딩머신 인스턴스마다 생김.
        

```

