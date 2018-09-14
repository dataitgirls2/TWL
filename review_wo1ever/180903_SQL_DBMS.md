





# 180903

## 오전 - SQL과 database, DBMS

#### 데이터베이스는?

#### DBMS언어

- 데이터 정의 언어(DDL: data definition language): Create, Drop, Alter
  - 데이터베이스라던지 테이블이나 컬럼이 어떤 데이터 타입인가, 등으로 지정해주는 것
- 데이터 조작 언어(DML: data manipulation language): Selectt, Insert, Delete, Update
- 데이터 제어 언어(DCL: data control language): Grant, Revoke, Commit, Rollback
  - 특정 사용자에게 권한을 부여하는 것, 어떤 사용자에게는 읽기 권한만, 어떤 사용자에게는 쓰기 권한을 줄 수 있음
  - Rollback: 돈만 빠져나가고 물건이 주문 안 된 상황 등에서 다시 뒤로 되돌아가야함

#### 테이블

#### SQL은?

#### 온라인으로 배우기

#### (https://www.w3schools.com/sql/default.asp): 에서 실습 예제

- `SELECT * FROM Customers;` Customers 테이블에서 * (all) 모두 가져오기

  보통 이런 쿼리는 아주 소수만 권한을 가지고 있음.

- `LIMIT 1` 컬럼 보고싶으면 1줄만 나타나게 됨

- `SELECT CustomerID, CustomerName, Address, City, PostalCode
  from Customers
  order by CustomerID asc
  limit 5`

- `inner join`보통 양쪽에 다 같은게 있을 때

- `group by column_name`유니크한 애들만 뽑고 싶을 때, '어떤 고객이 주문 고객인가?' 등



#### SQL 실습

##### 1. 구매 테이블에서 구매 고객의 유니크한 이름만을 구해 오기

~~~sql
select distinct Customers.CustomerName
from Orders
join Customers on Orders.CustomerID = Customers.CustomerID
~~~

##### 2. 구매 테이블에서 가장 많이 구매한 고객의 이름을 구해 오기

내 답안

~~~sql
SELECT count(Orders.CustomerID)
FROM Orders
join [Customers] on Orders.CustomerID = Customers.CustomerID
group by Customers.CustomerID
order by count(orders.CustomerID) desc
limit 9
~~~

배로쌤 답안

~~~sql
select c.CustomerName, Count(*) as cnt
from Orders as o inner join Customers as c
	on o.CustomerID = c.CustomerID
group by o.CustomerID
having count(*) > 5
~~~

##### 3. 구매 테이블에서 가장 많이 판매된 5개의 상품의 이름과 횟수를 구해보세요

[OrderDetails]

| OrderDetailID | OrderID | ProductID | Quantity |
| ------------- | ------- | --------- | -------- |
| 1             | 10248   | 11        | 12       |

[Products]

| ProductID | ProductName | SupplierID | CategoryID | Unit               | Price |
| --------- | ----------- | ---------- | ---------- | ------------------ | ----- |
| 1         | Chais       | 1          | 1          | 10 boxes x 20 bags | 18    |

내 답안

~~~SQL
SELECT p.ProductName, count(od.orderID) as cnt, sum(od.quantity)
FROM Products as p
	inner join OrderDetails as od on p.ProductID = od.ProductID
group by p.ProductID
order by cnt desc
~~~

배로쌤 답안

~~~sql
SELECT p.ProductName, Count(d.ProductID) AS '판매횟수', SUM(Quantity) AS '판매수량'
FROM Orders o 
	INNER JOIN OrderDetails d ON o.OrderID = d.OrderID 
	INNER JOIN Products p ON p.ProductID = d.ProductID 
GROUP BY d.ProductName
ORDER BY SUM(Quantity) DESC
LIMIT 5
~~~

- count를 하게 되면 전체 행의 갯수를 세어줌.
- 상품 이름, 판매 횟수, 판매 수량을 표시함.



##### 4. 배송기사(Shipper)가 배송한 주문 건과 상품 갯수를 구해보세요

[shippers]

| ShipperID | ShipperName    | Phone          |
| --------- | -------------- | -------------- |
| 1         | Speedy Express | (503) 555-9831 |

[orderdetails]

| OrderDetailID | OrderID | ProductID | Quantity |
| ------------- | ------- | --------- | -------- |
| 1             | 10248   | 11        | 12       |

