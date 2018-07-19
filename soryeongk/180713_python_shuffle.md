
[View in Colaboratory](https://colab.research.google.com/github/soryeongk/TIL/blob/master/Dataitgirls/180713_python_shuffle.ipynb)


```python
from random import shuffle

def shuffle0(data):
    shuffle(data)
    return data

data0 = [1,2,3,4,5,6,7]
print(shuffle0(data0))
```

    [1, 6, 2, 4, 3, 7, 5]
    


```python
import random

def shuffle1(data):
    result = [0 for i in range(len(data))]
    index_list = []
    for index in range(len(data)):
        rand_index = random.randint(0,len(data)-1)
        while rand_index in index_list:
            rand_index = random.randint(0,len(data)-1)
        index_list.append(rand_index)
        result[index] = data[rand_index]
    return result

data1 = [3,2,4,5,6,7]
shuffle1(data1)
```




    [2, 3, 6, 4, 5, 7]




```python
# 랜덤수를 선정해서 그 만큼 오른쪽 왼쪽 왔다갔다.
import random

index_list = [i for i in range(len(data))]
new_index = []
for index in index_list:
    while index not in new_index:
        for r in range(random.randint(1,20)):
            index += 1
            if index > len(data)-1:
                index = 0
for datum in data:
    for n_index in new_index:
        result[n_index] = datum
    
data2 = [8,2,5,3,9,1]
temp_dict={}
for datum in data2:
    temp_dict[datum] = data2.index(datum)

```




    {1: 5, 2: 1, 3: 3, 5: 2, 8: 0, 9: 4}


