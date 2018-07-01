# gitbash & sourcetree _ 20180629
  *lectured by 배로*  
  
__git__ : 이력을 관리하는 저장소  
버전 관리의 필요성 때문에 생겨난 것. 
충돌이 일어났을 때 이를 고칠 수 있는 방법을 이력을 통해 확인할 수 있다.
git 안에서 add와 commit이 가능하다.  
__push__ : local에서 github server로 파일을 내보내는 것.  
__git hub__ : 매개체이다.  
__commit__ : 변경내용을 저장하는 것.

저장소를 원격(remote)에도 만들고 local에도 만들고 동기화하는 것이 오늘 할일.

- git bash 명령어  
ls : 파일 리스트 불러오기  
pwd : 깃이 있는 위치를 찾는 것.
remote set url https : 원격저장소의 url을 https로 하겠다는 것.
git remote -v : remote의 버전을 확인하라는 것.
xxxx(어떤 명령어) -m : m은 메세지라는 뜻이다. " test" = comment임. 
git init : git config  파일을 생성해주고 폴더안에서 git을 쓸 수 있게 만드는 것임. 
git add : 파일을 하나 생성한 것. 메모장을 열었다는 것이라는데, 어제는 unstage->stage라고 배웠음.  
이거 헛갈리니 내일 질문. 
- 에러가 떴을 때  
git status부터 확인하자. 