[orders]

| OrderID | CustomerID | EmployeeID | OrderDate  | ShipperID |
| ------- | ---------- | ---------- | ---------- | --------- |
| 10248   | 90         | 5          | 1996-07-04 | 3         |

내 답안(못품 ㅠㅠ)

~~~sql
SELECT s.shippername, count(o.shipperid), sum(od.quantity)
from orders as o
join orderdetails as od
	on od.orderid = o.orderid
join shippers as s
	on s.shipperid = o.shipperid
group by o.shipperid, s.shippername
~~~

~~~sql
SELECT s.shippername, count(distinct o.orderid), sum(od.quantity)
from orders as o
	join orderdetails as od on od.orderid = o.orderid
	join shippers as s on s.shipperid = o.shipperid
group by s.shippername
~~~

배로쌤 답안

~~~sql
SELECT ShipperName, COUNT(DISTINCT o.OrderID),  SUM(Quantity) AS '상품갯수'
FROM Orders o 
	INNER JOIN OrderDetails d ON o.OrderID = d.OrderID 
	INNER JOIN Products p ON p.ProductID = d.ProductID 
	INNER JOIN Shippers s ON s.ShipperID = o.ShipperID 
GROUP BY s.ShipperName 
~~~



##### 5. 가장 많이 판매 된 상품의 이름을 구해보세요

배로쌤 답안

~~~sql
SELECT ProductName, MAX(Q)
FROM(
	SELECT p.ProductName, SUM(Quantity) AS Q
	FROM OrderDetails AS d
 	   INNER JOIN Products AS p 
		ON d.ProductID = p.ProductID
	GROUP BY d.ProductID 
) 

SELECT p.ProductName, SUM(Quantity) AS Q
FROM OrderDetails AS d
	INNER JOIN Products AS p 
		ON d.ProductID = p.ProductID
GROUP BY d.ProductID 
ORDER BY Q DESC
LIMIT 1
~~~

#### DATABASE - SQL lite

- csv불러온 다음, 첫 행을 컬럼명으로 사용, 가져온 테이블 우클릭해서 각 column type 수정: TEXT, INTEGER, ... 등
- `pk` : primary key로 설정하기.





## 오후 - SW멘토링 캠프 (5회차)

### SW welcoms

- 과기정통부
- 한국정보화진흥원

### 14:30 ~ 17:00

### 민윤정멘토님(AI: Artificial Intelligence)

한 2년 새 갑자기 많이 나왔다. 생각보다 빨리 딥러닝, 인공지능 기술이 활용되고 있다. AI가 이길 수 있는 분야와 그렇지 않은 분야를 미리 알고 도전하자.

#### 인간이 하기 어려운 일들

- Doing the same things over and over again
- Processing and evaluating patterns in big data
- Repetitive tasks and solving problems that involve <u>crunching large, well-organized data sets</u>

#### 사람이 기계보다 잘 할 수 있는 분야

- Understand context or nuance
  - 문맥이나 뉘앙스를 잘 캐치하는 일
  - 하지만 최근 Google에서 duplex(?)를 발표. broken Eng를 읽어내며 식당 예약 프로세스를 성공
- Empathy & Sympathy
  - 동정심, 공감능력 등 상대방과의 감정을 공유하는 일 (reaction)
- Dealing with ambiguity and gray areas
  - 모호하거나 정답이 없는 일들

#### 사용할 수 있는 여러가지 분야

딥러닝, 머신러닝을 통하여 정말 여러가지 분야에 사용할 수 있음.

- AI shoul help people work
  - 사람의 일을 도와주어야 함
- faster, more efficiently and more safely
  - 더 빠르고, 효율적이고, 더 안전해야 하겠다.

#### 미래의 사무공간에서 어떤 기술이 쓰일까? - Enterprise s/w AI

많은 기업들이 IT 기술을 이용하고 있음

- AI for CRM: 고객관리
- AI for BI: 비즈니스에 디시젼메이킹을 도와주는 도구
- AI & ML platform: eg) Leonardo
- Document Management
- 음성인식 AI device
- Recruitment
  - 봇으로 개인정보나 간단한 질문들을 함.
  - 자연어를 이해하고 그에 맞춰 대응
  - 어떤 사람이 우리 일에 가장 적합할까를 예측하기도 함.

