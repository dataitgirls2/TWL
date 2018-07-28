# 20180706 _ git rebase.md



```add README.md``` : 수정하는 코드

```git config -- ls``` : name과 email 설정되어있어야한다.

```git push -u origin master``` : 특정상태로 돌아가고 싶을 때, 수정하고 싶을 때.  



처음들어갈 땐 master branch하나만 있다. 

```git add ``` : git으로 관리하겠다. 저장한 것은 commit하는 것이다. 저장로그는 commit log인 것이다. commit -> push가 꼭 해야하는게 아니라 commit은 로컬에서 계속 바꾸고 push는 한번에 해도된다. 

다 모아서 commit message를 다 모아서 한 번에 push해도된다. 

```git push -u master branch```  : push하는 것. 

회사에서 일할 때는 issue에 대해서 생성한다. issue번호로 branch를 만든다. 

- git branch

  : **브랜치를 사용하는 이유 ** 

  예를 들어 서비스는 계속 운영해야하는데 새로운 피처도 넣어야 하고 그 와중에 보안 이슈가 있다. 이럴 때 개발하던 피처를 보안패치 하는데 같이 넣어 완성되지 않은 피처를 라이브 서비스에 내보내면 더 큰 문제가 될 수도 있을거에요.예를 들어 게임 서버에 보안 이슈가 있어서 아이템이 계속 털리고 있다고 가정합니다.이 때 재빠르게 보안 패치가 필요할거에요. 그런데 한쪽에서 신규 퀘스트를 개발하고 있었어요. 아직 개발은 완성되지 않은 상태인데 이 퀘스트가 완성되지 않은 채로 보안 패치와 같이 나가야 한다면?신규 퀘스트 작업하던 것을 다 삭제하고 보안패치만 할 수도 없겠죠. 이럴 때 브랜치를 사용해요.

  다른 사람들과 내 것을 동기화하고 싶을 때. 보안패치가 다른 사람 폴더에 있어서 이것을 내것과 통합해서 master branch와 통합하는 것. 그 다음에 pull request를 한다.  기준은 master branch이고 sidebar로 다 fetch해오는 것. 

  회사에서는 issue마다 branch를 다만들어서 side bar가 너무 많이 생기기도 한다. 그래서 다 삭제한다. side bar에서도 branch를 딸 수가 있어서 master와 branch가 따로 길을 가기도 한다. 

  과거 history 로 돌아갈 수도 있다. 

  - __branch 만들기__

```git checkout -b 2019```: 브랜치를 만들어라. 

mv downloads/대한민국\헌법.



덮어 쓰고 git bash에서 확인했다. 소스트리를 사용하면 수정내용을 시각적으로 볼 수 있다. 

```git push -u origin``` : push하는 것 .

pull request : master로 merge. describe 하는 게 좋다.\

- twl 소스트리로 

  ```mkdir ``` : folder 생성. 

  ``` vi README.md```

    

  ```git status```

  ```git commit -m ```: commit message 생성. 

  ```git remote -v``` : git 어디장소에 저장되는지. 

  

  readme.md 파일을 만들면 목록을 만들 수 있다. 

  ```git clone "주소"```

  

  

  1. 포크해온 계정에 있는 튜토리얼을 clone한다. 
  2. 

- git 최신상태로 유지하기.

  ```git fetch```

  ```git merge```

  ```git pull``` = ```git fetch```  + ```merge```

  ```git pull --rebase ```  : 저장소의 이력을 간결히 함. 		

  - ```git -- rebase upstream master```
  -  파일 naming rule : date_lecture title.md

  

  - 실습 할 것 : 
  - 튜토리얼 저장소를 클론해 오는 것 : 

  - ```git remote add upstream ```  "주소" : master 폴더에 있는 것을 내 포크해온 것으로 옮기는 것. 
  - ```git remote -v ```: 확인.
  - 내 포크해온 계정에 master를 rebase하는 법.
  - ``` git pull--rebase upstream master```: twl에 없었던 다른 사람것이 다 생김. 
  - ```git push -u origin master``` : 내 걸로 업데이트 하는 것. 
  - ```git push -f origin master```:  

  ```git mv '파일명'
  git mv 파일명 새로운 파일명 
  
  git push -u origin master 
  
  ```

  김슬

