# Keep Moving, Keep Learning

- 세상에는 한 두 가지 정도의 사람이 있다?

1. 일은 일대로, 퇴근 후 3시간은 꼭 자기계발을 하는 성실한 사람
2. 1을 못하기 때문에 일을 하면서 성장해야 하는 사람

- 계획은 수정하라고 있는 것. 
  - 시프 트릴로지를 생각해 보자. 처음 세운 계획대로 되는게 하나도 없지 않은가? 과업을 수행하면서 처음 알못 상태에서 세운 멍청한 계획을 새로 습득한 정보에 맞춰 다시 수립.
  - 계획은 알못 상태에서만 세우기에는 너무 중요하다!
  - (plan a bit and)Explore first!
- 참고도서: Lessons learned in software testing ~~한글판 번역이 좀 구리다고 함~~



# Tidying Data

- **Tidy data? (http://vita.had.co.nz/papers/tidy-data.html)** 곰국 참조
- tidydata의 기본 원칙
  - 하나의 컬럼에는 하나의 값만! 성별+나이같은건 곤란합니다;;
  - 하나의 행에는 하나의 observation만
  - 논리적으로 완결된 단위들끼리 묶어 테이블을 만들자

- ~~귀찮은~~전처리 없이 바로 사용할 수 있도록 다듬어진 데이터, 일관성 있고 분석하기 좋은 형태.

- 유용한 패턴들

  ~~~python
  # .str은 데이터프레임의 스트링 관련 메소드를 모아놓은 네임스페이스
  df['lon'] = df['coor'].str.extract(r"(.+),.+", expand=False).astype(np.float32)
  
  # 되도록이면 이런 방식은 쓰지 말자. 걍 regex 쓰셈
  df['state'] = df['name'].str.split('(')
  df['state'] = df['state'].apply(lambda x: x[-1].replace(')', '')) 
  
  # slicing: 자료 길이가 일정할 때 사용할 수 있음. 유연하지 못함
  
  # 집합 개념을 이용해서 적절한 패턴 찾기
  pattern = r"(^일[가-힣]{0,2})|[^가-힣](일[가-힣]{0,2})|주말"
  a = set(df['closingdays'])
  b = set(df['closingdays'][df['closingdays'].str.contains(pattern)])
  a - b
  ~~~

- 데이터프레임을 쓸 때 **pandas**에서 제공하는 메소드를 사용하면 더 빠르다, c로 효율적인 연산!

- **python** 메소드 (i.e. for loop, lambda)는 데이터프레임 연산에 쓰기에는 너무 느리다! 데이터 양이 많아질수록 연산속도 저하가 심해짐

- merge 메소드: 뭔가 vlookup같은 것? 나뉜 것을 합치기는 쉬우나 합쳐진 것을 다시 나누는 것은 어려움



## 기타

- 메모장~~과 엑셀~~좀 쓰지 맙시다;; 아톰 같은 좋은 IDE 쓰세여!
- 다음 컴퓨터는 마소꺼 말고 맥 사세여 매애애애애애애애액!: 윈도우는 한글을 좀 이상하게 취급해요. 솔직히 맥 쓰는 사람들 보면 뭔가 굉장히 편해보임
- 반드시 빅데이터가 아니라도 적절한 샘플링을 통해 유사한/더 나은 결과를 얻을 수 있다. 통계를 열심히 공부하자!