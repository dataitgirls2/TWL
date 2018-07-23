# 180706_8일차 - 배로쌤 


## 지난시간 복습

### 1. Add? commit? Push?

untracked -> tracked 하려면

git add 대한민국.txt : add를 보면 tracked상태로 올려놀 수 있음 

commit : 임시저장,,

push ; 원격에 올리기 

git commit :  임시저장하면서 기록을 남기는 것이기 때문에 이런걸 한다. 



### 2. git bash 를 통해 간단한 명령어를 사용해 볼 수 있습니다.

- mkdir 폴더명  : 해당경로명에 폴더 날리기 

- rm :  삭제한다. 
- rm -rf / : 컴퓨터에 있는 파일 모두 날리겠다는 뜻이다. (복구 불가능하니 절대 주의)
- rm - rf tutorial  은  튜토리얼 폴더 날리기 

- git push -u

  -u : upstream

  -f : force (puch가 안됄 때 강제로 push)

  f는 이미 푸시했는데 커밋메시지를 수정하거나 할때 아니면 특정 상태로 돌아가고 싶을때 

  머지되었을때 다시 이전으로 돌리고 다시 푸시하고 싶으면 사용함

- git config --list : 이름과 이메일 설정 볼 수 있음 

- w : 저장
- q : 닫기
- wq : 저장 후 닫기

- mv : 파일이동 

  mv ~/data/TWL/ .     ( 마침표 하면 해당주소로 그 파일을 옮긴다는 뜻임 )

- cp : 파일복사

- git init : 앞으로 해당 파일을 git 으로 관리하겠다.

- git remote -v :  현재 설정되어 있는 원격저장소 보기

- ls : 목록을 보여줍니다.

- ls -al : 숨김파일까지 전체 파일 목록을 볼 수 있음 (id_rsa파일자체가 숨김파일)

- ls -al ~/.ssh : ssh폴더가 있는지 확인하고 해당 폴더에 id_rsa.pub 파일이 있는지 확인합니다.

  해당 키가 등록되어 있는지 GitHub에 가서 확인합니다. 

  

### 3. SSH 프로토콜을 사용해 GitHub 즐기기

**clone or download**

''클론''해오면 내 로컬에서도 볼 수 있다. ssh키로 통신을 하려면 깃으로 시작하는 경로를 가져오면 

ssh키를 통해 깃헙에 접근 할 수 있습니다. 

 

## git branch

왜 굳이 branch 를 만드느냐?

현업에서 이슈번호로  branch를 만들면 이  branch는 어떤 업무에 대한 것이구나. 이것을 파악하기가 쉽습니다. 

**git branch브랜치를 사용하는 이유**

예를 들어 서비스는 계속 운영해야하는데 새로운 피처도 넣어야 하고 그 와중에 보안 이슈가 있다. 이럴 때 개발하던 피처를 보안패치 하는데 같이 넣어 완성되지 않은 피처를 라이브 서비스에 내보내면 더 큰 문제가 될 수도 있을거에요.예를 들어 게임 서버에 보안 이슈가 있어서 아이템이 계속 털리고 있다고 가정합니다.이 때 재빠르게 보안 패치가 필요할거에요. 그런데 한쪽에서 신규 퀘스트를 개발하고 있었어요. 아직 개발은 완성되지 않은 상태인데 이 퀘스트가 완성되지 않은 채로 보안 패치와 같이 나가야 한다면?신규 퀘스트 작업하던 것을 다 삭제하고 보안패치만 할 수도 없겠죠. 이럴 때 브랜치를 사용해요.

**Q : 마스터 브랜치는 항상 최신버전으로 땡겨와서 거기서부터 브랜치를 나눠준다.** 

**만약 에전꺼를 그대로 쓰고 있으면 충돌이 발생한다.** 



## 브랜치 만들기

6월 29일차 참고해서 브랜치 만들기 

해당 constitiution 으로 경로 이동하고 

git checkout -b 2018 

