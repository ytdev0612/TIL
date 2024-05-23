```python
import pandas as pd
```


```python
s = pd.Series([9904312, 3448737, 2890451, 2466052],
              index=["서울", "부산", "인천", "대구"])
s
```




    서울    9904312
    부산    3448737
    인천    2890451
    대구    2466052
    dtype: int64




```python
pd.Series(range(10,14))
```




    0    10
    1    11
    2    12
    3    13
    dtype: int64




```python
s.index
```




    Index(['서울', '부산', '인천', '대구'], dtype='object')




```python
s.values
```




    array([9904312, 3448737, 2890451, 2466052], dtype=int64)




```python
s.name='인구'
s.index.name='도시'
```


```python
s
```




    도시
    서울    9904312
    부산    3448737
    인천    2890451
    대구    2466052
    Name: 인구, dtype: int64




```python
s/100 # 벡터화연산
```




    도시
    서울    99043.12
    부산    34487.37
    인천    28904.51
    대구    24660.52
    Name: 인구, dtype: float64




```python
s['부산']
```




    3448737




```python
# s[1]
s.iloc[1]
```




    3448737




```python
s
s[[0,3,1]]
s.iloc[[0,3,1]]
s[['서울', '대구', '부산']]
```




    도시
    서울    9904312
    대구    2466052
    부산    3448737
    Name: 인구, dtype: int64




```python
s
s[['부산','인천']]
s.iloc[[1,2]]
```




    도시
    부산    3448737
    인천    2890451
    Name: 인구, dtype: int64




```python
s[1:3]
s.iloc[1:3]
```




    도시
    부산    3448737
    인천    2890451
    Name: 인구, dtype: int64




```python
s
s['부산':'인천'] # 번호로 주면 끝 포함 x, 라벨은 끝 포함 o
```




    도시
    부산    3448737
    인천    2890451
    Name: 인구, dtype: int64




```python
s.부산
s.인천
```




    2890451




```python
s
```




    도시
    서울    9904312
    부산    3448737
    인천    2890451
    대구    2466052
    Name: 인구, dtype: int64




```python
'부산' in s
```




    True




```python
for k, v in s.items():
    print(k, v)
```

    서울 9904312
    부산 3448737
    인천 2890451
    대구 2466052
    


```python
s2 = pd.Series({"서울": 9631482, "부산": 3393191, "인천": 2632035, "대전": 1490158},
              index=['대전', '인천', '부산', '서울']) # 내가 지정한 순서대로 데이터 출력
s2 # 2015년 인구로 가정
```




    대전    1490158
    인천    2632035
    부산    3393191
    서울    9631482
    dtype: int64




```python
# s = pd.Series([9904312, 3448737, 2890451, 2466052],
#               index=["서울", "부산", "인천", "대구"])
s # 2010년도 인구로 가정
```




    도시
    서울    9904312
    부산    3448737
    인천    2890451
    대구    2466052
    Name: 인구, dtype: int64




```python
s-s2
```




    대구         NaN
    대전         NaN
    부산     55546.0
    서울    272830.0
    인천    258416.0
    dtype: float64




```python
# Series 간 연산시 양쪽 모두 자료가 존재하면 계산이 수행
# 어느 한쪽만 자료가 존재하면 NaN(Not a Number)이 나오고, 전체 결과 자료형 또한 float로 변환됨
ds = s-s2
ds
```




    대구         NaN
    대전         NaN
    부산     55546.0
    서울    272830.0
    인천    258416.0
    dtype: float64




```python
s.values
s2.values
```




    array([1490158, 2632035, 3393191, 9631482], dtype=int64)




```python
s.values - s2.values
```




    array([ 8414154,   816702,  -502740, -7165430], dtype=int64)




```python
ds
```




    대구         NaN
    대전         NaN
    부산     55546.0
    서울    272830.0
    인천    258416.0
    dtype: float64




```python
ds.notnull()
```




    대구    False
    대전    False
    부산     True
    서울     True
    인천     True
    dtype: bool




```python
ds[ds.notnull()]
```




    부산     55546.0
    서울    272830.0
    인천    258416.0
    dtype: float64




```python
s # 2010년도 인구
```




    도시
    서울    9904312
    부산    3448737
    인천    2890451
    대구    2466052
    Name: 인구, dtype: int64




```python
s2 # 2015년도 인구
```




    대전    1490158
    인천    2632035
    부산    3393191
    서울    9631482
    dtype: int64




```python
# 서울, 부산, 인천 도시에 대한 인구 증가(감소)율(%)을 출력하시오
rs = (s-s2)/s2*100
rs
rs = rs[rs.notnull()]
rs
```




    부산    1.636984
    서울    2.832690
    인천    9.818107
    dtype: float64




```python
rs['부산']
rs['부산']=1.63
rs['부산']
```




    1.63




```python
del rs['서울']
```


```python
rs
```




    부산    1.630000
    인천    9.818107
    dtype: float64




```python
obj = pd.Series([4, 7, -5, 3])
obj
```




    0    4
    1    7
    2   -5
    3    3
    dtype: int64




```python
obj.array
obj.index
```




    RangeIndex(start=0, stop=4, step=1)




```python
obj2 = pd.Series([4, 7, -5, 3], index=["d", "b", "a", "c"])
obj2
```




    d    4
    b    7
    a   -5
    c    3
    dtype: int64




```python
obj2.array
obj2.index
```




    Index(['d', 'b', 'a', 'c'], dtype='object')




```python
obj2['a']
```




    -5




```python
obj2['d'] = 6
obj2['d']
```




    6




```python
obj2
```




    d    6
    b    7
    a   -5
    c    3
    dtype: int64




```python
obj2[['c', 'a', 'd']]
```




    c    3
    a   -5
    d    6
    dtype: int64




```python
obj2[obj2 > 0]
```




    d    6
    b    7
    c    3
    dtype: int64




```python
'b' in obj2
```




    True




```python
sdata = {"Ohio": 35000, "Texas": 71000, "Oregon": 16000, "Utah": 5000}
sdata
```




    {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}




```python
obj3 = pd.Series(sdata)
obj3
```




    Ohio      35000
    Texas     71000
    Oregon    16000
    Utah       5000
    dtype: int64




```python
obj3.to_dict()
```




    {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}




```python
pd.Series(sdata)
```




    Ohio      35000
    Texas     71000
    Oregon    16000
    Utah       5000
    dtype: int64




```python
states = ["California", "Ohio", "Oregon", "Texas"]
states
```




    ['California', 'Ohio', 'Oregon', 'Texas']




```python
obj4 = pd.Series(sdata, index=states)
obj4
```




    California        NaN
    Ohio          35000.0
    Oregon        16000.0
    Texas         71000.0
    dtype: float64




