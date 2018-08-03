20180727_review

### 회귀분석(통계학의 꽃)

관찰된 연속형 변수들에 대해 두 변수 사이의 모형을 구한뒤 적합도를 측정해 내는 분석 방법이다.

회귀분석은 시간에 따라 변화하는 데이터나 어떤 영향, 가설적 실험, 인과 관계의 모델링등의 통계적 예측에 이용될 수 있다. 

(출처 : [회귀분석](https://ko.wikipedia.org/wiki/%ED%9A%8C%EA%B7%80_%EB%B6%84%EC%84%9D))

회귀분석 = 정규분포(확률분포) = 통계적 추정 = 검정





### 확률 & 확률분포

이산형 - 확률분포표

연속형 - 확률밀도함수





### 정규분포

특징

- 평균 = 최빈값 = 중앙값
- 확률이 mu를 중심으로 +-2sigma 내에 거의 모두 존재(95%)

정규분포는 2개의 매개 변수 [평균](https://ko.wikipedia.org/wiki/%ED%8F%89%EA%B7%A0_(%ED%86%B5%EA%B3%84%ED%95%99)) ![\mu ](https://wikimedia.org/api/rest_v1/media/math/render/svg/9fd47b2a39f7a7856952afec1f1db72c67af6161)과 [표준편차](https://ko.wikipedia.org/wiki/%ED%91%9C%EC%A4%80%ED%8E%B8%EC%B0%A8) {\displaystyle \sigma }![\sigma ](https://wikimedia.org/api/rest_v1/media/math/render/svg/59f59b7c3e6fdb1d0365a494b81fb9a696138c36)에 대해 모양이 결정되고, 이때의 분포를 {\displaystyle \mathrm {N} (\mu ,\sigma ^{2})}![{\mathrm  {N}}(\mu ,\sigma ^{2})](https://wikimedia.org/api/rest_v1/media/math/render/svg/997f90ed5b7e90906f4bdd6b1a377507b8439dbc)로 표기한다. 특히, 평균이 0이고 표준편차가 1인 정규분포 {\displaystyle \mathrm {N} (0,1)}![{\mathrm  {N}}(0,1)](https://wikimedia.org/api/rest_v1/media/math/render/svg/d15a45b474dded72fba385afd8397325a74d8986)을 **표준 정규 분포**(standard normal distribution)라고 한다. 

**NORMDIST('확률변수', '평균', '분산', 누적여부(T/F))** : 확률변수를 통해 확률을 구한다.

**NORMSINV**('확률') : 확률을 통해 확률변수(z)를 구한다.



### 통계적 추론

표본이 가진 정보로 모수를 추정하고 모수에 대한 가설이 옳은지를 판단하는 것



