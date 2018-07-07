# Github 사용하기_3

### 1. Repository 최신상태 유지하기

- 목표 : fork해온 데잇걸즈 /TWL repository를 동기화하여 나의 계정에서도 최신상태를 유지할 수 있다.
- How to :
  - 나의 계정/TWL을 local에 clone : git clone [git 주소]
  - 원격저장소 확인 : git remote -v (나의 계정 = origin)
  - daitgirls/TWL을 upstream으로 설정 : git remote add upstream [daitgirls/TWL git 주소]
  - 원격저장소 확인 : git remote -v (데잇걸즈 공동 TWL = upstream )
  - upstream에서 당겨오기(pull) : git pull --rebase upstream master 또는 git pull --rebase --autostash upstream master
  - Github에 동기화 : git push -u origin master
  - 만약 오류가 난다면, 폴더를 지우고 다시 clone하여 시도해본다.



### 2. 과제

- 앞으로 local에서 Typora로 작성한 파일을 git bash를 통해 나의 계정 TWL에 git add 하고 push 한다.
- 그리고 Github에서 pull request를 보내어 upstream을 동기화하여 최신상태로 유지해보자.



# 오후 특강

### 데이터 분석으로 세상을 바꿀 수 있을까요?

