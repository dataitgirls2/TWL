
# 청원페이지에서 번호, 분류, 제목, 내용 뽑아오기

국민청원 첫 페이지 하단의 청원 목록에서 번호, 분류, 제목, 참여인원을 추출하여 DataFrame에 담아주세요.


```python
import pandas as pd
```


```python
from urllib import request
from bs4 import BeautifulSoup
```


```python
url = "https://www1.president.go.kr/petitions?page=1"
with request.urlopen(url) as f:
  html = f.read().decode('utf-8')

bs = BeautifulSoup(html, 'html5lib')
```

## 1. 번호를 뽑아봅시다아


```python
content_elements = bs.select('div.bl_no')
contents_no = [c.text for c in content_elements]

contents_no
```




    ['번호',
     '번호 답변대기',
     '번호 답변대기',
     '번호 답변대기',
     '번호 답변대기',
     '번호 답변대기',
     '번호 답변대기',
     '번호 답변대기',
     '번호',
     '번호 243985',
     '번호 243984',
     '번호 243983',
     '번호 243982',
     '번호 243981',
     '번호 243980',
     '번호 243979',
     '번호 243978',
     '번호 243977',
     '번호 243976',
     '번호 243975',
     '번호 243974',
     '번호 243973',
     '번호 243972',
     '번호 243971']



번호, 답변대기 라는 말들은 필요가 없으니 빠이빠이 해줘야 한다

진영님의 질문에서 시작된 replace 방법..

뭘 좋아할지 몰라 다 준비해써 히히

함수는 하나하나 쓰기 귀찮고, 내가 만든 함수는 단 하나의 요소만 제거하기 때문에 매번 함수를 불러오기 때문에 효율적이지 않을수도..?

그래도 재사용이 가능하다는 장점이 있는데 흠

%time을 찍어볼까

### \#1 함수를 만들어서 표시


```python
def remove_e(data, element):
  temp = [d.replace(element, '') if element in d else d for d in data]
  result = [t for t in temp if t!='']
  return result
```


```python
%time
result1 = remove_e(contents_no, '번호')
result1 = remove_e(result1, ' ')
result1 = remove_e(result1, '답변대기')
result1
```

    CPU times: user 4 µs, sys: 2 µs, total: 6 µs
    Wall time: 11 µs
    




    ['243985',
     '243984',
     '243983',
     '243982',
     '243981',
     '243980',
     '243979',
     '243978',
     '243977',
     '243976',
     '243975',
     '243974',
     '243973',
     '243972',
     '243971']



### \#2 답변대기가 없는 내용 중에서 번호와 띄어쓰기 등을 제거하는 방법


```python
%time
result2 = [
    
    t.replace('번호', '').replace(' ','')
    for t in contents_no
    if '답변대기' not in t
    if '번호' in t
    if t.replace('번호', '').replace(' ','') != ''
    
          ]
result2
```

    CPU times: user 4 µs, sys: 1e+03 ns, total: 5 µs
    Wall time: 11.2 µs
    




    ['243985',
     '243984',
     '243983',
     '243982',
     '243981',
     '243980',
     '243979',
     '243978',
     '243977',
     '243976',
     '243975',
     '243974',
     '243973',
     '243972',
     '243971']



### \#3 답변대기가 없는 내용 중에서 번호와 띄어쓰기 등을 제거하는 방법2


```python
%time
result3 = []
for t in contents_no:
  if '답변대기' not in t:
    if '번호' in t:
      t = t.replace('번호', '')
      if t != '':
        result3.append(t.replace(' ', ''))
result3
```

    CPU times: user 3 µs, sys: 2 µs, total: 5 µs
    Wall time: 11 µs
    




    ['243985',
     '243984',
     '243983',
     '243982',
     '243981',
     '243980',
     '243979',
     '243978',
     '243977',
     '243976',
     '243975',
     '243974',
     '243973',
     '243972',
     '243971']



## 2. 분류를 뽑아봅시다아


```python
content_elements = bs.select('div.bl_category')
contents_categ = [c.text for c in content_elements]

contents_categ
```




    ['분류',
     '기타',
     '외교/통일/국방',
     '기타',
     '반려동물',
     '외교/통일/국방',
     '문화/예술/체육/언론',
     '반려동물',
     '분류',
     '분류  미래',
     '분류  안전/환경',
     '분류  일자리',
     '분류  보건복지',
     '분류  일자리',
     '분류  일자리',
     '분류  정치개혁',
     '분류  교통/건축/국토',
     '분류  인권/성평등',
     '분류  정치개혁',
     '분류  인권/성평등',
     '분류  성장동력',
     '분류  기타',
     '분류  육아/교육',
     '분류  정치개혁']



자세히 보니, 처음 9개는 다른 이야기이므로 신경쓰지말자!

번호 뽑기와 마찬가지의 방법을 사용하는데,

함수와 중복replace(?) 중에서 무엇이 더 효율적인지는 모르겠답


```python
result_categ = remove_e(contents_categ[8:],'분류')
result_categ = remove_e(result_categ, ' ')
result_categ
```




    ['미래',
     '안전/환경',
     '일자리',
     '보건복지',
     '일자리',
     '일자리',
     '정치개혁',
     '교통/건축/국토',
     '인권/성평등',
     '정치개혁',
     '인권/성평등',
     '성장동력',
     '기타',
     '육아/교육',
     '정치개혁']



이잉.... 중복이 발생했다....

사실 필요는 없지마눈 중복을 제거해봅시다아


```python
final = []
# final = [e for e in result_categ if e not in final]

for e in result_categ:
  if e not in final:
    final.append(e)
# 조금 더 짧게, 효율적으로 하고 싶은데.. 처음부터 중복이 발생하지 않게..!

final
```




    ['기타',
     '외교/통일/국방',
     '반려동물',
     '문화/예술/체육/언론',
     '미래',
     '안전/환경',
     '일자리',
     '보건복지',
     '정치개혁',
     '교통/건축/국토',
     '인권/성평등',
     '성장동력',
     '육아/교육']



## 3. 제목을 뽑아옵시다아


