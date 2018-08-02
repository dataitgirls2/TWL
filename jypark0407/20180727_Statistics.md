## GitHub Review

**Upstream, Origin, Master**

Upstream : The 'Master' repository where everyone has forked from

Origin : Forked from Upstream

Master : Default branch of local repository



**Setting up Remote Repositories**

1. Check if remote repositories are set

```text
$ git remote -v
```

2. Set remote repository 

   By Cloning (origin)

   ```text
   $ git clone (URL : usually copied directly from GitHub)
   ```

   By Remote Add (upstream)

   ```text
   $ git remote add upstream(URL : usually copied directly from GitHub)
   ```



**Sending Pull Request**

```text
$ git pull origin master # pull content from origin(remote repository) to master (local repository)
```

```text
$ git pull upstream master # pull content from upstream (remote repository) to master (local repository)
```



**Rebase?**

It's a shortcut command that execute all of these actions at once : fetch + merge+ add + commit

```text
$ git pull --rebase origin master 
```



**Merging vs Rebase**

Merging only incorporates new commits, while rebase completely replaces the branch with new commits. 

```text
$ git rebase master #origin --> master
$ git rebase -i master #shows the files that are about to be removed before executing the command.
```



CheatSheet : https://education.github.com/git-cheat-sheet-education.pdf



**Lesson from optimizing match rate using Machine Learning algorithm**

Learn to read the data first than focusing on fancy algorithms or its features

The more the data, the accurate it gets. Also remove outliers as many as possible



## 통계적 추론

**Standard Error** 표준 오차

measure of variability of a sample's characteristic (statistics. characteristic of a population is parameter)



**Confidence Levels** 신뢰도

A confidence level is the probability that the interval estimate will include the population parameter (i.e. mean, standard deviation)

> **[신뢰도]**와 **[정확도]**는 상충관계(trade-off)입니다. 즉 신뢰도를 높이려면 정확도는 어느정도 희생하는 수 밖에 없습니다. 정확도를 높이려면 신뢰도를 희생할 수 밖에 없고요.   그러면 정확도와 신뢰도를 동시에 높이는 방법이 없을까요? 통계학에서는 표본 크기를 크게 하면 됩니다. 그러나 이 경우 시간과 돈이 문제가 되겠지요.

http://www.hmsys.co.kr/statistics_1/s_2.html?num=20



**Confidence Interval** 신뢰 구간

A confidence interval gives an estimated range of values which is likely to include an unknown population parameter, the estimated range being calculated from a given set of sample data. 

여러 개의 다른 표본에서 신뢰 구간을 같은 방법으로 구할 경우 모평균을 포함하는 구간들의 비율. 점 추정과 비교하면, 단순히 점 하나로는 알 수 없는 표본 평균의 변동성을 알 수 있기 대문에 다른 표본과의 비교가 용이하다.  

http://www.boxnwhis.kr/2016/03/14/overlapping_ci_in_abtest.html

https://www.jcu.edu.au/__data/assets/pdf_file/0010/115939/Basic-Statistics-7_Probability-and-Confidence-Intervals.pdf



**정리**

표준 오차 : 포본 평균의 변동성을 측정. (구하는 방법 : 모집단(아니면 표본의 평균)/표본의 크기)

신뢰 구간 : (변동성이 있는) 표본들에서 모평균을 포함하는 구간들의 비율. (구하는 방법 : 표본 평균 +- 신뢰도의 Z score, 표준 오차)



**Statistical Hypothesis Test** 가설검정

단계

1) 가설을 수립 

예) 실제 모평균은 주어진 모평균의 값보다 더 크다. (예시에서 '모평균'은 사실 표본에서 추출되었음)

2) 유의수준 결정 - 임의로 값을 정해야 함

모수의 추정이 맞지 않을 확률을 결정

3) 기각역 설정 - 가설의 기각여부를 결정하는 범위계산 (유의수준이 결정되는 자동으로 계산됨)

4) 통계량의 계산 - 표본의 통계량을 이용해 가설검정

5) 의사결정 - 기각을 할지, 못할지 결정



##

`control`+`shift`+`arrow` : Jump to the very start/end



http://ezstat.snu.ac.kr/textbook_sources/chapter_18.pdf



