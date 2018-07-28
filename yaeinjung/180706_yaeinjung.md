# GIT 실습
## 2018 헌법 개정안 branch

### git bash 명령어
* `ls` 현재 디렉토리의 파일들을 보여줌
* `git remote -v` 리모트 설정 경로를 볼 수 있다
* `mv` 파일이동하는 명령어 
> mv 지금있는파일경로 이동할파일경로
* `git commit --amend` 커밋 메시지 수정
* `git config --list` 깃 설정 보기
* config 수정하고 싶을땐?
> cd ./.git
> vi config (vi 편집기로 config 파일을 열어줌)로 수정후 :wq!


## git 최신상태 유지하기
* `git pull --rebase` 

### EX ) TWL을 clone, upstream지정, pull해오기

* clone이란? git에 있는 리파지토리를 로컬로 가져오는것
* upstream ? 내 리파지토리로 pull 해올 리파지토리
* pull ? git에 있는 리파지토리의 내용을 내 로컬에 최신상태로 가져오는것

종류 | 깃허브에서 폴더명
--- | ---
upsteram | daitgirls/TWL
origin | yaein/TWL

* 로컬에 datatitgirls 폴더 생성
C://dataitgirls

* 로컬에 yaein/TWL 폴더 가져오기
```
$ git clone git@github.com:yaeinjung/TWL.git
```

* upstream 지정해주기
```
$ git remote add upstream git@github.com:dataitgirls2/TWL.git
```
* upstream 확인하기
```
$ git remote -v
origin  git@github.com:yaeinjung/TWL.git (fetch)
origin  git@github.com:yaeinjung/TWL.git (push)
upstream        git@github.com:dataitgirls2/TWL.git (fetch)
upstream        git@github.com:dataitgirls2/TWL.git (push)
```

* 로컬에 dataitgirls/TWL을 pull해오기
1. 로컬 _(C://dataitgirls/TWL)_ 에다가 upstream의 master에 있는걸 pull해옴
```
$ git pull --rebase upstream master
```
2. 로컬에 pull해온 것을 push해서 내 포크해온 리파지토리 _(yaein/TWL)_ 에 업데이트 해줌
```
$ git push -u origin master
```


* git pull이 안될때
```
$ git pull --rebase --autostash upstream master
```
* add할 파일이 여러개일때
```
$ git add .
```
