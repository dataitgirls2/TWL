# A. 실습 전 배로 선생님의 강의

### 1. Done is better than perfect!
- TIL (Today I Learned)로 일일 커밋하기. 
- 스택오버플로우에서 코드 보고 따라쓰기. 링크와 함께 복사 후 붙여넣기 하지 않고 직접 타이핑 해 보자. 남의 코드를 따라하더라도 직접 따라 쓰면 내 것이 된다.
- 오류를 경험하고, 오류를 통해 배우자.
- 캐글에 있는 튜토리얼을 보고 따라해 보자.
- 스프린트, 판다스, 장고 등 패키지의 이슈들을 해결해서 오픈소스에 기여해 보자.
- 정적 블로그를 운영 해 보자. 깃헙에서 무료로 이용 가능하고, 커밋 로그가 남으므로 이 활동으로 일일커밋을 할 수 있다. 

( 🤔 스택오버플로우, 캐글, 스프린트, 판다스, 장고 등이 뭔지는 나중에 찾아보자. ) 

# B. 실습 내용 

### 1. Github에 저장소 만들기 (repository)
- 우리는 오늘 TWL, TIL, tutorial 세 개의 repositories 를 만들었다.
- TIL repository = 내가 만든 나의 저장소로, 나의 로컬 (나의 컴퓨터 환경)에서 이용 가능하며 다른 사람들과 공유하지 않는 repository.
- TWL repository = daitgirls2 organization 에서 yebin 님이 만든 repository. 데잇걸즈 전원이 권한을 가짐.
- tutorial repository = daitgirls2 organization 에서 yebin 님이 만든 repository. 데잇걸즈 전원이 권한을 가짐. 

### 2. 포크 (fork) 
- 다른 사람이 생성한 repository를 fork하여 나의 페이지로 가져올 수 있다. 
- 우리는 오늘 TWL repository 를 fork 하여 나의 페이지로 가져와서, 내 Github 아이디를 이름으로 하는 개인 폴더를 하나씩 만들었다.

### 3. 풀리퀘스트 (full request)와 머지 (merge) 
- TWL repository 에 개인 폴더를 만든 것은 수정을 가한 것이므로, 그 내용을 반영해달라는 요청을 보내야 한다. 그것이 full request 이다. 
- 머지 권한을 가진 사람은 full request 를 확인한 후, 이것을 반영하고자 하는 허락을 내릴 수 있다. 이것이 merge 이다. 

### 4. 이슈 (issue) 
- 프로젝트 내에서 특정한 이슈가 있을 때, 그 내용을 Issues 에 게시할 수 있다.
- 이슈를 게시할 경우 고유한 넘버가 생성되며, 넘버는 '#'+'숫자'의 형태로 발생한다.
- 어떠한 활동을 통해 full request를 보낼 때, 특정 이슈에 관한 사항임을 알리고자 할 경우 생성된 고유 넘버를 태깅해서 나타낸다. 

### 5. 소스트리 (sourcetree) 소프트웨어 다운받기, SSH Key 설정하기
- 소스트리라는 프로그램을 통해 Github의 repository 에 쉽게 접근할 수 있다.
- ssh key는 고유의 식별 키로, github 계정과 sourcetree 를 연동하여 나의 로컬에서 repositories 에 접근할 수 있도록 한다. 

# C. 부가 설명과 복습 

### 1. 애란 선생님의 부가 설명 정리
- 내 로컬 환경에 폴더를 하나 만든다. 그 폴더에 특정 파일을 넣을 경우, 자동으로 그것이 repository로 인식된다. 
- 그 repository 는 크게 두 영역으로 구분된다. untracked 영역, tracked 영역, 
- repository 에 파일 A 를 넣을 경우 A 는 untracked 영역으로 들어가게 되고, 이 때 A 는 Git 과는 관련없는 개체들이다.
- 그러나 A 에 add 를 실행할 경우 A 는 tracked 영역으로 옮겨지며, 이 때 부터 버전 관리가 가능하게 된다.
- add 는 아직 배우지 않았지만 (...) untracked 영역에 있는 개체들을 tracked 영역으로 옮기기 위해 실행하는 것이 add 라고 생각하면 된다. 
- tracked 영역은 다시 staged 와 unstaged 로 나뉜다.
- staged 는 파일이 '영구히 저장될 준비'가 되었다는 것을 뜻한다. 즉, add 를 실행하면 파일은 untracked 에서 tracked + staged 로 이동한다.
- tracked + staged 에 놓인 파일 A 를 수정해서 A'를 만들면, A'는 tracked + unstaged로 이동한다.
- tracked + unstaged 에 놓인 파일 A' 를 tracked + staged 영역으로 옮길 때도 add 를 실행한다.
- 즉, add 는 tracked + staged 로 옮길 때도 사용하고, tracked + staged 상태에서 수정을 가해 tracked + unstaged 로 간 것을 다시 tracked + staged 로 이동시킬 때에도 사용한다.
- 이러한 결과를 '영구히 저장'하고자 할 때 commit 을 한다. 
- commit 은 tracked + staged 영역에 놓인 내용들이 통째로 복사가 되어 duplicated 되는 것을 뜻한다. 
- commit 을 하는 순간, 옛 버전은 v1이 되고, 현재 버전이 v2가 되는 것이다. 이런 식으로 v3, v4, v5, ... 식으로 버전관리가 실행된다.
- 이것이 Git의 시스템이다.
- 이러한 시스템은 나의 로컬 환경 (나의 컴퓨터)에서 실행 가능하며, 다른 사람의 로컬 환경 혹은 내 컴퓨터의 다른 폴더로 가져가고자 할 때 clone 기능을 쓴다.
- 그러면, tracked + staged 영역의 현재 버전과 이전의 히스토리까지 전부 복사된다.
- 복사된 정보들을 다른 로컬 환경에서 수정하면, v6이 생기는데 이 버전은 상위 환경에는 적용되지 않은 상태이다. 
- 그렇기 때문에 v6을 당겨가라고 요청하는 것이 pull request이고, 상위 로컬 환경의 주체가 pull request 를 승인하는 것이 merge 이다.
- 머지하게 되면, 원격으로 떨어져 있는 로컬 환경들에서 같은 버전을 보게 된다. 
- 우리 실습의 경우 add 등의 과정을 거치지 않았고, Github 서버에서 파일을 생성-수정하는 것이 add 가 실행된 것으로, 보이지 않았을 뿐. 
- fork 는 Git 에는 없는 용어로, Github 에 있는 repository 를 다른 github 서버로 옮겨가는 것이다. clone 의 개념이 github 에 적용된 것이라고 보면 됨. 
- 즉, 우리가 중앙 기구 (중앙 로컬 환경)으로 설정한 것이 daitgirls2 repository 인 것. Github 시스템 하에서의 약속과 같다.

( 😰 시간나면 그림으로 정리해 보기로 하자.)

# D. 요약 정리 
- Github 은 Git 이라는 시스템을 이용하여 원활하게 협업할 수 있도록 도와주는 장치(?) 시스템(?) 이다.
- Git이 뭔지 대략 감은 오지만 정확히는 모르겠다. 지금은 너무 피곤하니까 내일 찾아보자...




