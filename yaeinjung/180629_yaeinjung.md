#Today We Learned Git & Github
깃허브에 대해 배웠습니다..

 # Git 깃
* 이력을 관리하는 저장소. _(버전관리를 할 수 있는 것!)_
> 숙제_최종 / 숙제_최종_진짜 / 숙제_이게진짜최종

> -> 어떤 문서가 정말 최신이지?

* 어느 부분에서 충돌이 일어났는지, 누가 수정했는지 ... => 깃으로 해결할 수 있다

* 공동으로 작업할때 내 local에서 공용저장소에 올리거나, 다른사람이 올린것을 내 local로 가져오거나

* commit -> 작업한 것의 이력을 추가하는것 . 내가 언제 무엇을 수정 했는지, 어떤내용을 수정했는지 자세히 볼 수 있음
> commit을 하나로 만들어서 push 하고 싶을때는? option을 통해서 commit 메세지 수정 가능

1 | 2 | 3
-- | -- | --
git init | git add | git commit
폴더 초기화 | 스토리지에 올리기 | 컨펌

* `Pull Request`와  `Pull`의 차이점?
1. Pull Request 저장소에 내 꺼를 올리는 것
2. Pull 저장소에 있는걸 로컬로 가져오는 것


````
echo "# constitution-kr" >> README.md //README.md 파일에 constitution-kr을 씀
git init //깃 시작
git add README.md //README.md를 stage에 올림 
git commit -m "first commit" // firstcommit 으로 커밋
git remote add origin https://github.com/yaeinjung/constitution-kr.git //주소로 리모트를 지정해줌(여기로 올릴거다)
git push -u origin master //마스터에 업데이트함
````

