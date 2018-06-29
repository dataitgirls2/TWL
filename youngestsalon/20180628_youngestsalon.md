# 데잇걸즈 3일차 (2018.06.28.) TIL



### 서로 알아가기
- 자기소개 : 이그나이트 방식 활용 (1인당 PPT 슬라이드 5page, 1분)
- 네트워킹 질문 : 좋아하는 음식, 야구, 거주지 등
- 향후 다루고 싶은 데이터 : IoT를 위한 전력/가스 소비량, 교과서 속의 여성 묘사, 상권 분석 등



## GitHub & Markdown

### Introduction

1. 왜 GitHub을 사용하는가?
- 개발자 간의 협업 시 version 관리
- 개발자 각자의 커리어 관리

2. 어떻게 GitHub을 사용하는가?
- 공동 Repository(이하 'Repo') : 프로젝트 단위의 협업용 Tool
- 개인 Repo : 커리어 관리를 위한 일일 Commit(이하 '커밋')

3. 왜 일일 커밋을 하는가?
- 백문이 불여일타, Done is better than perfect
- 'Today I Learned' (그날 배운 것 : 이하 'TIL') 정리
- 오류를 경험하고, 오류를 통해 배운다.

4. 어떻게 일일 커밋을 할까? (= 무엇을 하면 좋을까?)
- 다른 사람의 저장소 따라하기
- Stack Overflow에서 배운 코드를 타이핑 (주의 : Ctrl C+V 하면 안됨)
    * Stack Overflow : 개발자들의 지식iN. https://stackoverflow.com/
- Kaggle에 있는 튜토리얼 따라하기
    * Kaggle (캐글) : 데이터 사이언티스트들의 지식iN 겸 경진대회장. https://www.kaggle.com/
- 책에서 본 코드를 따라 써보기
    * 각 IT출판사(길벗, 한빛미디어 등)의 베타리더, 리뷰어 모집에 응모해서 당첨된 책의 소스 리뷰하며 따라쓰기
    * 추가 의견(by 이은지) : 저의 경우, 코딩 관련 도서는 한빛미디어 책을 많이 보게 되는 것 같습니다.
- 간단한 튜토리얼 번역해보기 (ex. 장고걸스 튜토리얼)
- 스프린트 참여하기
    * 스프린트 : 오픈소스 발전에 기여하기 위해 현재 이슈 해결에 참여하는 것. 파이썬 한국 사용자 모임에서도 진행함.
- 정적 블로그 운영 
    * 정적 블로그 : '~.github.io' 주소로 되어있는 블로그. 입문자용 튜토리얼을 참고하거나, 잘 만들어진 테마를 Fork해서 만들 수 있음.
- (Cheating 주의) 마크다운 문서 편집 : PC 브라우저/휴대전화로도 가능하므로 일일 커밋이 끊기지 않게 할 수 있음


### GitHub 사용법 : 개인 단위 사용 기준

- Step 1. GitHub 가입  (+ Tip : 향후 취업시 활용을 생각하면 깔끔한 프로필 사진을 업로드 요망)
- Step 2. Repository 생성
- Step 3. 데이터 업로드/수정/편집 등등 (@ 브라우저 상의 GitHub 개인 Repo)
- Step 4. (Local PC, 즉 개인 컴퓨터 상에서 수정하려는 경우) Sourcetree 설치 -> Pull -> Add -> Commit -> Push 필요 (하단 참조)


### GitHub 사용법 실습 : 협업용 그룹 단위 사용, Local PC 편집 기준

