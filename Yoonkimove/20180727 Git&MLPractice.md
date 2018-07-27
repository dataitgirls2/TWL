#### **Git 다시 정리!**

git stash  # 어딘가에 저장

git stash pop  # 저장해놓은 것 가져오기 (최근 것부터 가져옴)

한 번에 전부 저장/가져옴 ??



내 branch에 pull request를 보낼 수도 있음(upstream에만 보내는 것이 아님)



**커밋 메세지는 어떻게 작성하는 것이 좋을까?**

1. 제목과 본문을 빈 행으로 분리한다 (여러 줄로 쓸 수 있음)

2. 제목 행을 50자로 제한한다
3. 제목 행 첫 글자는 대문자로 쓴다
4. 제목 행 끝에 마침표를 넣지 않는다
5. 제목 행에 명령문을 사용한다
6. 본문을 72자 단위로 개행한다
7. 어떻게 보다는 무엇과 왜를 설명한다



영어로 정리하자!!!



#### **커밋 메시지 수정하기**

$ git commit --amend 

커밋 메시지를 여러개 수정하기(예제는 이전 3개의 메시지를 수정함) 

$ git rebase -i HEAD~3   # 여기서 rebase는 pull rebase와 다름

rebase 종료하기 

$ git rebase --continue 

suqash로 커밋 합치기 



Conflict 지울 때는 아래 것부터!



#### **Git-flow 브랜치 이해하기** 

 항상 유지되는 메인 브랜치들(master, develop)과
 일정 기간 동안만 유지되는 보조 브랜치들(feature, release, hotfix) 

 •master : 제품으로 출시될 수 있는 브랜치
 •develop : 다음 출시 버전을 개발하는 브랜치
 •feature -*: 기능을 개발하는 브랜치
 •release-* : 이번 출시 버전을 준비하는 브랜치 •hotfix-* : 출시 버전에서 발생한 버그를 수정 하는 브랜치 



#### **Pull Request 보내기** 

 \1. 보내기 전에 commit squash
 \2. 내 저장소로 먼저 push
 \3. GitHub 내 저장소 페이지에서 Pull request 4. PR에 빠진 내용이 없는지 확인
 \5. @리뷰어에게 멘션하기
 \6. 이슈번호 넣어주기
 \7. Pull Request 생성
 \8. 리뷰 받기
 \9. 머지하기 (오픈소스라면 메인테이너가 머지) 



#### **오픈소스로 배우는 협업**

성공한 프로젝트로부터 배우기

https://github.com/pandas-dev/pandas/wiki 





#### **이진 분류 Binary Classification** - 실습

두 가지로 분류하는 것(0/1)

ex) titanic kaggle



Cross-validation ?



