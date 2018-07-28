#### 2018.07.27. 데잇걸즈 TWL : 기계학습으로 분류하기, 가설검정



#### 1. 오전 : 기계학습으로 분류하기

- TWL 관련 안내 : 특강 연사 분들 메일주소 / 개인정보 남기지 마세요. 삭제 불가!

  

- GitHub, 잘 사용하고 계신가요?

  - GitHub 사용 구조 : TWL, 10 Minutes to Pandas 공동번역 예시

  - Branch는 왜 사용할까요?
  - Git Stash (@Sourcetree)
    1. upstream 혹은 origin의 최신 소스를 가져오고 싶을때
    2. 내 저장소의 commit되지 않은 내용을 git stash로 임시 저장함
    3. 임시 저장한 자료는 git stash pop으로 꺼낼 수 있음
  - 좋은 Commit Message를 작성하는 7가지 방법 ([원문](https://chris.beams.io/posts/git-commit/)/[번역](https://item4.github.io/2016-11-01/How-to-Write-a-Git-Commit-Message/))
    1. 제목과 본문을 빈 행으로 분리한다.
    2. 제목 행을 50자로 제한한다.
    3. 제목 행 첫 글자는 대문자로 쓴다.
    4. 제목 행 끝에 마침표를 넣지 않는다.
    5. 제목 행에 명령문을 사용한다.
    6. 본문을 72자 단위로 개행한다.
    7. '어떻게'보다는 '무엇'과 '왜'를 설명한다.
  - Commit Message 수정하기
    1. 마지막 Commit을 수정 : $git commit --amend
    2. 커밋 메시지를 여러 개 수정 : $git rebase -i HEAD~3
    3. rebase 종료 : $git rebase --continue
    4. suqash로 commit 합치기
  - Git-flow branch 이해하기 : master, develop, feature-\*, release-\*, hotfit-\*
  - Open Source에 Pull Request 보내기
    1. 보내기 전에 먼저 Commit squash
    2. 내 저장소로 먼저 push
    3. GitHub 내 저장소 페이지에서 Pull request
    4. PR에 빠진 내용이 없는지 확인 (프로필 사진 등)
    5. @리뷰어에게 멘션하기
    6. 이슈번호 넣어주기
    7. Pull Request 생성
    8. 리뷰 받기
    9. Merge (Open Source의 경우 Maintainer가 Merge)
  - Open Source로 배우는 협업
    - 형식에 맞게 Full request 보내기 : 제목/본문에 issue 번호 붙이기, 스타일 체크 등
    - 성공한 프로젝트의 프로젝트 관리를 보고 배우기
  - 광고 : 8/15 Pycon에서 판다스 스프린트를 합니다. 참여해보세요! 스프린트는 무료! ㅎㅎ



- 기계학습으로 분류하기

  ~~~
  "기계가 일일이 코드로 명시하지 않은 동작을 데이터로부터 학습하여 시행할 수 있도록 하는 알고리즘을 개발하는 연구 분야" - 아서 사무엘
  ~~~

  - [위키백과](https://ko.wikipedia.org/wiki/%EA%B8%B0%EA%B3%84_%ED%95%99%EC%8A%B5) 참조

    

  - 실습 : 기계 학습 예시 (이진 분류 : 'Binary_classification.ipynb')

    - 목표 : 국민청원에서 평균보다 많이 추천 받을지, 적게 추천 받을지를 머신러닝으로 판단
    - 학습 세트 : 데이터 세트 = (최근 들어온 청원인) 7 : (이전에 들어온 청원인) 3
    - 학습 세트의 양 > 데이터 세트의 양(quantity) 이어야 underfitting 문제 방지 가능
    - TF-IDF 적용 
      1. 특정 청원에서는 자주 언급되지만 다른 청원에서는 언급되지 않는 단어의 경우
      2. 해당 청원 내에서 해당 단어에 가중치를 부여함 : 해당 단어가 중요하다고 판단하는 것
      3. 검색엔진에서 많이 사용되는 기법임
    - Tip : 공식문서를 보고 학습하는 방법 = 튜토리얼 코드를 따라하면 좋음





#### 2. 오후 : 가설검정

- 회귀분석 
  - 예측하고 싶은 자료와 그 자료에 영향을 미치는 자료들의 선형식을 도출하는 것
  - 회귀분석이 가능한 자료의 조건 
    - 예측하고 싶은 자료는 정규분포를 따라야 하고, 연속형 변수여야 함
  - 일반화 선형 모형 : 여러 다른 분포를 가정하고 회귀분석을 하는 것
    - 이산형 분포 중 2가지 카테고리만 있는 경우 이항분포를 사용
  - 통계적 추론 : 추정치, 표준오차(추정치의 잘못된 정도를 알려주는 것)가 존재
  - 가설검정 : 자료에 영향을 미칠 것으로 추정한 자료가 실제로 영향을 미치는지 입증하는 것
  - 회귀분석이 가능하다 = 정규분포(확률분포) + 통계적 추정 + 검정이 무엇인지 알고 있다



- 확률분포

  - 통계 : 표본을 바탕으로 모집단을 추론하는 것. 확률이 있어야 의미가 있음

  - 확률 : 근원사건들이 일어날 가능성이 모두 같을 때, 사건이 일어날 확률

  - 이산확률변수 - 확률분포표 : 발생할 사건에 대해 확률을 나열한 것

  - 연속확률변수 - 확률밀도함수 : 확률의 밀도가 어느 구간이 더 높고/낮은지를 영역으로 표현

  - '정규분포의 특징 이해' 슬라이드 정답 : 50점, 70점, 2.5%, 2~3등

  - 정규분포의 표준화 : 정규분포인 두 개 이상의 그룹을 비교하기 위해 하나의 기준으로 재배치

  - 표준정규분포 함수

    - NORMSINV(확률) : 표준정규분포 역함수 값 반환 (확률을 넣으면 해당하는 z값 출력)
    - NORMSDIST(z) : 표준정규분포 함수의 값을 반환 (z값을 넣으면 누적확률 값을 출력)
    - NORMSINV(0) = '#NUM!' 오류 발생 (→ 표준정규분포는 무한한 Long tail이므로 0%가 불가능)

  - 중심극한의 정리 

    - 모집단이 정규분포를 따르지 않더라도 성립함

    - 실습 : 국민청원 sampled 파일 log(참여인원(votes))로 중심극한의 정리 확인
    - sampled 파일 불러오면서 한글 깨질 때 : 데이터 → 데이터 가져오기 → CSV → UTF-8 지정

  - 통계적 추론 

    - 표본이 가지고 있는 정보를 이용하여 모수에 관한 결론을 유도, 모수에 대한 가설의 옳고 그름을 판단
    - 모수의 추정, 모수에 대한 가설검증으로 나눌 수 있음

    - 표본을 통해 모집단을 예측하려면 둘 사이의 연결고리가 필요함

  - 표준편차 vs. 표준오차

    - 표준편차 : 데이터의 흩어진 정도를 평가, 평균으로부터 표본들의 흩어져 있는 산포도를 나타냄
    - 표준오차 : 모평균을 추정했을 시, 추정량은 표본으로부터 모집단을 추론한 것이기 때문에 불완전함

  - 모평균에 대한 구간추정



- 가설검정
  - 가설검정 단계
    1. 가설을 수립
    2. 유의수준 결정 : 모수의 추정이 맞지 않을 확률을 결정 (일반적으로 5%로 설정)
    3. 기각역 설정 : 가설의 기각여부를 결정하는 범위계산 (유의수준이 결정되면 자동적으로 계산됨)
    4. 통계량의 계산 : 표본의 통계량을 이용해 가설검정
    5. 의사결정 : 기각을 할지, 못할지 결정
  - 가설의 정의
    - 가설 : 주어진 사실 혹은 조사하고자 하는 사실이 어떠하다는 주장이나 추측
    - 귀무가설 : 연구자가 증명하고자 하는 실험가설과 반대되는 입자. (= 효과(혹은 차이)가 없다)
    - 대립가설 : 귀무가설의 반대. 연구자가 실험을 통해 규명하고자 하는 가설 (= 효과(혹은 차이)가 있다)
  - 유의수준 & 기각역
    - 유의수준 : 귀무가설이 참일 때, 귀무가설에 대한 판단의 오류 수준. 가설검정 전에 미리 정해야 함.
    - 기각역 : 귀무가설을 기각하게 되는 영역
    - 검정통계량 : 가설검정을 위해 사용되는 주요 표본 통계량
    - 기각역에 검정통계량이 포함되는 경우 : 귀무가설 기각, 대립가설 채택
    - 채택역에 검정통계량이 포함되는 경우 : 귀무가설 채택, 대립가설 기각
    - 유의확률(p-value) : 귀무가설이 맞다는 전제 하에, 통계값이 실제로 관측된 값 이상일 확률
  - 1종 오류, 2종 오류
    - 1종 오류 : 귀무가설이 실제로는 옳으나 기각한 경우
    - 2종 오류 : 귀무가설이 실제로는 옳지 않으나 기각하지 않은 경우
    - 1종 오류에 더 주의를 기울여야 함 (1종 오류가 좀 더 치명적인 결과를 불러오기 때문 : 신약개발 예제)



- 과제
  - 필수 : 자신이 관심 있는 청원(키워드/카테고리) 또는 청원 관련 이슈에 대한 가설 검정
  - 필수2 : 1일 1통계. 매일매일 복습하고 체크 @통계 수업 복습 체크 구글 스프레드 시트
  - 선택 : 오늘(7/27) 수업 자료 중 가설검정 추가 예제 1~3