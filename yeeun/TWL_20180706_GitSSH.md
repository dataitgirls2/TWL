# *DON'T PANIC*

# GIT

## SSH key 등록하기

1. Generate a new SSH key: sourcetreed의 'SSH Key 생성 또는 불러오기'는 오류 남:
- 이 명령어로 id_rsa라는 키를 생성한 후 내 로컬 Users/Username/.ssh 폴더를 만들어 여기에 저장합니다.

~~~
ls -al ~/.ssh	# ssh 폴더에 어떤 키가 있는지 조회
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
~~~

2. ensuring the ssh-agent is running. If not, adding it

~~~
eval $(ssh-agent -s)
ssh-add ~/.ssh/id_rsa	#자기 private key 등록
~~~

3. Github에 키 등록
- 내 로컬 Users/Username/.ssh에 들어가 id_rsa 퍼블릭 키를 메모장 등으로 열고, 텍스트를 복사하거나 다음 명령어를 실행해서 퍼블릭 키 내용물을 클립보드에 복사합니다
  ~~~
  ls -al ~/.ssh	# C/.ssh를 보여줌
  clip < ~/.ssh/id_rsa.pub
  ~~~

- 깃허브에서 내 계정 SSH키로 등록합니다
   
## Remote Repository SSH 키로 등록하기
- origin 연결을 remote ssh로 변경시키기
  ~~~
  git remote set-url origin git@github.com:USERNAME/REPOSITORY NAME.git
  ~~~

- add upstream 
  - HTML로 등록
  ~~~
  git remote add upstream https://github.com/ORIGINAL OWNER/ORIGINAL REPOSITORY NAME.git
  ~~~
  - SSH로 등록(업스트림 없을때 그냥 add upstream 해도 됨)
  ~~~
  git remote set-url upstream git@github.com:dataitgirls2/TWL.git
  ~~~
  
- 제대로 되었는지 확인하기
  ~~~
  git remote -v
  ~~~

## 명령어

- git init: create a new local repository

- -f : force

- -u: upstream

- git remote -v: remote로 설정된 경로를 보여줌

- git status: 현재 origin, upstream 상황을 조회

- ls: dir과 비슷

- ls -al: 숨겨진 파일까지 보여줌

  ~~~
  ls -al ~/.ssh	# C/.ssh를 보여줌
  clip < ~/.ssh/id_rsa.pub	# id_raa.pub(ssh 퍼블릭 키) 내용 클립보드에 복사
  ~~~

  

- 폴더 옮기기

  ~~~
  mv -rf OldDirectory NewDirectory
  ~~~

## PULLING

- 로컬 저장소를 원격 저장소에 맞춰 갱신하기: 편집충돌 주의!

- git fetch(중앙 저장소에서 로컬 저장소로)|merge 는 잘 안 씀

- git pull: fetch + merge 기능. 중앙 저장소(내 포크) 소스를 로컬 저장소로 가져옴

- git pull --rebase: 커밋 없이 add. 저장소 이력을 간결하게 유지하는데 좋음


## PUSHING

1. Adding file(s) in Index

   ~~~
   git add Filename	# in doubt, try * instead of Filename
   ~~~

2. commit

   ~~~
   git commit -m "Enter message here"
   ~~~

3. Forced push

   ~~~
   git push origin BranchName -f	
   ~~~

## Branch

- 안전하게 격리된 상태에서 무언가를 만들 때 사용.

- 새로운 가지를 생성해 개발 진행 -> 완료 시 master branch로 돌아와 병합

- Creating a branch + moving to it 

  ~~~
  git checkout -b NewBranchName
  ~~~

- Moving to a specific branch

  ~~~
  git checkout BranchName		# try master
  ~~~

- Pushing a specific branch to a remote storage(origin)

  ~~~
  git push origin BranchName
  ~~~



# Quick Setup 내용 백업

~~~
echo "# sandbox" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/snakefeet42/sandbox.git
git push -u origin master
~~~



## 정체 불명의 광역적 오류

왜 저 파일만 문제가 되는지 모르겠다. 파일명이나 확장자 문제는 아닌 듯.

> $ git status
> On branch master
> Changes not staged for commit:
>   (use "git add <file>..." to update what will be committed)
>   (use "git checkout -- <file>..." to discard changes in working directory)
>
> ​    **modified:   DassomLee/20180629_statistics&constitution**
>
> no changes added to commit (use "git add" and/or "git commit -a")

~~~
git add .	# add all: git ignore
git commit -m 'add files'	# unstaged상태 파일 다 커밋 로컬 저장소에 일단
git push -f origin master
~~~

