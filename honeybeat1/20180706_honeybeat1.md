
<h1 id="today-we-learned">Today We Learned</h1>
<h2 id="fri-dash">2018/07/06 fri 💨</h2>
<h3 id="git-최신-상태로-유지하기lemon">Git 최신 상태로 유지하기🍋</h3>
<p>다음의 순서에 따라 튜토리얼 폴더를 최신 상태로 유지한다.</p>
<p><strong>1. cd c://dataitgirls</strong></p>
<ul>
<li>디렉토리 c드라이브 복사위치로 정해주기</li>
</ul>
<p><strong>2. git clone <a href="mailto:git@github.com">git@github.com</a>:honeybeat1/tutorial.git</strong></p>
<ul>
<li>튜토리얼 (내 깃헙) 주소로 복제해준다.</li>
<li>Origin에서 my local PC로 복사하는 것</li>
</ul>
<p><strong>3. cd c://dataitgirls/tutorial</strong></p>
<ul>
<li>c 드라이브 복제된 tutorial 폴더로 디렉토리 수정해주기</li>
</ul>
<p><strong>4. git remote add upstream <a href="mailto:git@github.com">git@github.com</a>:dataitgirls2/tutorial.git</strong></p>
<ul>
<li>이번엔 복제할 게 있는 (update 상태 확인해야 하는) 원격 저장소를 upstream으로 추가(연결) 해주기</li>
</ul>
<p><strong>5. git remote -v</strong></p>
<ul>
<li>연결된 저장소 확인</li>
<li>origin은 내 계정 원격 저장소</li>
<li>upstream은 공동 계정 원격 저장소</li>
</ul>
<p><strong>6. git pull --rebase upstream master</strong></p>
<ul>
<li>rebase : 자동화, 동기화</li>
<li>소스 관리 매너</li>
<li>upstream 자동화 할 저장소</li>
<li>master 해당 branch 이름</li>
<li>로컬 pc와 원격 저장소가 자동화 된다</li>
</ul>
<p><strong>7. git push -u origin master</strong></p>
<ul>
<li>로컬pc에 있는 걸 origin(내 깃헙 계정) 으로 push 한다(동기화)</li>
</ul>
<p>만일 rebase 단계에서 에러가 생기면<br>
git pull --rebase --autostash upstream master<br>
git add.<br>
git commit -m 'add files’<br>
을 통해 에러 해결</p>
<h2 id="그-외-알아둬야-하는-명령어honey_pot">그 외 알아둬야 하는 명령어🍯</h2>
<ul>
<li>git mv 파일명 파일옮길주소(폴더)<br>
– ex) git mv <a href="http://README.md">README.md</a> honeybeat/</li>
<li>git mv 파일원래이름 파일바꿀이름</li>
<li>git mv -rf 이전폴더경로 옮길폴더경로<br>
– 폴더 안의 파일 전체 다 옮길 때</li>
<li>git cp 파일 복사</li>
<li>git fetch 가져오기</li>
<li>git merge 가져온 거 합치기</li>
<li>git pull = git fetch + git merge  한번에</li>
<li>git push -u origin 2018<br>
– 2018 브랜치로 push하기</li>
<li>vi <a href="http://README.md">README.md</a><br>
– 파일 편집기 열어서 수정하거나 생성 가능</li>
<li>:q 편집기 닫기 / :w 편집기 수정사항 저장</li>
<li>git status<br>
– 현재 상황</li>
<li>commit amend 파일 수정</li>
</ul>
<hr>
<p>SSH KEY</p>
<ul>
<li>Github과 통신할 수 있게, 접근 가능하게 하는 키</li>
<li>한번 등록하면 간편하게 사용할 수 있다</li>
</ul>

