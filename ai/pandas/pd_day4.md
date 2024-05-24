```python
import pandas as pd
import numpy as np
```


```python
obj = pd.Series(["a", "a", "b", "c"] * 4)
obj
```




    0     a
    1     a
    2     b
    3     c
    4     a
    5     a
    6     b
    7     c
    8     a
    9     a
    10    b
    11    c
    12    a
    13    a
    14    b
    15    c
    dtype: object




```python
obj.describe()
```




    count     16
    unique     3
    top        a
    freq       8
    dtype: object




```python
"""
pickle : 파이썬 객체를 파일로 저장(텍스트로 저장x)
텍스트 수집 -> 정제 -> 분석 -> 시각화 -> (모델링) -> 유지보수
ex) 10기가바이트(raw text) -> parsing -> 분석 대상 텍스트만 추출 -> dict, list 등에 저장
pickle 모듈 : 파이썬 객체(dict, list, df, series, ...)에 저장된 정제된 텍스트를 바이너리 형식으로 파일에 저장
(속도 빠름, 용량 작음)
"""
```




    '\npickle : 파이썬 객체를 파일로 저장(텍스트로 저장x)\n텍스트 수집 -> 정제 -> 분석 -> 시각화 -> (모델링) -> 유지보수\nex) 10기가바이트(raw text) -> parsing -> 분석 대상 텍스트만 추출 -> dict, list 등에 저장\npickle 모듈 : 파이썬 객체(dict, list, df, series, ...)에 저장된 정제된 텍스트를 파일로 저장 \n'




```python
import pickle
```


```python
myList=['a', 'b']
```


```python
with open('pic_ex1.pickle', 'wb') as f:
    pickle.dump(myList, f)
```


```python
with open("pic_ex1.pickle","rb") as f:
    myData=pickle.load(f)
```


```python
myData
```




    ['a', 'b']




```python
price = pd.read_pickle('data/examples/yahoo_price.pkl')
price
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
      <th>AAPL</th>
      <th>GOOG</th>
      <th>IBM</th>
      <th>MSFT</th>
    </tr>
    <tr>
      <th>Date</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2010-01-04</th>
      <td>27.990226</td>
      <td>313.062468</td>
      <td>113.304536</td>
      <td>25.884104</td>
    </tr>
    <tr>
      <th>2010-01-05</th>
      <td>28.038618</td>
      <td>311.683844</td>
      <td>111.935822</td>
      <td>25.892466</td>
    </tr>
    <tr>
      <th>2010-01-06</th>
      <td>27.592626</td>
      <td>303.826685</td>
      <td>111.208683</td>
      <td>25.733566</td>
    </tr>
    <tr>
      <th>2010-01-07</th>
      <td>27.541619</td>
      <td>296.753749</td>
      <td>110.823732</td>
      <td>25.465944</td>
    </tr>
    <tr>
      <th>2010-01-08</th>
      <td>27.724725</td>
      <td>300.709808</td>
      <td>111.935822</td>
      <td>25.641571</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>2016-10-17</th>
      <td>117.550003</td>
      <td>779.960022</td>
      <td>154.770004</td>
      <td>57.220001</td>
    </tr>
    <tr>
      <th>2016-10-18</th>
      <td>117.470001</td>
      <td>795.260010</td>
      <td>150.720001</td>
      <td>57.660000</td>
    </tr>
    <tr>
      <th>2016-10-19</th>
      <td>117.120003</td>
      <td>801.500000</td>
      <td>151.259995</td>
      <td>57.529999</td>
    </tr>
    <tr>
      <th>2016-10-20</th>
      <td>117.059998</td>
      <td>796.969971</td>
      <td>151.520004</td>
      <td>57.250000</td>
    </tr>
    <tr>
      <th>2016-10-21</th>
      <td>116.599998</td>
      <td>799.369995</td>
      <td>149.630005</td>
      <td>59.660000</td>
    </tr>
  </tbody>
</table>
<p>1714 rows × 4 columns</p>
</div>




```python
volume = pd.read_pickle('data/examples/yahoo_volume.pkl')
volume
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
      <th>AAPL</th>
      <th>GOOG</th>
      <th>IBM</th>
      <th>MSFT</th>
    </tr>
    <tr>
      <th>Date</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2010-01-04</th>
      <td>123432400</td>
      <td>3927000</td>
      <td>6155300</td>
      <td>38409100</td>
    </tr>
    <tr>
      <th>2010-01-05</th>
      <td>150476200</td>
      <td>6031900</td>
      <td>6841400</td>
      <td>49749600</td>
    </tr>
    <tr>
      <th>2010-01-06</th>
      <td>138040000</td>
      <td>7987100</td>
      <td>5605300</td>
      <td>58182400</td>
    </tr>
    <tr>
      <th>2010-01-07</th>
      <td>119282800</td>
      <td>12876600</td>
      <td>5840600</td>
      <td>50559700</td>
    </tr>
    <tr>
      <th>2010-01-08</th>
      <td>111902700</td>
      <td>9483900</td>
      <td>4197200</td>
      <td>51197400</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>2016-10-17</th>
      <td>23624900</td>
      <td>1089500</td>
      <td>5890400</td>
      <td>23830000</td>
    </tr>
    <tr>
      <th>2016-10-18</th>
      <td>24553500</td>
      <td>1995600</td>
      <td>12770600</td>
      <td>19149500</td>
    </tr>
    <tr>
      <th>2016-10-19</th>
      <td>20034600</td>
      <td>116600</td>
      <td>4632900</td>
      <td>22878400</td>
    </tr>
    <tr>
      <th>2016-10-20</th>
      <td>24125800</td>
      <td>1734200</td>
      <td>4023100</td>
      <td>49455600</td>
    </tr>
    <tr>
      <th>2016-10-21</th>
      <td>22384800</td>
      <td>1260500</td>
      <td>4401900</td>
      <td>79974200</td>
    </tr>
  </tbody>
</table>
<p>1714 rows × 4 columns</p>
</div>




```python
volume.to_pickle('pic_ex2.pkl')
```


```python
returns = price.pct_change() # (현재행-이전행)/현재행
returns
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
      <th>AAPL</th>
      <th>GOOG</th>
      <th>IBM</th>
      <th>MSFT</th>
    </tr>
    <tr>
      <th>Date</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2010-01-04</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2010-01-05</th>
      <td>0.001729</td>
      <td>-0.004404</td>
      <td>-0.012080</td>
      <td>0.000323</td>
    </tr>
    <tr>
      <th>2010-01-06</th>
      <td>-0.015906</td>
      <td>-0.025209</td>
      <td>-0.006496</td>
      <td>-0.006137</td>
    </tr>
    <tr>
      <th>2010-01-07</th>
      <td>-0.001849</td>
      <td>-0.023280</td>
      <td>-0.003462</td>
      <td>-0.010400</td>
    </tr>
    <tr>
      <th>2010-01-08</th>
      <td>0.006648</td>
      <td>0.013331</td>
      <td>0.010035</td>
      <td>0.006897</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>2016-10-17</th>
      <td>-0.000680</td>
      <td>0.001837</td>
      <td>0.002072</td>
      <td>-0.003483</td>
    </tr>
    <tr>
      <th>2016-10-18</th>
      <td>-0.000681</td>
      <td>0.019616</td>
      <td>-0.026168</td>
      <td>0.007690</td>
    </tr>
    <tr>
      <th>2016-10-19</th>
      <td>-0.002979</td>
      <td>0.007846</td>
      <td>0.003583</td>
      <td>-0.002255</td>
    </tr>
    <tr>
      <th>2016-10-20</th>
      <td>-0.000512</td>
      <td>-0.005652</td>
      <td>0.001719</td>
      <td>-0.004867</td>
    </tr>
    <tr>
      <th>2016-10-21</th>
      <td>-0.003930</td>
      <td>0.003011</td>
      <td>-0.012474</td>
      <td>0.042096</td>
    </tr>
  </tbody>
</table>
<p>1714 rows × 4 columns</p>
</div>




```python
# 다음주 월요일(분산, 공분산, 상관계수(분석))
returns['AAPL'].corr(returns['GOOG'])
```




    0.4079185761679696




```python
returns['AAPL'].corr(returns['IBM'])
```




    0.38681743611391




```python
returns['AAPL'].corr(returns['MSFT'])
```




    0.38969458628057835




```python
returns.corr() # 상관관계
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
      <th>AAPL</th>
      <th>GOOG</th>
      <th>IBM</th>
      <th>MSFT</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>AAPL</th>
      <td>1.000000</td>
      <td>0.407919</td>
      <td>0.386817</td>
      <td>0.389695</td>
    </tr>
    <tr>
      <th>GOOG</th>
      <td>0.407919</td>
      <td>1.000000</td>
      <td>0.405099</td>
      <td>0.465919</td>
    </tr>
    <tr>
      <th>IBM</th>
      <td>0.386817</td>
      <td>0.405099</td>
      <td>1.000000</td>
      <td>0.499764</td>
    </tr>
    <tr>
      <th>MSFT</th>
      <td>0.389695</td>
      <td>0.465919</td>
      <td>0.499764</td>
      <td>1.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