```python
content_elements = bs.select('div.bl_subject')
contents_subj = [c.text for c in content_elements]

contents_subj
```




    ['제목',
     '\n\t\t\t\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\t\t\t\t제목 문재인 대통령님께 청원합니다.',
     '\n\t\t\t\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\t\t\t\t제목 제주도 불법 난민 신청 문제에 따른 난민법, 무사증 입국, 난민신청허가 폐지/개헌 청원합니다.',
     '\n\t\t\t\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\t\t\t\t제목 가해자들은 떳떳이 생활하고, 집단 성폭행 당한 피해자인 저희아이는 오히려 더 죄인같이 생활하고 있습니다. 미성년자 성폭행범 처벌을 더 강하하여 주세요.',
     '\n\t\t\t\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\t\t\t\t제목 개.고양이 식용종식 전동연(개를 가축에서 제외하라)',
     '\n\t\t\t\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\t\t\t\t제목 남편선교사가 안티폴로감옥에 있습니다.(필리핀)',
     '\n\t\t\t\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\t\t\t\t제목 디스패치 폐간을 요청합니다.',
     '\n\t\t\t\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\t\t\t\t제목 표창원 의원의 개,고양이 도살 금지 법안을 통과 시켜주세요!',
     '제목',
     '\n\t\t\t\t\t\t\t\t\t\t\t\t제목 네이버 블로그는 짝퉁 유통의 숙주\n\t\t\t\t\t\t\t\t\t\t\t',
     '\n\t\t\t\t\t\t\t\t\t\t\t\t제목 비흡연자를위한 대책\n\t\t\t\t\t\t\t\t\t\t\t',
     '\n\t\t\t\t\t\t\t\t\t\t\t\t제목 롯데그룹 총수 신동빈 회장을 제발 불구속 재판받게 ...\n\t\t\t\t\t\t\t\t\t\t\t',
     '\n\t\t\t\t\t\t\t\t\t\t\t\t제목 어린이집 유치원 실내온도 냉/난방 규제 온도를 마련 ...\n\t\t\t\t\t\t\t\t\t\t\t',
     '\n\t\t\t\t\t\t\t\t\t\t\t\t제목 연간 3억실의 공실이 발생하는 숙박업의 현실을 반영 ...\n\t\t\t\t\t\t\t\t\t\t\t',
     '\n\t\t\t\t\t\t\t\t\t\t\t\t제목 특수고용직 형태이지만, 상당수가 불법인 가맹본부를 ...\n\t\t\t\t\t\t\t\t\t\t\t',
     '\n\t\t\t\t\t\t\t\t\t\t\t\t제목 노회찬 주검을 보면서 단언 합니다..\n\t\t\t\t\t\t\t\t\t\t\t',
     '\n\t\t\t\t\t\t\t\t\t\t\t\t제목 지하철 노약자석 없애주세요.\n\t\t\t\t\t\t\t\t\t\t\t',
     '\n\t\t\t\t\t\t\t\t\t\t\t\t제목 국가와 경찰은 일베에 할머니 나체 사진을 무단 유포 ...\n\t\t\t\t\t\t\t\t\t\t\t',
     '\n\t\t\t\t\t\t\t\t\t\t\t\t제목 이재명,은수미 조사철저\n\t\t\t\t\t\t\t\t\t\t\t',
     '\n\t\t\t\t\t\t\t\t\t\t\t\t제목 국제선 계류장 항공기소음 및 항공기 매연부터 개선시 ...\n\t\t\t\t\t\t\t\t\t\t\t',
     '\n\t\t\t\t\t\t\t\t\t\t\t\t제목 대한민국 증시 코스닥 코스피 이대로 괜찮아보이시나 ...\n\t\t\t\t\t\t\t\t\t\t\t',
     '\n\t\t\t\t\t\t\t\t\t\t\t\t제목 서민죽이는 신용보증재단\n\t\t\t\t\t\t\t\t\t\t\t',
     '\n\t\t\t\t\t\t\t\t\t\t\t\t제목 교과과정에서의 학생들의 예체능 교육 확대에 대한 청 ...\n\t\t\t\t\t\t\t\t\t\t\t',
     '\n\t\t\t\t\t\t\t\t\t\t\t\t제목 이재명지사 의혹 해소\n\t\t\t\t\t\t\t\t\t\t\t']




```python
result_subj = remove_e(contents_subj[8:],'\n')
result_subj = remove_e(result_subj, '\t')
result_subj = remove_e(result_subj, '제목')
result_subj = remove_e(result_subj, ' ')
result_subj
```




    ['네이버블로그는짝퉁유통의숙주',
     '비흡연자를위한대책',
     '롯데그룹총수신동빈회장을제발불구속재판받게...',
     '어린이집유치원실내온도냉/난방규제온도를마련...',
     '연간3억실의공실이발생하는숙박업의현실을반영...',
     '특수고용직형태이지만,상당수가불법인가맹본부를...',
     '노회찬주검을보면서단언합니다..',
     '지하철노약자석없애주세요.',
     '국가와경찰은일베에할머니나체사진을무단유포...',
     '이재명,은수미조사철저',
     '국제선계류장항공기소음및항공기매연부터개선시...',
     '대한민국증시코스닥코스피이대로괜찮아보이시나...',
     '서민죽이는신용보증재단',
     '교과과정에서의학생들의예체능교육확대에대한청...',
     '이재명지사의혹해소']



## 4. 참여인원을 뽑아옵시다아


