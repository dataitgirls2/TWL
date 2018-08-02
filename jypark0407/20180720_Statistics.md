## Review - Basics of Statistics

**EDA : Exploratory Data Analysis**

> Exploratory Data Analysis is an approach/philosophy for data analysis that employs a variety of techniques (mostly graphical) to : 
>
> 1. maximize insight into a data set
> 2. uncoer underlying structure
> 3. extract important variables
> 4. detect outliers and anomalies
> 5. test underlying assumptions

> Most EDA techniques are graphica in nature with a few quantitative techniqiues. The reason for the heavy reliance on graphics is that by its very nature the main role of EDA is to open-mindely explore, and graphics gives the analysts unparalled power to do so. 
>
> Examples of graphical techniques include : 
>
> 1. Plotting the raw data (ex) histogram)
>
> 2. Plotting the statistics (ex) boxplot)
>
> 3. Using multiple plots per page
>
>    source : https://www.itl.nist.gov/div898/handbook/eda/section1/eda11.htm

TL;DR

EDA is an initial approach in data analysis to derive reports about the raw data, often using visual techniques. Data analysts/scientists can suggest statistical hypothesis or statistical models after EDA. Examples include boxplot and histogram. 



**Types of Variable** 자료의 분류

- Numerial Variable 수치형 변수

  - Continuous Variable 연속형 변수

    > A variable that may contain any value within some range
    >
    > ex) temperature, distance

  - Discrete Variable 이산형 변수

  - > A variable whose values are whole numbers 
    >
    > ex) number of children

- Cateogorical Variable 범주형 변수

  - Nominal Variable 명목형 변수

    > A variable whose categories are ordered equally 
    >
    > ex) countries, subjects

  - Ordinal Variable 순위형 변수

  - > A variable whose categories can be meaningfully ordered 
    >
    > ex) exam grades

source : http://www-ist.massey.ac.nz/dstirlin/CAST/CAST/Hstructures/structures_c2.html



**Summarizing Categorical Variables ** 범주형 자료의 요약

- 범주 (category)의 종류, 나타나는 횟수를 요약. 
- 전체에서 차지하는 범주의 비교 파악.

도수분포표 (Frequency Distribution) : 도수, 상대도수를 테이블로 만든다.

원형그래프 (Pie Chart)

막대그래프 (Bar Graph)

파레토그림 : 상대 도수가 큰 순서로 범주를 왼쪽부터 오른쪽로 배열하여 만듦.

a type of chart that contains both bars and a line graph, where individiual values are represented in descending order by bars and the cumulative total is represented by the line. 



**Summarizing Continuous Variables** 연속형 자료의 요약

- 점도표 : 수평선을 긋고 눈금을 표시한 후 각 관측값에 해당하는 위치에 점을 찍어 표시

- 도수 분포표 : 모든 관측값을 포함하는 범위를 몇 개의 구간으로 나누어 작성

  범주형 자료의 도수 분포표와 비쇼해서 계급구간이 추가되었음.

- Histogram 히스토그램 : A representation of the distribution of numerical data. It is an estimate of the probability distribution of a continuous variable. It displays 'relative' frequencies. 

  - vs. Bar Graph : Histogram is concerned with the frequency of the data, and has no gaps between the bars as they represent continuous data. In the meanwhile, bar graph illustrates all other data types. (categorical data)




**Summarizing Discrete Variables 이산형 자료의 요약**

* 이산형자료는 수치자료로서 관측값의 크기가 의미가 있으므로 파레토 그림과 같이 범주의 순서가 바뀌는 기법은 피해야 한다. 



**Box Plot (aka Box and Whisker Disagram)**

* A standardized way of displaying the distribution of data based on the five number of summary : minimum, maximum, 1st and 3rd quartile and median. 
* Can see 
  * if there are any outliers 
  * if the data is symmetrial or skewed



**Correlation, Correlation Coefficient** 상관 관계

> In statistics, dependence or association is any statistical relationship, whether casual or not, bewteen two random variables or bivaraite data. In the broadest sense, correlation is any statistical association, though in common usage it most often refers to how close two variables are to having a linear relationship with each other. 

* Pearson's Product-moment coeffeicient 피어슨 계수 

  - The most common way to measure the dependence between two variables 
  - The value is derived by diving the covariance of the two varibles by the product of their standard deviations

* Correlation and Linearity

  * Scatter Plots of Anscombe's Quartet

    * A set of four different pairs of variables with the same mean, variance, correlation and regression line but the distribution of the variables are all different. 
    * Created by the statistician Francis Anscombe who wanted to counter argue the opinions among statisticians that 'numerical calcuations are exact, but graphs are rough.'

    https://en.wikipedia.org/wiki/Anscombe%27s_quartet



## Probability 확률

- Random Variable (확률 변수)  : a variable whose possible values are outcomes of a random phenomenon. 
  - Continuous probability distribution : the probabilities of the possible values of a continuous random variable (infinite and uncountable)
  - Discrete probability distribution : the probabilites of possible values of a discrete random variable (finite and countable)

https://support.minitab.com/en-us/minitab-express/1/help-and-how-to/basic-statistics/probability-distributions/supporting-topics/basics/continuous-and-discrete-probability-distributions/



* Normal Distribution : a very common continuous probability distribution. It is useful because of the central limit theroem, which states that as the number of variables goes up, variables get evenly distributed, leading the shape of the probability distribution to bell shape. 
  * Probability Density Function : Graphical representation of probability of random variables
  * Cumulative Distribution Function : Graphical representation of cumulative probability of random variables (easier to notice the point when the curve reaches 1.0)
* Standard Normal Distribution : A 'standardized' normal distribution that has an average of 0 and variance of 1.
* z-scre(standard score) : indicates how many standards deviations an element is from the mean. 



**Variable vs Random Variable**

 A variable is an unknown quantity that has an undetermined magnitude, and random variables are used to represent events in a sample space or related values as a dataset. A random variable itself is a function.

https://www.differencebetween.com/difference-between-variable-and-vs-random-variable/



**Random Variable vs Probability**

확률과 확률 변수의 차이점은 다음과 같다.

- 확률은 표본으로 이루어진 집합 즉, 사건에 대해 할당된 숫자이지만 확률 변수는 표본 하나 하나에 대해 할당된 숫자이다.
- 확률은 0부터 1사이의 숫자만 할당할 수 있지만 확률 변수는 모든 실수 범위의 숫자를 할당할 수 있다.

확률 변수를 사용하면 모든 표본은 하나의 실수 숫자로 변하기 때문에 표본 공간을 실수의 집합 즉 **수직선(number line)**으로 표시할 수 있다. 표본의 집합인 사건(event)은 이 수직선 상의 숫자의 집합인 **구간(interval)**으로 표시된다.

https://datascienceschool.net/view-notebook/4bcfe70a64de40ec945639236b0e911d/



**Central Limit Theorem**

Normalized independent random variables tends towards a normal distribution even if the original varaibles are not normally distributed. The number of variables should be over 30 or so.



**Statistical Inference** 통계적 추론

- Use sample data to derive attributes of the population

  - either to validate the numerical attribute of the population 
  - or to validate the assumption of the population (statistical model)

- Statistical proposition : 

  - point estimation 점추정

  - interval estimation 구간추정

  - credible interval

    

**Standard Error** 표준오차

the standard deviation of the sampling distribution or an estimate of the standard deviation of estimate. 

It refers to the difference between the actual estimate and the assumed estimate of the population. 

