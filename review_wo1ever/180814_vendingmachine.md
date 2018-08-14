# 180814

## 오전/오후 - 프로그래밍 연습 (애란쌤)

### 프로젝트를 시작하는 방법들 10m

#### 프로젝트 시작하는 방법 #1 - 다른 사람의 소스코드를 복제(clone)해서 시작

1. github에서 “fork”하여 내 계정의 repository로 가져온다.
2. 내 계정의 repository를 “clone”하여 내 컴퓨터로 가져온다.
3. 개발 시작

#### 프로젝트 시작하는 방법 #2 - github에 repository 만들고 시작

1. github에서 “Create Repository”를 해서 빈 repository를 만든다.
2. “clone”하여 내 컴퓨터로 가져온다.
3. 개발 시작

#### 프로젝트 시작하는 방법 #3 - 내 컴퓨터에서 시작

1. 내 컴퓨터에서 빈 폴더를 만든다.
2. “git init” 명령을 입력하여 일반 폴더를 git repository로 변환한다.
3. 개발 시작
4. github에서 “Create Repository”를 해서 빈 repository를 만든다.
5. 내 컴퓨터에서 git add remote 명령으로 origin을 등록하고 push 한다.
6. 계속 개발



### #3 으로 시작해보기

```bash
wolever@wolever-PC MINGW64 /d/projects/vendingmachine (master)
$ touch test_vm.py
```

- 해당 경로에 test_vm.py를 생성함
- `echo Hello > test.txt` 를 만들어도 비슷한 기능을 하게 될 수 있음.
  - 이건 그냥 echo의 기능을 수행하다 보니 얻어걸리는 기능.
- `touch test_vm.py`는 빈 파일을 만드는 데에 유용하게 활용됨.

#### 파이썬 가상환경 만들기(Anaconda Prompt)

- `cd <프로젝트 폴더 경로>`로 디렉토리를 변경해 줌.
- `pipenv --python 3.6` 으로 가상 환경을 설정
- `pip install pytest` : 테스트 주도개발을 위한 라이브러리를 설치해줌.
- `pipenv run pytest` : test_~ 로 시작하는 파일명들을 모두 test해 줌.



```bash
wolever@wolever-PC MINGW64 /d/projects/vendingmachine (master)
$ ll
total 6
-rw-r--r-- 1 wolever 197121  151 8월  14 12:04 Pipfile
-rw-r--r-- 1 wolever 197121 3249 8월  14 12:05 Pipfile.lock
-rw-r--r-- 1 wolever 197121  118 8월  14 12:07 test_vm.py
-rw-r--r-- 1 wolever 197121    0 8월  14 12:10 vm.py
```

보통 test_vm 이 있다면 vm도 있음.(웬만하면 파일은 짝으로 존재)



#### TDD(테스트 주도 개발: Test-driven development) 시연

1. 테스트를 추가한다.
2. 테스트를 실행하여 테스트 실패를 확인한다.
3. 코드를 고쳐서 최대한 빨리 테스트를 성공시킨다.
4. 코드를 깔끔하게 다듬는다. 깔끔한 코드(clean code)란?
   - 의도가 잘 드러난다
   - 중복이 없다
5. 테스트를 다시 실행하여 여전히 성공하는지 확인한다.
6. GOTO 1
7. ...

##### 피보나치 수열 fibo() TDD!

- TDD를 얼마나 촘촘하게 조정하느냐의 문제
- 만약 피보나치(1000)을 찾고 싶다면 과연 함수가 몇 번이나 호출될까
  - 기하급수적으로 호출회수가 늘어남(?)
- TDD를 이용한다고해서 테스트를 안해도 된다는 것은 아님.
  - fibo()에 text를 입력한다면? 음수를 입력한다면? 소수점을 입력한다면?



7. 테스트를 추가한다.
8. 테스트를 실행하여 테스트 실패를 확인한다.
9. 코드를 고쳐서 최대한 빨리 테스트를 성공시킨다.
10. 코드를 깔끔하게 다듬는다. 깔끔한 코드(clean code)란?
    1. 의도가 잘 드러난다
    2. 중복이 없다
    3. DTSTTCPW → “Do the simplest thing that could possibly work.
    4. ”YAGNI → “”You ain’t gonna need it.”
11. 테스트를 다시 실행하여 여전히 성공하는지 확인한다.
12. GOTO 1

#### 자판기 요구사항 세트

