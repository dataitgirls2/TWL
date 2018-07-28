+ matplotlib --> Seaborn


+ [Plotting Gallery](https://plotnine.readthedocs.io/en/stable)


+ df2.<TAB>
:사용가능한 기능 목록 나타남

+ df2.A?
:A 설명 나타남


df.sort_index(axis=1, ascending=False)

axis=0 행기준

Axis=1 열기준 column


df['A’] 열 하나 

Df[[‘A’, ‘B’]] 열 두개




+ pep8 : python 권장 문법(스타일 가이드)
(아톰에서 pep8 plug-in 사용하면 자동 가이드)

+ 검색하기

Factory = df[( df.title.str.find(‘개성공단’) != -1 ) | (df.content.str.find(‘개성공단’)]

Factory.shape


+ df.[‘title’].str?


crypto = df[( df.title.str.find('가상화폐') != -1 ) | ( df.content.str.find('가상화폐') != -1  )]

crypto.shape

+ 정규표현식 사용을 위해 import

import re
p = r'.*(돌봄|아이|초등|보육).*'
care = df[df['title'].str.match(p) |
           df['content'].str.match(p, flags=re.MULTILINE)]
care.shape

Df[‘a’] = df[‘a’].astype(‘바꿀 타입 이름')
