### 20180716_TWL_assignments

> 지난 수업 피드백 공유

* #### api vs. user interface 

  -api(application Programming Interface) : 개발자가 컴퓨터간의 상호작용, 약속 

​	인간이 얼마나 쉽게 쓸수 있는 가의 측면에서는 별로 차이가 없다

​	인간의 "attention"

​	ex. python 의 함수

​	-user interface :사물과 프로그램, 시스템 사이에서 의사소통 할 수 있도록 만들어진 가상적 매개체 

> 과제 점검

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def shuffle0(list): <- list 가 아니라 data 
	temp = data[2]
	data[2] = data[3]
	data[3] = temp 
	#swaping 
		: '원래 데이터는 바뀌어선 안된다는 조건'에 위배되는 과정이다 
	"""
	함수에 대한 설명  < - 함수에 대한 설명을추가할 필요가 있따 
	"""
	pass <- pass 대신에 반환해야할 필요가 있다 = return 

print(shuffle0([1,2,3,4,5]))
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

​	- 예약어 와 built in 함수 

​	- ==  vs. =

~~~~~~~~~~~~~~~
def shuffle0(list): 
	temp = data[2]
	data[2] = data[3]
	data[3] = temp 
	return data

score = [1,2,3,4,5]
shuffled_socre = shuffle0(score)

#swaping 
		: '원래 데이터는 바뀌어선 안된다는 조건'에 위배되는 과정이다
		위 과정은원래 list 를 바꾸는 과정이다.
		
=>> 위 문제를 해결하려면원본을 복사하는 변수를 생성해준다 
def shuffle0(list): 
	result = data[:] <- 이렇게 복사본을 반들어주는게 보통 관행 
	temp = data[2]
	data[2] = data[3]
	data[3] = temp 
	return data
score = [1,2,3,4,5]
shuffled_socre = shuffle0(score)

~~~~~~~~~~~~~~~

계란 사와 우유있으면 두개 사와 ... 엔지니어 유머라는디 ㅇㅅㅇ