```python
content_elements = bs.select('div.bl_agree')
contents_votes = [c.text for c in content_elements]

contents_votes
```




    ['참여인원',
     '\n\t\t\t\t\t\t\t\t\t\t\t\t참여인원  224,539명\n\t\t\t\t\t\t\t\t\t\t\t',
     '\n\t\t\t\t\t\t\t\t\t\t\t\t참여인원  714,875명\n\t\t\t\t\t\t\t\t\t\t\t',
     '\n\t\t\t\t\t\t\t\t\t\t\t\t참여인원  342,647명\n\t\t\t\t\t\t\t\t\t\t\t',
     '\n\t\t\t\t\t\t\t\t\t\t\t\t참여인원  214,634명\n\t\t\t\t\t\t\t\t\t\t\t',
     '\n\t\t\t\t\t\t\t\t\t\t\t\t참여인원  207,275명\n\t\t\t\t\t\t\t\t\t\t\t',
     '\n\t\t\t\t\t\t\t\t\t\t\t\t참여인원  207,742명\n\t\t\t\t\t\t\t\t\t\t\t',
     '\n\t\t\t\t\t\t\t\t\t\t\t\t참여인원  209,571명\n\t\t\t\t\t\t\t\t\t\t\t',
     '참여인원',
     '\n\t\t\t\t\t\t\t\t\t\t\t\t참여인원 0명\n\t\t\t\t\t\t\t\t\t\t\t',
     '\n\t\t\t\t\t\t\t\t\t\t\t\t참여인원 0명\n\t\t\t\t\t\t\t\t\t\t\t',
     '\n\t\t\t\t\t\t\t\t\t\t\t\t참여인원 0명\n\t\t\t\t\t\t\t\t\t\t\t',
     '\n\t\t\t\t\t\t\t\t\t\t\t\t참여인원 1명\n\t\t\t\t\t\t\t\t\t\t\t',
     '\n\t\t\t\t\t\t\t\t\t\t\t\t참여인원 3명\n\t\t\t\t\t\t\t\t\t\t\t',
     '\n\t\t\t\t\t\t\t\t\t\t\t\t참여인원 2명\n\t\t\t\t\t\t\t\t\t\t\t',
     '\n\t\t\t\t\t\t\t\t\t\t\t\t참여인원 0명\n\t\t\t\t\t\t\t\t\t\t\t',
     '\n\t\t\t\t\t\t\t\t\t\t\t\t참여인원 2명\n\t\t\t\t\t\t\t\t\t\t\t',
     '\n\t\t\t\t\t\t\t\t\t\t\t\t참여인원 0명\n\t\t\t\t\t\t\t\t\t\t\t',
     '\n\t\t\t\t\t\t\t\t\t\t\t\t참여인원 2명\n\t\t\t\t\t\t\t\t\t\t\t',
     '\n\t\t\t\t\t\t\t\t\t\t\t\t참여인원 1명\n\t\t\t\t\t\t\t\t\t\t\t',
     '\n\t\t\t\t\t\t\t\t\t\t\t\t참여인원 1명\n\t\t\t\t\t\t\t\t\t\t\t',
     '\n\t\t\t\t\t\t\t\t\t\t\t\t참여인원 0명\n\t\t\t\t\t\t\t\t\t\t\t',
     '\n\t\t\t\t\t\t\t\t\t\t\t\t참여인원 0명\n\t\t\t\t\t\t\t\t\t\t\t',
     '\n\t\t\t\t\t\t\t\t\t\t\t\t참여인원 5명\n\t\t\t\t\t\t\t\t\t\t\t']




```python
result_votes = remove_e(contents_votes[8:],'\n')
result_votes = remove_e(result_votes, '\t')
result_votes = remove_e(result_votes, '참여인원')
result_votes = remove_e(result_votes, ' ')
result_votes = remove_e(result_votes, '명')
result_votes = remove_e(result_votes, ',')  # 숫자로 바꾸는 상황을 감안해서,, ㅎ
result_votes
```




    ['0', '0', '0', '1', '3', '2', '0', '2', '0', '2', '1', '1', '0', '0', '5']



데이터 프레임에 넣어서 예쁘게 만들기!

d = {'col1': [1, 2], 'col2': [3, 4]}
>>> df = pd.DataFrame(data=d)


```python
d = {'번호':result1, '분류':result_categ, '제목':result_subj, '참여인원':result_votes}

df = pd.DataFrame(data=d)
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>번호</th>
      <th>분류</th>
      <th>제목</th>
      <th>참여인원</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>243985</td>
      <td>미래</td>
      <td>네이버블로그는짝퉁유통의숙주</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>243984</td>
      <td>안전/환경</td>
      <td>비흡연자를위한대책</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>243983</td>
      <td>일자리</td>
      <td>롯데그룹총수신동빈회장을제발불구속재판받게...</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>243982</td>
      <td>보건복지</td>
      <td>어린이집유치원실내온도냉/난방규제온도를마련...</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>243981</td>
      <td>일자리</td>
      <td>연간3억실의공실이발생하는숙박업의현실을반영...</td>
      <td>3</td>
    </tr>
    <tr>
      <th>5</th>
      <td>243980</td>
      <td>일자리</td>
      <td>특수고용직형태이지만,상당수가불법인가맹본부를...</td>
      <td>2</td>
    </tr>
    <tr>
      <th>6</th>
      <td>243979</td>
      <td>정치개혁</td>
      <td>노회찬주검을보면서단언합니다..</td>
      <td>0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>243978</td>
      <td>교통/건축/국토</td>
      <td>지하철노약자석없애주세요.</td>
      <td>2</td>
    </tr>
    <tr>
      <th>8</th>
      <td>243977</td>
      <td>인권/성평등</td>
      <td>국가와경찰은일베에할머니나체사진을무단유포...</td>
      <td>0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>243976</td>
      <td>정치개혁</td>
      <td>이재명,은수미조사철저</td>
      <td>2</td>
    </tr>
    <tr>
      <th>10</th>
      <td>243975</td>
      <td>인권/성평등</td>
      <td>국제선계류장항공기소음및항공기매연부터개선시...</td>
      <td>1</td>
    </tr>
    <tr>
      <th>11</th>
      <td>243974</td>
      <td>성장동력</td>
      <td>대한민국증시코스닥코스피이대로괜찮아보이시나...</td>
      <td>1</td>
    </tr>
    <tr>
      <th>12</th>
      <td>243973</td>
      <td>기타</td>
      <td>서민죽이는신용보증재단</td>
      <td>0</td>
    </tr>
    <tr>
      <th>13</th>
      <td>243972</td>
      <td>육아/교육</td>
      <td>교과과정에서의학생들의예체능교육확대에대한청...</td>
      <td>0</td>
    </tr>
    <tr>
      <th>14</th>
      <td>243971</td>
      <td>정치개혁</td>
      <td>이재명지사의혹해소</td>
      <td>5</td>
    </tr>
  </tbody>
</table>
</div>



끼욧 이쁘다

생각해보니 같은일을 엄청 반복한 기분..!

그리하야 함수로 묶어보려 한다.

## 한 방에 해버리기! 원샷 원킬!


```python
what_to_know = ['no', 'category', 'subject', 'agree']  # 각각 번호, 분류, 제목, 참여인원을 의미
address = 'div.bl_'+what_to_know[0]

