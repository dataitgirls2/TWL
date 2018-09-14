# 180906

## 오전 - GA익히기

### google analysis

#### Google Analytics 소개

- 세상에서 가장 널리 쓰임 + 세상에서 가장 방치됨
- 데이터 분석, 빅데이터 등이 유행하면서 갑자기 더 중요해짐

이상적인 세상에서는?

- Build --> Measure --> Learn 싸이클 중 Measure, Learn단계의 핵심 도구 중 하나
- 마케팅 퍼포먼스 개선, 웹 사이트 UX 개선, 상품 가격 최적화, 컨텐츠 최적화 등
- 한 회사에서 채용공고를 통해 지원한 사람이 최종면접까지 합격하는가? 와 같은 프로젝트도 했었음. > 3년 뒤의 퍼포먼스가 어떤가? 까지 확장되었어도 재밌었을 듯

#### 여담 - JD?

블리자드나 우아한 형제들 같은 경우 JD가 친절하고, CTO가 열심히 기술 블로그를 운영. 회사가 이상하다 싶으면 피하세요.

#### GA가 수집하는 데이터

GA 데이터 수집 과정:

1. GA계정 생성
2. 추적 코드(자바스크립트 코드 조각) 발급받기
3. 추적 코드를내 웹 사이트에 심기
4. 사용자가 웹 사이트에 접속하면 사용자 브라우저로 추적 코드가 함께 전송됨
5. 사용자 브라우저에서 추적코드가 실행되어 데이터를 수집
6. 수집한 데이터를 GA수집 서버로 전송
7. 사용자가 다른 링크를 클릭
8. GOTO 4

##### Network > collect ~ > Headers > Query String Parameters

- `Query String Parameter`: 어떤 파라미터들이 어떤 값을 주는 지 알려줌

- `ul`: ko-kr 코리아

- `sr`: 해상도

- `cid`: 내 브라우저의 고유 ID > 쿠키만 삭제해도 리셋되는 값. 해당 사용자를 계속 추적할 수 있음.



#### 지표 만들기 연습

| Time                | IP           | CID  | URL             | Referrer   |
| ------------------- | ------------ | ---- | --------------- | ---------- |
| 2018-01-01 03:50:15 | 210.10.313.1 | 1    | /index.html     | naver.com  |
| 2018-01-01 03:50:30 | 210.10.313.1 | 1    | /list.html      |            |
| 2018-01-01 03:50:30 | 53.101.5.10  | 2    | /product_a.html | google.com |
| 2018-01-01 03:50:35 | 210.10.313.1 | 1    | /index.html     |            |
| 2018-01-01 15:00:05 | 123.12.32.43 | 1    | /index.html     |            |

- 방문객 수: 전체 row 수
- 인기있는 페이지: URL의 groupby sum
- 접속 지역: IP
- 개개인의 접속 패턴: Time + CID 
- 접속자의 수: unique CID

- 웹사이트 내 주요 동선: CID + URL
  - 다시 홈페이지로 돌아간다? 헤멘다, 혹은 원하는 정보를 못찾았다?
  - 어떤 사람이 어느 페이지에 많이 머물렀나?: CID + URL + TIME

- 주요 이탈 페이지
- 주요 유입 웹사이트: Referrer
  - Referrer이 없는 경우: 북마크를 통해, 주소를 직접 입력해서, 앱으로 들어온 경우
- 체류 시간(방문 시간, 세션 길이): Time + CID

**TIME에 따라 하나의 세션으로 만들어줄 수 있음.**

보통 한 세션은 20분~30분으로 취급하지만 동영상 같은 경우에 세션을 하나로 유지해야 한다면 조금 다른 방법을 써줌.

- 몇 시간 간격으로 들어오는 지,
- 얼마나 오래 머무르는 지,
- 각 페이지에 대한 모든 사람들의 체류시간, 등 많은 정보들을 알 수 있음.



#### 박진영님의 GA 사용기

- SEO(Search Engine Optimize)
  - Content Marketing
    - 기업들이 유저들을 유입시키기 위해 블로그를 정성들여 작성하는 경우가 많음.
    - Listicles: 사람들에게 쉽게 이해시키기 위해 리스트 형식으로 나열
    - Keyword ~
  - Technical Audit

- 돈 안들이고 마케팅하는 좋은 방법: Reddit, Facebook, Stack Exchange, Stack over flow 등을 활용해서 최대한 많은 커뮤니티 마케터로서 기여를 많이 하며 인지도를 알림.
  - 브랜딩이나, 프로덕트에 대한 친근감을 높일 수 있음.

- Display: 전면광고
  - (eg) 조선일보 사이트에서도 ad가 붙은 글과 아닌 글이 있음. 자체 콘텐츠 아니면 광고

