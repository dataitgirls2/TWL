
[View in Colaboratory](https://colab.research.google.com/github/soryeongk/TIL/blob/master/Dataitgirls/180708_python_sigma.ipynb)


```python
candidates = {
  'alan': [8, 14, 6, 8, 14, 9, 14, 9, 15, 5],
  'brad': [11, 4, 11, 7, 9, 7, 8, 7, 6],
  'cate': [16, 22, 15, 12, 3, 20, 17, 13, 23],
  'dave': [24, 15, 18, 18, 12, 9, 19, 23, 13, 14, 18]
}
```


```python
def average(list_data):
  return sum(list_data)/len(list_data)
average_list = sorted([(n, average(a)) for n, a in candidates.items()], key=lambda s: s[1], reverse=True)
average_list
```




    [('dave', 16.636363636363637),
     ('cate', 15.666666666666666),
     ('alan', 10.2),
     ('brad', 7.777777777777778)]




```python
def sigma(list_data): #[8, 14, 6, 8, 14, 9, 14, 9, 15, 5]
    return (sum((list_data[n]-average(list_data))**2 for n in range(len(list_data)))/len(list_data))**0.5
```


```python
sigma_list = sorted([(k,sigma(v)) for k,v in candidates.items()], key=lambda s: s[1])
print(sigma_list)
```

    [('brad', 2.1487866228681907), ('alan', 3.515679166249389), ('dave', 4.354156369028381), ('cate', 5.734883511361751)]
    