volume
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
      <th>AAPL</th>
      <th>GOOG</th>
      <th>IBM</th>
      <th>MSFT</th>
    </tr>
    <tr>
      <th>Date</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2010-01-04</th>
      <td>123432400</td>
      <td>3927000</td>
      <td>6155300</td>
      <td>38409100</td>
    </tr>
    <tr>
      <th>2010-01-05</th>
      <td>150476200</td>
      <td>6031900</td>
      <td>6841400</td>
      <td>49749600</td>
    </tr>
    <tr>
      <th>2010-01-06</th>
      <td>138040000</td>
      <td>7987100</td>
      <td>5605300</td>
      <td>58182400</td>
    </tr>
    <tr>
      <th>2010-01-07</th>
      <td>119282800</td>
      <td>12876600</td>
      <td>5840600</td>
      <td>50559700</td>
    </tr>
    <tr>
      <th>2010-01-08</th>
      <td>111902700</td>
      <td>9483900</td>
      <td>4197200</td>
      <td>51197400</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>2016-10-17</th>
      <td>23624900</td>
      <td>1089500</td>
      <td>5890400</td>
      <td>23830000</td>
    </tr>
    <tr>
      <th>2016-10-18</th>
      <td>24553500</td>
      <td>1995600</td>
      <td>12770600</td>
      <td>19149500</td>
    </tr>
    <tr>
      <th>2016-10-19</th>
      <td>20034600</td>
      <td>116600</td>
      <td>4632900</td>
      <td>22878400</td>
    </tr>
    <tr>
      <th>2016-10-20</th>
      <td>24125800</td>
      <td>1734200</td>
      <td>4023100</td>
      <td>49455600</td>
    </tr>
    <tr>
      <th>2016-10-21</th>
      <td>22384800</td>
      <td>1260500</td>
      <td>4401900</td>
      <td>79974200</td>
    </tr>
  </tbody>
</table>
<p>1714 rows × 4 columns</p>
</div>




```python
returns.corrwith(volume)
```




    AAPL   -0.075565
    GOOG   -0.007067
    IBM    -0.204849
    MSFT   -0.092950
    dtype: float64




```python
obj = pd.Series(["c", "a", "d", "a", "a", "b", "b", "c", "c"])
obj
```




    0    c
    1    a
    2    d
    3    a
    4    a
    5    b
    6    b
    7    c
    8    c
    dtype: object




```python
uniques = obj.unique()
uniques
```




    array(['c', 'a', 'd', 'b'], dtype=object)




```python
obj.value_counts() # 시리즈.value_counts()
```




    c    3
    a    3
    b    2
    d    1
    dtype: int64




```python
obj.to_numpy() # 시리즈 -> 넘파이 배열
```




    array(['c', 'a', 'd', 'a', 'a', 'b', 'b', 'c', 'c'], dtype=object)




```python
pd.value_counts(obj.to_numpy()) # 출력은 가능, 기본 내림차순 정렬
```




    c    3
    a    3
    b    2
    d    1
    dtype: int64




```python
pd.value_counts(obj.to_numpy(), sort=False) # 출력은 가능, 정렬x
```




    c    3
    a    3
    d    1
    b    2
    dtype: int64




```python
pd.value_counts(obj.to_numpy(), ascending=True) # 출력은 가능, 오름차순정렬
```




    d    1
    b    2
    c    3
    a    3
    dtype: int64




```python
obj.value_counts(ascending=True)
```




    d    1
    b    2
    c    3
    a    3
    dtype: int64




```python
obj.value_counts()
```




    c    3
    a    3
    b    2
    d    1
    dtype: int64




```python
obj.value_counts(sort=False)
```




    c    3
    a    3
    d    1
    b    2
    dtype: int64




```python
obj
```




    0    c
    1    a
    2    d
    3    a
    4    a
    5    b
    6    b
    7    c
    8    c
    dtype: object




```python
'a' in obj
```




    False




```python
1 in obj
9 in obj
```




    False




```python
obj[obj.isin(['b','c'])]
```




    0    c
    5    b
    6    b
    7    c
    8    c
    dtype: object




```python
to_match = pd.Series(["c", "a", "b", "b", "c", "a"])
to_match
```




    0    c
    1    a
    2    b
    3    b
    4    c
    5    a
    dtype: object




```python
unique_vals = pd.Series(["c", "b", "a"])
unique_vals
```




    0    c
    1    b
    2    a
    dtype: object




```python
pd.Index(unique_vals)
```




    Index(['c', 'b', 'a'], dtype='object')




```python
pd.Index(unique_vals).get_indexer(to_match)
```




    array([0, 2, 1, 1, 0, 2], dtype=int64)




```python
to_match = pd.Series(["c", "a", "b", "b", "c", "a"])
unique_vals = pd.Series(["c", "b", "a"])
indices = pd.Index(unique_vals).get_indexer(to_match)
indices
data = pd.DataFrame({"Qu1": [1, 3, 4, 3, 4],
                     "Qu2": [2, 3, 1, 2, 3],
                     "Qu3": [1, 5, 2, 4, 4]})
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
      <th>Qu1</th>
      <th>Qu2</th>
      <th>Qu3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>2</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3</td>
      <td>3</td>
      <td>5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>2</td>
      <td>4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>3</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 데이터프레임, 행렬
# 공통점 : 2차원
# 차이점 : 행렬(모든 자료의 타입이 동일), 데이터프레임(모든 자료의 타입이 동일하지 않아도 됨, 각 열은 동일 타입)
```


```python
# 리스트, 벡터(1차원)
# 차이점 : 리스트 다양한 타입, 벡터 동일한 타입
# myLIst=[1,'a',2.1,True]
# np.array([1,'a']) -> array(['1', 'a'])로 통일됨
```


```python
data['Qu1'].value_counts()
```




    3    2
    4    2
    1    1
    Name: Qu1, dtype: int64




```python
data['Qu1'].value_counts().sort_index()
```




    1    1
    3    2
    4    2
    Name: Qu1, dtype: int64