- email tracking
  - 어떤 뉴스레터 보냈는데 봤어? 안봤으면 한번 봐바 등으로 마케팅
  - GA를 이용할 수 있음.
- Referrer를 통한 tracking
  - 외부에서 유입되는 모든 사이트들을 트래킹하여 어느 사이트에서의 유입률이 가장 많은 지 알 수 있음.
- URL builder
- Keyword plan



#### Pandas 10분 완성 살펴보기...

- 획득 > 전체트래픽 > 채널: 어느 경로로 유입되는 지 알 수 있음.

- 모바일 VS desktop: 잠재고객 > 모바일 > 기기/개요
  - 그런데 모바일에서 보는 '평균세션시간'과 데스크탑이 3배 이상 차이가 난다. > 모바일에서 무슨 문제가 있을 확률이 높음.
  - 이탈률(bounce rate)가 높으면 당연히 체류시간이 낮을 수 밖에 없음
- Google webmaster와 연동해 놓으면 검색어 키워드와 그 사용량을 알 수 있음.
- 잠재고객 > 인구통계/관심분야: google은 여러가지 사이트를 통해서 이용자들의 나이를 유추함. 관심사 등도 관련 검색이나 클릭 등을 통해 유추함.
- 스크롤 속도나 한 스크롤에서도 머무는 시간을 알아볼 수 있을 듯



결과가 나왔을 때 그 결과들을 어떻게 발전시킬 지까지도 미리 생각해보고 실험을 진행하기



---

## 오후 - SQL #2 배로쌤

#### instakart 실습 (kaggle경진대회의 데이터 셋)

sample_submissions.csv 데이터셋은 사용하지 않을 것

- `aisle`: 세부 상품군

##### 1. product_name이 Banana인 데이터의 aisles명과 department명을 찾아 보세요.

```sql
select product_name, a.aisle, d.department
from products as p
	inner join departments as d
		on p.department_id = d.department_id
	inner join aisles as a
		on a.aisle_id = p.aisle_id
where p.product_name = 'Banana'
```

- 외래 키로 되어있는 애들은 어떤 테이블에서 가져오는 지 지정해 주어야 함.

##### 2. Banana가 들어가는 상품 명과 department명을 Like구문을 활용하여 모두 찾아 보세요.

~~~sql
select department, p.product_name
from products as p
	left join departments as d
		on p.department_id = d.department_id
where p.product_name like "%Banana%"
	and department = 'snacks'
~~~

- join할 때에도 데이터가 적은 쪽을 앞쪽에 적어주면 처리 속도가 조금 빨라짐.

##### 3. order 테이블의 eval_set이 test인 것을 기준으로 요일별 주문수량을 구해 보세요. (참고로 0부터 시작하며, 0은 토요일 입니다.)

~~~sql
select order_dow, count(*)
from orders
where eval_set = 'test'
group by order_dow
order by count(*) desc
~~~

##### 4. order 테이블의 eval_set이 test인 것을 기준으로 시간대별 주문수량을 구하고 주문량이 많은 순으로 정렬해 보세요.

~~~sql
select order_hour_of_day, count(*)
from orders
where eval_set = 'test'
group by order_hour_of_day
order by count(*) desc
~~~

##### 5. order_products__train 테이블을 기준으로 재주문(reorder)이 가장 많은 제품명 상위 10개와 재주문 수를 구해 보세요.

~~~sql
select p.product_name, sum(reordered)
from order_products__train as opt
	join products as p
		on p.product_id = opt.product_id
group by p.product_name
order by sum(reordered) desc
limit 10
--재주문 여부를 sum이 아닌 count로 세고 싶으면 where구문에 reordered = 1을 넣어주어야 함.
~~~

##### 6. 주말(토, 일)에 가장 주문량이 가장 많은 시간대 상위 3개 구해 보세요.

~~~sql
select order_hour_of_day, count(*)
from orders
where order_dow  in (0,1) and eval_set = 'test'
group by order_hour_of_day
order by count(*) desc
limit 3
~~~

##### 7. SELECT와 LIMIT 구문을 사용하고 주문수가 10,000건 이상인 department, aisle, product_name 과 주문 수를 많은 순으로 구해 보세요.

~~~sql
select d.department, a.aisle, p.product_name, count(distinct(order_id)) as "주문수" 
from order_products__train as o
	inner join products as p
		on p.product_id = o.product_id
	inner join aisles as a
		on a.aisle_id = p.aisle_id
	inner join departments as d
		on d.department_id = p.department_id
group by product_name
having count(*) > 10000
--groupby 하는 등 추가로 내가 계산한 값들을 having으로 조건을 정해줄 수 있음
order by count(*) desc
~~~

- having: groupby 하는 등 추가로 내가 계산한 값들을 having으로 조건을 정해줄 수 있음