what_to_remove = ['번호 ', '제목 ', '참여인원 ', '명', ',', '\n', '\t', '분류 ']

df_dict = {}

for i in range(len(what_to_know)):
  address = 'div.bl_' + what_to_know[i]
  contents = [c.text for c in bs.select(address)]
  for e in what_to_remove:
    contents = remove_e(contents, e)
  df_dict[what_to_know[i]] = contents[9:]
```


```python
df = pd.DataFrame(data=df_dict)
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>agree</th>
      <th>category</th>
      <th>no</th>
      <th>subject</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>정치개혁</td>
      <td>244029</td>
      <td>정치인과 정치깡패?</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0</td>
      <td>정치개혁</td>
      <td>244028</td>
      <td>토착비리가 만연한 지자체의 범죄 이대로 묵과 할것인 ...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>기타</td>
      <td>244027</td>
      <td>정치인들 얼마만큼 깨끗한지 전수조사 부탁합니다</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1</td>
      <td>경제민주화</td>
      <td>244026</td>
      <td>김재익 같으신 분을 뽑으세요</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1</td>
      <td>정치개혁</td>
      <td>244025</td>
      <td>대통령 문재인이 대통령직에서 물러나고 법의 심판을 ...</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2</td>
      <td>안전/환경</td>
      <td>244024</td>
      <td>지구온난화 대비</td>
    </tr>
    <tr>
      <th>6</th>
      <td>5</td>
      <td>정치개혁</td>
      <td>244023</td>
      <td>노회찬 의원님 타살이 의심 할 대목이다.</td>
    </tr>
    <tr>
      <th>7</th>
      <td>16</td>
      <td>정치개혁</td>
      <td>244022</td>
      <td>이재 상세히수사촉구 강력히 해야합니다</td>
    </tr>
    <tr>
      <th>8</th>
      <td>1</td>
      <td>정치개혁</td>
      <td>244021</td>
      <td>이번기회에국회의원들 다조사하세요</td>
    </tr>
    <tr>
      <th>9</th>
      <td>0</td>
      <td>행정</td>
      <td>244020</td>
      <td>배달대행업체의 세금계산서 의무 발행 요청드려요</td>
    </tr>
    <tr>
      <th>10</th>
      <td>1</td>
      <td>경제민주화</td>
      <td>244019</td>
      <td>모든 공공분야는 국가에서 관리해야 합니다.~~^^</td>
    </tr>
    <tr>
      <th>11</th>
      <td>1</td>
      <td>기타</td>
      <td>244018</td>
      <td>개인회생변제기간단축제도를전국에서시행해주시길부탁 ...</td>
    </tr>
    <tr>
      <th>12</th>
      <td>7</td>
      <td>성장동력</td>
      <td>244017</td>
      <td>원자력을 없애면 나라가 망한다 청원제안</td>
    </tr>
    <tr>
      <th>13</th>
      <td>2</td>
      <td>외교/통일/국방</td>
      <td>244016</td>
      <td>[노무현 전 대통령과 노회찬 의원의 죽음과 이박과 ...</td>
    </tr>
    <tr>
      <th>14</th>
      <td>3</td>
      <td>정치개혁</td>
      <td>244015</td>
      <td>드루킹 수사 더 철저하게 수사할것을 청원합니다</td>
    </tr>
  </tbody>
</table>
</div>



# 10개 페이지에서 내용 뽑아오기!

국민청원 목록 첫 페이지 주소는 https://www1.president.go.kr/petitions?page=1 입니다.

두번째 페이지 주소는 https://www1.president.go.kr/petitions?page=2 입니다.

처음 10개 페이지에 순차적으로 방문하여 번호, 분류, 제목, 참여인원을 추출하고 그 결과를 DataFrame에 담아주세요.


```python
what_to_know = ['no', 'category', 'subject', 'agree']  # 각각 번호, 분류, 제목, 참여인원을 의미
address = 'div.bl_'+what_to_know[0]

what_to_remove = ['번호 ', '제목 ', '참여인원 ', '명', ',', '\n', '\t', '분류 ']
# 지워야 할, 필요없는 내용을 목록에 담아둠

df_dict = {}

count = 10  # 몇 개의 페이지 부를거야?

for i in range(1,count+1):
  
  url = 'https://www1.president.go.kr/petitions?page='+str(i)
  # 10개 페이지는 마지막 숫자만 바뀌는 점을 이용
  with request.urlopen(url) as f:
    html = f.read().decode('utf-8')
  bs = BeautifulSoup(html, 'html5lib')
  
  for i in range(len(what_to_know)):
    address = 'div.bl_' + what_to_know[i]
    contents = [c.text for c in bs.select(address)]
    
    for e in what_to_remove:
      contents = remove_e(contents,e)
    df_dict[what_to_know[i]] = contents[9:]
    
  df = pd.DataFrame(data=df_dict)
  print(df)
  if i < count:
    print('\n')
```

       agree   category      no                            subject
    0      0   외교/통일/국방  244067  북한의 핵무기 폐기 실패했습니다   그 책임을 문재인 ...
    1      0       정치개혁  244066     드루킹비밀조직들이 댓글조직들 불법사찰조직들 여론 ...
    2      6       정치개혁  244065                           이재 지사 사퇴
    3      4       정치개혁  244064                              이재 탄원
    4      0       성장동력  244063                  퇴근시 간판전원 끄기 운동합시다
    5      1      경제민주화  244062  현 경제상황의 점검이 필요합니다.  52시간근로 최저 ...
    6      7       정치개혁  244061                        김경수 드루킹도 조사
    7      2     인권/성평등  244060           문재인정부는 난민 문제 왜 넉놓고 있는건가?
    8      0       정치개혁  244059     댓글조직들 불법사찰조직들 여론몰이조직들이 드루킹 ...
    9      0       정치개혁  244058          국회원 특할비도 철저한 수사와 처벌을 하세요.
    10     3      안전/환경  244057                      촛불로 난민을 몰아냅시다
    11     1       정치개혁  244056   네이트에 문대통령 비방하는   댓글이 조직적으로 운 ...
    12     1         기타  244055                  위안부 문제는 어떻게 되는건가요
    13    22         기타  244054                           이재은 사퇴하라
    14     2       성장동력  244053               코스닥 활성화 정책 어떻게 된건가요?
    
    
       agree category      no                            subject
    0      0       기타  244052                       원전풀가동 안하냐...
    1      2     정치개혁  244051    문재인 대통령님 제발 착한아이 콤플렉스로부터 벗어 ...
    2      4     정치개혁  244050  드루킹댓글조작. 특검 팀의 특검법 위반 여부를. 조사 ...
    3      1    경제민주화  244049          소상공인들의 순이익에 따른 최저임금 등급매기기
    4      1       행정  244048    국민을 심판하는 판사올바른 판사는 국민이 뽑는 시 ...
    5     49     정치개혁  244047                          이재 은수미 사퇴
    6      2    육아/교육  244046           경찰대학 입학 갑작스런 인원축소 부당합니다.
    7      0     보건복지  244045                      정신병자를 입원시켜주세요
    8      0     농산어촌  244044                 양식장 폐사하는 물고기 살려줍시다
    9      5       행정  244043             고 노회찬의원 무궁화 대훈장 추서바랍니다
    10     0     보건복지  244042                      정신병자를 입원시켜주세요
    11    14     정치개혁  244041                         이재투하게 발켜주라
    12     2    안전/환경  244040                     건설근로자들 쉬게 해주세요
    13    28   인권/성평등  244039         이재경기도지사에 대한 철저한 수사를 촉구합니다.
    14     0    안전/환경  244038                       기무사문건 작성자 청산
    
    
       agree category      no                           subject
    0      5     정치개혁  244037  소상공인 채무 탕감 반대합니다.(성실히 갚은 사람들 ...
    1      0    안전/환경  244036                    건설근로자들 쉬게 해주세요
    2      3      일자리  244035   영세 자영업자를 위한 최소한도의 보장인 노란우산공 ...
    3      0     보건복지  244034  일베 박카스 할머니 나체 유포하고 조롱한 사건은 처 ...
    4      3      일자리  244033  비정규직을개처럼 취급하는 IBK기업은행! 직접고용하 ...
    5     50     정치개혁  244032            이재 경기지사 관련 엄중한 수사촉구!!!
    6      5     정치개혁  244031   와 노회찬 투신하고 그알 이재 조폭하고 박전 기무 ...
    7     30     정치개혁  244030                     이재도지사 사퇴요구합니다
    8      5     정치개혁  244029                        정치인과 정치깡패?
    9      1     정치개혁  244028  토착비리가 만연한 지자체의 범죄 이대로 묵과 할것인 ...
    10     2       기타  244027         정치인들 얼마만큼 깨끗한지 전수조사 부탁합니다
    11     1    경제민주화  244026                   김재익 같으신 분을 뽑으세요
    12    10     정치개혁  244025   대통령 문재인이 대통령직에서 물러나고 법의 심판을 ...
    13     2    안전/환경  244024                          지구온난화 대비
    14     9     정치개혁  244023            노회찬 의원님 타살이 의심 할 대목이다.
    
    
       agree   category      no                           subject
    0      9       정치개혁  244023            노회찬 의원님 타살이 의심 할 대목이다.
    1     60       정치개혁  244022              이재 상세히수사촉구 강력히 해야합니다
    2      2       정치개혁  244021                 이번기회에국회의원들 다조사하세요
    3      0         행정  244020         배달대행업체의 세금계산서 의무 발행 요청드려요
    4      1      경제민주화  244019       모든 공공분야는 국가에서 관리해야 합니다.~~^^
    5      2         기타  244018     개인회생변제기간단축제도를전국에서시행해주시길부탁 ...
    6      8       성장동력  244017             원자력을 없애면 나라가 망한다 청원제안
    7      3   외교/통일/국방  244016   [노무현 전 대통령과 노회찬 의원의 죽음과 이박과 ...
    8      5       정치개혁  244015         드루킹 수사 더 철저하게 수사할것을 청원합니다
    9      1         기타  244014                       국민청원을 없애주세요
    10     1       정치개혁  244013                        노회찬 대표님 문상
    11     0      경제민주화  244012   현금영수증 제도를 활용하여 소상공인 활성화를 도모 ...
    12     0     인권/성평등  244011  카카오톡의 영구정지 및 구매한 것에 대한 효력 무효 ...
    13     0        일자리  244010       소상공인 죽이는 쇼셜앱 수수료율 제재 청원합니다.
    14     1        일자리  244009             파격적공개공모일자리창출단기간확정프로적트
    
    
       agree   category      no                           subject
    0     48       정치개혁  244008                       이재 정확한 수사하길
    1      5       성장동력  244007                   드루킹 일당은 더 있습니다.
    2      3      경제민주화  244006   연대보증이 폐지됫다지만 아직도 고통받는 사람이 많 ...
    3      1         기타  244005                    법치주의를 우롱하는 이런짓
    4      2         기타  244004                             성인오락실
    5     11         행정  244003   부천오정경찰서 실종팀의 무관심한 수사로 주말 폭염 ...
    6      3     인권/성평등  244002        소방관 경찰관등 체력시험을 남녀모두 같게해주세요
    7      8         기타  244001                     문재인 그냥 사퇴하세요.
    8      4       정치개혁  244000              노회찬 의원님 국립묘지로 보내 주세요
    9      0       정치개혁  243999    우리나라에 보수비밀조직들에 비밀단체 비밀조직들이 ...
    10     3   외교/통일/국방  243998   참전국가유공자수당을 최저생계비 이상으로 인상을 청 ...
    11    32       정치개혁  243997                        이재은수미 처벌하라
    12     1       정치개혁  243996  드루킹 수사 국민들이 납득 할수 있는 결과로 마무리 ...
    13     8      육아/교육  243995                   여름방학 기간을 늘려주십시오
    14    18       농산어촌  243994       세계 일류 고기능성 과일나무가 죽어가고 있습니다.
    
    
       agree   category      no                           subject
    0      9       정치개혁  243993         드루킹을 민주사회의 적폐로 엄벌에 처해주세요.
    1      1         기타  243992   대한항공의 기업이름과 기업로고인 태극문양 사용 중 ...
    2      0         기타  243991            검찰 인력 늘려서 수사의 질을 높여주세요
    3      0       정치개혁  243990   익에 기대서 인터넷에서 범죄를 저지르고 있는 사람 ...
    4      8      경제민주화  243989  빚 탕감 소각정책을 취소해주세요. 대국민 공감에 어 ...
    5    129       정치개혁  243988                     이제 은수미 조폭관련수사
    6     74       정치개혁  243987   이재전 성남시장과 조폭연루설  확실한 조사를 바랍 ...
    7      0      육아/교육  243986  살인적인 폭염에 적절한 조치 바랍니다.(폭염 경보시 ...
    8      4      경제민주화  243985               2019 최저시급 인상에 파급 효과
    9     14   교통/건축/국토  243984               건축법 개정을 간곡히 부탁드립니다.
    10    56       정치개혁  243983   이재 도지사 조사를 위해 청원 링크 띄워요 한곳에 ...
    11     1         미래  243982                네이버 블로그는 짝퉁 유통의 숙주
    12     0      안전/환경  243981                        비흡연자를위한 대책
    13     2        일자리  243980   롯데그룹 총수 신동빈 회장을 제발 불구속 재판받게 ...
    14    11       보건복지  243979  어린이집 유치원 실내온도 냉/난방 규제 온도를 마련 ...
    
    
       agree   category      no                           subject
    0      5        일자리  243978  연간 3억실의 공실이 발생하는 숙박업의 현실을 반영 ...
    1      1        일자리  243977    특수고용직 형태이지만 상당수가 불법인 가맹본부를 ...
    2      4   교통/건축/국토  243976                   지하철 노약자석 없애주세요.
    3   1691     인권/성평등  243975  국가와 경찰은 일베에 할머니 나체 사진을 무단 유포 ...
    4     68       정치개혁  243974                        이재은수미 조사철저
    5      1     인권/성평등  243973  국제선 계류장 항공기소음 및 항공기 매연부터 개선시 ...
    6      2       성장동력  243972   대한민국 증시 코스닥 코스피 이대로 괜찮아보이시나 ...
    7      2         기타  243971                      서민죽이는 신용보증재단
    8      5      육아/교육  243970  교과과정에서의 학생들의 예체능 교육 확대에 대한 청 ...
    9     35       정치개혁  243969                        이재지사 의혹 해소
    10    16       정치개혁  243968                이재 죽이기의 배후를 밝혀주십시요
    11     0      경제민주화  243967                      골목 상권 활성화 방안
    12     8     인권/성평등  243966    여성만생각하는 여성들의 페미짓을 그만두게 처벌을 ...
    13     6         행정  243965    조용하고 한적한곳에 경찰들 주차하고 쉬고있는모습 ...
    14     9       정치개혁  243964   몰래 카메라 범죄 앞에 눈감은 정의의 여신 누구를 ...
    
    
       agree   category      no                            subject
    0      4       정치개혁  243963              특별사면 제도 자체를 없애야합니다...
    1      2        일자리  243962    한국산업인력공단 국가기술자격시험 응시제도 개선(특 ...
    2      1       보건복지  243961                               미소금융
    3     12        일자리  243960   용역에서 자회사로 글자만 바꾼 처우개선 IBK기업은 ...
    4      8         미래  243959  오늘만 생각하는 정치 그만해주세요... 제발 부탁드립 ...
    5      2      안전/환경  243958                         차량2대이상세금관련
    6      3        일자리  243957                     Lg전자 불법도급 및 갑질
    7     14       성장동력  243956                 문재인 대통령 하야를 청원합니다.
    8      1   외교/통일/국방  243955   한번만 도와주십시오 우리나라 군 세무조사 (방산비리 ...
    9      1         미래  243954          네이버 블로그에서 짝퉁판매자들 단속좀 해주세요
    10     9     인권/성평등  243953                       여성가족부를 없에주세요
    11     4      경제민주화  243952                    영세 하청업을 보살펴 주세요
    12     0         행정  243951   공무원들의  예산집행  제대로  이행되는지  감찰좀 ...
    13    10     인권/성평등  243950                           여성가족부 폐지
    14    17         미래  243949                 문재인대통령을 탄핵을 청원합니다.
    
    
       agree   category      no                            subject
    0      0       정치개혁  243948                   알맹이 없는 강정 글거 부스럼
    1      2       정치개혁  243947                    Ibk기업은행 비정규직 실체
    2      6   외교/통일/국방  243946    군대기피 목적으로 어린나이에 해외 나가서 영주권을 ...
    3      8       성장동력  243945                 탈원전 정책 지금이라도 인정하세요
    4      2      경제민주화  243944      존경하는 새   시대의 새  대통령님  께 아룁니다.
    5      1       농산어촌  243943    중력을 이용하는 농법으로 대한민국 농업인들에게 새 ...
    6      4        일자리  243942            IBK국책은행 기업은행 진실혹은 거짓!!!
    7      1         행정  243941   건축과/보육과/소방과/부서별 서로 다른 업무진행으로 ...
    8      7         기타  243940    김상조 공정거래위원장님 하림지주 빨리 수사 종결해 ...
    9     17         기타  243939                              누진제폐기
    10     2         기타  243938  특검 수사 제대로 하지 않는다면 두고 두고 원망만 쌓 ...
    11     2       정치개혁  243937   조폭 동원해 급여 안주는 정치인이 4월혁 회장인 나 ...
    12     5       보건복지  243936    공휴일 및 절을 연차로 다 공제해서 여름휴가로 쓸 ...
    13    12         미래  243935         문재인대통령을  탄핵하며더불어 민주당을탄핵합니다
    14    28       보건복지  243934  살인더위 피할 수 있게 한시적 전기 누진세 폐지해 주 ...
    
    
       agree category      no                            subject
    0      1     성장동력  243933                        소상공인 대출건 문의
    1     12     정치개혁  243932          한국계외국인들 동족취급하는 적폐들 폐지해주세요
    2      1       미래  243931                            만나고싶습니다
    3      1     보건복지  243930               국민건강보험금 산정문제를 제기합니다.
    4      5       기타  243929                        자영업자들 살려주세요
    5      5       기타  243928                    대통령님과 대화를 원합니다.
    6      3    경제민주화  243927   주식 전일 종가를 다음 날 무조건 시초가로 출발하는 ...
    7      1    육아/교육  243926                 박근혜 치적 연금개혁을 인정하라.
    8     35   인권/성평등  243925                           난민 절대 반대
    9      0       미래  243924         남극 북극 얼음이 녹아가는 현실에 대체할게없나요
    10     5     보건복지  243923            대통령 각하께 담배값 인상을 청원드립니다.
    11   142     정치개혁  243922    이재 은수미 청원 한곳으로 모아주세요. 꼭 없어져 ...
    12    11      일자리  243921  "제조업 한다는 자부심 다 잃었다 이 땅서 더는 못버 ...
    13     4    안전/환경  243920                 응급실폭행범 엄중 처벌 바랍니다.
    14    57       기타  243919                          이재경기지사 관련
    
    
    

# 100개의 임의 청원의 제목과 본문을 뽑아오기!

2018년 7월 17일 현재 국민청원의 글 번호는 1번부터 238663번까지 부여되어 있습니다.

하지만 중간중간 삭제된 청원이 있어서 실제 청원 수는 238663개보다 적습니다.

309510번 청원글 본문의 URL은 https://www1.president.go.kr/petitions/309510 입니다.

URL에서 글번호만 바꾸면 해당 청원의 본문으로 이동할 수 있습니다.

이러한 URL 패턴의 특성을 활용하여 전체 청원 중 임의로 100개 청원의 제목과 본문을 추출하여 DataFrame에 담아주세요.


```python
import random
```

실제 청원 수를 구할 수 있을까?

[] 랜덤한 수 100개를 리스트에 담는다. (중복 x)

[] 리스트의 랜덤수를 하나씩 뽑아와서 URL을 바꾼다.

[] 이상의 방법으로 하나씩 뽑아 데이터 프레임을 만든다.

일단 번호는 244075까지 있지만, 삭제된 경우가 있음

각 페이지는 15개까지의 목차를 보여주기 때문에, (끝번호-첫번호)+1이 15 미만이라면, 전체번호(244075)에서 부족한 수만큼을 계속 빼는 것을 반복

예를들어, 끝번호-첫번호+1이 13이라면 2개의 청원이 삭제되었으므로 244075-2를 하여 total에 저장하고 다음 페이지를 확인

몇 페이지가 있는가?를 어차피 확인해야 함

그럼 그냥 몇 페이지가 있는지를 확인하고 마지막 페이지를 제외한 페이지 수에 15를 곱하고 마지막 페이지의 목차 개수를 더하면 될 듯

마지막 페이지라는 것을 어떻게 알 수 있지? 목차의 개수가 15 미만이겠지?

마지막 페이지가 15개일수도 있나? ㅇㅇ 그것도 고려해야 함

< 이렇게 해보자ㅏ >
1. 첫 페이지의 마지막 번호(가장 최근의 번호)를 불러오고 15로 나눈 몫을 구한다.
2. 지워진 청원의 개수가 그리 많지 않다는 가정 하에, 그 몫값을 페이지 번호로 하여 그 페이지부터 시작한다.
3. 만약 청원이 많이 지워진 상태라면, 몫값의 페이지가 없을 수도 있으니, 그런 경우에는 10페이지 더 앞당겨서 시작한다.


```python
with request.urlopen('https://www1.president.go.kr/petitions?page=1') as f:
  html = f.read().decode('utf-8')
bs = BeautifulSoup(html, 'html5lib')
recent_num = [c.text for c in bs.select('div.bl_no')][9]
recent_num = int(recent_num.replace('번호 ',''))
recent_num
```




    244115




```python
url_num = recent_num // 15

while True:
  url = 'https://www1.president.go.kr/petitions?page='+str(url_num)
  with request.urlopen(url) as f:
    html = f.read().decode('utf-8')
  bs = BeautifulSoup(html, 'html5lib')
  plz_total = len([c.text for c in bs.select('div.bl_no')][9:])
  if plz_total != 15:
      total = 15 * (url_num-1) + plz_total
      break
  url_num += 1

total
```




    244116




```python
url = 'https://www1.president.go.kr/petitions/50'
with request.urlopen(url) as f:
  html = f.read().decode('utf-8')
bs = BeautifulSoup(html, 'html5lib')
contents = [c.text for c in bs.select('div.View_write')]
contents
```




    ['\n\t\t\t\t\t\t\t\t\t\t\t안녕하십니까? 대통령님 간단하게 제소개 부터 하겠습니다. 저는 치위생과 3학년 학생입니다. 다름이 아니라 너무 억울한 \n\t\t\t\t\t\t\t\t\t\t\t일이 생겨  이렇게 글을 적어봅니다. 저희 3학년들은 올해 아주 중요한 시험이  있었습니다.3년동안 힘들게 고생하여 이제곧 \n\t\t\t\t\t\t\t\t\t\t\t끝난다.조금만 힘을내자 라는 생각으로 견뎌내고 있었는데 갑자기 어제 과 단톡방의  이내용이 사실이냐면서 한장의 사진을 \n\t\t\t\t\t\t\t\t\t\t\t보내주었습니다. 그사진은 국시원에서 올린 공지글을 캡쳐한 사진이였습니다.국시원에서 국가고시 날짜가 변경 되었다. \n\t\t\t\t\t\t\t\t\t\t\t그러니 이글을  널리퍼트려줘라라는 의미를 가진 내용이였습니다. 그내용을 읽고 너무 황당하고 어이가 없어서 국시원쪽으로 전화를 해보니 자신들은 어쩔수없었다 나라에서 그날 공무원 시험을 봐야한다 하루의 2번 국시를 볼수없다 \n\t\t\t\t\t\t\t\t\t\t\t그래서 자신들과 보건복지부에서  다시 날짜를 정했는데 그날이 내년 18년 1월 5일이다 라는것입니다. \n\t\t\t\t\t\t\t\t\t\t\t그 말을  듣고 더욱 이해할수가 없었습니다. 먼저 그날 시험을 보기로한 국시생은 저희였는데 갑자기 아무런 말도 문자도  \n\t\t\t\t\t\t\t\t\t\t\t없고 그공지글도 그냥 통보였습니다. 국가에서보는 시험이 일반 초중고 수행평가도 아니고 갑자기 이런식으로  바뀐다는게 \n\t\t\t\t\t\t\t\t\t\t\t말이 됩니까? 고등학생들이 보는 모의고사,수능도 이런식으로  변경 하지않습니다.  통보로 날짜를 변경하는건  저희  \n\t\t\t\t\t\t\t\t\t\t\t에비 의료기사들을 무시하는걸로 보입니다. 저희학교 교수님들은 학생들에게 자부심을 가져라 치과위생사라는 직업을 아끼고 사랑하고 자부심을 가져도 되는 직업이니깐  당당 해져도 괜찮다고  말씀하셨습니다. 하지만 저는  그러지 못할꺼같습니다.  아마 저뿐만이아니라 마음 학생들도 자존심도 낮아지고 무시받는다고 생각했을것입니다. \n\t\t\t\t\t\t\t\t\t\t\t17년 12월16일날의 시험을 봐야하는  국시생들은 저희 예비 치과위생사들 입니다. 공무원 시험이 갑자기 잡혀서  봐야한다면 다른날로 정하는게 맞지않을까요? 먼저 그날의 시험을 보기로 한 학생들은 저희입니다 \n\t\t\t\t\t\t\t\t\t\t\t왜 갑자기 저희가 양보해야하고  피해를봐야합니까?  저희국시 앞으로 4달남은상태였고 지금 많은 학생들이 지쳐지만 \n\t\t\t\t\t\t\t\t\t\t\t12월만 참으면 된다 라는 생각으로  견딘 학생들에게는 1월에 본다는 통보는 너무 가혹합니다. \n\t\t\t\t\t\t\t\t\t\t\t제발  원래대로12월 16일날 국시를 볼수 있도록  도와주세요  제발 다시 정정 해주세요. \n\t\t\t\t\t\t\t\t\t\t\t부탁드립니다.   \n\t\t\t\t\t\t\t\t\t\t\t꼭  끝까지  읽어보셨으면 좋겠습니다. \n\t\t\t\t\t\t\t\t\t\t']




```python
what_to_know = ['h3.petitionsView_title', 'div.View_write']  # 각각 번호, 분류, 제목, 참여인원을 의미
address = 'div.bl_'+what_to_know[0]

what_to_remove = ['\n', '\t']
# 지워야 할, 필요없는 내용을 목록에 담아둠

df_dict = {}

count = 100  # 몇 개의 페이지를 부를거야?

random_index = [random.randint(1, total) for i in range(count)]
print(random_index)

for i in range(count):
  url = 'https://www1.president.go.kr/petitions/'+str(random_index[i])
  with request.urlopen(url) as f:
    html = f.read().decode('utf-8')
  bs = BeautifulSoup(html, 'html5lib')
  
  for n in range(len(what_to_know)):
    address = what_to_know[n]
    contents = [c.text for c in bs.select(address)]
    
    for e in what_to_remove:
      contents = remove_e(contents,e)
    df_dict[what_to_know[n]] = contents
    
  df = pd.DataFrame(data=df_dict)
  print(df)
  if i < count:
    print('\n')
```

    [227870, 160278, 35208, 21547, 36573, 88015, 7840, 219288, 151714, 42545, 170862, 86507, 190575, 68903, 239653, 42522, 5812, 235356, 177369, 228551, 222976, 150575, 136423, 215075, 2709, 223805, 4903, 20105, 23092, 199003, 66117, 105380, 21384, 139307, 45991, 89581, 42342, 180713, 25068, 237070, 168564, 171841, 191639, 188993, 122338, 80499, 214308, 25141, 83099, 147477, 99882, 211776, 37238, 218185, 174344, 65131, 85075, 52922, 9041, 76776, 183921, 200077, 148111, 199309, 151373, 41193, 139115, 233513, 139169, 140675, 80998, 13398, 226644, 18482, 175074, 141652, 46684, 234677, 54407, 53816, 39643, 68239, 36678, 210743, 221262, 131722, 82321, 140143, 109192, 55994, 5582, 9384, 181983, 149475, 139409, 153626, 146246, 239505, 60269, 107892]
    


    ---------------------------------------------------------------------------

    HTTPError                                 Traceback (most recent call last)

    <ipython-input-294-35ec1f3dff9c> in <module>()
         14 for i in range(count):
         15   url = 'https://www1.president.go.kr/petitions/'+str(random_index[i])
    ---> 16   with request.urlopen(url) as f:
         17     html = f.read().decode('utf-8')
         18   bs = BeautifulSoup(html, 'html5lib')
    

    /usr/lib/python3.6/urllib/request.py in urlopen(url, data, timeout, cafile, capath, cadefault, context)
        221     else:
        222         opener = _opener
    --> 223     return opener.open(url, data, timeout)
        224 
        225 def install_opener(opener):
    

    /usr/lib/python3.6/urllib/request.py in open(self, fullurl, data, timeout)
        530         for processor in self.process_response.get(protocol, []):
        531             meth = getattr(processor, meth_name)
    --> 532             response = meth(req, response)
        533 
        534         return response
    

    /usr/lib/python3.6/urllib/request.py in http_response(self, request, response)
        640         if not (200 <= code < 300):
        641             response = self.parent.error(
    --> 642                 'http', request, response, code, msg, hdrs)
        643 
        644         return response
    

    /usr/lib/python3.6/urllib/request.py in error(self, proto, *args)
        568         if http_err:
        569             args = (dict, 'default', 'http_error_default') + orig_args
    --> 570             return self._call_chain(*args)
        571 
        572 # XXX probably also want an abstract factory that knows when it makes
    

    /usr/lib/python3.6/urllib/request.py in _call_chain(self, chain, kind, meth_name, *args)
        502         for handler in handlers:
        503             func = getattr(handler, meth_name)
    --> 504             result = func(*args)
        505             if result is not None:
        506                 return result
    

    /usr/lib/python3.6/urllib/request.py in http_error_default(self, req, fp, code, msg, hdrs)
        648 class HTTPDefaultErrorHandler(BaseHandler):
        649     def http_error_default(self, req, fp, code, msg, hdrs):
    --> 650         raise HTTPError(req.full_url, code, msg, hdrs, fp)
        651 
        652 class HTTPRedirectHandler(BaseHandler):
    

    HTTPError: HTTP Error 404: Not Found