![20180628_GitHub_구조도](https://github.com/YoungestSalon/TIL/blob/master/TIL_20180628_GitHub_v2.jpg?raw=true)

- Step 1. GitHub 가입 @ 브라우저 GitHub 페이지
- Step 2. GitHub 내 Organization 생성 및 그룹 구성원 초대 @ 브라우저 GitHub 페이지
    * 데잇걸즈2 Organization : https://github.com/dataitgirls2)
- Step 3. Organization 내 그룹 단위 Repository 생성 @ 브라우저 GitHub 페이지
    * 데잇걸즈 2 TWL : https://github.com/dataitgirls2/TWL
- Step 4. 그룹 Repo를 개인 GitHub로 Fork @ 브라우저 GitHub 페이지
    * youngestsalon TWL : https://github.com/YoungestSalon/TWL)
    * Fork : 그룹 Repo를 개인 GitHub로 복사(복제?)해오는 행위
- Step 5. Sourcetree 설치 (* Sourcetree 설치파일 다운로드 : https://www.sourcetreeapp.com/)
    * Sourcetree : GitHub Repo의 사본을 Local PC에 저장하여 편집할 수 있게 하는 프로그램
    * 설치 시 Git을 함께 설치해야 하며, SSH는 설정하지 않아도 무방
    * MAC PC의 경우 설치 후 SSH 설정하였으며, Windows PC의 경우 SSH 설정 생략함
    * SSH : Web 환경 내 Server - User간 통신 시 보안 검증을 위한 기술 장치로, 공인인증서와 유사함.
    * SSH는 컴퓨터가 임의의 숫자열을 생성하는 것이기 때문에, 생성작업할 때 마우스를 흔들어주면 random에 도움을 줘서 작업이 빨라짐(...)
- Step 6. GitHub Server 상의 개인 Repo를 Local PC로 Clone @ Sourcetree 프로그램
- Step 7. 소스 코드 편집 작업 (추가, 수정, 삭제 등등)
- Step 8. 편집을 완료한 소스코드에 대해 Add 처리
    * Local PC 상의 Repo는 Untracked, Intracked & Staged, Intracked & Unstaged의 세 가지 상태로 나뉨
    * Untracked : 소스 코드를 편집한 직후의 상태
    * Intracked & Staged : Untracked의 코드를 Add 처리하면 이 상태가 됨. (= Commit이 가능한 상태가 됨)
    * Intracked & Unstaged : 편집을 완료한 코드를 Add 처리한 후 수정하면 Unstaged로 변경되며, 수정 완료 후 다시 Add하면 Staged로 다시 변경.
    * 즉, Add의 기능은 두 가지 : Untracked -> Intracked, Unstaged -> Staged
- Step 9. Add 처리를 완료한 코드에 대한 Commit 처리 (= 작업 완료 선언. GitHub Web Server 개인 Repo로 Push할 수 있도록 대기 시킴)
- Step 10. Push 처리 (= Local PC 상의 Commit 완료된 코드가 GitHub Web Server상의 개인 Repo로 저장됨)
- Step 11. Pull Request 처리
    * Pull Request : 개인 Repo에 저장된 코드를 그룹 Organization 내 Repo에 반영하도록 요청하는 절차. 흔히 줄여서 '풀리퀘'라 하는듯.
- Step 12. Merge 처리
    * Merge : Pull Request에 대하여 Organization Repo로의 반영을 승인하는 작업. Oranization 상의 별도 권한이 부여된 경우에만 가능.
    * Pull Request된 코드가 바로 Organization Repo에 반영되는 것은 아님. Merge되지 않으면 reject인 셈.
    * 참고로, 데잇걸즈2 교육생 32인의 경우 모두 Organization Repo에 대한 Merge 권한을 가지고 있습니다.


### GitHub 사용법 : 기타
- Markdown 문서 생성 @ 브라우저 GitHub 페이지 : 문서 생성 시 '~.md'로 확장자 설정을 해야 함  (Ex. README.md)
- Issues 폴더 생성 @ 브라우저 GitHub 페이지 데잇걸즈2 Repo
- 그룹 Organization 내 Issue를 생성한 후 Pull Requests Tab 내 Comment를 작성하면서 사용할 수 있는 Tip
    1. Comment 작성 Editor의 우측 상단 아이콘 중 오른쪽에서 네 번째(줄 3개 왼쪽에 체크 표시) 선택 : 체크박스 목록 생성 기능
    2. ':'(Clone)을 입력하면 이모티콘(이모지)를 선택할 수 있음
    3. 앞서 생성한 Issues 폴더의 링크 주소를 입력하면 Issue 번호가 출력됨.
    
    
    
### 기타 운영 관련 공지
- 내일 교육 내용 : (오전) 통계 수업 by 지현님 / (오후) GitHub & Sourcetree & Markdown 계속 (+ 10 mins to Pandas?) by 배로님
- 오늘 숙제 : 금일 교육 만족도(?) 설문 조사 @Google Docs (Slack 참조), TWL Pull Requests & Merge, 이력서/자소서/롤러코스터 3종 세트 제출
- 명찰 : 교육 완료 시(10/6) 반납해야 함
- 아침/저녁 : 교육장 책상 원복 및 정리를 다 함께 도우면 좋겠습니다 (by 영웅님)
- 칭찬 포스트잇 : 하루 1개, 내일부터는 전지가 벽면에 셋팅될 예정



- 강의 준비/진행에 힘써 주신 배로님, 프로그램 준비에 애써주신 데잇걸즈2 관계자 여러분께 모두 감사드립니다.
- GitHub 익히느라 동기 여러분 모두 고생 많으셨습니다.

- 자기소개 때 보여드렸던 브런치 '데이터 과학의 도구들' 글 주소 : https://brunch.co.kr/@youngestsalon/53
- 혹시, 저하고 같이 점심에 도시락 싸오시거나 배달시켜 드실 분 계시다면 Slack으로 Direct Message 부탁 드립니다. :) 

