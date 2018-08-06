#### 2018.08.06 데잇걸즈 TWL : 지리 데이터 다루기



1. ##### 오전 : 복습, 소스트리, 이터레이션 회의

- 복습 : 기계학습과 수학

- [실습] 국민청원 카테고리의 기타 예측하기

    ![20180806_petition_modeling](https://github.com/YoungestSalon/TIL/blob/master/20180806_petition_modeling.jpg?raw=true)

  - XGBoost 분산형 그래디언트 부스팅 알고리즘
  - 분석의 정확도 개선 : ngram_range와 max_features 숫자 올리기
  - 랜덤 포레스트의 random_state
    - 항상 같은 숫자를 넣어서 고정시켜야 함
    - 파라메터 외의 나머지 변수에 대한 변인 통제 같은 개념 
    - random_state 값이 변하면 결과의 변동 원인이 파라메터인지 아닌지를 알수 없음

- [실습] Source Tree 

  - Stash(임시 저장소) 사용법 실습 : [블로그](http://americanopeople.tistory.com/12) 참조
  - Checkout 사용법 실습 : 10 Minutes to Pandas 동기화  

  ~~~
  [Terminal]
  Local 컴퓨터에 폴더 생성
  git init
  git remote add origin https://github.com/YoungestSalon/10minutes2pandas
  git remote -v
  git remote add upstream https://github.com/dataitgirls2/10minutes2pandas
  git remote -v
  git pull --rebase upstream master
  수정 작업
  git add 파일명
  git commit -m "메시지"
  git push -u upstream master
  ~~~

  ~~~
  [Source Tree : Checkout 사용법 실습]
  1. Clone : https://github.com/YoungestSalon/10minutes2pandas
  2. Terminal에서 실행
  - git remote add upstream https://github.com/dataitgirls2/10minutes2pandas
  - git remote -v (origin / upstream 체크)
  3. 좌측 원격 → upstream → master 더블클릭 → 체크아웃
  
  * origin 설정이 틀린 경우 (@Terminal) 
  git remote set-url origin https://github.com/YoungestSalon/10minutes2pandas
  
  * upstream 설정이 틀린 경우 (@Terminal)
  git remote set-url upstream https://github.com/dataitgirls2/10minutes2pandas
  ~~~

- 이터레이션 회의

  - 유의점 
    - 변경 가능한 factor는 4가지 : 인력 추가, 범위/일정/퀄리티 변경
    - 원칙적으로 인력 추가, 퀄리티 수준 변경은 선택하면 안 됨. 현재는 일정 변경도 불가.
    - "산모가 10명이 된다고 해서 아이를 1개월 만에 출산할 수는 없다" (= 인력 추가는 선택 X)
    - 따라서, 프로젝트 범위의 유연한 변경이 필요할 수 있음.

  ~~~
  [F조 이터레이션 회의]
  - 주제 : 복합쇼핑몰의 성공/실패 요인
  - 데이터 수집 방법/일정
     1. 2015~2017 유통산업 백서 : https://news.joins.com/article/21425969 기사 참조
     2. 2018 복합쇼핑몰 전망 : http://naver.me/FCN1absy 참조
  - 수집 대상 데이터 
     1. 시설 정보 : 층수, 면적, 편의시설/조경 시설, 교통 수단, 영화관 여부/스크린 수
     2. 상권 정보 : 매출, 방문자 수, 입점 현황 
  - 편의점/코워킹 스페이스 데이터 : 필요한 팀 없으면 데이터 수집 중단 예정
  - 결정사항 : Free research + 개인별 의견 Slack에 사전 upload → 내일(8/7) 오후 중 추가 회의
  ~~~

  

2. ##### 오후 : 주소/지리 데이터 다루기

- 개념 정리 : Open Street Map, folium(폴리움), 위도/경도의 좌표 표시, [Geo-location API](https://cloud.google.com/maps-platform/?hl=ko)

- Google Geo-location API 설정

  - 프로젝트 생성
  - [사용자 인증 정보 페이지](https://console.cloud.google.com/apis/credentials?hl=ko) 접속 → 사용자 인증 정보 만들기 → API 키 
  - [Geocoding API](https://console.cloud.google.com/apis/library/geocoding-backend.googleapis.com?hl=ko&project=my-jmt) 사용 설정 : API 키를 재발급 받은 경우, Geocoding API를 다시 실행시켜야 함

- [실습] 공덕역 맛집지도 그리기 (@Google Colaboratory)

- [실습] 공공데이터 상권정보 분석하기 (@Anaconda)

- [추가] SourceTree에서 SSH Key 설정하기 @Windows OS

  ~~~
  - SSH key 생성 : SourceTree → 도구 → SSH 관리자 실행 → SSH key 생성
  - SSH Key 등록 : GitHub → Setting → SSH and GPG keys → SSH keys → New SSH key
  - SSH 로딩 : SourceTree → 옵션 → 일반 → SSH 클라이언트 설정 → SSH 클라이언트 → OpenSSH 선택
  ~~~

  
