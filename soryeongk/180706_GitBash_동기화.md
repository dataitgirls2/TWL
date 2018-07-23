# GIt Bash

* git hub에 있는 repository를 clone해오기
  * $ git clone git@github.com:사용자명/repository.git
  * repository명의 폴더가 생성됨
* 생성된 폴더의 위치로 이동
* 원래 저장소(dataitgirls)의 upstream 을 지정
  * $ git remote add upstream git@github:원래저장소/repository.git
  * $ git remote -v를 통해 origin과 upstream을 확인할 수 있음
  * TIL과 같이 fork하지 않은 repository는 할 필요 없음
* 최신 상태를 로컬에 동기화
  * $ git pull --rebase upstream master
  * upstream의 master의 내용을 로컬로 pull
* 로컬의 내용을 사용자의 repository로 동기화
  * $ git push -u origin master
  * origin의 master로 내용을 push

# 시빅해킹

: 공공문제를 해결(정부의 역할)하거나 이야기(언론의 역할)하는 프로그램을 만드는 것

* 사건은 흔히 여러장소, 여러 시간대에 걸쳐 일어남
* 최소한 같은 사건끼리라도 묶어 볼 수 없을까?에서 시작한 것
* 같은 사건 == 같은 시간 && 같은 장소
* EXIF : 사진이나 영상 파일에 들어있는 메타정보
  * 카메라의 종류 설정, 사진을 찍은 시간과 위치
  * 
* Clustering : 컴퓨터가 데이터를 분석해서 비슷한 사건끼리 그룹화를 시키는 것
  * scikit-learn in Python
* 실시간으로 묶어볼 수도 있음
* 매년 3월 첫 토요일 Open Data Day
* 재밌는 커뮤니티 : Pyjog, Null채움 등
