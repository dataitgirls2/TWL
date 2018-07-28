# 180726_목 오전수업 TidyData 애란쌤

## 숙제_TIP


- clab노트북 : https://colab.research.google.com/drive/1pVqAYa0PBtaMQLbTuSNKufAenwu6nzqS#scrollTo=2CZfRiyQB3Sg

## 데이터 공부하는 이유 ? 

- 작지만 내가 흥미있고 나에게 유용한 데이터분석결과를 계속 만들어보는 것 (남이 만든거 상관없이)
- 다른 사람이 잘 해놓은 데이터분석 코드를 계속 읽어보고 탐구해보는것



- 책추천 : 

lessons learned in sotfware testing 

**스프트에워 테스팅 법칙 293가지** 

(사람들이 어떤종류의 실수를 많이하는지, 어떤걸 넣으면 오류를 잘 찾아내는지.. 그런 교훈들을 모아놓은 책입니다. , 인지심리학적인 이야기를 합니다. 공부하면 도움이 되실 것 같아요! )

코드를 짤면 잘못된것만 찾는 사람들..그 분야에서 재미있는 책..





---------





## 분석하기 좋은 데이터는? = Tidy data



- 도서관 데이터의 형태를 어떻게 바꾸면 좋을지 토론하기

  - 어떤 질문에 답하기 어려웠나? 왜 어려웠나?
  - 데이터가 어떤 형태라면 좋았을까?
> **Tidy data?** (**http://vita.had.co.nz/papers/tidy-data.html**)

> 아래와 같은 데이터를 Tidy data 라고 부른다. 
>
> - 변수 : 하나에 컬럼에는 하나의 '변수'가 담겨야 한다. ex 도서관명 
> - 관찰 : 하나에 행에는 하나의 observation이 남긴다. 
> - **단위 (units) : 서로 다른 데이터가 섞여있으면 안된다.** 

​	Ex) 월화수목금토일 + 주말포함 이렇게 나오면 안된다. 

​	     단위는 잘 이해 안갔다..

​            (논리적 단위들끼리 묶여진 표로 나눠서 구분해서 보관한다..?)



- 데이터는 조금 수집해보고 활용해보고...항상 점진적으로 해야 합니다!

- 위경도 뽑아낼때 슬라이스 이용해서 뽑아내는 법 

http://pandas.pydata.org/pandas-docs/stable/generated/pandas.melt.html



- groupby 는 ?  시도 카운트 수 셀때 

- pandas - merge : 서로 다른 두 테이블을 합치기. key가 동일해야 겹칠 수 있음



-----

- 제대로 처리되었는지 확인하기 ( 차집합 연산해보기 )

ex ) pattern = r'일요일|주말|[\b\s,]일[\b\s,]'

차집합 집합연산을 통해 정확히 되었는지 확인해봐야 합니다.

a = set(df['휴관일'])
b = set(df['휴관일'][df['휴관일'].str.contains(pattern)])  # 여기 이해 안감 @@@@@@@@@@@
a - b  

만약 도서관명과 휴관일을 같이 나타내고 싶으면 / 데이터 프레임에서 특정 2개의 컬럼을 뽑아내봅시다.

df.loc[df['휴관일'].str.contains(pattern)][['도서관명', '휴관일']]



result = df['도서관명'].str.extract(r'\(([^)]+)\)$', expand=False) 

true로 하면 데이터프레임(표인데 하나의 컬럼이 하나의 시리즈잖아요, 원래 여러개의 시리즈가 뭉쳐있는게 데이터프레임이잖아요. 이 나오고 fALSE를 하면 판다스 시리즈가 나옴, 컬럼이 1개인 데이터프레임이 나옴

result



----



## 네이버 클로바 배순민님 특강

네이버클로바팀

AI R&D Director 



네이버에서 AI는 무엇인가?





클로바 : 네이버와 라인이 함께 작년에 만든.. 인공지능 플랫폼

Search & Clova 조직을 통합..

서치조직안에 서치와 클로바조직따로있음



클로바 4가지 큰 조직 : 영상 / 음성(귀로듣는,말하는(합성)) / 추천 / NLU

 

음성인식, 합성기술... 

clova ai research : 연구를 활발히 하고 있습니다. 



starGAN , 2018 

Image-to-imgage translation 



The Conversation (2018) : 같은 오디오안에 여러 목소리가 있지만

입모양을 통해서 분리해내는 기술 발표예정.



딥러닝.. 



1956년 ai라는 단어가 처음만들어짐.

1974년 겨울 

1980년 뉴런을 똑같이 만들면..?

1997년 IBM Deep blue 체스

2011년 IBM Watson 

2012년 고양이 cat인식 -- 딥러닝의 쓰나미, 이때부터 아주 활발해지기 시작!

2016년 알파고



Neural Networks 

살짝만 따라해보자..

PASCAL Visual ovject challenge



딥러닝 관련 연구를 하고 있다. 



NSML  툴을 활용해서 쓰고 있습니다. 





Near Future Direction of Ai 미래 AI특징

1. channel diversity : 모바일, sharing 
2. 땅이커서 기계가 없다.. 현금에 대한 신뢰가 낮고 범죄율이 높다. 
3. 사람들은 더 이상 소비하고 싶지 않고 생산하고 싶어한다. creating



soonmin.bae@navercorp.com

Clover-jobs@navercorp.com

이력서를 보내주세요.



@ 유명학회에 논문이 많이 제출되던데 , 연구만 하는사람과 서비스를 하는 사람이 따로 있는가

- 반반하는거 같아요. 본인이 더 잘하는것을 합니다. 



- engineer 는 좀 더 응용쪽, 프로그래밍쪽, 논문쪽은 resarch scientist 

직군, 직무, 계급이 거의 분리되어 있지 않습니다. 



- 포지션 : 

research scientist

AI software engineer 

research internship 

global residency





-----