```python
data
# 모든 열 단위로 각 숫자의 빈도수를 출력
data[:].value_counts()
data.value_counts()
```




    Qu1  Qu2  Qu3
    1    2    1      1
    3    2    4      1
         3    5      1
    4    1    2      1
         3    4      1
    dtype: int64




```python
data['Qu1'].value_counts()
```




    3    2
    4    2
    1    1
    Name: Qu1, dtype: int64




```python
# def f1(x):
#     return x.max()-x.min()
# frame.apply(f1)
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
      <th>Qu1</th>
      <th>Qu2</th>
      <th>Qu3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>2</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3</td>
      <td>3</td>
      <td>5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>2</td>
      <td>4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>3</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>




```python
# def aaa(x):
#     return x.value_counts()

# data.apply(aaa)

data.apply(pd.value_counts).fillna(0)
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
      <th>Qu1</th>
      <th>Qu2</th>
      <th>Qu3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.0</td>
      <td>2.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2.0</td>
      <td>2.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2.0</td>
      <td>0.0</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
data = pd.DataFrame({"a": [1, 1, 1, 2, 2], "b": [0, 0, 1, 0, 0]})
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
      <th>a</th>
      <th>b</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>




```python
data.value_counts()
```




    a  b
    1  0    2
    2  0    2
    1  1    1
    dtype: int64




```python
df = pd.read_csv('data/examples/ex1.csv')
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
      <th>a</th>
      <th>b</th>
      <th>c</th>
      <th>d</th>
      <th>message</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>2</td>
      <td>3</td>
      <td>4</td>
      <td>hello</td>
    </tr>
    <tr>
      <th>1</th>
      <td>5</td>
      <td>6</td>
      <td>7</td>
      <td>8</td>
      <td>world</td>
    </tr>
    <tr>
      <th>2</th>
      <td>9</td>
      <td>10</td>
      <td>11</td>
      <td>12</td>
      <td>foo</td>
    </tr>
  </tbody>
</table>
</div>




```python
#cat data/examples/ex1.csv
```


```python
df2 = pd.read_csv('data/examples/ex2.csv', header=None)
df2
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
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>2</td>
      <td>3</td>
      <td>4</td>
      <td>hello</td>
    </tr>
    <tr>
      <th>1</th>
      <td>5</td>
      <td>6</td>
      <td>7</td>
      <td>8</td>
      <td>world</td>
    </tr>
    <tr>
      <th>2</th>
      <td>9</td>
      <td>10</td>
      <td>11</td>
      <td>12</td>
      <td>foo</td>
    </tr>
  </tbody>
</table>
</div>




```python
df2 = pd.read_csv('data/examples/ex2.csv', header=None, names=['a', 'b', 'c', 'd', 'msg'])
df2
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
      <th>a</th>
      <th>b</th>
      <th>c</th>
      <th>d</th>
      <th>msg</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>2</td>
      <td>3</td>
      <td>4</td>
      <td>hello</td>
    </tr>
    <tr>
      <th>1</th>
      <td>5</td>
      <td>6</td>
      <td>7</td>
      <td>8</td>
      <td>world</td>
    </tr>
    <tr>
      <th>2</th>
      <td>9</td>
      <td>10</td>
      <td>11</td>
      <td>12</td>
      <td>foo</td>
    </tr>
  </tbody>
</table>
</div>




```python
df=pd.read_csv("data/examples/ex2.csv", header=None, names=['a','b','c','d','msg'], index_col='msg')
df
#index_col : 특정 열의 값을 행 인덱스 라벨로 설정
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
      <th>a</th>
      <th>b</th>
      <th>c</th>
      <th>d</th>
    </tr>
    <tr>
      <th>msg</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>hello</th>
      <td>1</td>
      <td>2</td>
      <td>3</td>
      <td>4</td>
    </tr>
    <tr>
      <th>world</th>
      <td>5</td>
      <td>6</td>
      <td>7</td>
      <td>8</td>
    </tr>
    <tr>
      <th>foo</th>
      <td>9</td>
      <td>10</td>
      <td>11</td>
      <td>12</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.read_csv("data/examples/csv_mindex.csv")
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
      <th>key1</th>
      <th>key2</th>
      <th>value1</th>
      <th>value2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>one</td>
      <td>a</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>one</td>
      <td>b</td>
      <td>3</td>
      <td>4</td>
    </tr>
    <tr>
      <th>2</th>
      <td>one</td>
      <td>c</td>
      <td>5</td>
      <td>6</td>
    </tr>
    <tr>
      <th>3</th>
      <td>one</td>
      <td>d</td>
      <td>7</td>
      <td>8</td>
    </tr>
    <tr>
      <th>4</th>
      <td>two</td>
      <td>a</td>
      <td>9</td>
      <td>10</td>
    </tr>
    <tr>
      <th>5</th>
      <td>two</td>
      <td>b</td>
      <td>11</td>
      <td>12</td>
    </tr>
    <tr>
      <th>6</th>
      <td>two</td>
      <td>c</td>
      <td>13</td>
      <td>14</td>
    </tr>
    <tr>
      <th>7</th>
      <td>two</td>
      <td>d</td>
      <td>15</td>
      <td>16</td>
    </tr>
  </tbody>
</table>
</div>




```python
df = pd.read_csv("data/examples/csv_mindex.csv", index_col = ['key1', 'key2'])
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
      <th></th>
      <th>value1</th>
      <th>value2</th>
    </tr>
    <tr>
      <th>key1</th>
      <th>key2</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="4" valign="top">one</th>
      <th>a</th>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>b</th>
      <td>3</td>
      <td>4</td>
    </tr>
    <tr>
      <th>c</th>
      <td>5</td>
      <td>6</td>
    </tr>
    <tr>
      <th>d</th>
      <td>7</td>
      <td>8</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">two</th>
      <th>a</th>
      <td>9</td>
      <td>10</td>
    </tr>
    <tr>
      <th>b</th>
      <td>11</td>
      <td>12</td>
    </tr>
    <tr>
      <th>c</th>
      <td>13</td>
      <td>14</td>
    </tr>
    <tr>
      <th>d</th>
      <td>15</td>
      <td>16</td>
    </tr>
  </tbody>
</table>
</div>




```python
df = pd.read_csv("data/examples/ex3.txt")
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
      <th>A         B         C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>aaa -0.264438 -1.026059 -0.619500</td>
    </tr>
    <tr>
      <th>1</th>
      <td>bbb  0.927272  0.302904 -0.032399</td>
    </tr>
    <tr>
      <th>2</th>
      <td>ccc -0.264273 -0.386314 -0.217601</td>
    </tr>
    <tr>
      <th>3</th>
      <td>ddd -0.871858 -0.348382  1.100491</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.loc[1:3]
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
      <th>A         B         C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>bbb  0.927272  0.302904 -0.032399</td>
    </tr>
    <tr>
      <th>2</th>
      <td>ccc -0.264273 -0.386314 -0.217601</td>
    </tr>
    <tr>
      <th>3</th>
      <td>ddd -0.871858 -0.348382  1.100491</td>
    </tr>
  </tbody>
</table>
</div>




```python
df = pd.read_csv("data/examples/ex3.txt", sep='\s+')
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
      <th>A</th>
      <th>B</th>
      <th>C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>aaa</th>
      <td>-0.264438</td>
      <td>-1.026059</td>
      <td>-0.619500</td>
    </tr>
    <tr>
      <th>bbb</th>
      <td>0.927272</td>
      <td>0.302904</td>
      <td>-0.032399</td>
    </tr>
    <tr>
      <th>ccc</th>
      <td>-0.264273</td>
      <td>-0.386314</td>
      <td>-0.217601</td>
    </tr>
    <tr>
      <th>ddd</th>
      <td>-0.871858</td>
      <td>-0.348382</td>
      <td>1.100491</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.loc[1]
```




    a              5
    b              6
    c              7
    d              8
    message    world
    Name: 1, dtype: object