2018브런치로 스위치 되었다. 

git branch해서 보면 2018 branch 가 생긴다.

/Users/jieun/Downloads : 나의 경로주소 

mv ~/Downlodads/대한민국\헌법.txt .

ls -al 해서 보면 파일이 달라진 것을 알 수 있다. 용량도 달라진것을 볼 수 있다. 

git diff : 하면 달라진 내용을 볼 수 있다.=> 소스트리를 사용하면 변경된 내용을 더 편하게 볼 수 있다. 

git add 대한민국\헌법.txt

git status : 스테이지 상태에 올라와있는지 보기 

git commit -m '2018개정안' 

git  branch

git push -u origin origin 2018 

2018 브랜치로 푸시해주기 

그러면 2018 브랜치가 생김 

브랜치를 풀리퀘 생성하면  (2018 => 마스터) 브랜치로 풀리퀘 해서 보면 바뀐내용을 쓉게 볼 수 있습니다. 

머지하면 마스터브랜치에 반영되고, 머지하면 마스터에 2018 헌법으로 나온다. 



## git 최신 상태로 유지하기

1. 데잇걸즈 tutorial fork 해오기  (이미 했으면 생략)

2. (forked해왔던) 지은 tutorlal 에서 클론주소 복사

3. git clone 주소

4. 3번을 하면 자동으로 데잇걸즈폴더안에 튜토리얼 폴더가 만들어짐

5. cd ~/dataitgirls/tutorial  쓰고 이동하기

6.  git remote -v 해서 원격 저장소 제대로 생성되었는지 확인하기 

7. 데잇걸즈 tutorial 에서 클론주소 복사하기

8. upstream 원격 저장소 추가하기 

   git remote add upstream 클론주소  : 

9. git remote -v  해서 master말고 upstream 이 잘 추가되었는지 보기 

10. git pull --rebase upstream master  해서 upstream에 있는 master로 pull해오기

​     ( 업스트림에 설정된 데잇걸즈의 마스터를 가져오겠다. 우리 계정에 있는 저장소로 데잇걸즈 저장소의 내용을 가져올 명령어임 git pull --reavase 하려면 모든 파일이 staged에 올라가 있어야 합니다. )

11. 아직 내 깃허브에 저장소에는 반영이 안되어있다! 

    git push origin master  해서 나의 origin에다가 push해줘야 내 저장소에 동기화되어 바로 볼 수있다.



## git bash통해 폴더 만들기, 파일 옮기기 (for Mac)

C 에 데잇걸즈 폴더만들고 깃으로 만든것을 그쪽으로 옮겨줄게요. 

cd ~/ 여기로 이동해서

mkdir dataitgirls : 폴더만들고

cd dataitgirls/

mv ~/data/TWL/ .     ( 마침표 하면 해당주소로 그 파일을 옮긴다는 뜻임 )

Cd TWL 

git config --list

Mv ~ data/tutirial/ .

Tutoirial, TWL, TIL , TUTORIAL파일로 옮겨서 실습합시다. 



## 질문 : mv 사용하는 방법은?

mv(뛰어쓰기)이동전할파일(뛰어쓰기)이동후경로



이동후 경로가 현재 경로인 경우에는 점(.)을 써줍니다.

mv ~/Downloads/대한민국\ 헌법.txt .

\ 역슬래시 쓰는 이유 : 대한민국 헌법이 띄어쓰기가 되어있으므로 띄어쓴부분을 문자로 인식하라고 넣어줌




-----



## 김슬님 특강 - 데이터분석으로 세상을 바꿀 수 있을까요? 

(Q&A : sl@dotface.kr)

" 항상 자신이 틀릴 수도 있다는 생각으로 오픈소스로 공개해서 사람들에게 체크를 받는것이 중요하다고 생각합니다. "

### Civic Hacking(시빅해킹) 이란 ?

공공문제를 해결하는 프로그램을 만들거나

공공문제를 이야기하는 프로그램을 만드는것



