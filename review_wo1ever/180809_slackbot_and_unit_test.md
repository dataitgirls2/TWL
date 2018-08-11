# 180809

## 오전수업 테스트주도개발 (애란쌤)

#### Stepwise refinement

- 이 닦기 task
  - 칫솔을 찾는다.
  - 치약을 찾는다.
  - 치약을 짠다.
    - 치약 뚜껑을 연다.
      - 엄지와 검지로 뚜껑을 잡는다.
      - 손가락을 시계반대방향으로 돌린다.
      - 뚜껑이 열릴 때까지 반복한다.
    - 짠다.
    - 치약 뚜껑을 닫는다.
  - 이를 닦는다.
  - 헹군다.

위의 방식처럼 더 작고 간단한 부분 부분으로 세분화하여 업무를 정의하면 처음엔 어려워보일 지 몰랐던 일들이 간단해질 수 있음.

### 수업목표

##### 파이썬 프로그래밍에 익숙해지기 위한 수련

##### 자동화된 단위 테스트 만들기

##### 리팩토링(refactoring): 프로그램의 동작은 유지하면서 설계를 개선하기

##### 애자일 방법론 실천법: 테스트 주도 개발(test-driven development) 익히기



### 테스트 주도 개발

#### 자동화된 단위 테스트 만들기

우리가 만약 main.py를 수정한다면, 매 번 확인할 때마다 껐다 켜고 다시 실행시켜서 확인해 보아야 함.

만약 로직과 실제 봇을 실행하는 프로세스를 분리시킨다면 매 번 껏다켜지 않아도 로직을 확인해 볼 수 있을 것

dependency graph를 그려볼 수 있음.

`pipenv install pytest`: 부분 부분의 단위별 유닛테스트를 진행해주는 패키지를 설치함.

자동화된 테스트를 저장하는 파일(tests.py)을 또 만들어줌.

`pipenv run pytest tests.py`로 실행시켜 줌.

```python
def test_roll_a_die():
    expected = {"1", "2", "3", "4", "5", "6"}
    # actual = set()
    # for i in range(1000):
    #     actual.add(answer("주사위"))
    actual = {answer("주사위") for _ in range(1000)}
    # 집합(set)에 하나의 원소를 add, 1000번 했을 경우 하나씩은 무조건 있겠지?
    assert expected == actual


def test_do_nothing_for_unknown_patterns():
    actual = answer("웅앵웅")
    assert actual is None
```

코드를 짠 다음 test를 만든다? test를 짠 후 코드를 만든다?



파이썬에서 대문자로 쓰는 것들은 대부분 Class로 정의됨.



## 오후수업 상권분석

`mkdir` (make directory) 파일 하나 만드는것