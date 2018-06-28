# A. 실습 전 배로 선생님의 강의

### 1. Done is better than perfect!
- TIL (Today I Learned)로 일일 커밋하기. 
- 스택오버플로우에서 코드 보고 따라쓰기. 링크와 함께 복사 후 붙여넣기 하지 않고 직접 타이핑 해 보자. 남의 코드를 따라하더라도 직접 따라 쓰면 내 것이 된다.
- 오류를 경험하고, 오류를 통해 배우자.
- 캐글에 있는 튜토리얼을 보고 따라해 보자.
- 스프린트, 판다스, 장고 등 패키지의 이슈들을 해결해서 오픈소스에 기여해 보자.
- 정적 블로그를 운영 해 보자. 깃헙에서 무료로 이용 가능하고, 커밋 로그가 남으므로 이 활동으로 일일커밋을 할 수 있다. 

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
- repository 에 아무 파일을 넣을 경우 그 파일들은 untracked 영역으로 들어가게 되고, 이 때에 파일들은 Git 과는 관련없는 개체들이다.
- 그러나 그 파일들에 add 를 실행할 경우 그 파일들은 tracked 영역으로 옮겨지며, 이 때 부터 버전 관리가 가능하게 된다.
- add 는 아직 배우지 않았지만 (...) untracked 영역에 있는 개체들을 tracked 영역으로 옮기기 위해 실행하는 것이 add 라고 생각하면 된 
- tracked 영역은 두개로 나뉘는데, staged 와 unstaged 로 나뉜다.
- staged 는 파일이 '영구히 저장될 준비'가 되었다는 것을 뜻한다. 

