# 여태동안 한 Git 용어정리
* remote에 저장소를 등록해줌
* git push -u origin master
> origin에 있는 master 브랜치에 올리겠다.
> origin(yaeinjung/TWL)이 아니고 upstream이라면 내가 지정해준 upstream(dataitgirls/TWL)으로 됨
* commit메세지 수정하기는
```
$ git commit --amend
```
* git status -> 어떤게 스테이지 상태에 있는지 , 상태들을 볼 수 있음
* rebase
* 로컬에서 작업을 하다보면 file들이 많이 생김-> 이런 파일들까지 불필요하게 commit할 필요 없기 때문에 .gitignore에 그런 파일목록을 써줌 git add .을 했을때 그런 파일들을 지우고 해줌

## 터미널을 사용하는 이유?
* 보통 파이썬을 쓰게 되는데 큰 용량의 데이터를 다루다보면 로컬에서 안될때가 많음 그래서 AWS같은 서버에 들어가서 작업을 해야함. 근데 그 서버에는 소스트리가 없기 때문에 터미널 명령어가 필요하다.


# GitHub에 정적 블로그 만들기

* github 레파지토리에 내아이디.github.com 레파지토리 만들기
* settings에서 깃헙페이지 보기
* 도메인을 샀다면 커스텀도메인으로 특정 도메인설정 가능

## 루비
Ruby on Rails라는 웹 프레임워크 때문에 루비가 유명해졌음

## Jekyll을 이용해서 정적 블로그 만들기

* Jekyll 테마 포크해오기
* 포크해온 테마에 gh-pages 브랜치 생성
* Settings-Github pages에서 gh-pages 브랜치로 설정
* 내 깃헙블로그/포크해온레파지토리
* source tree로 내 깃허브 블로그 열기

# Kaggle
* 데이터 사이언스에 관한 특정 경진대회에 참여할 수 있다
* 파이썬 머신러닝때는 사이킥런이라는 accuracy 측정 도구를 주로 쓴다.
* 머신러닝이나 딥러닝같은 분야를 공부해 볼 수 있다. - 코드를 보고 공부가능
* Kernel로 잘 만들어진 데이터셋을 볼 수 있다.
* fork해서 내거에서 볼 수도 있음

* 일일커밋 할 게 없으면 kaggle을 따라해보면 할 게 정말 많다.

## Survey 2017
* 캐글을 쓰는 사람들이 어떤 사람들인지에 대한 인사이트를 얻을 수 있었음.
* conversion Rate -소득
* freeForm - 주관식데이터
* multiform - 객관식데이터
* NaN -> 결측치 (응답x)
* value_counts() 각 항목이 몇개 인지 세어줌

* edwith-> 데이터 교육?