```python
df=pd.read_csv("data/examples/ex4.csv", skiprows=[0,2,3])
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
      <th>a</th>
      <th>b</th>
      <th>c</th>
      <th>d</th>
      <th>message</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>2</td>
      <td>3</td>
      <td>4</td>
      <td>hello</td>
    </tr>
    <tr>
      <th>1</th>
      <td>5</td>
      <td>6</td>
      <td>7</td>
      <td>8</td>
      <td>world</td>
    </tr>
    <tr>
      <th>2</th>
      <td>9</td>
      <td>10</td>
      <td>11</td>
      <td>12</td>
      <td>foo</td>
    </tr>
  </tbody>
</table>
</div>




```python
df=pd.read_csv('data/examples/ex5.csv')
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
      <th>something</th>
      <th>a</th>
      <th>b</th>
      <th>c</th>
      <th>d</th>
      <th>message</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>one</td>
      <td>1</td>
      <td>2</td>
      <td>3.0</td>
      <td>4</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>two</td>
      <td>5</td>
      <td>6</td>
      <td>NaN</td>
      <td>8</td>
      <td>world</td>
    </tr>
    <tr>
      <th>2</th>
      <td>three</td>
      <td>9</td>
      <td>10</td>
      <td>11.0</td>
      <td>12</td>
      <td>foo</td>
    </tr>
  </tbody>
</table>
</div>




```python
df=pd.read_csv('data/examples/ex5.csv').fillna('NULL')
df
df=pd.read_csv('data/examples/ex5.csv').fillna('AAA')
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
      <th>something</th>
      <th>a</th>
      <th>b</th>
      <th>c</th>
      <th>d</th>
      <th>message</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>one</td>
      <td>1</td>
      <td>2</td>
      <td>3.0</td>
      <td>4</td>
      <td>AAA</td>
    </tr>
    <tr>
      <th>1</th>
      <td>two</td>
      <td>5</td>
      <td>6</td>
      <td>AAA</td>
      <td>8</td>
      <td>world</td>
    </tr>
    <tr>
      <th>2</th>
      <td>three</td>
      <td>9</td>
      <td>10</td>
      <td>11.0</td>
      <td>12</td>
      <td>foo</td>
    </tr>
  </tbody>
</table>
</div>




```python
df=pd.read_csv('data/examples/ex5.csv', na_values=['world'])
df
# na_values는 리스트에 담긴 특정 문자(열)에 해당되는 데이터에 대해 결측값으로 읽어지도록 하는 옵션
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
      <th>something</th>
      <th>a</th>
      <th>b</th>
      <th>c</th>
      <th>d</th>
      <th>message</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>one</td>
      <td>1</td>
      <td>2</td>
      <td>3.0</td>
      <td>4</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>two</td>
      <td>5</td>
      <td>6</td>
      <td>NaN</td>
      <td>8</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>three</td>
      <td>9</td>
      <td>10</td>
      <td>11.0</td>
      <td>12</td>
      <td>foo</td>
    </tr>
  </tbody>
</table>
</div>




```python
df=pd.read_csv('data/examples/ex5.csv', na_values=['9', '10', '?'])
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
      <th>something</th>
      <th>a</th>
      <th>b</th>
      <th>c</th>
      <th>d</th>
      <th>message</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>one</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>3.0</td>
      <td>4</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>two</td>
      <td>5.0</td>
      <td>6.0</td>
      <td>NaN</td>
      <td>8</td>
      <td>world</td>
    </tr>
    <tr>
      <th>2</th>
      <td>three</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>11.0</td>
      <td>12</td>
      <td>foo</td>
    </tr>
  </tbody>
</table>
</div>




```python
df=pd.read_csv('data/examples/ex5.csv')
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
      <th>something</th>
      <th>a</th>
      <th>b</th>
      <th>c</th>
      <th>d</th>
      <th>message</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>one</td>
      <td>1</td>
      <td>2</td>
      <td>3.0</td>
      <td>4</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>two</td>
      <td>5</td>
      <td>6</td>
      <td>NaN</td>
      <td>8</td>
      <td>world</td>
    </tr>
    <tr>
      <th>2</th>
      <td>three</td>
      <td>9</td>
      <td>10</td>
      <td>11.0</td>
      <td>12</td>
      <td>foo</td>
    </tr>
  </tbody>
</table>
</div>




```python
# df=pd.read_csv('data/examples/ex5.csv', na_filter=True)
# df+
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
      <th>something</th>
      <th>a</th>
      <th>b</th>
      <th>c</th>
      <th>d</th>
      <th>message</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>one</td>
      <td>1</td>
      <td>2</td>
      <td>3.0</td>
      <td>4</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>two</td>
      <td>5</td>
      <td>6</td>
      <td>NaN</td>
      <td>8</td>
      <td>world</td>
    </tr>
    <tr>
      <th>2</th>
      <td>three</td>
      <td>9</td>
      <td>10</td>
      <td>11.0</td>
      <td>12</td>
      <td>foo</td>
    </tr>
  </tbody>
</table>
</div>




```python
df=pd.read_csv("data/examples/ex5.csv", na_values=['one', 'foo'])
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
      <th>something</th>
      <th>a</th>
      <th>b</th>
      <th>c</th>
      <th>d</th>
      <th>message</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>NaN</td>
      <td>1</td>
      <td>2</td>
      <td>3.0</td>
      <td>4</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>two</td>
      <td>5</td>
      <td>6</td>
      <td>NaN</td>
      <td>8</td>
      <td>world</td>
    </tr>
    <tr>
      <th>2</th>
      <td>three</td>
      <td>9</td>
      <td>10</td>
      <td>11.0</td>
      <td>12</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
df=pd.read_csv("data/examples/ex6.csv")
df
df.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 10000 entries, 0 to 9999
    Data columns (total 5 columns):
     #   Column  Non-Null Count  Dtype  
    ---  ------  --------------  -----  
     0   one     10000 non-null  float64
     1   two     10000 non-null  float64
     2   three   10000 non-null  float64
     3   four    10000 non-null  float64
     4   key     10000 non-null  object 
    dtypes: float64(4), object(1)
    memory usage: 390.8+ KB
    


```python
# 부족한 메모리, 빅 데이터 읽기 방법
# 1) 큰 메모리를 구매
# 2) 분산 환경 구성
# 3) 빅 데이터를 쪼개서 읽기(해당 방법 사용)

# chksize = 1000 # 한번에 1천개씩 데이터 읽기
# for cnt, chunk in enumerate(pd.read_csv('파일명', chunksize=chksize)):
    # 처리작업(chunk)
```


```python
chker = pd.read_csv('data/examples/ex6.csv', chunksize=1000)
type(chker)
```




    pandas.io.parsers.readers.TextFileReader




```python
chker
```




    <pandas.io.parsers.readers.TextFileReader at 0x2613157f130>




