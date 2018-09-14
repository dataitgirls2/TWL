# 180827

## 오전수업 데이터 전처리(배로쌤)

### 데이터 전처리 심화

A = [1, 2, 3, 4, 5, 6, 7, 8, 9]

- `A[::]` [1, 2, 3, 4, 5, 6, 7, 8, 9]

- `A[::-1]` [9, 8, 7, 6, 5, 4, 3, 2, 1]
- `A[::-2]` [9, 7, 5, 3, 1]



```python
from sklearn.preprocessing import MinMaxScaler

def normalize_age(data):
    scaler = MinMaxScaler()
    data["Age"] = scaler.fit_transform(data["Age"].values.reshape(-1,1))
    return data


def normalize_fare(data):
    scaler = MinMaxScaler()
    data["Fare"] = scaler.fit_transform(data["Fare"].values.reshape(-1,1))
    return data

train_data = normalize_age(train_data)
test_data = normalize_age(test_data)

train_data = normalize_fare(train_data)
test_data = normalize_fare(test_data)

train_data.head()
```

