# 텍스트 앞/뒤로 빈줄을 제거
text.strip()
# \n와 \r을 공백으로 제거
text.replace('\n','').replace('\r','')

자주 쓰면 외워지므로 외우는 데에 부담 가지지 말자!
복,붙을 많이 하게 되는 경우 함수로 만들기(고수들은 1번 이상 복붙하면 함수 제작)
ToDo 리스트 만들기
실무에서 상당수의 플젝은 일정 지연, 리소스 부족, 요구사항 변경 등 다양한 이유로 인해 계획한 범위를 모두 구현하지 못하고 끝나곤 함, 
so 작업의 순서를 잘 세워서 중간에 멈추더라도 중요한 부분이 완료될 수 있도록 하고, 중간 결과를 자주 공유하느 것이 중요
구체적 질문에서부터 분석 시작하기
시간에 따른 차이도 비교하기 좋은 데이터
dom -> html 엘리먼트
데이터 클렌징에 전체 시간 80%가 소모
코드의 아름다움을 신경쓰는 사람들은 하나의 함수가 5줄이 넘지 않도록 제작
각 함수가 TMI하지 않게 필요한 부분만 수행하게 해서 다른 곳에서 재사용 가능케 함

<CSS>
엘리먼트 선택자: p → 태그 이름이 p인 엘리먼트
<p id="welcome">애란이네 책방에 오신 것을 환영합니다.</p>
<p class="highlight">마음껏 구경하세요.</p>

아이디 선택자: #welcome → id 속성이 welcome인 엘리먼트
<p id="welcome">애란이네 책방에 오신 것을 환영합니다.</p>

클래스 선택자: .highlight → class 속성이 highlight인 엘리먼트
<p class="highlight">마음껏 구경하세요.</p>
<li class="highlight">만화</li>


* 선택자의 조합
p.highlight → 태그 이름이 p이면서 class 속성이 highlight인 엘리먼트
<p class="highlight">마음껏 구경하세요.</p>

body .highlight → 태그 이름이 body인 엘리먼트의 자손(descendents) 중 class 속성이 highlight인 엘리먼트
<p class="highlight">마음껏 구경하세요.</p>
<li class="highlight">만화</li>

body > .highlight → 태그 이름이 body인 엘리먼트의 직계자식(immediate children) 중 class 속성이 highlight인 엘리먼트
<p class="highlight">마음껏 구경하세요.</p>



구글 검색은 자연어 처리가 안되어서 단어 따로 검색해도 됨