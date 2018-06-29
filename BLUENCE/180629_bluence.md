# 180629 오전 확률과통계 1일차  - 박지현선생님

### 통계학의 정의 

ex) 모집단 : 투표할 수 있는 모든 사람 => 모집단의 특성 : 모수 


표본을 뽑아서 모집단의특성을 추론하는 것 => 표본의 특성 : 통계량

### 통계 목표 : 


통계량과 모수사이의 관계를 알아서 표본으로 모집단을 추론해야한다. 모수와 어느정도 일치할지 아는 것은 필연적이므로 ‘확률’도 알아야 함 


평균을 예측할 수 있는 ‘신뢰구간’을 구합니다.

### 신뢰구간? 
Ex) 문재인 투표율 30% , 100개중 이 평균(30%)을 포함할 확률이 95개만 포함된다는 것 

(1) 금천구 25~35 


(2) 성동구 20~25 사이


…. 100개의 표본이 있다.


### 차원의 저주 ( 변수가 많을때 줄이는 방법은? )


-	missing비율이 큰 변수 지우기


-	현업과 상의해서 변수제거 (도메인선택하고 제거, 매우 중요)


-	PCA 


-	Lasso


### 분석 프로세스 

SEMMA : 솔루션 업체인 SAS사 주도로 만들어진 방법론 (셈마)

분석의 시작 : 그림!!!! 가장 열심히 해야한다!!! 모든 인사이트는 여기서 나온다

그림을 그리고 데이터를 탐색해보는 것을 EDA라고 한다.

EDA : exploratory data analysis, 탐색적 자료 분석 


여러가지 방법을 통해 어떤 변수가 중요한 변수이고, 특징이 무엇인지 알아내는 것이 중요하다. 


### 자료의 분류

-	수치형 변수(Numerical) : 연속형(키는 끊어지지 않고 정확한걸로 잴수록 달라짐) / 이산형


-	범주형 변수(categorical) : 명목형(Nominal):혈액형,성별,통신사 / 순위형 :학년,등급


# 오후 수업 깃허브 사용법 – 박조은(배로)쌤 


## 깃허브 README.md 파일 원격저장소에 푸시해보기 실습 
### 푸시하는 순서 : add -> commit -> push순으로 해야 한다. 

git init – 깃이라는 폴더를 만들어줌 / git이라는 숨김 기본파일을 만들어줌 (그 폴더안에서 깃을 쓸 수 있게 해줌 )


git add – 깃이란 파일 생성한다. (메모장을 열었다.)


git commit – 수정 후 파일 저장 (메모장 저장하기)


git push – 깃허브로 업로드 (인터넷에 업로드하기)


(1) 파일을 찾기위해 우선 터미널에서 'cd 경로' 를 치고 들어간다. cd=change directory

(2) 아래와 같이 순서대로 입력한다. md파일을 만들어주고(echo) , git 초기화(init)하고 , add => commit => 해당 url을 origin이라는 저장소이름으로 설정하고


remote add한다


echo "# constitution-kr" >> README.md


git init


git add README.md


git commit -m "first commit"


git remote add origin git@github.com:BLUENCE/constitution-kr.git


git push -u origin master

## 깃 명령어 정리


https://blog.outsider.ne.kr/572