평범한 개발자 

데이터 분석 왜 배우시나요? 

- 컨텐츠 분석, 소비자 니즈 파악. 
- 데이터 분석이 핫하기 때문에 월급을 받는 방법으로 배우는 사람들이 많다. 그런 목적을 달성하기도 어렵다. 또한 유지되기 어렵다. 세상에 대한 호기심, 애정이 있는 사람과는 차이가 난다. 





civic hacking :

공공문제를 해결하는 프로그램, 이야기하는 프로그램을 만드는 것.  요즘 메타가 무슨 얘기를 해도 정치라고 한다. 정보는 언론의 역할이다.

##### 동시다발적으로 일어나는 상황을 일목요연하게 모아보자. 

최소한 같은 사건이라도 모아보자. 

exif : 사진이나 영상 파일에 들어 있는 메타 정보 

-> 카메라종류/ 카메라 설정 / 사진을 찍은 시간  / 위치. 

묶어 보자 (clustering) : 비슷한 그룹끼리 묶는 것 

알고리즘 별로 묶는 것은 차이가 있다. 

www.witness.kr : 사진 클러스터링 site

q : 이걸 실시간으로 묶어 볼 순 없을까? 사건이 일어났을 때 사진이 많이 올라올 것이다. -> 반대로 사건 detecting이 가능할 것이다. 

트위터에서 사건 detecting이 가능하다. 미국의 지방정부에서 전복시도가 있었다. 등등. 

참여연대 열려라에서 국회

분당 후 발의 경향.  이어지는 그래프로 분석. 

- 탄핵이 정말 될까? MCMC ID IRT -> 블랙박스처럼 계속 돌려보는 것. OUTPUT이 나올만한 INPUT을 돌려봄. 
- 의회의 POLARIZATION 분석을 위해 개발. /공화당과 민주당의 의사결정 분화. 대법관들의 보수화 경향. 
- 헌법재판관들이 어떤 표를 했는지 기록이 남아있음. 헌재 성향 분석. 

여론조사는 어디까지 믿을 수 있을까? 

신호와 소음. 

여론조사 오차 : 실제 결과와 여론자사의 차이 비교 기관 평가 결과? 

정보공개 청구 포털 OPEN.GO.KR 

OPEN DATA DAY 3년에 열리는 OPEN DATA DAY. 

- 재판은 인종에게 공정한가? 

  미국에서는 판사들이 프로그램을 참고하여 판결함. 재범율 참고 등.

  여기에 인종은 안넣게 되어있다. 

  - 오픈소스 ~ 협력. 오픈소스 의료도 있고 

    성당과 시장 : 모든 좋은 소프트웨어는 개발자 개인의 가려온 곳을 긁는 것으로부터 시작된다. 

- 여론조사 결과는 왜 틀릴까?

  : 샤이 트럼프 일 수도 있고, 설문조사 문항에서 어휘 한 두개를 바꿀 수도 있다. 

  -----------

  1. ```fork```
  2. ```clone```

  3: ```remote upstream```

4. ```git pull --rebase``` : fetch, merge, add , commit를 한 번에 한다. 
5. unstage 된 file이 있을 수 있다. 같은 folder로 작업하기 때문에 우리 모두에게 생겨날 수 있는 것이다. ```git add . ```로 다 옮겨주면 된다. 오류가 나는 상황을 반기는 게 좋다. 최대한 많은 오류를 겪는게 도움이 된다.  

만약 push가 안될 때 auto stash를 하면된다. git add/ commit/ push가 되면 

6. pull request



- bash - vi - editing- mode 

  - bash vi exit :

    1. press ```esc``` key

    2. Press ```:```

    3. Enter the following ```q!```

       

  - bash vi save

  - : Write your file by entering ```:w``` and quit by entering ```:q ```

  -   