## Object-Oriented Programming

Class : 추상적인 정의. 상태와 연산을 정의

Instance : Class에 의해 정의된 개념들의 실제 사례들



참고 : Dot Notation

http://reeborg.ca/docs/oop_py_en/oop.html



## 자판기 만들기

* Test 반복 줄이기

```python
def test_10():
	m = VendingMachine()
    assert coin = '10원을 넣었습니다' == m.run("동전 10")
        
def test_100():
	m = VendingMachine()
	assert coin = '100원을 넣었습니다' == m.run("동전 100")
```

```python
def test_인식_하는_동전():
    m = VendingMachine()
    valid_coins = ["10", "50", "100", "500"]
    for coin in valid_coins:
        assert coin + "원을 넣었습니다" == m.run("동전 " + coin)
        # 동전 뒤에 스페이스 없으면 오류난다...주의!
```



* int, str구분하기

  * coin list에 있는 coin이 int라서 에러남. 

  ```python
  elif cmd == "동전":
              coin = str(params[0])
              coin_list = [10, 50, 100, 500]
              if coin in coin_list:
                  self._change += int(coin)
                  return coin + "원을 넣었습니다"
  ```

  * coin을 str으로 변환. 

  ```python
  elif cmd == "동전":
              coin = str(params[0])
              coin_list = ["10", "50", "100", "500"]
              if coin in coin_list:
                  self._change += int(coin)
                  return coin + "원을 넣었습니다"
  ```

  

* Test를 통해 중복 제거, 의도 드러내기



## Git Branch

```python
git checkout -b coin  # make new branch named 'coin' and move there
```



참고 : Command Line/Git Command

https://explainshell.com/



## Cartogram

일반 지도 vs 카토그램

일반 지도 : 데이터를 왜곡할 수 있다

카토그램 : 지형을 왜곡할 수 있다

http://slownews.kr/63722



지형을 왜곡하지 않고 스케일만 조정하기도 함.



**Multidimensional Data Visualization**

http://www.juiceanalytics.com/writing/better-know-visualization-small-multiples





## 데이터 분석의 목적 및 생각해봐야 할 점

데이터 분석 - 실행 가능한 인사이트 및 실행 후 성과 평가.

실행 '할 수 없는' 인사이트라면?

- 데이터 공유 - 기록을 남기고, 다른 사람들이 교육하는데 도움을 주기
- 이미 알려진 사실이나 정보를 쉽게 표현
- 좋은 지표 제시 - 지표에 따라서 인사이트가 많이 달라질 수 있다.
  - GA's conversion rate : visit-oriented
- 좋은 질문들, 가설들 찾아내기



성과 평가는 어떻게 할까?