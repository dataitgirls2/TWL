# 180628
## 스스로에게 동기부여하기

Today I Learned/Today We Learned
1. 따라하기(마크다운부터 시작)
2. 스택오버플로우 링크, 코딩, 타이핑, 설명>오류경험을 통해 배우기
3. 튜토리억 확인 (10 minutes for pandas)
4. 책에서 본 코드를 따라 써 보기
5. 튜토리얼 번역해보기
6. 스프린트 참여: 파이썬, 장고, 판다스 패키지들과 관련 이슈를 해결하여 오픈소스에 기여.
7. 정적 블로그 운영: github으로 정적 블로그 만들기(Jekyll)

## github 이용하기
**ssh key** : 소스트리 사용 시 최초 1회  
한 번 설정 해 두면 github으로 따로 로그인 등이 필요하지 않음.


__github__: 개인 git들을 이어줌

git 레퍼지토리(로컬 폴더)  
- untracked영역>__add__>tracked영역(ver관리 가능)  
* tracked는 두 가지로 나뉨  
staged(영구 저장될 준비가 됨, 디폴트) / unstaged(수정을 위해 잠시 불러옴)

- unstaged>__add__>staged(숨김/표시 느낌)

- staged파일>__커밋__(영구저장) 하면 ver1으로 업데이트되고, 내 staged되어 있는 것이 ver2가 됨.  
- __clone__: 내역들까지 모두 복사, 버전을 바꿔도 업뎃 안 됨

내가 __clone__ 한 것을 땡겨서 가져가!: __pull request__  
너가 가져 간 것을 반영시켜조: __merge__

\<github 용어>  
github>__fork__>다른 github으로 보냄 >수정 후 __pullrequest__> 승인한다고 하면 __merge__