* [Shuffle 함수 과제 피드백.ipynb - Colaboratory](https://colab.research.google.com/drive/1EUaBP1QFtFV9pCMkLXk177ocRGwiXdRU)



> 첫번째 예시

~~~~~~~~~~~~~~~~~~~~~~~~~~~~
^원래 관행대로 한다면 ?

import random 
	data = [1,2,3,4,5]
	random.shuffle(data)
	copied
^random 모듈만의 관행대로 한다면?

def shuffle(data) : 
	copied= data[:]
	random.shuffle(copied)
	return copied 
> 무슨 차이인지 잘은 모르겠네 ㅇㅅㅇ 
데이터가 아무리 크더라도 매 실행마다 반환하는게 아니라 , inplace 에서 적용을한다 즉 원래 데이터 세트를 건들인다 .
~~~~~~~~~~~~~~~~~~~~~~~~~~~~





> 두번째 예시 

 import random  <- module vs. package?  정체가 불분명하다 

​	data = [12345]

​	random.sample(data, len(data)) 



#비복원 임의 추출 (= replace )대체 한다기 보다는 

​						한번 확인 한 후에 주머니에 다시 공을 넣는 것 처럼 

> 세번 쨰 예시 _r희영님 

#정렬과 shuffle

​	컴퓨터는 정렬 하지만 사람들은 shuffle 이라고생각 

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def sort_by_len(data): # 인자의 길이 순으로 리스트를 출력
    result = sorted(d, key=len)
    return result
        
d= ["chicken", "bentto", "pizza", "chinese", "icecream", "milk", "pretzel"]
print(Sortbylen(d)) 

# 장점 : 한 번 쓰기에는 좋다. / 단점 : 랜덤하다고 말할 수 없을 정도로 규칙이 확실한 리스트이다ㅠㅠ
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



* "길이" 대신 해시값(hash value)을 사용하면 hash-based sampling이라는 임의 추출 방법이 됩니다. 이후에 배울 내용 중 하나.  

​	데이터가 바뀌면 출력 값도 바뀐다. 주어진 데이터에 어떤 연산_len_을 적용하고 그거 에 따라 바뀌게 끔 

* 이름을 잘 지 어주는 것도 중요하지만 붙여줄 필요가 없는 함수에는 붙이지 않는 것도 매우 중요하다. 

  

  #대소문자에 예민한 단어 = case sensitive

​	사실 그냥 윗서랍에 있는 알파벳들이 upper case vise versa 

> 네 번째 예시_지윤님

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 현재 시간을 이용한 랜덤
import time
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
 
def shuffle1(data):
  now = int(time.time())
  random = now % 10
  result = data.copy()
  length = len(data)-1
  for num in range(length) :
    temp = result[num]
    result[num] = result[length - random]
    result[length-random] = temp
  return result
  
print('shuffle ', shuffle1(data))
print('원본 ', data)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* 랜덤을 잘 생성하는 알고리즘은 매우 중요하다. 

  미국수출규제에 걸릴 만큼 중요	

  ex. active  x

  

> 다섯번 째 예제_ 안세영 님 

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import random

a = [1, 2, 3, 4, 5]

def shuffle2(data):
  n = len(data)
  
  shuffled_data = data[:]
  
  for i in range(20):
    random_index = random.randint(0,n-1)  
  
    random_index2 = random.randint(0,n-1)
  
    value = shuffled_data.pop(random_index)
  
    shuffled_data.insert(random_index2,value)
  
  return shuffled_data

print(a)
print(shuffle2(a))
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

임의의 수를 임의의 위치에 넣기 

#문제 : 과연 얼마나 섞어야 하는가 ㅇㅅㅇ 

​	range(20)

> 여섯번 째 예제_이은지님 

~~~~~~~~~~~~~~~~~~~~~~~~~~~
import random                                        # Random 모듈 호출

data = ["Heroes", "Bears", "Eagles", "Twins", "Wyverns", "Lions", "Giants", "Dinos", "Tigers", "Wiz"]
data4 = []                                           # 결과값 입력을 위한 리스트 생성

def shuffle2(data):
    while True:                                      # 무한 반복. 이 부분을 for 문으로 처리하면 결과값 리스트가 모두 채워지지 않아도 함수가 끝나는 오류가 발생.
        if int(len(data)) == int(len(data4)):        # 원본 리스트(data)와 결과값 리스트(data4)의 인덱스가 동일해지면...
            break                                    # 함수 종료
        else:                                        # 원본 리스트(data)와 결과값 리스트(data4)의 인덱스가 동일하지 않으면...
            choice = random.choice(data)             # 원본 리스트(data)의 요소 중 하나를 random하게 선택 : 이미 들어있으면 하지말고 없으면 넣어라 
            if choice in data4:                      # 선택된 요소(choice)가 결과값 리스트(data4)에 이미 존재한다면...
                pass                                 # 아무 변화 없이 pass
            else:                                    # 선택된 요소가 결과값 리스트에 없다면...
                data4.append(choice)                 # 결과값 리스트에 선택된 요소를 추가
    return data4

data_4th = shuffle2(data)
print(data_4th)
print(data)

>수정 
mport random  # Random 모듈 호출

data = ["Heroes", "Bears", "Eagles", "Twins", "Wyverns", "Lions", "Giants", "Dinos", "Tigers", "Wiz"]

def shuffle2(data):
    # 결과값 입력을 위한 리스트 생성
    data_4 = []                                       
    # 무한 반복. 이 부분을 for 문으로 처리하면 결과값 리스트가 모두 채워지지 않아도 함수가 끝나는
    # 오류가 발생.
    while True:                                       
        if len(data) == len(data4):                   # 원본 리스트(data)와 결과값 리스트(data4)의 인덱스가 동일해지면...
            break                                     # 함수 종료
        else:                                         # 원본 리스트(data)와 결과값 리스트(data4)의 인덱스가 동일하지 않으면...
            choice = random.choice(data)              # 원본 리스트(data)의 요소 중 하나를 random하게 선택
            if choice in data4:                       # 선택된 요소(choice)가 결과값 리스트(data4)에 이미 존재한다면...
                pass                                  # 아무 변화 없이 pass
            else:                                     # 선택된 요소가 결과값 리스트에 없다면...
                data4.append(choice)                  # 결과값 리스트에 선택된 요소를 추가
    return data4

data_4th = shuffle2(data)
print(data_4th)
print(data)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

* while 참이면 계속 실행 

​		어떤 조건이 충족되면 그 함수를 이탈 한다. 

​		len 은 이미 int 이기때문에 int 쓸 필요 ㄴㄴ 

​	#data4 : 빈 바구니를 함수안에 넣어주면 사용자인터페이스에 더 가까 워 질 수 있다. 

​	information hiding 

* 주석을 먼저 코딩을 나중에 

> 여섯번 째 예시 _ 박소현 장예빈 

~~~~~~~~~~~~~~~~~~~~~~
Fisher-Yates sampling : 엄청유명 , 알고리즘과 동일
개선의 여지가 있음 (in-place swapping)

from random import randint

def shuffle3(data):
  new_list = data.copy() 		# copy 라는 명령어 써서 복사 
  result = []
  x = 0
  for x in range(len(data)):
    index = (randint(0, len(new_list) - 1)) #파이썬에서는 0부터 시작하기 때문에 len - 1해줘야함 
    result.append(new_list[index])
    del new_list[index]
    (x += 1) # 있어도되고 없어도 되고 
  print(result)
  
shuffle3([1, 2, 3, 4, 5])
~~~~~~~~~~~~~~~~~~~~~~

* 추가

  -각도 매핑 

  -fisher-yates algorithm 개선

   	제일 뒤에 있는 것과 남은 것 중 하나를 랜덤하게 뽑고 둘을바꾼다 => 메모리 효율 증가 

  * 얼마나 잘 섞였는 지 계산하기 