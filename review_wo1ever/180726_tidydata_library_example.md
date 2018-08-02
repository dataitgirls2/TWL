# 180726

## 오전수업

### tidydata

#### 도서관 데이터 실습

Google colab 이용

#### tidydata

우리 기준에서는 tidydata 기준이 썩 훌륭함.

하나의 행에는 하나의 obs(unit)가 담김.

서로 다른 단위의 데이터가 섞여있으면 안됨.

categorical column으로 관리하면 좋을 지도 모름.

예를들어

| **도서관A** | 도서수     | 123  |
| ----------- | ---------- | ---- |
| 도서관A     | 연속간행물 | 2324 |
| 도서관A     | 비도서     | 45   |
| 도서관B     | 도서수     | 5657 |
| 도서관B     | 연속간행물 | 87   |
| ...         | ...        | ...  |

이렇게 사용한다면, group by = 도서관, 총 도서 수(sum)이라던가 '도서수'만 고르기 등이 조금 더 자연스럽게 표현됨.

판다스의 merge 서로 다른 칼럼을 합쳐줌.



## 오후수업

### Naver AI Platform 배수민님

#### 클로바 Clova

네이버와 라인이 만든 인공지능

##### Search & Clova AI

영상(Show)

음성 인지(Speak)

추천(Recognition)

자연어 이해(Natural text understanding) : 그 문자가 어느것을 의미하는 것인가

##### New Search Experience

카메라 모양 누르면? 음성검색, 이미지 검색 등 가능.

##### New Voice Experience

클로바 : 인터페이스를 음성으로만 설정.

##### Beyond App and Device -

가전 / 앱에 제공 가능.



interspeech 학회 : lib모양을 보고 음성을 추출

NSML기능들을 사용