```python
chker = pd.read_csv('data/examples/ex6.csv', chunksize=1000)
for piece in chker:
    print(piece['key'].value_counts())
    print('='*50)
```

    S    48
    O    44
    F    40
    H    39
    Q    39
    J    39
    G    38
    R    38
    X    37
    I    37
    V    35
    U    33
    D    32
    E    32
    W    31
    L    31
    K    31
    A    30
    M    29
    Y    28
    T    27
    N    27
    C    27
    Z    26
    B    25
    P    25
    7    17
    6    17
    4    17
    3    15
    8    13
    1    13
    2    11
    9    11
    0     9
    5     9
    Name: key, dtype: int64
    ==================================================
    O    48
    L    44
    X    40
    I    39
    R    38
    F    37
    Q    35
    D    34
    V    33
    K    33
    E    32
    H    31
    J    31
    T    31
    A    31
    U    30
    N    30
    Z    30
    M    28
    S    27
    Y    27
    G    26
    P    26
    W    25
    B    24
    C    23
    5    20
    0    19
    9    19
    8    19
    4    18
    1    16
    3    16
    2    14
    6    14
    7    12
    Name: key, dtype: int64
    ==================================================
    A    40
    O    40
    X    39
    E    39
    M    38
    H    37
    T    36
    G    36
    K    34
    L    34
    U    33
    F    32
    B    32
    N    31
    V    31
    S    30
    P    30
    Z    29
    W    29
    J    29
    D    28
    R    28
    Q    28
    Y    27
    C    27
    I    25
    6    20
    0    19
    9    19
    7    18
    3    15
    2    14
    4    14
    8    14
    5    14
    1    11
    Name: key, dtype: int64
    ==================================================
    X    43
    J    41
    V    38
    Q    38
    D    38
    C    37
    E    37
    N    36
    P    35
    B    35
    F    35
    L    33
    S    32
    K    32
    R    31
    A    31
    M    30
    H    30
    O    29
    Y    28
    W    28
    I    28
    G    27
    U    26
    Z    24
    T    23
    5    21
    6    18
    3    17
    1    16
    2    16
    0    15
    9    15
    8    13
    4    12
    7    12
    Name: key, dtype: int64
    ==================================================
    E    54
    Q    42
    L    40
    H    39
    P    38
    K    38
    M    36
    X    35
    Y    35
    D    34
    W    33
    U    33
    N    33
    I    31
    T    31
    Z    31
    F    31
    A    31
    G    30
    B    27
    V    26
    O    26
    C    26
    J    25
    S    24
    2    20
    4    18
    R    18
    0    18
    3    18
    5    17
    6    17
    8    16
    7    13
    9     8
    1     8
    Name: key, dtype: int64
    ==================================================
    Y    42
    F    41
    K    41
    X    38
    V    37
    L    35
    W    35
    E    35
    J    34
    M    33
    R    33
    P    32
    N    32
    U    32
    I    32
    D    31
    S    31
    B    30
    G    28
    H    28
    Q    27
    O    26
    A    25
    1    25
    C    25
    T    24
    Z    23
    5    22
    9    20
    7    20
    6    17
    8    17
    3    16
    4    13
    2    12
    0     8
    Name: key, dtype: int64
    ==================================================
    L    41
    C    41
    Z    39
    W    39
    X    38
    O    37
    I    36
    T    36
    R    35
    H    34
    J    33
    N    32
    G    31
    D    31
    F    31
    P    30
    E    30
    B    30
    V    30
    U    29
    M    29
    Q    28
    8    25
    Y    24
    A    23
    K    22
    7    22
    S    21
    9    20
    0    18
    4    18
    2    17
    1    16
    5    15
    3    11
    6     8
    Name: key, dtype: int64
    ==================================================
    J    42
    M    40
    X    39
    E    39
    D    39
    A    38
    V    38
    G    37
    P    35
    Q    35
    R    34
    L    34
    H    34
    B    34
    Y    33
    I    33
    O    32
    U    30
    N    29
    T    28
    K    27
    F    26
    S    26
    C    26
    W    25
    Z    22
    6    21
    4    19
    8    18
    2    16
    7    14
    0    14
    3    13
    5    13
    1    12
    9     5
    Name: key, dtype: int64
    ==================================================
    O    42
    U    41
    S    40
    A    39
    V    37
    E    35
    T    35
    P    35
    J    34
    K    34
    M    34
    Q    34
    I    33
    Z    33
    Y    32
    W    32
    B    32
    R    29
    F    29
    D    28
    N    27
    X    27
    C    26
    H    25
    L    24
    G    24
    7    22
    4    21
    9    18
    1    17
    2    17
    3    15
    0    14
    6    12
    8    12
    5    11
    Name: key, dtype: int64
    ==================================================
    K    42
    M    41
    U    39
    Y    38
    P    38
    E    35
    R    34
    Q    34
    I    33
    T    33
    H    33
    F    33
    B    33
    A    32
    Z    31
    G    31
    L    30
    N    29
    S    29
    J    29
    C    28
    W    28
    X    28
    3    26
    D    25
    V    23
    6    22
    4    21
    O    19
    0    17
    2    15
    9    15
    8    15
    5    15
    7    14
    1    12
    Name: key, dtype: int64
    ==================================================
    


```python
tot = pd.Series([], dtype='int64') # 빈 시리즈 정의, 정수가 저장될 수 있음
tot
```




    Series([], dtype: int64)




```python
ser1=pd.Series([10,20])
ser1
```




    0    10
    1    20
    dtype: int64




```python
# tot + ser1
tot.add(ser1, fill_value=0)
```




    0    10.0
    1    20.0
    dtype: float64




```python
# ex6.csv dml, key 열에 대해 문자별 빈도수를 출력하시오.
chker = pd.read_csv('data/examples/ex6.csv', chunksize=1000)
tot = pd.Series([], dtype='int64') # 빈 시리즈 정의, 정수가 저장될 수 있음
for piece in chker:
    # print(piece['key'].value_counts())
    tot = tot.add(piece['key'].value_counts(), fill_value=0)
tot
```




    0    151.0
    1    146.0
    2    152.0
    3    162.0
    4    171.0
    5    157.0
    6    166.0
    7    164.0
    8    162.0
    9    150.0
    A    320.0
    B    302.0
    C    286.0
    D    320.0
    E    368.0
    F    335.0
    G    308.0
    H    330.0
    I    327.0
    J    337.0
    K    334.0
    L    346.0
    M    338.0
    N    306.0
    O    343.0
    P    324.0
    Q    340.0
    R    318.0
    S    308.0
    T    304.0
    U    326.0
    V    328.0
    W    305.0
    X    364.0
    Y    314.0
    Z    288.0
    dtype: float64




```python
tot.sort_values(ascending=False)
```




    E    368.0
    X    364.0
    L    346.0
    O    343.0
    Q    340.0
    M    338.0
    J    337.0
    F    335.0
    K    334.0
    H    330.0
    V    328.0
    I    327.0
    U    326.0
    P    324.0
    D    320.0
    A    320.0
    R    318.0
    Y    314.0
    G    308.0
    S    308.0
    N    306.0
    W    305.0
    T    304.0
    B    302.0
    Z    288.0
    C    286.0
    4    171.0
    6    166.0
    7    164.0
    8    162.0
    3    162.0
    5    157.0
    2    152.0
    0    151.0
    9    150.0
    1    146.0
    dtype: float64




```python
df = pd.read_csv('data/examples/ex7.csv')
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
      <th>a</th>
      <th>b</th>
      <th>c</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>2</td>
      <td>3</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>2</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.columns
df.index
df.values
```




    array([[1, 2, 3],
           [1, 2, 3]], dtype=int64)




```python
import csv
```


```python
reader = csv.reader(open('data/examples/ex7.csv'))
```


```python
for line in reader:
    print(line)
```

    ['a', 'b', 'c']
    ['1', '2', '3']
    ['1', '2', '3']
    


```python
 obj = """
{"name": "Wes",
 "cities_lived": ["Akron", "Nashville", "New York", "San Francisco"],
 "pet": null,
 "siblings": [{"name": "Scott", "age": 34, "hobbies": ["guitars", "soccer"]},
              {"name": "Katie", "age": 42, "hobbies": ["diving", "art"]}]
}
"""
```


```python
import json
```


