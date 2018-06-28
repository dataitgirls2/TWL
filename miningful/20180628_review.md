# Today We learned about GitHub
## What is GitHub
### 일종의 저장소라고 볼 수 있다. 
### 오픈 프로젝트를 저장하고 공유하는데 유용한 것으로 알려져 있다.
### 작업 히스토리가 남아 수정된 사항이 무엇인지 확인하기 용이하고 피드백에 유용하다.
## How to make GitHub
### 1.Repository
#### 먼저 Repository 를 만든다. 이는 콘텐츠 저장 폴더의 개념과 비슷하다.
#### 생성된 Repository에 새로운 하위 폴더들을 만들고, 마크다운한다.
#### 마크다운이란? 편집의 의미와 동일하다고 보면 된다. ".md"라는 확장자 명으로 사용한다.
### 2.Pork
#### 타인의 GitHub 문서를 내 GitHub으로 가져와 내용을 수정 보완하고 편집하려 할 때, Pork를 이용한다.
#### Pork 하면 내 Repository 목록에 Pork 해온 Repository가 생성된다.
#### 내 Repository에 생성된 Pork 문서를 수정 보완한 후 Pull request 단계로 넘어간다.
### 3.Pull request
#### Pork 해와서 나의 Repository 내에서 수정한 파일 내용을 원조 GitHub에 또한 반영될 수 있도록 하기 위해서 Pull Request 가 필요하다.
#### 일종의 원격조정과 같이 내 작업환경에서 수정한 내용이 연동되어 다른 작업환경에 또한 동일하게 반영될 수 있도록 하는 과정이다.
### 4.Merge
#### Pull requset 를 보내면 관리자는 내용을 확인 한 후 업데이트 할 지 판단한다. 그리고 Merge를 통해 수정 내용을 병합시켜 Pull request를 받아들인다.
## Source Tree
### SSH key
#### 통신에 쓰이는 키 
#### 로컬에서 파일을 수정. 수정된 파일이 깃헙에 반영안돼있음.
#### 내 깃헙에 푸쉬해줘야되는데 SSH키를 통해 깃헙에 generate된 키를 내 로컬 SSH키로 저장해주면 따로 로그인안해줘도 푸쉬해줄 수 있음.
### What is Push?
#### GitHub과 GitHub 간의 파일 연동을 pull request 라고 한다면, 내 컴퓨터와 내 GitHub의 연동을 Push 라고 할 수 있다.
