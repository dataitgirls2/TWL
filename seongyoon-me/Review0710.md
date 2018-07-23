# 180706 수업 복습 _ 0710(화) 기록

- git bash 들어가서 작업표시줄에 처음 경로 표시가 필요해

  - c/dataitgirls/TWL에 작업 환경 필요       
  -  C:\\\dataitgirls      //처음 시작할 때 dataitgirls로.
  - git clone  git@github.com:seongyoon-me/TWL.git    //git clone을 함. 깃허브 본인 계정의 TWL로
  - git remote -v     //remote 저장소    깃 저장소를 -v 본다.
  - git remote add origin git@github.com:seongyoon-me/TWL.git       // ???

  오류

  - git init  (초기화)

  - git remote add origin git@github.com:seongyoon-me/TWL.git      //따라서 오류가 발생  시 git init으로 초기화 필요해

  - git remote add origin git@github.com:seongyoon-me/TWL.git

  - git remote -v

    origin git@github.com:seongyoon-me/TWL.**git** (fetch)

    origin git@github.com:seongyoon-me/TWL.git (push)

  - vi "first.md"       //vi 파일을 만들어 줄 때 확장명도 써야해

  - cd TWL (상대경로)      //cd/dataitgirls 안에서 상대경로를 나타내기 때문에 그냥 TWL 써도 상관 없다.

    

    

    ### 순서

    git add "first.md"        // first.md라는 파일을 추가

    git commit -m "first"     //커밋을 받아줌

    git push -u origin          //커밋 된 것을 push함 

    git checkout -b "first"   //스위치 됨 새로운 브랜치인 'first'로

    git checkout "master"

    git checkout "first"

    git add "first.md"는    git add .        //같이 사용 할 수 있음 git add . 은 git 안에 파일 모두 다 사용 가능

    git commit "message"

    git push -u origin 

    git push -f origin 

  ---------------------------

  

  ![1531190364069](C:\Users\정성윤\AppData\Local\Temp\1531190364069.png)

  

  

  ![1531190395450](C:\Users\정성윤\AppData\Local\Temp\1531190395450.png)

  

  ![1531190430563](C:\Users\정성윤\AppData\Local\Temp\1531190430563.png)

  

  

  ![1531190441805](C:\Users\정성윤\AppData\Local\Temp\1531190441805.png)

  

  ---------------------

  ## 데잇걸즈 하면서 전문성을 키우는 방법

  의도적 수련?

  1일 1commit

  전문성을 키우는 방법... 

  짜투리 시간을 이용하여 공부. (출근, 퇴근 시간 이용)

  예제 코드를 그대로 작성하고 지우고 다시 재생산 마치 언어를 공부하는 것처럼.

  영어 단어 외우는 방법처럼..

  책 보고 치는 것 보다 재생산하는 방법이 좋다.

  하루하루를 평가하는 방법...

  TIL . TWL . 

  튜토리얼 재생산...

  파이썬?? -> 보고 이해하고 재생산이 필요해요...

  


  

  

  