```python
res = json.loads(obj) # obj에 저장된 딕셔너리 구조의 문자열을 읽어서 json 형식으로 변환하여 res에 저장
res
```




    {'name': 'Wes',
     'cities_lived': ['Akron', 'Nashville', 'New York', 'San Francisco'],
     'pet': None,
     'siblings': [{'name': 'Scott', 'age': 34, 'hobbies': ['guitars', 'soccer']},
      {'name': 'Katie', 'age': 42, 'hobbies': ['diving', 'art']}]}




```python
type(res)
```




    dict




```python
type(obj)
```




    str




```python
asjson=json.dumps(res) #res에 저장된 딕셔너리 구조의 데이터를 문자열로 저장
asjson
```




    '{"name": "Wes", "cities_lived": ["Akron", "Nashville", "New York", "San Francisco"], "pet": null, "siblings": [{"name": "Scott", "age": 34, "hobbies": ["guitars", "soccer"]}, {"name": "Katie", "age": 42, "hobbies": ["diving", "art"]}]}'




```python
res['siblings']
```




    [{'name': 'Scott', 'age': 34, 'hobbies': ['guitars', 'soccer']},
     {'name': 'Katie', 'age': 42, 'hobbies': ['diving', 'art']}]




```python
pd.DataFrame(res['siblings'])
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
      <th>name</th>
      <th>age</th>
      <th>hobbies</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Scott</td>
      <td>34</td>
      <td>[guitars, soccer]</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Katie</td>
      <td>42</td>
      <td>[diving, art]</td>
    </tr>
  </tbody>
</table>
</div>




```python
data = pd.read_json('data/examples/example.json')
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
      <th>a</th>
      <th>b</th>
      <th>c</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>2</td>
      <td>3</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4</td>
      <td>5</td>
      <td>6</td>
    </tr>
    <tr>
      <th>2</th>
      <td>7</td>
      <td>8</td>
      <td>9</td>
    </tr>
  </tbody>
</table>
</div>




```python
# data frame -> csv
data.to_csv('data_to_csv.csv')
```


```python
# data frame -> json
data.to_json()
```




    '{"a":{"0":1,"1":4,"2":7},"b":{"0":2,"1":5,"2":8},"c":{"0":3,"1":6,"2":9}}'




```python
data.to_json('data.to_json.json')
```


```python
tables = pd.read_html("data/examples/fdic_failed_bank_list.html")
tables
```




    [                             Bank Name             City  ST   CERT  \
     0                          Allied Bank         Mulberry  AR     91   
     1         The Woodbury Banking Company         Woodbury  GA  11297   
     2               First CornerStone Bank  King of Prussia  PA  35312   
     3                   Trust Company Bank          Memphis  TN   9956   
     4           North Milwaukee State Bank        Milwaukee  WI  20364   
     ..                                 ...              ...  ..    ...   
     542                 Superior Bank, FSB         Hinsdale  IL  32646   
     543                Malta National Bank            Malta  OH   6629   
     544    First Alliance Bank & Trust Co.       Manchester  NH  34264   
     545  National State Bank of Metropolis       Metropolis  IL   3815   
     546                   Bank of Honolulu         Honolulu  HI  21029   
     
                        Acquiring Institution        Closing Date  \
     0                           Today's Bank  September 23, 2016   
     1                            United Bank     August 19, 2016   
     2    First-Citizens Bank & Trust Company         May 6, 2016   
     3             The Bank of Fayette County      April 29, 2016   
     4    First-Citizens Bank & Trust Company      March 11, 2016   
     ..                                   ...                 ...   
     542                Superior Federal, FSB       July 27, 2001   
     543                    North Valley Bank         May 3, 2001   
     544  Southern New Hampshire Bank & Trust    February 2, 2001   
     545              Banterra Bank of Marion   December 14, 2000   
     546                   Bank of the Orient    October 13, 2000   
     
               Updated Date  
     0    November 17, 2016  
     1    November 17, 2016  
     2    September 6, 2016  
     3    September 6, 2016  
     4        June 16, 2016  
     ..                 ...  
     542    August 19, 2014  
     543  November 18, 2002  
     544  February 18, 2003  
     545     March 17, 2005  
     546     March 17, 2005  
     
     [547 rows x 7 columns]]




```python
len(tables)
```




    1




```python
tables[0]
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
      <th>Bank Name</th>
      <th>City</th>
      <th>ST</th>
      <th>CERT</th>
      <th>Acquiring Institution</th>
      <th>Closing Date</th>
      <th>Updated Date</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Allied Bank</td>
      <td>Mulberry</td>
      <td>AR</td>
      <td>91</td>
      <td>Today's Bank</td>
      <td>September 23, 2016</td>
      <td>November 17, 2016</td>
    </tr>
    <tr>
      <th>1</th>
      <td>The Woodbury Banking Company</td>
      <td>Woodbury</td>
      <td>GA</td>
      <td>11297</td>
      <td>United Bank</td>
      <td>August 19, 2016</td>
      <td>November 17, 2016</td>
    </tr>
    <tr>
      <th>2</th>
      <td>First CornerStone Bank</td>
      <td>King of Prussia</td>
      <td>PA</td>
      <td>35312</td>
      <td>First-Citizens Bank &amp; Trust Company</td>
      <td>May 6, 2016</td>
      <td>September 6, 2016</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Trust Company Bank</td>
      <td>Memphis</td>
      <td>TN</td>
      <td>9956</td>
      <td>The Bank of Fayette County</td>
      <td>April 29, 2016</td>
      <td>September 6, 2016</td>
    </tr>
    <tr>
      <th>4</th>
      <td>North Milwaukee State Bank</td>
      <td>Milwaukee</td>
      <td>WI</td>
      <td>20364</td>
      <td>First-Citizens Bank &amp; Trust Company</td>
      <td>March 11, 2016</td>
      <td>June 16, 2016</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>542</th>
      <td>Superior Bank, FSB</td>
      <td>Hinsdale</td>
      <td>IL</td>
      <td>32646</td>
      <td>Superior Federal, FSB</td>
      <td>July 27, 2001</td>
      <td>August 19, 2014</td>
    </tr>
    <tr>
      <th>543</th>
      <td>Malta National Bank</td>
      <td>Malta</td>
      <td>OH</td>
      <td>6629</td>
      <td>North Valley Bank</td>
      <td>May 3, 2001</td>
      <td>November 18, 2002</td>
    </tr>
    <tr>
      <th>544</th>
      <td>First Alliance Bank &amp; Trust Co.</td>
      <td>Manchester</td>
      <td>NH</td>
      <td>34264</td>
      <td>Southern New Hampshire Bank &amp; Trust</td>
      <td>February 2, 2001</td>
      <td>February 18, 2003</td>
    </tr>
    <tr>
      <th>545</th>
      <td>National State Bank of Metropolis</td>
      <td>Metropolis</td>
      <td>IL</td>
      <td>3815</td>
      <td>Banterra Bank of Marion</td>
      <td>December 14, 2000</td>
      <td>March 17, 2005</td>
    </tr>
    <tr>
      <th>546</th>
      <td>Bank of Honolulu</td>
      <td>Honolulu</td>
      <td>HI</td>
      <td>21029</td>
      <td>Bank of the Orient</td>
      <td>October 13, 2000</td>
      <td>March 17, 2005</td>
    </tr>
  </tbody>
</table>
<p>547 rows × 7 columns</p>
</div>




```python
pd.read_excel("data/examples/ex1.xlsx")
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
      <th>Unnamed: 0</th>
      <th>a</th>
      <th>b</th>
      <th>c</th>
      <th>d</th>
      <th>message</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>3</td>
      <td>4</td>
      <td>hello</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>5</td>
      <td>6</td>
      <td>7</td>
      <td>8</td>
      <td>world</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>9</td>
      <td>10</td>
      <td>11</td>
      <td>12</td>
      <td>foo</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.read_excel("data/examples/ex1.xlsx", index_col=0) # Sheet1
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
      <th>a</th>
      <th>b</th>
      <th>c</th>
      <th>d</th>
      <th>message</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>2</td>
      <td>3</td>
      <td>4</td>
      <td>hello</td>
    </tr>
    <tr>
      <th>1</th>
      <td>5</td>
      <td>6</td>
      <td>7</td>
      <td>8</td>
      <td>world</td>
    </tr>
    <tr>
      <th>2</th>
      <td>9</td>
      <td>10</td>
      <td>11</td>
      <td>12</td>
      <td>foo</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.read_excel("data/examples/ex1.xlsx", index_col=0, sheet_name='Sheet1') # Sheet1
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
      <th>a</th>
      <th>b</th>
      <th>c</th>
      <th>d</th>
      <th>message</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>2</td>
      <td>3</td>
      <td>4</td>
      <td>hello</td>
    </tr>
    <tr>
      <th>1</th>
      <td>5</td>
      <td>6</td>
      <td>7</td>
      <td>8</td>
      <td>world</td>
    </tr>
    <tr>
      <th>2</th>
      <td>9</td>
      <td>10</td>
      <td>11</td>
      <td>12</td>
      <td>foo</td>
    </tr>
  </tbody>
