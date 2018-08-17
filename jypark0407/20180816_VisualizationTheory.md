## 시각화 이론

**색상 지각 (color perception)**

- 눈의 망막과 중심와에 원뿔세포가 분포. 
- 각 원뿔세포는 반응 범위가 다르다
- 시지각은 패턴이 바뀌는 부분에서 민감하게 반응.



**색 디자인 가이드**

* 정량적 데이터 : 데이터의 크기 차이와 색거리 차이가 되도록 일치하게 표현
* 범주형 데이터 : 명도와 채도를 유지하고 색조 변화를 사용. 



**명도(Brightness)**

- 밝고 어두움

- 인간의 눈은 명도에 가장 민감

- 명도대비 - 배경에 따라서 정함

  ex) White 배경 : 어둡게

  Black배경 : 밝게

  

**채도**(Saturation)

- 색상의 포함 정도. 순수한 자체 빛의 밝기에서 나온 유채색성
   * Chroma
   * Colorfulness
  * Purity/pure color



**색상(hue)** 

- 주파수 파장에 길리에 따라 구별된 빛의 주파장 영역

- 보색 : 

  

**Color Wheel**

1차색 --> 2차색 (1차색들을 섞은 것) --> 3차색 (2차색들을 섞은 것)



**색깔을 어떻게 골라야 할지 모를때?**

요하네스 이텐의 7가지 법칙을 참고

http://www.worqx.com/color/itten.htm



**Color Harmonies**

https://htmlcolorcodes.com/color-picker/



**색의 시인성 (visibility)**

- 명도 차가 클수록 시인성이 높음
- 배경색과의 관계를 먼저 생각해야 함 (같은 색이여도 배경에 따라서 분위기가 다름.)



**주목성 (attractiveness of color)**

- 사람들의 시선을 끄는 힘이 강한 정도. 대체적으로 고채도, 난색계의 색.





**데이터 살펴보기**

- 의도에 따라서 데이터의 색깔을 다르게 한다
- 'lie factor' - 데이터가 말하지 않는 내용을 시각화로 표현할 수 있으므로 주의. 
- 천문학 등의 자연과학 분야에 특화된 컬러 코드도 있음.



## 팀 프로젝트 팁 (데잇걸즈 1기)

주제에 맞는 데이터 찾는 시간

데이터 전처리

스텝을 정하고 다같이 참여하는 방식이 더 잘맞았다.



## Kaggle Titanic - Data Visualization

https://www.rstudio.com/wp-content/uploads/2015/03/ggplot2-cheatsheet.pdf



**결측치가 있을 때 데이터 시각화?**

1. dropna()를 사용해서 결측치를 버림
2. missingno package를 이용해서 결측치도 시각화에 포함시킴
3. fillna()를 사용해서 결측치를 어떤 값으로 채워줌 



**데이터 - 데이터 시각화의 관계**

데이터의 종류에 따라서 효과적인 데이터 시각화가 다르다.

- Categorical Data vs Continuous Data
- Scatterplot, Histogram, Heat Map, etc.