```python
obj4.notnull()
obj4.notna()

pd.notnull(obj4)
pd.notna(obj4)
```




    California    False
    Ohio           True
    Oregon         True
    Texas          True
    dtype: bool




```python
obj4.isnull()
obj4.isna()

pd.isnull(obj4)
pd.isna(obj4)
```




    California     True
    Ohio          False
    Oregon        False
    Texas         False
    dtype: bool




```python
obj3
```




    Ohio      35000
    Texas     71000
    Oregon    16000
    Utah       5000
    dtype: int64




```python
obj4
```




    California        NaN
    Ohio          35000.0
    Oregon        16000.0
    Texas         71000.0
    dtype: float64




```python
obj3+obj4
```




    California         NaN
    Ohio           70000.0
    Oregon         32000.0
    Texas         142000.0
    Utah               NaN
    dtype: float64




```python
obj4.name = "population"
obj4.index.name = "state"
obj4
```




    state
    California        NaN
    Ohio          35000.0
    Oregon        16000.0
    Texas         71000.0
    Name: population, dtype: float64




```python
obj
```




    0    4
    1    7
    2   -5
    3    3
    dtype: int64




```python
obj.index = ["Bob", "Steve", "Jeff", "Ryan"]
```


```python
obj
```




    Bob      4
    Steve    7
    Jeff    -5
    Ryan     3
    dtype: int64




