# 180706

## 배로선생님

### git과 git bash

로컬 깃헙과 git@~~와 연결시켜준다

- `git remote -v`

  설정된 remote경로가 출력

- `git config --list`

  name과 email이 설정되어 있는지를 확인하기 위해 사용

- `ls -al`

  직접 보기

- w저장 q끝내기

- `vi .git/config`

- `git push -u origin master`

  (마스터 브랜치에 푸시)

  upstream 의 약자, -u와 -f를 많이 사용. false 특정 상태로 돌아가고 싶을 때 이미 머지가 되어서 이전 상태로 돌린 후 다시 push하고 싶을 때

- untracked -> tracked 로 올리려면 git add

수정된 버전 기록: 커밋기록이 남음. 커밋은 계속 바꾸고 나중에 푸시 한번 할 수 있음.

`git commit -m '1987년 대한민국 헌법 개정안'`

`git push -u origin master`

커밋한 1987년 헌법 개정안이 커밋된 후 마스터 브랜치로 푸시됨 (github에 올라감)

#### 브랜치, git 사용하는 이유

- 협업을 잘 하기 위하여

```
git commit -m 'first commit'
git remote -v
git push origin master
git push -u origin master
```

```
rm -rf tutorial/
	tutorial 폴더를 지우는 명령어
```

##### 내 저장소로 동기화시키고 싶은 경우

origin말고 upstream으로 설정해줌 : 저장소의 것을 땡겨와서 내 꺼에 merge

```
git pull --rebase
	가장 많이 쓰는 명령어, fetch 와 merge를 한번에 해 줌.
	언제 master에서 무엇을 동기화 시켜줬다는 log가 남음.
```

```
git remote add upstream
	origin 말고도 upstream이 생김
```

1. fork

2. clone 내 것을 받아옴

3. rebase upstream

4. `git pull rebase` 로 가지고 옴

   (git fetch, merge, add, commit을 하나의 과정으로)

   add 하고 commit한 로그가 남지 않아 간결하게 유지.

   * git add . 

     unstaged 되어있던 모든 파일을 add 시켜 줌.

###### 실습

클론 받아와서 upstream으로 업데이트하기

```
git clone GITHUB경로
```

fork해 온 것의 원래 저장소를 upstream

wo1ever : origin

dataitgirls : upstream



#### 오수후업 강의 -김슬님

###### 3가지 스고이

1. 맨 처음 질문하는 사람 - 다음 사람이 질문하기 쉬워짐
2. 바보같은 질문하는 사람 - 질문의 문턱을 낮춰줌
3. 관계없는 질문하는 사람 - 이야기의 범위를 넓혀줌

###### 데이터 분석 왜 배우시나요?

본인만의 애정과 호기심을 가지고 분석을 배우면 훨씬 도움이 될 것

###### 시빅해킹

* 공공 문제를 해결하는 프로그램을 만들거나 (정부의 역할)
* 공공 문제를 이야기하는 프로그램을 만듬 (언론의 역할)

###### 동시 다발적으로 발생하는 현장상황을 일목요연하게 모아보기

(eg) paris attack 당시, sns 사진

- EXIF : 사진이나 영상 파일에 들어있는 메타정보
  - 시간
  - 기기
  - ... 등
- clustering : 그룹화시킴
  - Clustering Algorithms > In scikit-learn

###### 실시간으로 묶어서 볼 수는 없을까?

어떤 사건이 발생한 것을 실시간으로 알 수 있음

###### 결과

내가 살면서 접하기 힘들었던, 새로운 사건이 끊임없이 발생함.

###### 당에서 떨어져 나온 새 당 사람들은 원래 당 사람들과 다른 사람들이었을까?

- 의안정보시스템 > 열려라국회 사이트
- Graph 분석 in Python (Network X)
- 공동 발의를 한 사람들을 선으로 잇고, 각 당은 색으로 표시

###### 탄핵이 정말 될까? ... 등 많은 분석들

###### 여론조사는 어디까지 믿을 수 있을까?

- 중앙선거여론조사심위위원회
- FiveThirtyEight's Pollster Ratings : 스포츠가 많음

**Open Data Day** : 매월 3월 첫째 주 토요일(?)

###### Q&A

귀납과 영역의 이론? 현실적으로 객관적이게 되는것이 매우 불가능.

팀 프로젝트로 진행했던 경우가 많음

팀 프로젝트의 협력은 데이터 수집부터 분석, 개발 등으로 나눔

over communication이란 없다 (!)

프로젝트 주제를 정하는 방법 : 데이터부터 시작하는 경우, 사회적 이슈부터 시작하는 경우, 해외 기사들을 보다가(한국에서도 할 수 있지 않나?!) 등

Null채움 : 매주 월요일 저녁

pyjob

해커톤

'통계학의 피카소는 누구인가요'

'어쩌다보니 통계학자'