#### 2018.07.19. 데잇걸즈2 TWL : 크롤링#3, 기계학습 기초이론



- Crawling 과제 피드백

  - 구글 검색의 생활화

  - 함수 : 반복 작업의 제거

  - To-do List 만들기

  - 중간 결과물 공유하기

  - 프로젝트가 잘 망하는 방법 : 특정 기능이라도 사용 가능하도록 구현해야 함

  - 질문에서 시작하기

    

- 중간점검 : 나는 누구, 여기는 어디?

  - 문제 : 매번 웹사이트를 방문하여 데이터 수집하기가 귀찮음

  - 대안 : 파이썬 크롤러 만들기 but HTML의 나무 구조로 인해 정보 추출이 어려움

  - 대안 추가: html5lib.parse() but 나무 구조를 만들어도 여전히 정보 추출이 어려움

  - 대안 추가 : beautifulsoup

    

- CSS 선택자(Selector)

  - CSS (Cascading Style Sheets) 

    1. 마크업 언어의 표현 방식을 지정하는 언어
    2. 문서의 부분별 스타일을 정하는 형식 (Ex. [CSS Zen Garden](http://www.csszengarden.com/))
    3. 관심사의 분리 : 하나의 일만 맡아서 그 일을 아주 잘하기
    4. 장점 : 문서의 스타일 변경이 쉬움, 웹 크롤링을 쉽게 해줌

  - 엘리먼트, 아이디, 클래스

    1. 엘리먼트 선택자 : 이름
    2. 아이디 선택자 : #이름
    3. 클래스 선택자 : **.**이름 (이름 앞에 콤마가 있음)

  - 자식 vs. 자손

    1. 한 칸 비움 : 자손

    2. \> + 한 칸 비움 : 자식

       

- Plotnine 실습



- 한국어 구조 수업 (by 지영님) : [GitHub Markdown 자료 참조](https://github.com/jiyoung-choi/TIL/blob/master/%ED%95%9C%EA%B5%AD%EC%96%B4%20%EB%8B%A8%EC%9C%84.md)

  

  - 문장의 단위

    - 문단 : 글에서 여러 문장들이 모여 하나의 완결된 생각을 나타내는 단위
    - 문장 : 서술, 물음, 명령, 감탄 등의 형식을 통하여 하나의 완결된 뜻을 나타내는, 말과 글을 이루는 기본 단위.
    - 구절 : 구와 절을 아울러 이르는 것
      1. 구 : 둘 이상의 단어가 모여 문장의 일부분을 이루는 토막
      2. 절 : 주어와 술어를 갖췄으나 독립하여 쓰이지 못하고 다른 문장의 한 성분으로 쓰이는 단위
    - 어절 : 문장을 구성하고 있는 각각의 마디. 띄어쓰기 단위.

    

  - 한국어의 형태

    - 단어 : 일정한 뜻과 기능을 가지며 홀로 쓰일 수 있는 가장 작은 말의 단위.

    - 형태소 : 뜻을 가진 가장 작은 말의 단위.

      1. 자립 형태소 : 다른 형태소와 결합하지 않고 홀로 자립하여 쓰일 수 있는 형태소.
      2. 의존 형태소 : 자립 형태소와는 반대로 혼자서는 쓰일 수 없는 형태소.
      3. 실질 형태소 : 구체적인 대상이나 동작, 상태 등 실제 의미를 나타내는 형태소.
      4. 형식 형태소 : 문법적 의미가 있는 형태소. 어휘 형태소와 함께 쓰여 그들 사이의 관계를 나타냄.

      

  - 한국어의 소리 체계

    - 음절 : 모음, 자음이 어울려 한 덩이로 내는 말소리의 단위

    - 음운 : 말의 뜻을 구별하게 해 주는 소리의 가장 작은 단위.

    - 음소 : 말의 뜻을 구별 짓는 소리의 음운론 상의 최소 단위.

    - 운소 : 소리의 높낮이, 길이, 세기 등과 같이 단어의 뜻을 다르게 하는데 관여하는 소리의 단위.

      

  - 기타

    - 체언 : 문장에서 명사, 대명사, 수사와 같이 문장의 주어나 목적어 등의 기능을 하는 말
    - 복합 명사 : 명사 + 명사가 결합해 명사가 된 경우.  Ex. 녹색성장
    - 단일 명사 : 녹색 / 성장

    

- 한국어 자연어 처리를 위해 왜 soynlp를 사용하는가?

  - KoNLpy : Javascript 사용으로 인한 복잡한 설치 과정. 신조어에 대한 분석 능력이 약함.
  - soynlp : 파이썬만으로 개발 → 설치 과정이 간편함. 비지도학습 → 신조어 분석 능력이 개선됨.



- soynlp로 자연어 처리 시작하기 (실습) : 월요일에 계속할 예정
  - Tokenizer : 어절 단위로 띄어쓰기를 인식해서 Token을 만들고, Token을 Vector로 인식함.



- 과제
  - 개인별
    1. soynlp 실습 : 개인별 관심사 반영하여 워드클라우드 그린 후, 슬랙 실습 채널에 이미지 올리기
    2. TWL 올리기, 가드닝
  - 조별 : 튜토리얼 정리(E조), 10 minutes to pandas(D조)