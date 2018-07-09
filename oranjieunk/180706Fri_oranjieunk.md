commit 여러번 ▶ push

clear # 화면 초기화

ls -al
git commit --amend
w 저장, q 끝내기

git status #상태보기

git remote add origin 주소
git remote -v #설정 확인
vi .git/config
wq:

git push -u origin master #u : upstream

git에서는 vi로 편집하는 게 좋음
notepad에서는 원치않은 문자가 붙거나 글자가 깨지기도 함

git def로 수정사항 볼 수 있음

cd C:\\Dataitgirls

최신 상태로 유지하기
git fetch
git merge
git pull # git fetch + merge
git pull --rebase

git remote add upstream 주소
git pull --rebase upstream maser # 우리 계정에 있는 저장소로 데잇걸즈 저장소의 내용을 가져올 명령어

* git branch -m {기존 Branch 이름} {새로운 Branch 이름}업
* git branch -d {삭제할 Branch 이름}

cd 폴더명 : 하위폴더 이동
cd .. : 상위폴더 이동

로컬 저장소에 동기화 : git clone 주소

폴더 이동하기 : mv -rf 이전폴더경로 옮길폴더경로

<fork로 업데이트 실습>
git clone git@github.com:oranjieunk/tutorial.git
git remote add upstream git@github.com:dataitgirls2/tutorial.git
git remote set-url upstream git@github.com:dataitgirls2/tutorial.git
git pull --rebase upstream master

rebase : upstream 주소의 내용을 로컬로 가져옴

<로컬에 파일 새로 만들고, commit하기>
vi "README.md"
git add "180703Tue_oranjieunk.md"
git mv "180703Tue_oranjieunk.md" "180703Tue_oranjieunk.md"
git commit -m "파일 제목 바꾸기"
git push -u origin

https://www.slideshare.net/combineads/2018-4-next-104272149
멜론 셀프 서비스 분석 환경과 NEXT

http://smalldataguru.com/%EB%AF%B8%EA%B5%AD-%EC%9D%B8%ED%84%B4%EC%89%BD%EC%97%90%EC%84%9C-%EB%B0%B0%EC%9A%B4-%EB%8D%B0%EC%9D%B4%ED%84%B0-%EC%82%AC%EC%9D%B4%EC%96%B8%ED%8B%B0%EC%8A%A4%ED%8A%B8-%EB%8D%B0%EC%9D%B4%ED%84%B0/
미국 인턴쉽에서 배운 데이터 사이언티스트

동적 블로그 : 서버, 서버스크립트가 있는 것 