</table>
</div>




```python
df = pd.read_excel("data/examples/ex1.xlsx", index_col=0, sheet_name='Sheet2') # Sheet2
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
      <th>q</th>
      <th>w</th>
      <th>e</th>
      <th>r</th>
      <th>message</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>2</td>
      <td>3</td>
      <td>4</td>
      <td>hello</td>
    </tr>
    <tr>
      <th>1</th>
      <td>5</td>
      <td>6</td>
      <td>7</td>
      <td>8</td>
      <td>world</td>
    </tr>
    <tr>
      <th>2</th>
      <td>9</td>
      <td>10</td>
      <td>11</td>
      <td>12</td>
      <td>foo</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.to_excel('ex1_copy.xlsx', sheet_name='MySheet1')
```


```python
# *titanic 데이터셋에 대해 다음 작업을 수행하시오.
df = pd.read_csv('data/datasets/titanic/train.csv')
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
      <th>PassengerId</th>
      <th>Survived</th>
      <th>Pclass</th>
      <th>Name</th>
      <th>Sex</th>
      <th>Age</th>
      <th>SibSp</th>
      <th>Parch</th>
      <th>Ticket</th>
      <th>Fare</th>
      <th>Cabin</th>
      <th>Embarked</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>Braund, Mr. Owen Harris</td>
      <td>male</td>
      <td>22.0</td>
      <td>1</td>
      <td>0</td>
      <td>A/5 21171</td>
      <td>7.2500</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>Cumings, Mrs. John Bradley (Florence Briggs Th...</td>
      <td>female</td>
      <td>38.0</td>
      <td>1</td>
      <td>0</td>
      <td>PC 17599</td>
      <td>71.2833</td>
      <td>C85</td>
      <td>C</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>Heikkinen, Miss. Laina</td>
      <td>female</td>
      <td>26.0</td>
      <td>0</td>
      <td>0</td>
      <td>STON/O2. 3101282</td>
      <td>7.9250</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>1</td>
      <td>1</td>
      <td>Futrelle, Mrs. Jacques Heath (Lily May Peel)</td>
      <td>female</td>
      <td>35.0</td>
      <td>1</td>
      <td>0</td>
      <td>113803</td>
      <td>53.1000</td>
      <td>C123</td>
      <td>S</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>0</td>
      <td>3</td>
      <td>Allen, Mr. William Henry</td>
      <td>male</td>
      <td>35.0</td>
      <td>0</td>
      <td>0</td>
      <td>373450</td>
      <td>8.0500</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>886</th>
      <td>887</td>
      <td>0</td>
      <td>2</td>
      <td>Montvila, Rev. Juozas</td>
      <td>male</td>
      <td>27.0</td>
      <td>0</td>
      <td>0</td>
      <td>211536</td>
      <td>13.0000</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>887</th>
      <td>888</td>
      <td>1</td>
      <td>1</td>
      <td>Graham, Miss. Margaret Edith</td>
      <td>female</td>
      <td>19.0</td>
      <td>0</td>
      <td>0</td>
      <td>112053</td>
      <td>30.0000</td>
      <td>B42</td>
      <td>S</td>
    </tr>
    <tr>
      <th>888</th>
      <td>889</td>
      <td>0</td>
      <td>3</td>
      <td>Johnston, Miss. Catherine Helen "Carrie"</td>
      <td>female</td>
      <td>NaN</td>
      <td>1</td>
      <td>2</td>
      <td>W./C. 6607</td>
      <td>23.4500</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>889</th>
      <td>890</td>
      <td>1</td>
      <td>1</td>
      <td>Behr, Mr. Karl Howell</td>
      <td>male</td>
      <td>26.0</td>
      <td>0</td>
      <td>0</td>
      <td>111369</td>
      <td>30.0000</td>
      <td>C148</td>
      <td>C</td>
    </tr>
    <tr>
      <th>890</th>
      <td>891</td>
      <td>0</td>
      <td>3</td>
      <td>Dooley, Mr. Patrick</td>
      <td>male</td>
      <td>32.0</td>
      <td>0</td>
      <td>0</td>
      <td>370376</td>
      <td>7.7500</td>
      <td>NaN</td>
      <td>Q</td>
    </tr>
  </tbody>
</table>
<p>891 rows × 12 columns</p>
</div>




```python
# 1. 승선항구(Embarked)가 'C'인 자료만 추출하시오.
df[df['Embarked'] == 'C']
# 2. SibSp + Parch 의 합이 0인 자료만 추출하시오.
df[df.SibSp + df.Parch == 0]
# 3. Pclass가 1인 자료만 추출하시오.
df[df['Pclass']==1]
# 4. Fare 열 값이 20이상 50미만인 자료만 추출하시오.
df[(df.Fare >= 20) & (df.Fare <50)]
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
      <th>PassengerId</th>
      <th>Survived</th>
      <th>Pclass</th>
      <th>Name</th>
      <th>Sex</th>
      <th>Age</th>
      <th>SibSp</th>
      <th>Parch</th>
      <th>Ticket</th>
      <th>Fare</th>
      <th>Cabin</th>
      <th>Embarked</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>7</th>
      <td>8</td>
      <td>0</td>
      <td>3</td>
      <td>Palsson, Master. Gosta Leonard</td>
      <td>male</td>
      <td>2.0</td>
      <td>3</td>
      <td>1</td>
      <td>349909</td>
      <td>21.0750</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>9</th>
      <td>10</td>
      <td>1</td>
      <td>2</td>
      <td>Nasser, Mrs. Nicholas (Adele Achem)</td>
      <td>female</td>
      <td>14.0</td>
      <td>1</td>
      <td>0</td>
      <td>237736</td>
      <td>30.0708</td>
      <td>NaN</td>
      <td>C</td>
    </tr>
    <tr>
      <th>11</th>
      <td>12</td>
      <td>1</td>
      <td>1</td>
      <td>Bonnell, Miss. Elizabeth</td>
      <td>female</td>
      <td>58.0</td>
      <td>0</td>
      <td>0</td>
      <td>113783</td>
      <td>26.5500</td>
      <td>C103</td>
      <td>S</td>
    </tr>
    <tr>
      <th>13</th>
      <td>14</td>
      <td>0</td>
      <td>3</td>
      <td>Andersson, Mr. Anders Johan</td>
      <td>male</td>
      <td>39.0</td>
      <td>1</td>
      <td>5</td>
      <td>347082</td>
      <td>31.2750</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>16</th>
      <td>17</td>
      <td>0</td>
      <td>3</td>
      <td>Rice, Master. Eugene</td>
      <td>male</td>
      <td>2.0</td>
      <td>4</td>
      <td>1</td>
      <td>382652</td>
      <td>29.1250</td>
      <td>NaN</td>
      <td>Q</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>880</th>
      <td>881</td>
      <td>1</td>
      <td>2</td>
      <td>Shelley, Mrs. William (Imanita Parrish Hall)</td>
      <td>female</td>
      <td>25.0</td>
      <td>0</td>
      <td>1</td>
      <td>230433</td>
      <td>26.0000</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>885</th>
      <td>886</td>
      <td>0</td>
      <td>3</td>
      <td>Rice, Mrs. William (Margaret Norton)</td>
      <td>female</td>
      <td>39.0</td>
      <td>0</td>
      <td>5</td>
      <td>382652</td>
      <td>29.1250</td>
      <td>NaN</td>
      <td>Q</td>
    </tr>
    <tr>
      <th>887</th>
      <td>888</td>
      <td>1</td>
      <td>1</td>
      <td>Graham, Miss. Margaret Edith</td>
      <td>female</td>
      <td>19.0</td>
      <td>0</td>
      <td>0</td>
      <td>112053</td>
      <td>30.0000</td>
      <td>B42</td>
      <td>S</td>
    </tr>
    <tr>
      <th>888</th>
      <td>889</td>
      <td>0</td>
      <td>3</td>
      <td>Johnston, Miss. Catherine Helen "Carrie"</td>
      <td>female</td>
      <td>NaN</td>
      <td>1</td>
      <td>2</td>
      <td>W./C. 6607</td>
      <td>23.4500</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>889</th>
      <td>890</td>
      <td>1</td>
      <td>1</td>
      <td>Behr, Mr. Karl Howell</td>
      <td>male</td>
      <td>26.0</td>
      <td>0</td>
      <td>0</td>
      <td>111369</td>
      <td>30.0000</td>
      <td>C148</td>
      <td>C</td>
    </tr>
  </tbody>