https://ko.wikipedia.org/wiki/%EC%8B%9C%EB%B9%85_%ED%95%B4%ED%82%B9

시빅 해킹은 보통 개발자가 중심이 되어 정부 데이터를 시각화하거나 시민의 삶을 편하게 만들어 주는 서비스 개발을 목표로 하지만 시빅 해커는 도시와 공동체의 문제를 해결하고자 하는 사람이라면 디자이너, 데이터 과학자, 시민운동가, 기업가, 정부 직원 모두가 될 수 있다. 시빅 해커는 [코드포아메리카](https://en.wikipedia.org/wiki/Code_for_America)(CodeForAmerica)와 같은 [비정부기구](https://ko.wikipedia.org/wiki/%EB%B9%84%EC%A0%95%EB%B6%80%EA%B8%B0%EA%B5%AC)에서 일하거나 [Azavea](http://www.azavea.com/)와 같은 공간정보 기반 영리조직에서 일하기도 하고 취미로 시빅해킹을 하기도 한다. [[6\]](https://ko.wikipedia.org/wiki/%EC%8B%9C%EB%B9%85_%ED%95%B4%ED%82%B9#cite_note-openbook-6) [해커톤](https://ko.wikipedia.org/wiki/%ED%95%B4%EC%BB%A4%ED%86%A4)을 통하여 아이디어를 빠르게 기획하고 이후 지속적으로 서비스를 유지해 나가기도 한다.

- [프로그래머](https://ko.wikipedia.org/wiki/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8): 시빅해킹은 기술적 솔루션을 기반으로 공공의 문제를 해결하고자 하므로 프로그래머의 서비스 개발이 중요하다.
- [디자이너](https://ko.wikipedia.org/wiki/%EB%94%94%EC%9E%90%EC%9D%B4%EB%84%88): UX를 통하여 정부 2.0 운동을 촉진시키고 보다 편리한 서비스를 시민에게 제공할 수 있다.[[7\]](https://ko.wikipedia.org/wiki/%EC%8B%9C%EB%B9%85_%ED%95%B4%ED%82%B9#cite_note-7)
- [시민](https://ko.wikipedia.org/wiki/%EC%8B%9C%EB%AF%BC): 시빅해킹은 시민에 의한, 시민을 위한 서비스이다. 시민이 제공하는 데이터는 시빅 해킹 서비스의 기반이 된다. [#메르스 확산지도](https://ko.wikipedia.org/wiki/%EC%8B%9C%EB%B9%85_%ED%95%B4%ED%82%B9#%EB%A9%94%EB%A5%B4%EC%8A%A4_%ED%99%95%EC%82%B0%EC%A7%80%EB%8F%84) 등 미리 정의된 공공 데이터 자료를 이용하지 않는 서비스는 시민의 자발적 참여를 통한 데이터 개선이 필수적이다. 또 [#소화전 입양하기](https://ko.wikipedia.org/wiki/%EC%8B%9C%EB%B9%85_%ED%95%B4%ED%82%B9#%EC%86%8C%ED%99%94%EC%A0%84_%EC%9E%85%EC%96%91%ED%95%98%EA%B8%B0) 등 실제 행동을 촉발하기 위한 시빅 해킹 프로젝트의 경우 시민의 실제 참여로 이어지는 것이 중요하다.



## 한국 사례[[편집](https://ko.wikipedia.org/w/index.php?title=%EC%8B%9C%EB%B9%85_%ED%95%B4%ED%82%B9&action=edit&section=9)]

- [메르스 확산지도](https://www.facebook.com/mersmap/): 언론보도와 정부 공식 발표를 참고하여 메르스 발병 상황 및 발병 환자 수용 병원 현황을 직접 지도에 표시해주는 서비스이다. [2015년 대한민국 중동호흡기증후군 유행](https://ko.wikipedia.org/wiki/2015%EB%85%84_%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD_%EC%A4%91%EB%8F%99%ED%98%B8%ED%9D%A1%EA%B8%B0%EC%A6%9D%ED%9B%84%EA%B5%B0_%EC%9C%A0%ED%96%89) 당시 정부가 메르스 발병 병원 정보를 투명하게 알리고 있지 않다는 의혹에서 시작하여 한 시민이 직접 제작하여 운영하였다. [마리아DB](https://ko.wikipedia.org/wiki/%EB%A7%88%EB%A6%AC%EC%95%84DB), 시나트라, 앵귤라JS, 유니콘, [엔진엑스](https://ko.wikipedia.org/wiki/%EC%97%94%EC%A7%84%EC%97%91%EC%8A%A4)의 기술을 사용하여 구축했다. 페이스북과 [구글 지도](https://ko.wikipedia.org/wiki/%EA%B5%AC%EA%B8%80_%EC%A7%80%EB%8F%84)의 [공개API](https://ko.wikipedia.org/wiki/%EA%B3%B5%EA%B0%9CAPI) 또한 사용했다. 제보는 정부 데이터가 아닌 민간 제보를 활용했으며, 개발자가 직접 메일 또는 제보를 받은 뒤 루머 신고 5회 이상이 접수되면 삭제하도록 만들었다. [[17\]](https://ko.wikipedia.org/wiki/%EC%8B%9C%EB%B9%85_%ED%95%B4%ED%82%B9#cite_note-mersmap-17) 6월 10일 자정을 기준으로 서비스가 종료된 상태이다.

- [고위공직자 재산 공개](http://jaesan.newstapa.org/): 고위공직자들의 공시 재산 데이터를 재가공하여 재산 형성 과정, 현재 공시 재산 등을 확인할 수 있는 사이트이다. [#코드나무](https://ko.wikipedia.org/wiki/%EC%8B%9C%EB%B9%85_%ED%95%B4%ED%82%B9#%EC%BD%94%EB%93%9C%EB%82%98%EB%AC%B4)가 뉴스타파와 함께 제작했다. 대한민국 전자 관보에 업로드된 자료를 활용하여 고위공직자의 재산형성과정을 공개하였다. [[18\]](https://ko.wikipedia.org/wiki/%EC%8B%9C%EB%B9%85_%ED%95%B4%ED%82%B9#cite_note-gongjikja-18)

- [지켜보고 있다 대한민국 재정 프로젝트](http://transparency.codenamu.org/): 국가 재정의 투명성을 높이기 위한 민-관 협력 프로젝트이다. 공개된 정부의 재정 정보를 가공하여 어려운 재정 정보의 이해를 돕거나 재정 데이터를 보다 쉽게 활용할 수 있도록 데이터(row data) 아카이빙, 데이터 분석, 시각화 등을 진행한다. 결과로 [재정자립도 시각화 프로젝트](http://codeforseoul.org/LocalGovIndex/), [우리 지역 채무 탈출](http://getoutofdebt.kr/), [Shoveling](https://showveling-codeforseoul.appspot.com/) 등을 만들었다.[[19\]](https://ko.wikipedia.org/wiki/%EC%8B%9C%EB%B9%85_%ED%95%B4%ED%82%B9#cite_note-transparencyKoreaExample-19)

- [대한민국 지도 데이터형 변환](https://github.com/southkorea/southkorea-maps): 행정동을 기반으로 한 대한민국 지도를 GeoJSON([GeoServer](https://ko.wikipedia.org/wiki/GeoServer)), TopoJSON 등 다양한 형태로 변환하여 사용하기 쉽게 만들었다. [깃허브](https://ko.wikipedia.org/wiki/%EA%B9%83%ED%97%88%EB%B8%8C)에서 해당 프로젝트를 다운로드 받으면 용도에 따라 다양하게 행정동 별로 데이터 시각화 방식을 바꿀 수 있다. [#팀포퐁](https://ko.wikipedia.org/wiki/%EC%8B%9C%EB%B9%85_%ED%95%B4%ED%82%B9#%ED%8C%80%ED%8F%AC%ED%90%81)이 제작하였다.

- [대한민국 정치의 모든 것](http://pokr.kr/): 정치인, 의안 정보, 회의록, 정당 정보를 손쉽게 탐색할 수 있는 사이트다. '정치인' 탭에서는 의원 별로 기본정보, 입법활동 내역, 발언 내역, 검색추이 등을 확인할 수 있다. '의안' 탭에서는 새로 발의된 의안 및 수정내역을 확인할 수 있다. '회의' 탭은 국회 회의 일정을 알려준다. '정당' 탭에서는 1대부터 18대 국회까지 참여 정당을 실었으며 각 정당 별 의원을 확인할 수 있다. '지역' 탭에서는 지역별 출마자와 거주 의원을 볼 수 있다. [#팀포퐁](https://ko.wikipedia.org/wiki/%EC%8B%9C%EB%B9%85_%ED%95%B4%ED%82%B9#%ED%8C%80%ED%8F%AC%ED%90%81)이 제작하였다.

- [안심이](http://ansim.me/): 옛 안심병원이 이름을 바꾼 서비스로 항생제처방률, 주사제처방률 별로 병원 별 등급을 매겨 제공한다. 2012년 공공데이터캠프에서 구상되어 지금에 이르고 있다.

- [서울버스앱](https://play.google.com/store/apps/details?id=com.soothe0828.seoulbus&hl=ko): 서울시 및 수도권 버스 도착 정보를 알려주는 모바일 애플리케이션이다. 교통 관련 앱이 많던 2009년 공익성을 가지고 출시되어 큰 인기를 끌었다. [서울시 교통정보과](http://api.bus.go.kr/) [공개API](https://ko.wikipedia.org/wiki/%EA%B3%B5%EA%B0%9CAPI) 를 활용하여 제작하였다. 현재 [다음](https://ko.wikipedia.org/wiki/%EB%8B%A4%EC%9D%8C)에 인수된 상태이다. [[20\]](https://ko.wikipedia.org/wiki/%EC%8B%9C%EB%B9%85_%ED%95%B4%ED%82%B9#cite_note-20)

### 행사[[편집](https://ko.wikipedia.org/w/index.php?title=%EC%8B%9C%EB%B9%85_%ED%95%B4%ED%82%B9&action=edit&section=11)]

- [아트센터 나비 시빅 해커톤](http://nabihackathon-civichacking.com/): 도시 블랙아웃([정전](https://ko.wikipedia.org/wiki/%EC%A0%95%EC%A0%84))이 되었을 때 어떻게 대처해야 할지 방안을 고민한 시빅 해커톤으로 아트센터 나비가 주관하였다. 도시의 대정전사태를 대비하거나 정전사태에서 생존할 수 잇는 도구를 만드는 것을 목적으로 2016년 4월 진행되었다.



----



- EXIF : 사진이나 영상 파일에 들어있는 다양한 메타 정보
- clustreing , skit-learn 대표적인 머신러닝 라이브러리 

-  DBSCAN 이라는 알고리즘 사용하여 파리테러 같은시간, 장소 클로스터링함..
- Twitter streaming API 사용



그러나 국회기록.. 이미지파일로 올라옴..

- 이걸 [참여연대 열려라 국회] 가면 이미지데이터프를 텍스트 데이터로 옮겨놔주심...

- 파이썬에서 그래프 분석시에는 '' network X '' 를 사용함
- IRT :  설문응답을 분석하는것
- MCMC : 엄청반복해서 아웃풋이 나올만한 인풋이 뭔지 찾아냄. 인풋을바꿔가면서..아웃풋이 나올만한 인풋을 찾아낸다 

- 중앙선거여론조사심위위원회 : 여론조사기관이 여론조사시 여기에 다 기록하게 되어있음이것과 실제득표하고 함께 해보면 어떨까?



- 신호와소음 : http://book.daum.net/detail/book.do?bookid=KOR9788966187584

데이터 분석가들이 꼭 봐야하는 책이라고 생각하심 



마국에서 여론조사 오차비교해서 여런기관의 신뢰도를 매김 여론조사 방법 자체가 가지는 한계 감안 해야 함 ..

오래전에,  인구가 적은곳을 예측할 수록 틀릴 가능성이 높다. 

맞추기 쉬운곳들만 해서 한 업체들이 주로 상위에 랭크되어있으니까 믿지 마세요.



- 정보공개청구  제도 : 공공기관이 가지고 있는 정보를 국민에게 공개하도록 하는 제도.

- 아무나 신청하면 받아보실 수 있습니다. 

- 정부공개 청구 포털 open.go.kr 가면 이런식으로 신청가능

- 기관장 영업활동비 사용내역과 지출영수증 사본..

- 정보공개 청구대장 : 기관에 청구대장을 신청해서 그걸보고 '문서명'을 파악해서 문서를 신청 할 수 있습니다. 

- 시민단체중에 '정보공개센터' 라는 단체에 가서 정보공개센터를 통해 이슈를 해결하는 시민단체인데 

  만약 기관에서 정보를 안준다고 하면 여기에 도와달라고 하면 도와주세요.

  문제는 데이터가 이미지파일이라..open data day 에 모여서 친다..

- open data day :  전세계 3월 첫재주에 함 open data가지고 뭔가 하는날..

- 깃헙에서 '존맛국회' 치면 나옴 '차이나프로' , ''참복집' 등… : ' https://github.com/codeforseoul/jonmat

- How we analyzed the compas recidivism algorithm : 모두 공개되어 있다. / 미국 프로그램은 흑인에게 판결을 불리하게 내린다는 것을 밝히고 모든 분석과정을 공개함

- Open source = 협력 !! / 무료로 가져다써라는 말이 아니라. 협력을 함께 하자!
- Stereotype threat : 잘못된 데이터 분석이 가져올 수 있는 무서운 결과, 혈액형 미신과 같음..



신호와 소음 : 불확실한 시대, 예측은 어떻게 가능한가?『신호와 소음』은 2012년 치러진 미국 대통령 선거 결과를 정확하게 예측한 통계학자 네이트 실버가 자신의 통계학과 예측 철학을 담아낸 책이다. 통계학을 기반으로 어떻게 잘못된 정보(소음)을 거르고 진짜 의미 있는 정보(신호)를 찾을 것인지에 대해 다룬다. 정치, 경제, 스포츠, 기후, 전쟁, 테러, 전염병, 도박 등 다양한 분야에 걸쳐 ‘미래’를 제대로 예측하는 방법에 대해서 설명한다.책은 크게 두 부분으로 나뉘는데, 1부와 2부에서는 예측 문제를 진단하고, 3부와 4부에서는 베이즈주의적 해법을 적용하고 탐구한다. 각 장은 특정한 주제를 깊이 있게 다룬다. 특히 사전 확률을 도출한 뒤 새 정보가 나오면 가장 가능성 있는 것을 골라 사후 확률을 개선해 나가는 ‘베이즈 ...



**Q : 어떤 데이터를 분석할 지 감은 어떻게 잡으시나요?**

A : 가디언, 538 등등 데이터 분석을 잘하는 해외의 기사를 읽다가 한국버전으로  빠르게 적용할 수있다. 

https://projects.fivethirtyeight.com/pollster-ratings/



널채움 커뮤니티 : https://nullfull.github.io 깃허브 놀러오세용

PYJOG : http://blog.weirdx.io/

- 책추천 

1) 통계학의 피카소는 누구인가 

http://www.kyobobook.co.kr/product/detailViewKor.laf?barcode=9788973388547

2) 어쩌다 보니 통계학자 - 통계학의 거장 조지 박스의 삶과 추억

http://www.aladin.co.kr/shop/wproduct.aspx?ItemId=63822455

