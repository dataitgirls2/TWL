20180724

## 공부할 때

아래의 카테고리로 공부하는 것이 좋습니다.

그리고 cheetsheet을 인쇄하여 가지고 다니면서 공부합시다.





#### - 파이썬 문법 - 처음에만 힘든 것일 뿐 염려할 필요는 없습니다. 

#### - 라이브러리(넘파이, 판다스, html5lib, beautifulsoup) - 끊임없이 공부해야 합니다! / 새로운 것을 빨리 익히는 요령을 체득해야 합니다. /  

#### - 파이썬 속 미니언어들 (CSS, 정규표현식) - 한 번 배우면 어디서든 사용할 수 있어요! / 정규표현식 중요!! 



#### 알고리즘과 자료구조 - 이미 많은 알고리즘이 짜여 있습니다.

#### 통계/확률 - 모든 것의 기초. 정량적으로 이해할 수 있습니다. 예측이 가능하다.  



## A/B test (= RCT)

ex. 새 UI 디자인이 기존 UI 디자인에 비해 구매전환율의 향상에 효과적인가?

- UI를 교체하는 것이 아니라 새 UI와 기존 UI를 공존하게 하여 랜덤하게 사용자에 노출시켜 데이터를 수집하고 분석해야 한다.

 type1 error : 영향이 없는데 있는 것으로 판명하는 오류 - 화재경보기의 경우를 생각해보자. 

 type2 error : 영향이 있는데 없는 것으로 판명하는 오류





## 과제점검

- 보폭을 좁게하여 중간 단계를 확인한다.
- 다른 사람의 과제로부터 힌트를 얻고, 크레딧을 반드시.
- 실패한 코드도 의미있는 작업
- 매직넘버는 제외하자



# 정규표현식(regex)

- 특정한 규칙을 가진 문자열의 집합을 표현하는 데 사용하는 형식 언어 
- 정규 표현식의 각 문자는 [메타문자](https://ko.wikipedia.org/w/index.php?title=%EB%A9%94%ED%83%80%EB%AC%B8%EC%9E%90&action=edit&redlink=1)로 이해되거나 정규 문자('문자 그대로', 즉 '리터럴'의 의미로)로 이해된다. 
- 주로 **패턴**(pattern)으로 부르는 정규 표현식은 특정 목적을 위해 필요한 문자열 집합을 지정하기 위해 쓰이는 식
- 정규 표현식의 패턴은 대상 문자열과 일치시킨다. 이 패턴은 일련의 원자로 구성



정규표현식은?

입력한 텍스트의 하나하나를 읽어가며 후보를 추려낸다.

문 - 재 - 인



### 메타캐릭터

: 정규표현식에서 사용하는 기호를 메타 문자라고 한다. 메타 문자는 표현식 내부에서 특정한 의미를 갖는 문자를 말합니다.

^ = 문장의 시작

^문재인 : 문장의 첫 시작에 문재인이 나오는 것만 찾는다.

$ = 문장의 끝

문재인$ : 문장 끝에 오는 문재인만 찾는다.



만약, 문장 안에서 $가 나오는 것을 찾고 싶다면?

\\$ : $표시 그 자체를 의미한다.

\\$ 500 = $500 

\^ : ^표시 그 자체를 의미한다.



### 캐릭터 클래스

: 문자클래스 내부에 해당하는 문자열의 범위 중 한 문자만 선택한다는 의미, 문자클래스 내부에서는 메타문자를 사용할 수 없거나 다른 의미를 가진다.

[...] 괄호 안에 쓴 내용중 하나

[초중고] = 초 또는 중 또는 고



### 캐릭터 클래스 메타캐릭터

[a-zA-Z] = 알파벳 소문자 부터 대문자까지 하나

[중고]\[1-3] = 중1, 중2, 중3, 고1, 고2, 고3 



### 메타캐릭터 추가!

. = 아무거나 한 글자

\d = 숫자

\D = 숫자 아닌 것

\\s = 공백 한 글자 - 공백을 모두 찾아 지우고 싶을 때

\\S = 공백이 아닌 아무 글자 하나



### Alteration

(...|...|...) = bar로 구분된 것 들중 하나



### 양화사 (quantifier)

? : 0 또는 1개 반복

\* : 0 개 이상 반복

\+ : 1개 이상 반복

{숫자} : 정확히 '숫자'에 해당하는 개수 만큼



*연습하면서 패턴을 깰 수 있는 예시들을 찾아보자. (Should match VS Should not match)



### 찾아 바꾸기

​	re.sub(r'010-(\d\d\d\d)-(\d\d\d\d)', r"82-10-\1\2", '010-1234-')



### gmail 주소 찾기

​	\b\[a-z][\w\d]*@gmail\.com

![1532416794972](C:\Users\home\AppData\Local\Temp\1532416794972.png)

- greedy quantifier : 요소를 최대한 많이 찾으려고 한다.

- non-greedy quantifier : 요소를 최소한으로 찾으려고 하며, '?'를 추가하는 것으로 설정할 수 있다.

  .+?\\.



### ASCII code(American Standard Code for Information Interchange )

- 아스키는 7비트 인코딩으로, 33개의 출력 불가능한 제어 문자들과 공백을 비롯한 95개의 출력 가능한 문자들로 이루어진다.
- 출력 가능한 문자들은 52개의 영문 알파벳 대소문자와, 10개의 숫자, 32개의 특수 문자, 그리고 하나의 공백문자로 이루어진다. 
- 아스키 코드(ASCII Table)는 0번부터 127번까지만 사용한다. 





### 유니코드(Unicode) 

-  전 세계의 모든 문자를 컴퓨터에서 일관되게 표현하고 다룰 수 있도록 설계된 산업 표준
-  유니코드의 목적은 현존하는 문자 인코딩 방법들을 모두 유니코드로 교체하려는 것이다. 기존의 인코딩들은 그 규모나 범위 면에서 한정되어 있고, 다국어 환경에서는 서로 호환되지 않는 문제점이 있었음



### UTF-8

 유니코드를 위한 가변 길이  문자 인코딩 방식 중 하나 





## 정규표현식에 대한 이론

- regular expression
- 형식 언어 : 유한한 종류의 문자로 이루어진 유한한 길이의 문자열의 집합 
- Finite state automaton
- DNN(딥러닝), 인공신경망