- Task Scheduling
  - 방문기사님들 등 일을 효과적으로 계획해 줌.
  - 동선을 미리 분석해서 가장 최적으로 방문할 수 있게 스케줄링,

#### 특성

- Data driven application
- Analytics Drive Innovation; Predictive Analysis
- Intelligent Machines and Pattern Recognition
- Natural Ways
  - Google은 모든 프로그램에 이제 AI를 넣고 있다. 특히 번역 기능에서 그 성과를 발휘하는 중.
  - [endpoint](http://securitycream.tistory.com/7) 단위로(?) 번역을 분석

- (eg) 슬랙에 코노(Kono)봇을 넣을 수 있음. 여러가지 일정 관리 비서 AI
  - Event Type Classification 기술을 사용
  - ML Technology - ML Engine for Context Prediction
  - LSTM: 머신러닝에서 사용되는 어떤 연산의 종류
  - Kono Sync Connector for Enterprise On-prems
  - 3초 이내 답변하기 위한 기술이 필요

Google의 tensorflow를 설치하고 데이터를 넣는 것은 누구나 할 수 있음. 이것에 파라미터들을 튜닝해주는 과정이 필요함.

#### 요즘에 지고 있는 산업군

- 모바일앱'만'을 다루는 업종

- bot: (Ro)bot 에서 나온 말
- 유저들이 새로운 앱을 안깔고 있음. 매일 즐겨쓰는 앱의 갯수가 점점 줄어들고 있는 추세
- 이 시점에서 새 앱을 구축한다는 것은 좀 ..
- OS 어플리케이션이 업뎃 될 때 마다 새롭게 패치해 줘야 함.
- backend로 통신하는 AI들이 늘고 있음.
- 쾌적하고 빠르긴 하지만 줄어들 것. 필수적으로 살아남는 앱은 봇과 연동되는 서비스들을 만들어 낼 것.
  - 카카오 미니, 네이버의 라인스피커 등도 API등이 오픈되고 있어 밖에서 연동되어 쓰기가 좋아질 것.

#### AI 분야 유망 직종

- **프론트앤드 개발자**: 원래 많이 필요했음.
- **데이터 사이언티스트**: 컴퓨터 사이언티스트를 전공한 사람들, 머신러닝 알고리즘을 이용가능한, 데이터 학습과 튜닝법을 알고 있는 사람들이 점점 더 경쟁력 있어 질 것. 학위보다는 경험과 데이터로부터 얻은 인사이트가 중요해 질 것. 여기에서 코딩은 필수! 예전에는 big data를 모아서 통계확률 적인 접근법을 사용했음. 하지만 머신러닝에서는 goal에 맞춰 튜닝을 한다던가, 통계 기술과 접목한 여러가지 테크닉들을 씀. 이런 것을 할 때 데이터를 적절히 바라볼 수 있고, 코딩을 할 수 있고, 컨트롤 할 수 있고, 여러 머신러닝 튜닝을 할 줄 아는 그런 사람들이 수요가 높아짐.
- **보안과 백엔드 개발자들**: ICT분야, 특히 보안이슈가 굉장히 중요하고 필요한 스킬이 될 듯. 백엔드가 과거에는 DB에 넣고 빼는 그런것들이 중요했지만, 지금은 점점 DB들이 좋아지고 있고, DB modeling보다는 구현방법과 경험을 알고 있는 사람들의 수요가 높아질 것

[slide share](https://www.slideshare.net/)

[코세라](https://www.coursera.org/)

#### 데이터 사이언티스트로의 커리어?

시각화, 코딩, 코딩인터뷰, 캐글 수상자

- 캐글 컴피티션에서 이겨 본, 깃헙에 올라와있는 "코딩경험"
- 어떤 연구의 어떤 데이터를 다루어 봤는지, 논문만 쓸 수 있는 사람인지 혹은 그것으로 '진짜'분석을 할 수 있는 사람인지가 중요
- 데이터 분석 방법에도 여러가지 방법이 있는데,
  - 통계적 방법으로 분석
  - 머신러닝으로 분석
  - 딥러닝으로 분석(요즘 트렌드)
  - 하는 것에 대해 초점을 맞추고 그에 대해 잘 할 것 같은 사람을 뽑음
- 보통 '개발자'인턴은 힘들 것 같다.
- 깃헙에의 본인 코딩을 직접 짰는지, 그 코딩을 보고 보통 뽑음.