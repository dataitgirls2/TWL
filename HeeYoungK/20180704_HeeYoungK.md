# Python 자습하기

- prompt : \>>>와 ...

- 인터프리터 언어 : 실행 파일을 만들지 않아도 소스 파일을 직접 실행 할 수 있다.

  ​			   컴파일 언어보다 짧은 개발 / 디버깅 주기를 가짐

- 주석 : #로 시작

- 마지막에 인쇄된 표현식은 변수 _ 에 대입

  - \>>> tax = 12.5 / 100

    \>>> price = 100.50

    \>>> price * tax

    12.5625

    \>>> price + _

    113.0625

    \>>> round(_, 2)

    113.06

- int, float, decimal, fraction 등의 숫자 지원. 복소수 지원. 허수부 j, J접미사 사용(3+5j)

- \', \"의 사용과 \

  ```
  >>> 'spam eggs'  # single quotes
  'spam eggs'
  >>> 'doesn\'t'  # use \' to escape the single quote...
  "doesn't"
  >>> "doesn't"  # ...or use double quotes instead
  "doesn't"
  >>> '"Yes," they said.'
  '"Yes," they said.'
  >>> "\"Yes,\" they said."
  '"Yes," they said.'
  >>> '"Isn\'t," they said.'
  '"Isn\'t," they said.'
  ```

- ```
  >>> '"Isn\'t," they said.'
  '"Isn\'t," they said.'
  >>> print('"Isn\'t," they said.')
  "Isn't," they said.
  >>> s = 'First line.\nSecond line.'  # \n means newline
  >>> s  # without print(), \n is included in the output
  'First line.\nSecond line.'
  >>> print(s)  # with print(), \n produces a new line
  First line.
  Second line.
  ```

  ```
  >>> print('C:\some\name')  # here \n means newline!
  C:\some
  ame
  >>> print(r'C:\some\name')  # note the r before the quote
  C:\some\name
  ```

- \'python' 문자열 순서

  - 0번째~5번째: p, y, t, h, o, n
  - -1번째~-6번째: n, o, h, t, y, p

- ```
  >>> word[:2]   # character from the beginning to position 2 (excluded)
  'Py'
  >>> word[4:]   # characters from position 4 (included) to the end
  'on'
  >>> word[-2:]  # characters from the second-last (included) to the end
  'on'
  ```

- 내장함수 len : 문자열, 리스트에 적용

  ```
  >>> s = 'supercalifragilisticexpialidocious'
  >>> len(s)
  34
  ```

- Append (리스트의 끝에 새 항목 추가)

  ```
  >>> cubes.append(216)  # add the cube of 6
  >>> cubes.append(7 ** 3)  # and the cube of 7
  >>> cubes
  [1, 8, 27, 64, 125, 216, 343]
  ```

- 리스트

  - `list.``append`(*x*)

    리스트의 끝에 항목을 더합니다. `a[len(a):] = [x]` 와 동등합니다.

  - `list.``extend`(*iterable*)

    리스트의 끝에 이터러블의 모든 항목을 덧붙여서 확장합니다. `a[len(a):] = iterable` 와 동등합니다.

  - `list.``insert`(*i*, *x*)

    주어진 위치에 항목을 삽입합니다. 첫 번째 인자는 삽입되는 요소가 갖게 될 인덱스입니다. 그래서 `a.insert(0,x)` 는 리스트의 처음에 삽입하고, `a.insert(len(a), x)` 는 `a.append(x)` 와 동등합니다.

  - `list.``remove`(*x*)

    리스트에서 값이 *x* 와 같은 첫 번째 항목을 삭제합니다. 그런 항목이 없으면 에러입니다.

  - `list.``pop`([*i*])

    리스트에서 주어진 위치에 있는 항목을 삭제하고, 그 항목을 돌려줍니다. 인덱스를 지정하지 않으면, `a.pop()` 은 리스트의 마지막 항목을 삭제하고 돌려줍니다. (메서드 시그니처에서 *i* 를 둘러싼 꺾쇠괄호는 매개변수가 선택적임을 나타냅니다. 그 위치에 꺾쇠괄호를 입력해야 한다는 뜻이 아닙니다. 이 표기법은 파이썬 라이브러리 레퍼런스에서 지주 등장합니다.)

  - `list.``clear`()

    리스트의 모든 항목을 삭제합니다. `del a[:]` 와 동등합니다.

  - `list.``index`(*x*[, *start*[, *end*]])

    리스트에 있는 항목 중 값이 *x* 와 같은 첫 번째 것의 0부터 시작하는 인덱스를 돌려줍니다. 그런 항목이 없으면 [`ValueError`](https://docs.python.org/ko/3/library/exceptions.html#ValueError) 를 일으킵니다.선택적인 인자 *start* 와 *end* 는 슬라이스 표기법처럼 해석되고, 검색을 리스트의 특별한 서브 시퀀스로 제한하는 데 사용됩니다. 돌려주는 인덱스는 *start* 인자가 아니라 전체 시퀀스의 시작을 기준으로 합니다.

  - `list.``count`(*x*)

    리스트에서 *x* 가 등장하는 횟수를 돌려줍니다.

  - `list.``sort`(*key=None*, *reverse=False*)

    리스트의 항목들을 제자리에서 정렬합니다 (인자들은 정렬 커스터마이제이션에 사용될 수 있습니다. 설명은 [`sorted()`](https://docs.python.org/ko/3/library/functions.html#sorted) 를 보세요).

  - `list.``reverse`()

    리스트의 요소들을 제자리에서 뒤집습니다.

  - `list.``copy`()

    리스트의 얕은 사본을 돌려줍니다. `a[:]` 와 동등합니다.

```
>>> fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
>>> fruits.count('apple')
2
>>> fruits.count('tangerine')
0
>>> fruits.index('banana')
3
>>> fruits.index('banana', 4)  # Find next banana starting a position 4
6
>>> fruits.reverse()
>>> fruits
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']
>>> fruits.append('grape')
>>> fruits
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']
>>> fruits.sort()
>>> fruits
['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']
>>> fruits.pop()
'pear'
```