```python
data = {"state": ["Ohio", "Ohio", "Ohio", "Nevada", "Nevada", "Nevada"],
        "year": [2000, 2001, 2002, 2001, 2002, 2003],
        "pop": [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
data
```




    {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
     'year': [2000, 2001, 2002, 2001, 2002, 2003],
     'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}




```python
pd.Series(data)
```




    state    [Ohio, Ohio, Ohio, Nevada, Nevada, Nevada]
    year           [2000, 2001, 2002, 2001, 2002, 2003]
    pop                  [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]
    dtype: object




```python
frame = pd.DataFrame(data) # dict의 키가 dataframe의 열 이름, value에 해당하는 것들이 각각의 데이터로 옴
frame
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
      <th>state</th>
      <th>year</th>
      <th>pop</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Ohio</td>
      <td>2000</td>
      <td>1.5</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Ohio</td>
      <td>2001</td>
      <td>1.7</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Ohio</td>
      <td>2002</td>
      <td>3.6</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Nevada</td>
      <td>2001</td>
      <td>2.4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Nevada</td>
      <td>2002</td>
      <td>2.9</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Nevada</td>
      <td>2003</td>
      <td>3.2</td>
    </tr>
  </tbody>
</table>
</div>




```python
# data2 = {"state": ["Ohio", "Ohio", "Ohio", "Nevada", "Nevada", "Nevada"],
#         "year": [2000, 2001, 2002, 2001, 2002, 2003],
#         "pop": [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
# pd.DataFrame(data2)
```


```python
frame.head()
frame.tail()
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
      <th>state</th>
      <th>year</th>
      <th>pop</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>Ohio</td>
      <td>2001</td>
      <td>1.7</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Ohio</td>
      <td>2002</td>
      <td>3.6</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Nevada</td>
      <td>2001</td>
      <td>2.4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Nevada</td>
      <td>2002</td>
      <td>2.9</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Nevada</td>
      <td>2003</td>
      <td>3.2</td>
    </tr>
  </tbody>
</table>
</div>




```python
data
```




    {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
     'year': [2000, 2001, 2002, 2001, 2002, 2003],
     'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}




```python
pd.DataFrame(data, columns=["year", "state", "pop"])
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
      <th>year</th>
      <th>state</th>
      <th>pop</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2000</td>
      <td>Ohio</td>
      <td>1.5</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2001</td>
      <td>Ohio</td>
      <td>1.7</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2002</td>
      <td>Ohio</td>
      <td>3.6</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2001</td>
      <td>Nevada</td>
      <td>2.4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2002</td>
      <td>Nevada</td>
      <td>2.9</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2003</td>
      <td>Nevada</td>
      <td>3.2</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame2 = pd.DataFrame(data, columns=["year", "state", "pop", "debt"])
frame2
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
      <th>year</th>
      <th>state</th>
      <th>pop</th>
      <th>debt</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2000</td>
      <td>Ohio</td>
      <td>1.5</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2001</td>
      <td>Ohio</td>
      <td>1.7</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2002</td>
      <td>Ohio</td>
      <td>3.6</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2001</td>
      <td>Nevada</td>
      <td>2.4</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2002</td>
      <td>Nevada</td>
      <td>2.9</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2003</td>
      <td>Nevada</td>
      <td>3.2</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame2.index
```




    RangeIndex(start=0, stop=6, step=1)




```python
frame2.columns
```




    Index(['year', 'state', 'pop', 'debt'], dtype='object')




```python
frame2['state']
```




    0      Ohio
    1      Ohio
    2      Ohio
    3    Nevada
    4    Nevada
    5    Nevada
    Name: state, dtype: object




```python
frame2.state
```




    0      Ohio
    1      Ohio
    2      Ohio
    3    Nevada
    4    Nevada
    5    Nevada
    Name: state, dtype: object




```python
frame2.iloc[2]
```




    year     2002
    state    Ohio
    pop       3.6
    debt      NaN
    Name: 2, dtype: object




```python
frame2.loc[2]
```




    year     2002
    state    Ohio
    pop       3.6
    debt      NaN
    Name: 2, dtype: object




```python
# iloc : 고유의 행 인덱스 번호를 지정하여 자료를 참조
# loc :행 인덱스 라벨을 지정하여 자료를 참조
frame2
# loc : frame2를 출력했을 때 눈에 보이는 행 인덱스 라벨을 지정하여 자료 참조
# iloc : frame2를 출력했을 때 눈에 보이지 않는 고유의 인덱스 번호(0~5번...) -> 행 인덱스 라벨
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
      <th>year</th>
      <th>state</th>
      <th>pop</th>
      <th>debt</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2000</td>
      <td>Ohio</td>
      <td>1.5</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2001</td>
      <td>Ohio</td>
      <td>1.7</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2002</td>
      <td>Ohio</td>
      <td>3.6</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2001</td>
      <td>Nevada</td>
      <td>2.4</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2002</td>
      <td>Nevada</td>
      <td>2.9</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2003</td>
      <td>Nevada</td>
      <td>3.2</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame2.loc[1]
```




    year     2001
    state    Ohio
    pop       1.7
    debt      NaN
    Name: 1, dtype: object




```python
frame2.iloc[1]
```




    year     2001
    state    Ohio
    pop       1.7
    debt      NaN
    Name: 1, dtype: object




```python
frame2.iloc[-1]
```




    year       2003
    state    Nevada
    pop         3.2
    debt        NaN
    Name: 5, dtype: object




```python
# frame2.loc[-1] error 발생
```


```python
s
```




    도시
    서울    9904312
    부산    3448737
    인천    2890451
    대구    2466052
    Name: 인구, dtype: int64




```python
s.loc['서울']
```




    9904312




```python
# s.iloc['서울'] error 발생, 고유번호
s.iloc[0]
```




    9904312




```python
s.iloc[-1]
```




    2466052




```python
frame2
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
      <th>year</th>
      <th>state</th>
      <th>pop</th>
      <th>debt</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2000</td>
      <td>Ohio</td>
      <td>1.5</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2001</td>
      <td>Ohio</td>
      <td>1.7</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2002</td>
      <td>Ohio</td>
      <td>3.6</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2001</td>
      <td>Nevada</td>
      <td>2.4</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2002</td>
      <td>Nevada</td>
      <td>2.9</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2003</td>
      <td>Nevada</td>
      <td>3.2</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame2['debt']
```




    0    NaN
    1    NaN
    2    NaN
    3    NaN
    4    NaN
    5    NaN
    Name: debt, dtype: object




```python
# 데이터프레임의 특정 행/열을 추출하면 시리즈가 나오게 됨
```


```python
frame2.loc[2]
```




    year     2002
    state    Ohio
    pop       3.6
    debt      NaN
    Name: 2, dtype: object




```python
frame2['dept'] = 16.5
```


```python
frame2
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
      <th>year</th>
      <th>state</th>
      <th>pop</th>
      <th>debt</th>
      <th>dept</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2000</td>
      <td>Ohio</td>
      <td>1.5</td>
      <td>0.0</td>
      <td>16.5</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2001</td>
      <td>Ohio</td>
      <td>1.7</td>
      <td>1.0</td>
      <td>16.5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2002</td>
      <td>Ohio</td>
      <td>3.6</td>
      <td>2.0</td>
      <td>16.5</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2001</td>
      <td>Nevada</td>
      <td>2.4</td>
      <td>3.0</td>
      <td>16.5</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2002</td>
      <td>Nevada</td>
      <td>2.9</td>
      <td>4.0</td>
      <td>16.5</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2003</td>
      <td>Nevada</td>
      <td>3.2</td>
      <td>5.0</td>
      <td>16.5</td>
    </tr>
  </tbody>
</table>
</div>




```python
del frame2['dept']
```


```python
frame2
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
      <th>year</th>
      <th>state</th>
      <th>pop</th>
      <th>debt</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2000</td>
      <td>Ohio</td>
      <td>1.5</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2001</td>
      <td>Ohio</td>
      <td>1.7</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2002</td>
      <td>Ohio</td>
      <td>3.6</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2001</td>
      <td>Nevada</td>
      <td>2.4</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2002</td>
      <td>Nevada</td>
      <td>2.9</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2003</td>
      <td>Nevada</td>
      <td>3.2</td>
      <td>5.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
import numpy as np
```


```python
frame2["debt"] = np.arange(6.)
```


```python
frame2
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
      <th>year</th>
      <th>state</th>
      <th>pop</th>
      <th>debt</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2000</td>
      <td>Ohio</td>
      <td>1.5</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2001</td>
      <td>Ohio</td>
      <td>1.7</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2002</td>
      <td>Ohio</td>
      <td>3.6</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2001</td>
      <td>Nevada</td>
      <td>2.4</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2002</td>
      <td>Nevada</td>
      <td>2.9</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2003</td>
      <td>Nevada</td>
      <td>3.2</td>
      <td>5.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
val = pd.Series([-1.2, -1.5, -1.7], index=["two", "four", "five"])
val
```




    two    -1.2
    four   -1.5
    five   -1.7
    dtype: float64




```python
type(val)
```




    pandas.core.series.Series




```python
frame2
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
      <th>year</th>
      <th>state</th>
      <th>pop</th>
      <th>debt</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2000</td>
      <td>Ohio</td>
      <td>1.5</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2001</td>
      <td>Ohio</td>
      <td>1.7</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2002</td>
      <td>Ohio</td>
      <td>3.6</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2001</td>
      <td>Nevada</td>
      <td>2.4</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2002</td>
      <td>Nevada</td>
      <td>2.9</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2003</td>
      <td>Nevada</td>
      <td>3.2</td>
      <td>5.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
val
```




    two    -1.2
    four   -1.5
    five   -1.7
    dtype: float64




```python
frame2["debt"] = val
frame2
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
      <th>year</th>
      <th>state</th>
      <th>pop</th>
      <th>debt</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2000</td>
      <td>Ohio</td>
      <td>1.5</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2001</td>
      <td>Ohio</td>
      <td>1.7</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2002</td>
      <td>Ohio</td>
      <td>3.6</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2001</td>
      <td>Nevada</td>
      <td>2.4</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2002</td>
      <td>Nevada</td>
      <td>2.9</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2003</td>
      <td>Nevada</td>
      <td>3.2</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame2['state']
```




    0      Ohio
    1      Ohio
    2      Ohio
    3    Nevada
    4    Nevada
    5    Nevada
    Name: state, dtype: object




```python
frame2['eastern'] = frame2['state'] == 'Ohio'
```


```python
frame2
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
      <th>year</th>
      <th>state</th>
      <th>pop</th>
      <th>debt</th>
      <th>eastern</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2000</td>
      <td>Ohio</td>
      <td>1.5</td>
      <td>NaN</td>
      <td>True</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2001</td>
      <td>Ohio</td>
      <td>1.7</td>
      <td>NaN</td>
      <td>True</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2002</td>
      <td>Ohio</td>
      <td>3.6</td>
      <td>NaN</td>
      <td>True</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2001</td>
      <td>Nevada</td>
      <td>2.4</td>
      <td>NaN</td>
      <td>False</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2002</td>
      <td>Nevada</td>
      <td>2.9</td>
      <td>NaN</td>
      <td>False</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2003</td>
      <td>Nevada</td>
      <td>3.2</td>
      <td>NaN</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>




```python
del frame2['eastern']
```


```python
frame2
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
      <th>year</th>
      <th>state</th>
      <th>pop</th>
      <th>debt</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2000</td>
      <td>Ohio</td>
      <td>1.5</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2001</td>
      <td>Ohio</td>
      <td>1.7</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2002</td>
      <td>Ohio</td>
      <td>3.6</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2001</td>
      <td>Nevada</td>
      <td>2.4</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2002</td>
      <td>Nevada</td>
      <td>2.9</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2003</td>
      <td>Nevada</td>
      <td>3.2</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame2.columns
```




    Index(['year', 'state', 'pop', 'debt'], dtype='object')




```python
populations = {"Ohio": {2000: 1.5, 2001: 1.7, 2002: 3.6},
               "Nevada": {2001: 2.4, 2002: 2.9, 2003: 3.1}}
populations
```




    {'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6},
     'Nevada': {2001: 2.4, 2002: 2.9, 2003: 3.1}}




```python
pd.DataFrame(populations)
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
      <th>Ohio</th>
      <th>Nevada</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2000</th>
      <td>1.5</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2001</th>
      <td>1.7</td>
      <td>2.4</td>
    </tr>
    <tr>
      <th>2002</th>
      <td>3.6</td>
      <td>2.9</td>
    </tr>
    <tr>
      <th>2003</th>
      <td>NaN</td>
      <td>3.1</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame3 = pd.DataFrame(populations)
frame3
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
      <th>Ohio</th>
      <th>Nevada</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2000</th>
      <td>1.5</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2001</th>
      <td>1.7</td>
      <td>2.4</td>
    </tr>
    <tr>
      <th>2002</th>
      <td>3.6</td>
      <td>2.9</td>
    </tr>
    <tr>
      <th>2003</th>
      <td>NaN</td>
      <td>3.1</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame3.T
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
      <th>2000</th>
      <th>2001</th>
      <th>2002</th>
      <th>2003</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Ohio</th>
      <td>1.5</td>
      <td>1.7</td>
      <td>3.6</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Nevada</th>
      <td>NaN</td>
      <td>2.4</td>
      <td>2.9</td>
      <td>3.1</td>
    </tr>
  </tbody>
</table>
</div>




```python
populations
```




    {'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6},
     'Nevada': {2001: 2.4, 2002: 2.9, 2003: 3.1}}




```python
pd.DataFrame(populations)
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
      <th>Ohio</th>
      <th>Nevada</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2000</th>
      <td>1.5</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2001</th>
      <td>1.7</td>
      <td>2.4</td>
    </tr>
    <tr>
      <th>2002</th>
      <td>3.6</td>
      <td>2.9</td>
    </tr>
    <tr>
      <th>2003</th>
      <td>NaN</td>
      <td>3.1</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.DataFrame(populations, index=[2001, 2002])
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
      <th>Ohio</th>
      <th>Nevada</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2001</th>
      <td>1.7</td>
      <td>2.4</td>
    </tr>
    <tr>
      <th>2002</th>
      <td>3.6</td>
      <td>2.9</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.DataFrame(populations, index=[2001, 2002, 2004])
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
      <th>Ohio</th>
      <th>Nevada</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2001</th>
      <td>1.7</td>
      <td>2.4</td>
    </tr>
    <tr>
      <th>2002</th>
      <td>3.6</td>
      <td>2.9</td>
    </tr>
    <tr>
      <th>2004</th>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame3
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
      <th>Ohio</th>
      <th>Nevada</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2000</th>
      <td>1.5</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2001</th>
      <td>1.7</td>
      <td>2.4</td>
    </tr>
    <tr>
      <th>2002</th>
      <td>3.6</td>
      <td>2.9</td>
    </tr>
    <tr>
      <th>2003</th>
      <td>NaN</td>
      <td>3.1</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame3['Ohio']
```




    2000    1.5
    2001    1.7
    2002    3.6
    2003    NaN
    Name: Ohio, dtype: float64




```python
frame3['Ohio'][:2]
frame3['Ohio'].head(2)
frame3['Ohio'].iloc[[0,1]]
```




    2000    1.5
    2001    1.7
    Name: Ohio, dtype: float64




```python
frame3['Nevada'][:-2]
```




    2000    NaN
    2001    2.4
    Name: Nevada, dtype: float64




```python
pd.DataFrame({
    'Ohio': frame3['Ohio'][:2],
    'Nevada': frame3['Nevada'][:-2]
})
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
      <th>Ohio</th>
      <th>Nevada</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2000</th>
      <td>1.5</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2001</th>
      <td>1.7</td>
      <td>2.4</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame3
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
      <th>Ohio</th>
      <th>Nevada</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2000</th>
      <td>1.5</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2001</th>
      <td>1.7</td>
      <td>2.4</td>
    </tr>
    <tr>
      <th>2002</th>
      <td>3.6</td>
      <td>2.9</td>
    </tr>
    <tr>
      <th>2003</th>
      <td>NaN</td>
      <td>3.1</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame3.index.name='year'
```


```python
frame3.columns
```




    Index(['Ohio', 'Nevada'], dtype='object')




```python
frame3.columns.name = 'state'
```


```python
frame3
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
      <th>state</th>
      <th>Ohio</th>
      <th>Nevada</th>
    </tr>
    <tr>
      <th>year</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2000</th>
      <td>1.5</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2001</th>
      <td>1.7</td>
      <td>2.4</td>
    </tr>
    <tr>
      <th>2002</th>
      <td>3.6</td>
      <td>2.9</td>
    </tr>
    <tr>
      <th>2003</th>
      <td>NaN</td>
      <td>3.1</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame3.to_numpy()
```




    array([[1.5, nan],
           [1.7, 2.4],
           [3.6, 2.9],
           [nan, 3.1]])




```python
frame2
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
      <th>year</th>
      <th>state</th>
      <th>pop</th>
      <th>debt</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2000</td>
      <td>Ohio</td>
      <td>1.5</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2001</td>
      <td>Ohio</td>
      <td>1.7</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2002</td>
      <td>Ohio</td>
      <td>3.6</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2001</td>
      <td>Nevada</td>
      <td>2.4</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2002</td>
      <td>Nevada</td>
      <td>2.9</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2003</td>
      <td>Nevada</td>
      <td>3.2</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame2.to_numpy()
```




    array([[2000, 'Ohio', 1.5, nan],
           [2001, 'Ohio', 1.7, nan],
           [2002, 'Ohio', 3.6, nan],
           [2001, 'Nevada', 2.4, nan],
           [2002, 'Nevada', 2.9, nan],
           [2003, 'Nevada', 3.2, nan]], dtype=object)




```python
obj = pd.Series(np.arange(3), index=["a", "b", "c"])
obj
```




    a    0
    b    1
    c    2
    dtype: int32




```python
obj.index
```




    Index(['a', 'b', 'c'], dtype='object')




```python
index=obj.index
```


```python
index[1:]
```




    Index(['b', 'c'], dtype='object')




```python
obj2 = pd.Series([1.5, -2.5, 0], index=np.arange(1,4))
obj2
```




    1    1.5
    2   -2.5
    3    0.0
    dtype: float64




```python
4 in obj2.index
```




    False




```python
frame3
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
      <th>state</th>
      <th>Ohio</th>
      <th>Nevada</th>
    </tr>
    <tr>
      <th>year</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2000</th>
      <td>1.5</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2001</th>
      <td>1.7</td>
      <td>2.4</td>
    </tr>
    <tr>
      <th>2002</th>
      <td>3.6</td>
      <td>2.9</td>
    </tr>
    <tr>
      <th>2003</th>
      <td>NaN</td>
      <td>3.1</td>
    </tr>
  </tbody>
</table>
</div>




```python
2024 in frame3.index
'Utah' in frame3.columns
```




    False




```python
obj = pd.Series([4.5, 7.2, -5.3, 3.6], index=["d", "b", "a", "c"])
obj
```




    d    4.5
    b    7.2
    a   -5.3
    c    3.6
    dtype: float64




```python
obj.index
```




    Index(['d', 'b', 'a', 'c'], dtype='object')




```python
obj.reindex(["a", "b", "c", "d", "e"])
```




    a   -5.3
    b    7.2
    c    3.6
    d    4.5
    e    NaN
    dtype: float64




```python
obj2 = obj.reindex(["a", "b", "c", "d", "e"])
obj2
```




    a   -5.3
    b    7.2
    c    3.6
    d    4.5
    e    NaN
    dtype: float64




```python
obj3 = pd.Series(["blue", "purple", "yellow"], index=[0, 2, 4])
obj3
```




    0      blue
    2    purple
    4    yellow
    dtype: object




```python
obj3.reindex(np.arange(6))
```




    0      blue
    1       NaN
    2    purple
    3       NaN
    4    yellow
    5       NaN
    dtype: object




```python
obj3.reindex(np.arange(6), method='ffill') # 결측값을 대체할 때 방향을 forward(위->아래) fill
obj3.reindex(np.arange(6), method='bfill') # 결측값을 대체할 때 방향을 backward(아래->위) fill
```




    0      blue
    1    purple
    2    purple
    3    yellow
    4    yellow
    5       NaN
    dtype: object




```python
frame = pd.DataFrame(np.arange(9).reshape((3, 3)),
                     index=["a", "c", "d"],
                     columns=["Ohio", "Texas", "California"])
frame
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
      <th>Ohio</th>
      <th>Texas</th>
      <th>California</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>0</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>c</th>
      <td>3</td>
      <td>4</td>
      <td>5</td>
    </tr>
    <tr>
      <th>d</th>
      <td>6</td>
      <td>7</td>
      <td>8</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame2 = frame.reindex(index=["a", "b", "c", "d"])
frame2
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
      <th>Ohio</th>
      <th>Texas</th>
      <th>California</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>0.0</td>
      <td>1.0</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>b</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>c</th>
      <td>3.0</td>
      <td>4.0</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>d</th>
      <td>6.0</td>
      <td>7.0</td>
      <td>8.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
states = ["Texas", "Utah", "California"]
```


```python
frame
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
      <th>Ohio</th>
      <th>Texas</th>
      <th>California</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>0</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>c</th>
      <td>3</td>
      <td>4</td>
      <td>5</td>
    </tr>
    <tr>
      <th>d</th>
      <td>6</td>
      <td>7</td>
      <td>8</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame.reindex(columns=states)
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
      <th>Texas</th>
      <th>Utah</th>
      <th>California</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>1</td>
      <td>NaN</td>
      <td>2</td>
    </tr>
    <tr>
      <th>c</th>
      <td>4</td>
      <td>NaN</td>
      <td>5</td>
    </tr>
    <tr>
      <th>d</th>
      <td>7</td>
      <td>NaN</td>
      <td>8</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame
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
      <th>Ohio</th>
      <th>Texas</th>
      <th>California</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>0</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>c</th>
      <td>3</td>
      <td>4</td>
      <td>5</td>
    </tr>
    <tr>
      <th>d</th>
      <td>6</td>
      <td>7</td>
      <td>8</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame.loc[['a', 'd', 'c']]
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
      <th>Ohio</th>
      <th>Texas</th>
      <th>California</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>0</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>d</th>
      <td>6</td>
      <td>7</td>
      <td>8</td>
    </tr>
    <tr>
      <th>c</th>
      <td>3</td>
      <td>4</td>
      <td>5</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame.loc[['a','d','c'],'California']
frame.loc[['a','d','c'],['California','Texas']]
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
      <th>California</th>
      <th>Texas</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>2</td>
      <td>1</td>
    </tr>
    <tr>
      <th>d</th>
      <td>8</td>
      <td>7</td>
    </tr>
    <tr>
      <th>c</th>
      <td>5</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>




```python
obj = pd.Series(np.arange(5.), index=["a", "b", "c", "d", "e"])
obj
```




    a    0.0
    b    1.0
    c    2.0
    d    3.0
    e    4.0
    dtype: float64




```python
new_obj=obj.drop('c')
new_obj
```




    a    0.0
    b    1.0
    d    3.0
    e    4.0
    dtype: float64




```python
obj
```




    a    0.0
    b    1.0
    c    2.0
    d    3.0
    e    4.0
    dtype: float64




```python
obj.drop(['d', 'c'])
```




    a    0.0
    b    1.0
    e    4.0
    dtype: float64




```python
data = pd.DataFrame(np.arange(16).reshape((4, 4)),
                    index=["Ohio", "Colorado", "Utah", "New York"],
                    columns=["one", "two", "three", "four"])
data
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
      <th>one</th>
      <th>two</th>
      <th>three</th>
      <th>four</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Ohio</th>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>3</td>
    </tr>
    <tr>
      <th>Colorado</th>
      <td>4</td>
      <td>5</td>
      <td>6</td>
      <td>7</td>
    </tr>
    <tr>
      <th>Utah</th>
      <td>8</td>
      <td>9</td>
      <td>10</td>
      <td>11</td>
    </tr>
    <tr>
      <th>New York</th>
      <td>12</td>
      <td>13</td>
      <td>14</td>
      <td>15</td>
    </tr>
  </tbody>
</table>
</div>




```python
data.drop(["Colorado", "Ohio"])
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
      <th>one</th>
      <th>two</th>
      <th>three</th>
      <th>four</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Utah</th>
      <td>8</td>
      <td>9</td>
      <td>10</td>
      <td>11</td>
    </tr>
    <tr>
      <th>New York</th>
      <td>12</td>
      <td>13</td>
      <td>14</td>
      <td>15</td>
    </tr>
  </tbody>
</table>
</div>




```python
data
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
      <th>one</th>
      <th>two</th>
      <th>three</th>
      <th>four</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Ohio</th>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>3</td>
    </tr>
    <tr>
      <th>Colorado</th>
      <td>4</td>
      <td>5</td>
      <td>6</td>
      <td>7</td>
    </tr>
    <tr>
      <th>Utah</th>
      <td>8</td>
      <td>9</td>
      <td>10</td>
      <td>11</td>
    </tr>
    <tr>
      <th>New York</th>
      <td>12</td>
      <td>13</td>
      <td>14</td>
      <td>15</td>
    </tr>
  </tbody>
</table>
</div>




```python
# data.drop('two') error발생, 'two'라는 행 index가 없음
# data.drop(columns='two')
# data.drop('two', axis=1)
data.drop('two', axis='columns')
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
      <th>one</th>
      <th>three</th>
      <th>four</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Ohio</th>
      <td>0</td>
      <td>2</td>
      <td>3</td>
    </tr>
    <tr>
      <th>Colorado</th>
      <td>4</td>
      <td>6</td>
      <td>7</td>
    </tr>
    <tr>
      <th>Utah</th>
      <td>8</td>
      <td>10</td>
      <td>11</td>
    </tr>
    <tr>
      <th>New York</th>
      <td>12</td>
      <td>14</td>
      <td>15</td>
    </tr>
  </tbody>
</table>
</div>




```python
data
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
      <th>one</th>
      <th>two</th>
      <th>three</th>
      <th>four</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Ohio</th>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>3</td>
    </tr>
    <tr>
      <th>Colorado</th>
      <td>4</td>
      <td>5</td>
      <td>6</td>
      <td>7</td>
    </tr>
    <tr>
      <th>Utah</th>
      <td>8</td>
      <td>9</td>
      <td>10</td>
      <td>11</td>
    </tr>
    <tr>
      <th>New York</th>
      <td>12</td>
      <td>13</td>
      <td>14</td>
      <td>15</td>
    </tr>
  </tbody>
</table>
</div>




```python
data.drop('two', axis='columns', inplace=True)
```


```python
data
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
      <th>one</th>
      <th>three</th>
      <th>four</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Ohio</th>
      <td>0</td>
      <td>2</td>
      <td>3</td>
    </tr>
    <tr>
      <th>Colorado</th>
      <td>4</td>
      <td>6</td>
      <td>7</td>
    </tr>
    <tr>
      <th>Utah</th>
      <td>8</td>
      <td>10</td>
      <td>11</td>
    </tr>
    <tr>
      <th>New York</th>
      <td>12</td>
      <td>14</td>
      <td>15</td>
    </tr>
  </tbody>
</table>
</div>




```python
obj = pd.Series(np.arange(4.), index=["a", "b", "c", "d"])
obj
```




    a    0.0
    b    1.0
    c    2.0
    d    3.0
    dtype: float64




```python
obj[1]
obj[2:4]
obj[[1,3]] # obj.iloc[[1,3]]
obj[obj<2]
```




    a    0.0
    b    1.0
    dtype: float64




```python
obj1 = pd.Series([1, 2, 3], index=[2, 0, 1])
obj2 = pd.Series([1, 2, 3], index=["a", "b", "c"])
```


```python
obj1
```




    2    1
    0    2
    1    3
    dtype: int64




```python
obj2
```




    a    1
    b    2
    c    3
    dtype: int64




```python
obj1.iloc[:3]
obj1.loc[[2,0,1]]
```




    2    1
    0    2
    1    3
    dtype: int64




```python
obj2.loc['b':'c']
```




    b    2
    c    3
    dtype: int64




```python
obj2.loc['b':'c']=10
```


```python
obj2
```




    a     1
    b    10
    c    10
    dtype: int64




```python
data = pd.DataFrame(np.arange(16).reshape((4, 4)),
                    index=["Ohio", "Colorado", "Utah", "New York"],
                    columns=["one", "two", "three", "four"])
data
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
      <th>one</th>
      <th>two</th>
      <th>three</th>
      <th>four</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Ohio</th>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>3</td>
    </tr>
    <tr>
      <th>Colorado</th>
      <td>4</td>
      <td>5</td>
      <td>6</td>
      <td>7</td>
    </tr>
    <tr>
      <th>Utah</th>
      <td>8</td>
      <td>9</td>
      <td>10</td>
      <td>11</td>
    </tr>
    <tr>
      <th>New York</th>
      <td>12</td>
      <td>13</td>
      <td>14</td>
      <td>15</td>
    </tr>
  </tbody>
</table>
</div>




```python
data['two']
```




    Ohio         1
    Colorado     5
    Utah         9
    New York    13
    Name: two, dtype: int32




```python
data[["three", "one"]]
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
      <th>three</th>
      <th>one</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Ohio</th>
      <td>2</td>
      <td>0</td>
    </tr>
    <tr>
      <th>Colorado</th>
      <td>6</td>
      <td>4</td>
    </tr>
    <tr>
      <th>Utah</th>
      <td>10</td>
      <td>8</td>
    </tr>
    <tr>
      <th>New York</th>
      <td>14</td>
      <td>12</td>
    </tr>
  </tbody>
</table>
</div>




```python
data[:2]
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
      <th>one</th>
      <th>two</th>
      <th>three</th>
      <th>four</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Ohio</th>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>3</td>
    </tr>
    <tr>
      <th>Colorado</th>
      <td>4</td>
      <td>5</td>
      <td>6</td>
      <td>7</td>
    </tr>
  </tbody>
</table>
</div>




```python
data
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
      <th>one</th>
      <th>two</th>
      <th>three</th>
      <th>four</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Ohio</th>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>3</td>
    </tr>
    <tr>
      <th>Colorado</th>
      <td>4</td>
      <td>5</td>
      <td>6</td>
      <td>7</td>
    </tr>
    <tr>
      <th>Utah</th>
      <td>8</td>
      <td>9</td>
      <td>10</td>
      <td>11</td>
    </tr>
    <tr>
      <th>New York</th>
      <td>12</td>
      <td>13</td>
      <td>14</td>
      <td>15</td>
    </tr>
  </tbody>
</table>
</div>




```python
# three열 값이 5보다 큰 자료를 추출
data[data['three']>5]
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
      <th>one</th>
      <th>two</th>
      <th>three</th>
      <th>four</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Colorado</th>
      <td>4</td>
      <td>5</td>
      <td>6</td>
      <td>7</td>
    </tr>
    <tr>
      <th>Utah</th>
      <td>8</td>
      <td>9</td>
      <td>10</td>
      <td>11</td>
    </tr>
    <tr>
      <th>New York</th>
      <td>12</td>
      <td>13</td>
      <td>14</td>
      <td>15</td>
    </tr>
  </tbody>
</table>
</div>




```python
data
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
      <th>one</th>
      <th>two</th>
      <th>three</th>
      <th>four</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Ohio</th>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>3</td>
    </tr>
    <tr>
      <th>Colorado</th>
      <td>4</td>
      <td>5</td>
      <td>6</td>
      <td>7</td>
    </tr>
    <tr>
      <th>Utah</th>
      <td>8</td>
      <td>9</td>
      <td>10</td>
      <td>11</td>
    </tr>
    <tr>
      <th>New York</th>
      <td>12</td>
      <td>13</td>
      <td>14</td>
      <td>15</td>
    </tr>
  </tbody>
</table>
</div>




```python
data<5
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
      <th>one</th>
      <th>two</th>
      <th>three</th>
      <th>four</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Ohio</th>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Colorado</th>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>Utah</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>New York</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>




```python
data[data<5]=0
```


```python
data
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
      <th>one</th>
      <th>two</th>
      <th>three</th>
      <th>four</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Ohio</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>Colorado</th>
      <td>0</td>
      <td>5</td>
      <td>6</td>
      <td>7</td>
    </tr>
    <tr>
      <th>Utah</th>
      <td>8</td>
      <td>9</td>
      <td>10</td>
      <td>11</td>
    </tr>
    <tr>
      <th>New York</th>
      <td>12</td>
      <td>13</td>
      <td>14</td>
      <td>15</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 5, 6 출력
```


```python
data[(data == 5) | (data == 6)]
data.iloc[1][[1,2]]
data.loc['Colorado'][[1,2]]
data.loc['Colorado', ['two', 'three']]
```




    two      5
    three    6
    Name: Colorado, dtype: int32




```python
data
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
      <th>one</th>
      <th>two</th>
      <th>three</th>
      <th>four</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Ohio</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>Colorado</th>
      <td>0</td>
      <td>5</td>
      <td>6</td>
      <td>7</td>
    </tr>
    <tr>
      <th>Utah</th>
      <td>8</td>
      <td>9</td>
      <td>10</td>
      <td>11</td>
    </tr>
    <tr>
      <th>New York</th>
      <td>12</td>
      <td>13</td>
      <td>14</td>
      <td>15</td>
    </tr>
  </tbody>
</table>
</div>




```python
data.iloc[[1, 2]]
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
      <th>one</th>
      <th>two</th>
      <th>three</th>
      <th>four</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Colorado</th>
      <td>0</td>
      <td>5</td>
      <td>6</td>
      <td>7</td>
    </tr>
    <tr>
      <th>Utah</th>
      <td>8</td>
      <td>9</td>
      <td>10</td>
      <td>11</td>
    </tr>
  </tbody>
</table>
</div>




```python
data.iloc[[1, 2],[3,0]]
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
      <th>four</th>
      <th>one</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Colorado</th>
      <td>7</td>
      <td>0</td>
    </tr>
    <tr>
      <th>Utah</th>
      <td>11</td>
      <td>8</td>
    </tr>
  </tbody>
</table>
</div>




```python
data.iloc[2]
```




    one       8
    two       9
    three    10
    four     11
    Name: Utah, dtype: int32




```python
data.iloc[2,3]
```




    11




```python
data.iloc[2,[3,0]]
data.iloc[2,[3,0,1]]
```




    four    11
    one      8
    two      9
    Name: Utah, dtype: int32




```python
data
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
      <th>one</th>
      <th>two</th>
      <th>three</th>
      <th>four</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Ohio</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>Colorado</th>
      <td>0</td>
      <td>5</td>
      <td>6</td>
      <td>7</td>
    </tr>
    <tr>
      <th>Utah</th>
      <td>8</td>
      <td>9</td>
      <td>10</td>
      <td>11</td>
    </tr>
    <tr>
      <th>New York</th>
      <td>12</td>
      <td>13</td>
      <td>14</td>
      <td>15</td>
    </tr>
  </tbody>
</table>
</div>




```python
data[:3]
data.iloc[[0,1,2]]
data.loc['Ohio':'Utah']
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
      <th>one</th>
      <th>two</th>
      <th>three</th>
      <th>four</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Ohio</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>Colorado</th>
      <td>0</td>
      <td>5</td>
      <td>6</td>
      <td>7</td>
    </tr>
    <tr>
      <th>Utah</th>
      <td>8</td>
      <td>9</td>
      <td>10</td>
      <td>11</td>
    </tr>
  </tbody>
</table>
</div>




```python
data.loc['Ohio':'Utah', 'two']
```




    Ohio        0
    Colorado    5
    Utah        9
    Name: two, dtype: int32




```python
data.iloc[:]
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
      <th>one</th>
      <th>two</th>
      <th>three</th>
      <th>four</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Ohio</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>Colorado</th>
      <td>0</td>
      <td>5</td>
      <td>6</td>
      <td>7</td>
    </tr>
    <tr>
      <th>Utah</th>
      <td>8</td>
      <td>9</td>
      <td>10</td>
      <td>11</td>
    </tr>
    <tr>
      <th>New York</th>
      <td>12</td>
      <td>13</td>
      <td>14</td>
      <td>15</td>
    </tr>
  </tbody>
</table>
</div>




```python
data.iloc[:, :3]
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
      <th>one</th>
      <th>two</th>
      <th>three</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Ohio</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>Colorado</th>
      <td>0</td>
      <td>5</td>
      <td>6</td>
    </tr>
    <tr>
      <th>Utah</th>
      <td>8</td>
      <td>9</td>
      <td>10</td>
    </tr>
    <tr>
      <th>New York</th>
      <td>12</td>
      <td>13</td>
      <td>14</td>
    </tr>
  </tbody>
</table>
</div>




```python
data
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
      <th>one</th>
      <th>two</th>
      <th>three</th>
      <th>four</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Ohio</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>Colorado</th>
      <td>0</td>
      <td>5</td>
      <td>6</td>
      <td>7</td>
    </tr>
    <tr>
      <th>Utah</th>
      <td>8</td>
      <td>9</td>
      <td>10</td>
      <td>11</td>
    </tr>
    <tr>
      <th>New York</th>
      <td>12</td>
      <td>13</td>
      <td>14</td>
      <td>15</td>
    </tr>
  </tbody>
</table>
</div>




```python
data.loc['Ohio']
```




    one      0
    two      0
    three    0
    four     0
    Name: Ohio, dtype: int32




```python
data.three
```




    Ohio         0
    Colorado     6
    Utah        10
    New York    14
    Name: three, dtype: int32




```python
data.three > 5
```




    Ohio        False
    Colorado     True
    Utah         True
    New York     True
    Name: three, dtype: bool




```python
data[data.three>5]
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
      <th>one</th>
      <th>two</th>
      <th>three</th>
      <th>four</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Colorado</th>
      <td>0</td>
      <td>5</td>
      <td>6</td>
      <td>7</td>
    </tr>
    <tr>
      <th>Utah</th>
      <td>8</td>
      <td>9</td>
      <td>10</td>
      <td>11</td>
    </tr>
    <tr>
      <th>New York</th>
      <td>12</td>
      <td>13</td>
      <td>14</td>
      <td>15</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 1.
# (1) 임의로 두 개의 시리즈 객체를 만든다. 모두 문자열 인덱스를 가져야 하며 두 시리즈에 공통적으로 포함되지 않는 라벨이 있어야 한다.
se1 = pd.Series([1,2,3,4], index=['a', 'b', 'c', 'd'])
se1
```




    a    1
    b    2
    c    3
    d    4
    dtype: int64




```python
se2 = pd.Series([3,2,4,1], index=['a', 'b', 'c', 'e'])
se2
```




    a    3
    b    2
    c    4
    e    1
    dtype: int64




```python
# (2) 위에서 만든 두 시리즈 객체를 이용하여 사칙 연산을 한다.
se1 + se2
se1 - se2
se1 * se2
se1 / se2
```




    a    0.333333
    b    1.000000
    c    0.750000
    d         NaN
    e         NaN
    dtype: float64




```python
# 2. 다음 조건을 만족하는 임의의 데이터프레임을 하나 만든다.
# (1) 열의 갯수와 행의 갯수가 각각 5개 이상이어야 한다.
# (2) 열에는 정수, 문자열, 실수 자료형 데이터가 각각 1개 이상씩 포함되어 있어야 한다.
pd.DataFrame({'fruit' : ['apple', 'banana', 'mango', 'grape', 'peach'],
             'number' : [1,2,3,4,5],
             'height' : [123.4, 187.4, 160.3, 193, 169.9],
             'animal' : ['cat', 'dog', 'lion', 'monkey', 'tiger'],
             'city' : ['서울', '대전', '부산', '광주', '인천']})
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
      <th>fruit</th>
      <th>number</th>
      <th>height</th>
      <th>animal</th>
      <th>city</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>apple</td>
      <td>1</td>
      <td>123.4</td>
      <td>cat</td>
      <td>서울</td>
    </tr>
    <tr>
      <th>1</th>
      <td>banana</td>
      <td>2</td>
      <td>187.4</td>
      <td>dog</td>
      <td>대전</td>
    </tr>
    <tr>
      <th>2</th>
      <td>mango</td>
      <td>3</td>
      <td>160.3</td>
      <td>lion</td>
      <td>부산</td>
    </tr>
    <tr>
      <th>3</th>
      <td>grape</td>
      <td>4</td>
      <td>193.0</td>
      <td>monkey</td>
      <td>광주</td>
    </tr>
    <tr>
      <th>4</th>
      <td>peach</td>
      <td>5</td>
      <td>169.9</td>
      <td>tiger</td>
      <td>인천</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 3. 다음 데이터프레임에서 지정하는 데이터를 뽑아내거나 처리하라.

data = {
    "국어": [80, 90, 70, 30],
    "영어": [90, 70, 60, 40],
    "수학": [90, 60, 80, 70],
}
columns = ["국어", "영어", "수학"]
index = ["춘향", "몽룡", "향단", "방자"]
df = pd.DataFrame(data, index=index, columns=columns)
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
      <th>국어</th>
      <th>영어</th>
      <th>수학</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>춘향</th>
      <td>80</td>
      <td>90</td>
      <td>90</td>
    </tr>
    <tr>
      <th>몽룡</th>
      <td>90</td>
      <td>70</td>
      <td>60</td>
    </tr>
    <tr>
      <th>향단</th>
      <td>70</td>
      <td>60</td>
      <td>80</td>
    </tr>
    <tr>
      <th>방자</th>
      <td>30</td>
      <td>40</td>
      <td>70</td>
    </tr>
  </tbody>
</table>
</div>




```python
# (1) 모든 학생의 수학 점수를 시리즈로 나타낸다.
df['수학']
# (2) 모든 학생의 국어와 영어 점수를 데이터 프레임으로 나타낸다.
df[['국어', '영어']]
# (3) 모든 학생의 각 과목 평균 점수를 새로운 열로 추가한다.
df.loc['평균'] = df.mean()
# (4) 방자의 영어 점수를 80점으로 수정하고 평균 점수도 다시 계산한다.
df.loc['방자', '영어'] = 80
df.loc['평균'] = df.mean()
# (5) 춘향의 점수를 데이터프레임으로 나타낸다.
df.loc[['춘향']]
# (6) 향단의 점수를 시리즈로 나타낸다.
df.loc['향단']
```


```python
df.loc['방자', '영어'] = 80
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
      <th>국어</th>
      <th>영어</th>
      <th>수학</th>
      <th>(방자, 영어)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>춘향</th>
      <td>80.0</td>
      <td>90.0</td>
      <td>90.0</td>
      <td>80</td>
    </tr>
    <tr>
      <th>몽룡</th>
      <td>90.0</td>
      <td>70.0</td>
      <td>60.0</td>
      <td>80</td>
    </tr>
    <tr>
      <th>향단</th>
      <td>70.0</td>
      <td>60.0</td>
      <td>80.0</td>
      <td>80</td>
    </tr>
    <tr>
      <th>방자</th>
      <td>30.0</td>
      <td>80.0</td>
      <td>70.0</td>
      <td>80</td>
    </tr>
    <tr>
      <th>평균</th>
      <td>67.5</td>
      <td>65.0</td>
      <td>75.0</td>
      <td>80</td>
    </tr>
  </tbody>
</table>
</div>




```python
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
      <th>국어</th>
      <th>영어</th>
      <th>수학</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>춘향</th>
      <td>80.0</td>
      <td>90.0</td>
      <td>90.0</td>
    </tr>
    <tr>
      <th>몽룡</th>
      <td>90.0</td>
      <td>70.0</td>
      <td>60.0</td>
    </tr>
    <tr>
      <th>향단</th>
      <td>70.0</td>
      <td>60.0</td>
      <td>80.0</td>
    </tr>
    <tr>
      <th>방자</th>
      <td>30.0</td>
      <td>80.0</td>
      <td>70.0</td>
    </tr>
    <tr>
      <th>평균</th>
      <td>67.5</td>
      <td>65.0</td>
      <td>75.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.loc['평균'] = df.mean()
```


```python
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
      <th>국어</th>
      <th>영어</th>
      <th>수학</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>춘향</th>
      <td>80.0</td>
      <td>90.0</td>
      <td>90.0</td>
    </tr>
    <tr>
      <th>몽룡</th>
      <td>90.0</td>
      <td>70.0</td>
      <td>60.0</td>
    </tr>
    <tr>
      <th>향단</th>
      <td>70.0</td>
      <td>60.0</td>
      <td>80.0</td>
    </tr>
    <tr>
      <th>방자</th>
      <td>30.0</td>
      <td>80.0</td>
      <td>70.0</td>
    </tr>
    <tr>
      <th>평균</th>
      <td>67.5</td>
      <td>73.0</td>
      <td>75.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.loc[['춘향']]
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
      <th>국어</th>
      <th>영어</th>
      <th>수학</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>춘향</th>
      <td>80.0</td>
      <td>90.0</td>
      <td>90.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.loc['향단']
```




    국어    70.0
    영어    60.0
    수학    80.0
    Name: 향단, dtype: float64




```python

```