</table>
<p>215 rows × 12 columns</p>
</div>




```python
# * yahoo finance 사이트 데이터셋(finance.yahoo.com)
# 5. 2024년도 삼성전자 주가데이터를 가져온 다음 아래와 같은 작업을 수행해보세요.
df = pd.read_csv('samsung2024.csv', index_col=0)
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
      <th>Open</th>
      <th>High</th>
      <th>Low</th>
      <th>Close</th>
      <th>Adj Close</th>
      <th>Volume</th>
    </tr>
    <tr>
      <th>Date</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2023-05-24</th>
      <td>68100.0</td>
      <td>68700.0</td>
      <td>68000.0</td>
      <td>68500.0</td>
      <td>67485.750000</td>
      <td>8192896</td>
    </tr>
    <tr>
      <th>2023-05-25</th>
      <td>69900.0</td>
      <td>70000.0</td>
      <td>68700.0</td>
      <td>68800.0</td>
      <td>67781.312500</td>
      <td>14231160</td>
    </tr>
    <tr>
      <th>2023-05-26</th>
      <td>69800.0</td>
      <td>70400.0</td>
      <td>69500.0</td>
      <td>70300.0</td>
      <td>69259.093750</td>
      <td>19549511</td>
    </tr>
    <tr>
      <th>2023-05-30</th>
      <td>71300.0</td>
      <td>72300.0</td>
      <td>71200.0</td>
      <td>72300.0</td>
      <td>71229.492188</td>
      <td>27476897</td>
    </tr>
    <tr>
      <th>2023-05-31</th>
      <td>72400.0</td>
      <td>72500.0</td>
      <td>71000.0</td>
      <td>71400.0</td>
      <td>70342.812500</td>
      <td>25666087</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>2024-05-20</th>
      <td>78100.0</td>
      <td>79100.0</td>
      <td>77900.0</td>
      <td>78900.0</td>
      <td>78900.000000</td>
      <td>19456783</td>
    </tr>
    <tr>
      <th>2024-05-21</th>
      <td>78500.0</td>
      <td>79000.0</td>
      <td>78200.0</td>
      <td>78400.0</td>
      <td>78400.000000</td>
      <td>13690583</td>
    </tr>
    <tr>
      <th>2024-05-22</th>
      <td>78100.0</td>
      <td>78700.0</td>
      <td>77300.0</td>
      <td>77700.0</td>
      <td>77700.000000</td>
      <td>19521506</td>
    </tr>
    <tr>
      <th>2024-05-23</th>
      <td>77700.0</td>
      <td>79100.0</td>
      <td>77100.0</td>
      <td>78300.0</td>
      <td>78300.000000</td>
      <td>18728087</td>
    </tr>
    <tr>
      <th>2024-05-24</th>
      <td>76800.0</td>
      <td>77000.0</td>
      <td>75700.0</td>
      <td>75900.0</td>
      <td>75900.000000</td>
      <td>29022071</td>
    </tr>
  </tbody>
</table>
<p>245 rows × 6 columns</p>
</div>




```python
# 1) 각 열 단위로 최대값을 출력하시오.
df.max()
# 2) 각 열 단위로 최소값을 출력하시오.
df.apply(min)
# 3) 각 열 단위로 최대값-최소값을 출력하시오.
def max_min(a):
    return a.max()-a.min()
df.apply(max_min)
# 4) 기술통계를 구하시오.
# df.info()
df.describe()
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
      <th>Open</th>
      <th>High</th>
      <th>Low</th>
      <th>Close</th>
      <th>Adj Close</th>
      <th>Volume</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>245.000000</td>
      <td>245.000000</td>
      <td>245.00000</td>
      <td>245.000000</td>
      <td>245.000000</td>
      <td>2.450000e+02</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>73004.489796</td>
      <td>73557.551020</td>
      <td>72341.22449</td>
      <td>72919.591837</td>
      <td>72559.773055</td>
      <td>1.599096e+07</td>
    </tr>
    <tr>
      <th>std</th>
      <td>4179.254513</td>
      <td>4201.657816</td>
      <td>4030.83079</td>
      <td>4131.370371</td>
      <td>4351.893952</td>
      <td>6.855821e+06</td>
    </tr>
    <tr>
      <th>min</th>
      <td>66000.000000</td>
      <td>66700.000000</td>
      <td>65800.00000</td>
      <td>66000.000000</td>
      <td>65644.289063</td>
      <td>2.957915e+06</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>70100.000000</td>
      <td>70800.000000</td>
      <td>69600.00000</td>
      <td>70300.000000</td>
      <td>69604.726563</td>
      <td>1.155788e+07</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>72500.000000</td>
      <td>72900.000000</td>
      <td>72000.00000</td>
      <td>72400.000000</td>
      <td>72058.789063</td>
      <td>1.441728e+07</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>74600.000000</td>
      <td>75200.000000</td>
      <td>73700.00000</td>
      <td>74700.000000</td>
      <td>74646.539063</td>
      <td>1.900701e+07</td>
    </tr>
    <tr>
      <th>max</th>
      <td>85200.000000</td>
      <td>86000.000000</td>
      <td>84500.00000</td>
      <td>85300.000000</td>
      <td>85300.000000</td>
      <td>5.769127e+07</td>
    </tr>
  </tbody>
</table>
</div>




```python

```