```bash
wolever@wolever-PC MINGW64 /d/projects/vendingmachine (master)
$ echo .pytest_cache/ > .gitignore

wolever@wolever-PC MINGW64 /d/projects/vendingmachine (master)
$ cat .gitignore
.pytest_cache/

wolever@wolever-PC MINGW64 /d/projects/vendingmachine (master)
$ ls -als
total 19
4 drwxr-xr-x 1 wolever 197121    0 8월  14 14:10 ./
4 drwxr-xr-x 1 wolever 197121    0 8월  14 11:51 ../
4 drwxr-xr-x 1 wolever 197121    0 8월  14 14:13 .git/
1 -rw-r--r-- 1 wolever 197121   15 8월  14 14:10 .gitignore
0 drwxr-xr-x 1 wolever 197121    0 8월  14 12:05 .pytest_cache/
1 -rw-r--r-- 1 wolever 197121  151 8월  14 12:04 Pipfile
4 -rw-r--r-- 1 wolever 197121 3249 8월  14 12:05 Pipfile.lock
1 -rw-r--r-- 1 wolever 197121  118 8월  14 12:07 test_vm.py
0 -rw-r--r-- 1 wolever 197121    0 8월  14 12:10 vm.py
```

- `echo .pytest_cache/ > .gitignore`: .gitignore가 없다면 새로 생성한 후 pytest를 넣음.
  - 하지만 만약에 저 폴더 안에 뭐가 있는 상태이면 덮어써버림.(위험!)
- `echo .pytest_cache/ >> .gitignore` 이렇게 해주면 append됨.
- `rm -rf <파일/폴더명>`

#### 자판기 - 따라하기

> - 오늘의 내가 만든 코드는 내일의 나, 또 다른 개발자들이 모두 보는 코딩임.
>   - 변수 이름이나 함수 이름 등 신중하게 짓는 것이 좋음.
> - 에러가 난다면 무슨 에러가 났는지 주의깊게 읽어보기
> - 좋은 테스트란, 실행 순서와 상관없이 독립적으로 격리(test isolation) 되어야 함.
>   - 각 test의 순서를 매 실행마다 바꿔주기도 함.

- `git commit -am "커밋 노트"`: tracked인 파일을 수정한 경우, unstaged인 파일을 add하고 커밋까지 한번에 하기 위해 `-a`를 적어주고, `-a'm'`m을 추가해주어서 "커밋노트"까지 한번에 작성.
  - `git add .` > `git commit -m "~"` 를 한번에 실행해 줌.

#### 클래스 도입하기

클래스, 객체, 인스턴스?

- x = 1 : 정수 class의 instance인 객체가 생성되었다.

- df = pd.DataFrame( .... ) : DF class의 instance인 object가 생긴 후 df에 담김.

- df = pd.read_csv(...) : read_csv라는 함수를 호출한 것. return pd. DataFrame. 이런식으로 리턴될 것.

- df.head() : 데이터프레임 객체에 어떤 함수를 호출할 수 있는데, 이것은 매서드라고 함. 위의 pd는 모듈이어서 함수 호출이지만, df는 객체이기 떄문에 매서드라고 부름.

- x = 1

  y = x + 2

  z = x.\__add\_\_(2) : 사실 이런 함수가 실행되는 것. 정수 객체에는 \_\_add__라는 매서드가 담겨있음. (y와 z의 결과는 같음)

| 인스턴스의 리터럴 | 클래스       | 메서드                           |
| ----------------- | ------------ | -------------------------------- |
| 1                 | int          | \__add\_\_(), \_\_sub\_\_(), ... |
| 1.5               | float        | \__add\_\_(), is_integer(), ...  |
| “Hey”             | str          | lower(), strip(), ...            |
| [1, 2]            | list         | append(), sort(), ...            |
| (리터럴 없음)     | pd.DataFrame | head(), melt(), pivot(), ...     |

- 메서드는 객체에 귀속되는 것.

- 클래스 자체는 사실 아무것도 아닌 것. 클래스를 실제로 사용하려면 안의 인스턴스를 만들어주어야 함.

  - 메세지는 인스턴스에게 보내게 됨.

- 모든 메서드는 첫 번째 인자로 self라는 인자를 받아야 한다는 규칙.

  <test_vm.py>

  ```python
  def test_initial_change_should_be_zero():
      m = VendingMachine()
      assert "잔액은 0원입니다." == m.run("잔액")
  ```

  m 이 self로 들어오게 됨.

  <vm.py>

  ```python
  class VendingMachine:
      def __init__(self):
          self.change = 0
          
      def run(self):
          pass
  ```

#### 깃헙에 올리기

1. Repository 생성

2. 리모트 별명 등록:

   `git remote add origin git@github.com:aeranghang/test.git`

3. 푸시 + 현재 브랜치(local/master)가 origin/master를 트래킹하도록 등록:

   `git push -u origin master`

4. 다음부터는 그냥 `git push`