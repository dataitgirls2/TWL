# 저번 시간 복습

echo "# constitution-kr" >> [README.md](http://README.md)

git init

git add [README.md](http://README.md)

git commit -m "first commit"

git remote add origin <https://github.com/pje1740/constitution-kr.git>

git push -u origin master

(Git bash로 SSH Key 등록하기

Not used 떠 있는 SSH는 삭제해도 되는 Key

SSH key를 등록하면 git 계정 연결)





# 브랜치 만들고 변경된 파일 버젼 비교해보기

2018년 헌법개정안 파일을 다운로드 받습니다.

<https://drive.google.com/drive/u/0/folders/11REn11b5WaOTWVeHy-T3ddM48_Y_P7CB>



git checkout -b 2018 로 만듭니다. (가끔 터미널에서 한글 인코딩 문제로 오류가 발생하기 때문에 영문과 숫자로만 사용하는 것을 권장합니다.) 해당 명령어는 브랜치를 만들고 변경해 주는 역할을 합니다.



[Git - 브랜치란 무엇인가?](https://git-scm.com/book/ko/v1/Git-%EB%B8%8C%EB%9E%9C%EC%B9%98-%EB%B8%8C%EB%9E%9C%EC%B9%98%EB%9E%80-%EB%AC%B4%EC%97%87%EC%9D%B8%EA%B0%80%3F)

git branch 명령어를 실행하면 2개의 브랜치 목록이 나오며 활성화 되어 있는 브랜치 앞에 별표가 표시됩니다.

git checkout master 를 해보면 다시 마스터 브랜치로 이동하고, git checkout 2018로 2018 브랜치로 이동합니다.

브랜치를 이동한 상태에서 다운로드 받은 2018년 파일을 이 폴더로 옮겨줍니다.

git add “대한민국 헌법.txt” 로 변경상태를 Stage 상태로 보냅니다.

git commit -m “2018년 개정안” 으로 커밋 메시지를 작성하고 커밋합니다.

git push -u origin 2018 로 깃헙에 푸시합니다. (1987년 과정과 브랜치가 다릅니다.)

github 으로 가서 2018 브랜치를 master 브랜치로 pull request를 생성합니다.

이전 실습에서는 포크해온 저장소에 풀리퀘스트를 보냈지만, 이번에는 같은 저장소에서 다른 브랜치를 통해 풀리퀘스트를 생성했습니다.



# 실습

위치$Ls -al -> 아무것도 안 들어있는 것 확인

위치$ mv ~/Downloads/대한민국\헌법.txt.

Mv : 이동

Cp : 복사

위치$ ls -al

위치$ git init

$ git remote -v

$vi README.md :파일 열기

$ git add README.md : git으로 관리하겠다

$ git status : 깃 상태 확인 

$ git commit -m ‘대한민국 헌법 1987년'

$ git commit -ammend : 커밋 수정(노트패드나 vi편집기로 편집할 수 있음 vi권장)

:w :저장

:q :편집기 닫기

$ git remote add origin git@~~~

$ git remote -v :확인

$ git config —list :name, email설정 확인 가능

$ ls -al 

$ vi .git/config :[remote “origin”] 에서 url을 ssh로 고쳐도 됨

$ git remote -v 어느 저장소를 바라보는지 확인 가

$ git push -u origin master

$ git status : push한 파일은 안나오고 untracked file은 알려줌

$ git add 대한민국\헌법.txt

$ git status : 대한민국\헌법.txt가 뉴파일로 뜸

커밋 여러번 하고 나중에 push한번만 해도됨

$ git commit -m ‘1987년 대한민국 헌법’ : git hub에는 아직 반영x

$ git push -u origin master :(아직 git hub에 master branch뿐)

새 파일 같은 폴더에 다운받고

$ git checkout -b 2018 :2018이라는 브랜치가 생김

$ git branch : 브랜치 확인

$ git checkout master : 브랜치를 마스터로 바꾸기

$ git branch : 마스터에 불이 들어와있음

$ git checkout 2018 :2018 브랜치로 스위치하기'

$ git branch :2018에 불 들어옴

$ ls - al

$ mv ~/Downloads/대한민국\헌법.txt : (원래파일 필요 없으니 덮어쓰기)

$ 

$ git Dif : 달라진 내용 바로 확인해볼 수 있음

$ git add 대한민국\헌법.txt

$ git status 

$ git commit -m '2018 개정안'

$ git status :’nothing to commit, ~’

$ git push -u origin 2018 :2018branch에 push (비번 쳐야하는 경우도 있음)



Git hub에서 확인

Pull request (description 작성도! 2018 개정안 실습!) -> 파일 changed 확인 가능 

Merge -> master branch에 반영 -> 대한민국 헌법파일이 최신 버젼으로 바뀜





# \~bash로 새폴더 만들고 커밋하기~

원하는 리파지토리 포크를 하고

Git hub가서 리파지토리 클론 눌러서 주소 저장

$ cd ..

$ cd ~/폴더만들고 싶은 위치/

$ git clone 주소 : 자동으로 리파지토리와 같은 이름의 폴더가 생김

$ cd tutorial(폴더이름)



$ mkdir 'github계정' : 'github계정'에 폴더 생성

$ cd ''폴더이름'' : 위치 이동

$ vi README.md : 폴더에 파일 추가

$ git status : 상태 확인

$ git add README.md : state상태 만들기 (커밋할 수 있는 상태가 됨)

$ git commit -m ‘커밋 내용'

$ git remote -v :어느 저장소를 바라보는지 확인 가능

$ git push origin master :origin경로에 master 브랜치로 푸시하겠다는 의미

($ rm : 삭제)

($ rm -rf : 다 날리기)

(Bash에 단축키 등록 가능)



# \~Git 최신상태로 유지해주기~

cd /Users/heebunny/Downloads/dataitgirls/TWL

cd /Users/heebunny/Downloads/dataitgirls/tutorial

git@github.com:dataitgirls2/tutorial.git

<https://github.com/dataitgirls2/tutorial.git>

[https://github.com/HeeYoungK/TWL.git](https://github.com/HeeYoungK/tutorial.git)



**git fetch**

**git merge**

**git pull = git fetch + merge**

**git pull --rebase <<- 저장소의 이력을 간결하게 유지하기 위해 우리는 주로 이 명령어를 사용할거예요.**

## **git pull**

**중앙 저장소의 소스를 로컬 저장소로 가져옵니다.  또한 현재 작업중인 소스들의 Merge작업까지 통합하여 수행해요.**

## **git fetch**

**중앙 저장소의 소스를 로컬 저장소로 가져옵니다. 그러나 현재 작업중인 소스들을 변경하는 Merge 작업을 하지 않습니다.**



## 포크해 온 저장소의 소스를 가져오기

**우리는 데잇걸즈의 TWL저장소에서 fork 해 온 이후로 내 계정에 있는 저장소를 동기화하지 않았어요.**

**내 계정에 있는 저장소로 데잇걸즈 저장소에 있는 다른 동료 학습자의 TWL 내용을 내 로컬 폴더로 가져와 보고 싶어요. 이럴 때 어떻게 하면 좋을까요?**

**설정되어 있는 리모트 저장소를 봅니다.**

**git remote -vorigin  https://github.com/YOUR_USERNAME/YOUR_FORK.git (fetch)origin  https://github.com/YOUR_USERNAME/YOUR_FORK.git (push)**

**포크해 온 원래의 저장소를 추가해 줍니다.**

git remote add upstream <https://github.com/>ORIGINAL_OWNER/ORIGINAL_REPOSITORY.git

**upstream이 잘 추가되었는지 봅니다.**

**git remote -vorigin    https://github.com/YOUR_USERNAME/YOUR_FORK.git (fetch)origin    https://github.com/YOUR_USERNAME/YOUR_FORK.git (push)upstream  https://github.com/ORIGINAL_OWNER/ORIGINAL_REPOSITORY.git (fetch)upstream  https://github.com/ORIGINAL_OWNER/ORIGINAL_REPOSITORY.git (push)**

**이제 포크해온 저장소를 우리의 저장소와 동기화할 준비가 되었습니다.**

**git pull --rebase upstream master**

**우리 계정에 있는 저장소로 데잇걸즈 저장소의 내용을 가져올 명령어입니다.**

이후에 마스터에 push 하면 끝

$ git push -u origin master : (아직 git hub에 master branch뿐)



TWL, Tutorial을 이 방법으로 최신으로 유지!



## 실습 메모

TWL폴더 만들기

TWL$ cd ~/

~$ mkdir dataitgirls

~$ cd dataitgirls/

dataitfirls$ mv ~/data/TWL/ .

$ ls -al

$ ,,, config

$ TWL$ cd ..

$ dataitgirls$ mv ~/data/tutorial/ .

$ ls

$ mv ~/data/constitution-kr/ .

$ ls —al

$ 



**준비) 윈도우 유저는 C에 dataitgirls 라는 폴더를 생성합니다. 앞으로 우리가 실습하는 코드는 여기에 담아 둘 예정입니다.**

**맥 유저는 ~/ 경로에 같은 이름의 폴더를 생성합니다.**

**만약 미리 클론 받아 놓았다면 해당 폴더를 통째로 옮깁니다.**

**폴더를 옮길때는 다음의 명령어를 통해 옮겨요.**

**아직 git bash 에 익숙하지 않다면 탐색기 혹은 finder를 열어 드래그앤드롭으로 옮겨주어도 됩니다.**

**mv -rf 이전폴더경로 옮길폴더경로**

mv 파일명 폴더경로(현재 위치면 .)



1. ## **튜토리얼 저장소**

**데잇걸즈가 아닌 본인 계정의 Tutorial 저장소를 클론 받아와 로컬과 동기화 합니다.**

<https://github.com/HeeYoungK/tutorial.git>

git@github.com:HeeYoungK/tutorial.git



1. ## **TWL 저장소**

**본인 계정의 TWL 저장소를 클론 받아옵니다. 이미 받았다면 git pull —rebase 를 통해 최신 상태로 유지해 줍니다.**

**위에 있는 포크해 온 저장소의 소스를 가져오기를 참고하여 데잇걸즈 저장소를 upstream 으로 등록하고 rebase 해봅니다.**

$ git push -u origin master :(아직 git hub에 master branch뿐)

**자신의 저장소에 README.md 파일을 생성해 줍니다.**



1. ## **git rename**

**처음 실습했던 마크다운 파일의 이름을 변경해 봅니다.**

**TWL에 날짜와 깃헙 아이디 이어서 파일명으로 지정했는데 이 아이디를 제목으로 변경해 봅니다.**

**예를들어 20180702_yourgithubid.md 라면 20180702_statistics.md 로 변경해 봅니다.**

**git add 파일명 으로 stage 상태로 보냅니다.**

**git commit 파일명 으로 commit 하고 push 합니다.**



1. ## **TIL**

**마크다운 파일을 로컬PC에서 생성하고 github에 push 합니다.**

Cd /Users/heebunny/Downloads/dataitgirls/TWL

cd /Users/heebunny/Downloads/dataitgirls/TWL

huibaniui-MacBook-Pro:TWL heebunny$ git remote set-url upstream git@github.com:dataitgirls2/TWL.git
 huibaniui-MacBook-Pro:TWL heebunny$ git remote -v
 origin git@github.com:HeeYoungK/TWL.git (fetch)
 origin git@github.com:HeeYoungK/TWL.git (push)
 upstream git@github.com:dataitgirls2/TWL.git (fetch)

upstream git@github.com:dataitgirls2/TWL.git (push)





# 과제

오늘 TWL 은 맞은편 사람에게 merge 요청

아나콘다 설치하기
