```python
import pandas as pd
import numpy as np
```


```python
ser = pd.Series(np.arange(3.))
ser
```




    0    0.0
    1    1.0
    2    2.0
    dtype: float64




```python
ser.loc[2]
ser.iloc[2]
ser.iloc[-1]
# ser.loc[-1], error
```




    2.0




```python
ser2 = pd.Series(np.arange(3.), index=["a", "b", "c"])
ser2
```




    a    0.0
    b    1.0
    c    2.0
    dtype: float64




```python
ser2.loc['c']
ser2.iloc[2]
ser2.iloc[-1]
```




    2.0




```python
ser2[:2]
ser2.iloc[:2]
```




    a    0.0
    b    1.0
    dtype: float64




```python
ser2[:]
```




    a    0.0
    b    1.0
    c    2.0
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
# one열에 모두 1을 저장
data['one'] = 1
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
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>3</td>
    </tr>
    <tr>
      <th>Colorado</th>
      <td>1</td>
      <td>5</td>
      <td>6</td>
      <td>7</td>
    </tr>
    <tr>
      <th>Utah</th>
      <td>1</td>
      <td>9</td>
      <td>10</td>
      <td>11</td>
    </tr>
    <tr>
      <th>New York</th>
      <td>1</td>
      <td>13</td>
      <td>14</td>
      <td>15</td>
    </tr>
  </tbody>
</table>
</div>




```python
data['one']
data.loc[:, 'one']=2
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
      <td>2</td>
      <td>1</td>
      <td>2</td>
      <td>3</td>
    </tr>
    <tr>
      <th>Colorado</th>
      <td>2</td>
      <td>5</td>
      <td>6</td>
      <td>7</td>
    </tr>
    <tr>
      <th>Utah</th>
      <td>2</td>
      <td>9</td>
      <td>10</td>
      <td>11</td>
    </tr>
    <tr>
      <th>New York</th>
      <td>2</td>
      <td>13</td>
      <td>14</td>
      <td>15</td>
    </tr>
  </tbody>
</table>
</div>




```python
data.iloc[2]=5
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
      <td>2</td>
      <td>1</td>
      <td>2</td>
      <td>3</td>
    </tr>
    <tr>
      <th>Colorado</th>
      <td>2</td>
      <td>5</td>
      <td>6</td>
      <td>7</td>
    </tr>
    <tr>
      <th>Utah</th>
      <td>5</td>
      <td>5</td>
      <td>5</td>
      <td>5</td>
    </tr>
    <tr>
      <th>New York</th>
      <td>2</td>
      <td>13</td>
      <td>14</td>
      <td>15</td>
    </tr>
  </tbody>
</table>
</div>




```python
# four 열의 값이 5보다 큰 데이터를 추출하시오
data[data['four']>5]
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
      <td>2</td>
      <td>5</td>
      <td>6</td>
      <td>7</td>
    </tr>
    <tr>
      <th>New York</th>
      <td>2</td>
      <td>13</td>
      <td>14</td>
      <td>15</td>
    </tr>
  </tbody>
</table>
</div>




```python
data.loc[data['four']>5]
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
      <td>2</td>
      <td>5</td>
      <td>6</td>
      <td>7</td>
    </tr>
    <tr>
      <th>New York</th>
      <td>2</td>
      <td>13</td>
      <td>14</td>
      <td>15</td>
    </tr>
  </tbody>
</table>
</div>




```python
# three 열 값이 5인 자료를 추출하시오
data[data['three']==5]
data.loc[data['three']==5]
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
      <td>5</td>
      <td>5</td>
      <td>5</td>
      <td>5</td>
    </tr>
  </tbody>
</table>
</div>




```python
# three 열 값이 5인 자료의 two 열 값을 추출하시오
data[data['three']==5]['two']
```




    Utah    5
    Name: two, dtype: int32




```python
data[data['three']==5][['two']]
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
      <th>two</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Utah</th>
      <td>5</td>
    </tr>
  </tbody>
</table>
</div>




```python
data.loc[data['three']==5, 'two']=10
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
      <td>2</td>
      <td>1</td>
      <td>2</td>
      <td>3</td>
    </tr>
    <tr>
      <th>Colorado</th>
      <td>2</td>
      <td>5</td>
      <td>6</td>
      <td>7</td>
    </tr>
    <tr>
      <th>Utah</th>
      <td>5</td>
      <td>10</td>
      <td>5</td>
      <td>5</td>
    </tr>
    <tr>
      <th>New York</th>
      <td>2</td>
      <td>13</td>
      <td>14</td>
      <td>15</td>
    </tr>
  </tbody>
</table>
</div>




```python
s1 = pd.Series([7.3, -2.5, 3.4, 1.5], index=["a", "c", "d", "e"])
s2 = pd.Series([-2.1, 3.6, -1.5, 4, 3.1],
               index=["a", "c", "e", "f", "g"])
```


```python
s1
```




    a    7.3
    c   -2.5
    d    3.4
    e    1.5
    dtype: float64




```python
s2
```




    a   -2.1
    c    3.6
    e   -1.5
    f    4.0
    g    3.1
    dtype: float64




```python
s1+s2
```




    a    5.2
    c    1.1
    d    NaN
    e    0.0
    f    NaN
    g    NaN
    dtype: float64




```python
list('bcd')
```




    ['b', 'c', 'd']




```python
# df1 = pd.DataFrame(np.arange(9.).reshape(3,3), columns=['b', 'c', 'd'])
df1 = pd.DataFrame(np.arange(9.).reshape(3,3), columns=list('bcd'),
                   index=["Ohio", "Texas", "Colorado"])
df1
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
      <th>b</th>
      <th>c</th>
      <th>d</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Ohio</th>
      <td>0.0</td>
      <td>1.0</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>Texas</th>
      <td>3.0</td>
      <td>4.0</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>Colorado</th>
      <td>6.0</td>
      <td>7.0</td>
      <td>8.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
df2 = pd.DataFrame(np.arange(12.).reshape((4, 3)), columns=list("bde"),
                   index=["Utah", "Ohio", "Texas", "Oregon"])
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
      <th>b</th>
      <th>d</th>
      <th>e</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Utah</th>
      <td>0.0</td>
      <td>1.0</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>Ohio</th>
      <td>3.0</td>
      <td>4.0</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>Texas</th>
      <td>6.0</td>
      <td>7.0</td>
      <td>8.0</td>
    </tr>
    <tr>
      <th>Oregon</th>
      <td>9.0</td>
      <td>10.0</td>
      <td>11.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
df1 + df2
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
      <th>b</th>
      <th>c</th>
      <th>d</th>
      <th>e</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Colorado</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Ohio</th>
      <td>3.0</td>
      <td>NaN</td>
      <td>6.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Oregon</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Texas</th>
      <td>9.0</td>
      <td>NaN</td>
      <td>12.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Utah</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
df1 = pd.DataFrame({"A": [1, 2]})
df2 = pd.DataFrame({"B": [3, 4]})
```


```python
df1
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
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>




```python
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
      <th>B</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>3</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>




```python
df1+df2
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
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
df1 = pd.DataFrame(np.arange(12.).reshape((3, 4)),
                   columns=list("abcd"))
df2 = pd.DataFrame(np.arange(20.).reshape((4, 5)),
                   columns=list("abcde"))
```


```python
df1
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
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.0</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4.0</td>
      <td>5.0</td>
      <td>6.0</td>
      <td>7.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>8.0</td>
      <td>9.0</td>
      <td>10.0</td>
      <td>11.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
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
      <th>e</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.0</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>3.0</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>5.0</td>
      <td>6.0</td>
      <td>7.0</td>
      <td>8.0</td>
      <td>9.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>10.0</td>
      <td>11.0</td>
      <td>12.0</td>
      <td>13.0</td>
      <td>14.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>15.0</td>
      <td>16.0</td>
      <td>17.0</td>
      <td>18.0</td>
      <td>19.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
df1 + df2
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
      <th>e</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.0</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>6.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>9.0</td>
      <td>11.0</td>
      <td>13.0</td>
      <td>15.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>18.0</td>
      <td>20.0</td>
      <td>22.0</td>
      <td>24.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
df2['b'].loc[1]
df2['b'][1]
df2.loc[1, 'b']
df2.b[1]
```




    6.0




```python
np.nan # 결측값
```




    nan




```python
# df2['b'][1] = 2
df2['b'][1]=np.nan
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
      <th>e</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.0</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>3.0</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>5.0</td>
      <td>NaN</td>
      <td>7.0</td>
      <td>8.0</td>
      <td>9.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>10.0</td>
      <td>11.0</td>
      <td>12.0</td>
      <td>13.0</td>
      <td>14.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>15.0</td>
      <td>16.0</td>
      <td>17.0</td>
      <td>18.0</td>
      <td>19.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
df1 + df2
df1.add(df2)
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
      <th>e</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.0</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>6.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>9.0</td>
      <td>NaN</td>
      <td>13.0</td>
      <td>15.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>18.0</td>
      <td>20.0</td>
      <td>22.0</td>
      <td>24.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
df1.add(df2, fill_value=0) # fill_value=0 : NaN을 0으로 채워라
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
      <th>e</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.0</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>6.0</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>9.0</td>
      <td>5.0</td>
      <td>13.0</td>
      <td>15.0</td>
      <td>9.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>18.0</td>
      <td>20.0</td>
      <td>22.0</td>
      <td>24.0</td>
      <td>14.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>15.0</td>
      <td>16.0</td>
      <td>17.0</td>
      <td>18.0</td>
      <td>19.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
1/df1
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
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>inf</td>
      <td>1.000000</td>
      <td>0.500000</td>
      <td>0.333333</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.250</td>
      <td>0.200000</td>
      <td>0.166667</td>
      <td>0.142857</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.125</td>
      <td>0.111111</td>
      <td>0.100000</td>
      <td>0.090909</td>
    </tr>
  </tbody>
</table>
</div>




```python
df1.rdiv(1)
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
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>inf</td>
      <td>1.000000</td>
      <td>0.500000</td>
      <td>0.333333</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.250</td>
      <td>0.200000</td>
      <td>0.166667</td>
      <td>0.142857</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.125</td>
      <td>0.111111</td>
      <td>0.100000</td>
      <td>0.090909</td>
    </tr>
  </tbody>
</table>
</div>




```python
df1.div(2) # df/2
df1.rdiv(2) # 2/df
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
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>inf</td>
      <td>2.000000</td>
      <td>1.000000</td>
      <td>0.666667</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.50</td>
      <td>0.400000</td>
      <td>0.333333</td>
      <td>0.285714</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.25</td>
      <td>0.222222</td>
      <td>0.200000</td>
      <td>0.181818</td>
    </tr>
  </tbody>
</table>
</div>




```python
df1
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
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.0</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4.0</td>
      <td>5.0</td>
      <td>6.0</td>
      <td>7.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>8.0</td>
      <td>9.0</td>
      <td>10.0</td>
      <td>11.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
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
      <th>e</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.0</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>3.0</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>5.0</td>
      <td>NaN</td>
      <td>7.0</td>
      <td>8.0</td>
      <td>9.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>10.0</td>
      <td>11.0</td>
      <td>12.0</td>
      <td>13.0</td>
      <td>14.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>15.0</td>
      <td>16.0</td>
      <td>17.0</td>
      <td>18.0</td>
      <td>19.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
# df1.index
df1.columns
```




    Index(['a', 'b', 'c', 'd'], dtype='object')




```python
df2.columns
```




    Index(['a', 'b', 'c', 'd', 'e'], dtype='object')




```python
df1.reindex(columns=df2.columns, fill_value=0)
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
      <th>e</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.0</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>3.0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4.0</td>
      <td>5.0</td>
      <td>6.0</td>
      <td>7.0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>8.0</td>
      <td>9.0</td>
      <td>10.0</td>
      <td>11.0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>




```python
arr = np.arange(12.).reshape((3, 4))
arr
```




    array([[ 0.,  1.,  2.,  3.],
           [ 4.,  5.,  6.,  7.],
           [ 8.,  9., 10., 11.]])




```python
arr[0]
```




    array([0., 1., 2., 3.])




```python
arr-arr[0]
```




    array([[0., 0., 0., 0.],
           [4., 4., 4., 4.],
           [8., 8., 8., 8.]])




```python
frame = pd.DataFrame(np.arange(12.).reshape((4, 3)),
                     columns=list("bde"),
                     index=["Utah", "Ohio", "Texas", "Oregon"])
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
      <th>b</th>
      <th>d</th>
      <th>e</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Utah</th>
      <td>0.0</td>
      <td>1.0</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>Ohio</th>
      <td>3.0</td>
      <td>4.0</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>Texas</th>
      <td>6.0</td>
      <td>7.0</td>
      <td>8.0</td>
    </tr>
    <tr>
      <th>Oregon</th>
      <td>9.0</td>
      <td>10.0</td>
      <td>11.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
ser=frame.iloc[0]
ser
```




    b    0.0
    d    1.0
    e    2.0
    Name: Utah, dtype: float64




```python
frame-ser
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
      <th>b</th>
      <th>d</th>
      <th>e</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Utah</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>Ohio</th>
      <td>3.0</td>
      <td>3.0</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>Texas</th>
      <td>6.0</td>
      <td>6.0</td>
      <td>6.0</td>
    </tr>
    <tr>
      <th>Oregon</th>
      <td>9.0</td>
      <td>9.0</td>
      <td>9.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
series2 = pd.Series(np.arange(3), index=["b", "e", "f"])
series2
```




    b    0
    e    1
    f    2
    dtype: int32




```python
frame-series2
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
      <th>b</th>
      <th>d</th>
      <th>e</th>
      <th>f</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Utah</th>
      <td>0.0</td>
      <td>NaN</td>
      <td>1.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Ohio</th>
      <td>3.0</td>
      <td>NaN</td>
      <td>4.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Texas</th>
      <td>6.0</td>
      <td>NaN</td>
      <td>7.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Oregon</th>
      <td>9.0</td>
      <td>NaN</td>
      <td>10.0</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame.sub(series2)
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
      <th>b</th>
      <th>d</th>
      <th>e</th>
      <th>f</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Utah</th>
      <td>0.0</td>
      <td>NaN</td>
      <td>1.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Ohio</th>
      <td>3.0</td>
      <td>NaN</td>
      <td>4.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Texas</th>
      <td>6.0</td>
      <td>NaN</td>
      <td>7.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Oregon</th>
      <td>9.0</td>
      <td>NaN</td>
      <td>10.0</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame = pd.DataFrame(np.random.standard_normal((4, 3)),
                     columns=list("bde"),
                     index=["Utah", "Ohio", "Texas", "Oregon"])
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
      <th>b</th>
      <th>d</th>
      <th>e</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Utah</th>
      <td>-0.676655</td>
      <td>0.716241</td>
      <td>-2.116243</td>
    </tr>
    <tr>
      <th>Ohio</th>
      <td>-0.374615</td>
      <td>0.694301</td>
      <td>0.190466</td>
    </tr>
    <tr>
      <th>Texas</th>
      <td>-1.006158</td>
      <td>0.112140</td>
      <td>1.279163</td>
    </tr>
    <tr>
      <th>Oregon</th>
      <td>-0.107513</td>
      <td>-0.940028</td>
      <td>-1.677025</td>
    </tr>
  </tbody>
</table>
</div>




```python
np.abs(frame) # 절대값
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
      <th>b</th>
      <th>d</th>
      <th>e</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Utah</th>
      <td>0.676655</td>
      <td>0.716241</td>
      <td>2.116243</td>
    </tr>
    <tr>
      <th>Ohio</th>
      <td>0.374615</td>
      <td>0.694301</td>
      <td>0.190466</td>
    </tr>
    <tr>
      <th>Texas</th>
      <td>1.006158</td>
      <td>0.112140</td>
      <td>1.279163</td>
    </tr>
    <tr>
      <th>Oregon</th>
      <td>0.107513</td>
      <td>0.940028</td>
      <td>1.677025</td>
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
      <th>b</th>
      <th>d</th>
      <th>e</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Utah</th>
      <td>-0.676655</td>
      <td>0.716241</td>
      <td>-2.116243</td>
    </tr>
    <tr>
      <th>Ohio</th>
      <td>-0.374615</td>
      <td>0.694301</td>
      <td>0.190466</td>
    </tr>
    <tr>
      <th>Texas</th>
      <td>-1.006158</td>
      <td>0.112140</td>
      <td>1.279163</td>
    </tr>
    <tr>
      <th>Oregon</th>
      <td>-0.107513</td>
      <td>-0.940028</td>
      <td>-1.677025</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 열 단위로 최대값, 최소값 구해서 차를 출력
# max, min 함수
frame['b'].max()
frame['b'].min()
frame['b'].max()-frame['b'].min()
```




    0.8986446364652578




```python
def f1(x): # f1 함수에 각각의 열들이 하나씩 전달
    return x.max()-x.min()
#     print(x)
#     print(x.max())
#     print(x.min())
#     print(x.max()-x.min())
#     print('='*50)
    
frame.apply(f1) # frame에 열 단위로 f1함수를 적용해라
```




    b    0.898645
    d    1.656268
    e    3.395406
    dtype: float64




```python
def f1(x): # f1 함수에 각각의 열들이 하나씩 전달
    return x.max()-x.min()

frame.apply(f1, axis='columns') # frame에 열 단위로 f1함수를 적용해라
```




    Utah      2.832484
    Ohio      1.068917
    Texas     2.285320
    Oregon    1.569512
    dtype: float64




```python
def f1(x): # f1 함수에 각각의 열들이 하나씩 전달
    return x.max()-x.min()

frame.apply(f1, axis=0) # frame에 열 단위로 f1함수를 적용해라, axis=0 기본값
```




    b    0.898645
    d    1.656268
    e    3.395406
    dtype: float64




```python
def f1(x): # f1 함수에 각각의 열들이 하나씩 전달
    return x.max()-x.min()

frame.apply(f1, axis=1) # frame에 열 단위로 f1함수를 적용해라
```




    Utah      2.832484
    Ohio      1.068917
    Texas     2.285320
    Oregon    1.569512
    dtype: float64




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
      <th>b</th>
      <th>d</th>
      <th>e</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Utah</th>
      <td>-0.676655</td>
      <td>0.716241</td>
      <td>-2.116243</td>
    </tr>
    <tr>
      <th>Ohio</th>
      <td>-0.374615</td>
      <td>0.694301</td>
      <td>0.190466</td>
    </tr>
    <tr>
      <th>Texas</th>
      <td>-1.006158</td>
      <td>0.112140</td>
      <td>1.279163</td>
    </tr>
    <tr>
      <th>Oregon</th>
      <td>-0.107513</td>
      <td>-0.940028</td>
      <td>-1.677025</td>
    </tr>
  </tbody>
</table>
</div>




```python
def f2(x): # f1 함수에 각각의 열들이 하나씩 전달
    return x.max(), x.min()

frame.apply(f2, axis=0) # frame에 열 단위로 f1함수를 적용해라
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
      <th>b</th>
      <th>d</th>
      <th>e</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>-0.107513</td>
      <td>0.716241</td>
      <td>1.279163</td>
    </tr>
    <tr>
      <th>1</th>
      <td>-1.006158</td>
      <td>-0.940028</td>
      <td>-2.116243</td>
    </tr>
  </tbody>
</table>
</div>




```python
def f2(x): # f1 함수에 각각의 열들이 하나씩 전달
    return pd.Series([x.max(), x.min()])

frame.apply(f2, axis=0) # frame에 열 단위로 f1함수를 적용해라
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
      <th>b</th>
      <th>d</th>
      <th>e</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>-0.107513</td>
      <td>0.716241</td>
      <td>1.279163</td>
    </tr>
    <tr>
      <th>1</th>
      <td>-1.006158</td>
      <td>-0.940028</td>
      <td>-2.116243</td>
    </tr>
  </tbody>
</table>
</div>




```python
def f2(x): # f1 함수에 각각의 열들이 하나씩 전달
    return pd.Series([x.max(), x.min()], index=['max', 'min'])

frame.apply(f2, axis=0) # frame에 열 단위로 f1함수를 적용해라
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
      <th>b</th>
      <th>d</th>
      <th>e</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>max</th>
      <td>-0.107513</td>
      <td>0.716241</td>
      <td>1.279163</td>
    </tr>
    <tr>
      <th>min</th>
      <td>-1.006158</td>
      <td>-0.940028</td>
      <td>-2.116243</td>
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
      <th>b</th>
      <th>d</th>
      <th>e</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Utah</th>
      <td>-0.676655</td>
      <td>0.716241</td>
      <td>-2.116243</td>
    </tr>
    <tr>
      <th>Ohio</th>
      <td>-0.374615</td>
      <td>0.694301</td>
      <td>0.190466</td>
    </tr>
    <tr>
      <th>Texas</th>
      <td>-1.006158</td>
      <td>0.112140</td>
      <td>1.279163</td>
    </tr>
    <tr>
      <th>Oregon</th>
      <td>-0.107513</td>
      <td>-0.940028</td>
      <td>-1.677025</td>
    </tr>
  </tbody>
</table>
</div>




```python
print(f'{-0.676655:.2f}')
```

    -0.68
    


```python
x=1.161038
print(f'{x:.2f}')
```

    1.16
    


```python
def my_format(x):
    return f'{x:.2f}'

frame.applymap(my_format)
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
      <th>b</th>
      <th>d</th>
      <th>e</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Utah</th>
      <td>-0.68</td>
      <td>0.72</td>
      <td>-2.12</td>
    </tr>
    <tr>
      <th>Ohio</th>
      <td>-0.37</td>
      <td>0.69</td>
      <td>0.19</td>
    </tr>
    <tr>
      <th>Texas</th>
      <td>-1.01</td>
      <td>0.11</td>
      <td>1.28</td>
    </tr>
    <tr>
      <th>Oregon</th>
      <td>-0.11</td>
      <td>-0.94</td>
      <td>-1.68</td>
    </tr>
  </tbody>
</table>
</div>




```python
# def my_format(x):
#     return f'{x:.2f}'

# frame['b'].applymap(my_format) # 시리즈에서는 applymap을 사용할 수 없다

def my_format(x):
    return f'{x:.2f}'

frame['b'].map(my_format) # 시리즈에서는 map 함수를 사용하여 각 데이터를 변환
```




    Utah      -0.68
    Ohio      -0.37
    Texas     -1.01
    Oregon    -0.11
    Name: b, dtype: object




```python
import seaborn as sns
```


```python
tips = sns.load_dataset('tips')
tips
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
      <th>total_bill</th>
      <th>tip</th>
      <th>sex</th>
      <th>smoker</th>
      <th>day</th>
      <th>time</th>
      <th>size</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>16.99</td>
      <td>1.01</td>
      <td>Female</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>10.34</td>
      <td>1.66</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>21.01</td>
      <td>3.50</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>23.68</td>
      <td>3.31</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>24.59</td>
      <td>3.61</td>
      <td>Female</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>4</td>
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
      <th>239</th>
      <td>29.03</td>
      <td>5.92</td>
      <td>Male</td>
      <td>No</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>3</td>
    </tr>
    <tr>
      <th>240</th>
      <td>27.18</td>
      <td>2.00</td>
      <td>Female</td>
      <td>Yes</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
    <tr>
      <th>241</th>
      <td>22.67</td>
      <td>2.00</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
    <tr>
      <th>242</th>
      <td>17.82</td>
      <td>1.75</td>
      <td>Male</td>
      <td>No</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
    <tr>
      <th>243</th>
      <td>18.78</td>
      <td>3.00</td>
      <td>Female</td>
      <td>No</td>
      <td>Thur</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
<p>244 rows × 7 columns</p>
</div>




```python
print(tips['tip'].max())
print(tips['tip'].min())
```

    10.0
    1.0
    


```python
# def myformat(x):
#     return x.max(), x.min()

# pd.DataFrame(tips['tip']).apply(myformat)
def max_min(x):
    return x.max(), x.min()
pd.DataFrame(tips['tip']).apply(max_min)
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
      <th>tip</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>10.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
tips['tip'].max() - tips['tip'].min()
```




    9.0




```python
frame = pd.DataFrame(np.arange(8).reshape((2, 4)),
                     index=["three", "one"],
                     columns=["d", "a", "b", "c"])
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
      <th>d</th>
      <th>a</th>
      <th>b</th>
      <th>c</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>three</th>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>3</td>
    </tr>
    <tr>
      <th>one</th>
      <td>4</td>
      <td>5</td>
      <td>6</td>
      <td>7</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame.sort_index()
frame.sort_index(axis='columns')
frame.sort_index(axis='columns', ascending=False)
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
      <th>d</th>
      <th>c</th>
      <th>b</th>
      <th>a</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>three</th>
      <td>0</td>
      <td>3</td>
      <td>2</td>
      <td>1</td>
    </tr>
    <tr>
      <th>one</th>
      <td>4</td>
      <td>7</td>
      <td>6</td>
      <td>5</td>
    </tr>
  </tbody>
</table>
</div>




```python
obj = pd.Series([4, 7, -3, 2])
obj
```




    0    4
    1    7
    2   -3
    3    2
    dtype: int64




```python
obj.sort_values()
obj.sort_values(ascending=False)
```




    1    7
    0    4
    3    2
    2   -3
    dtype: int64




```python
obj = pd.Series([4, np.nan, 7, np.nan, -3, 2])
obj
```




    0    4.0
    1    NaN
    2    7.0
    3    NaN
    4   -3.0
    5    2.0
    dtype: float64




```python
obj.sort_values()
```




    4   -3.0
    5    2.0
    0    4.0
    2    7.0
    1    NaN
    3    NaN
    dtype: float64




```python
obj.sort_values(ascending=False) # NaN은 열외
```




    2    7.0
    0    4.0
    5    2.0
    4   -3.0
    1    NaN
    3    NaN
    dtype: float64




```python
obj.sort_values(na_position='first')
```




    1    NaN
    3    NaN
    4   -3.0
    5    2.0
    0    4.0
    2    7.0
    dtype: float64




```python
frame = pd.DataFrame({"b": [4, 7, -3, 2], "a": [0, 1, 0, 1]})
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
      <th>b</th>
      <th>a</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>4</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>7</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-3</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame.sort_values('a')
frame.sort_values(['a', 'b'])
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
      <th>b</th>
      <th>a</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2</th>
      <td>-3</td>
      <td>0</td>
    </tr>
    <tr>
      <th>0</th>
      <td>4</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>7</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>




```python
obj = pd.Series([7, -5, 7, 4, 2, 0, 4])
obj
```




    0    7
    1   -5
    2    7
    3    4
    4    2
    5    0
    6    4
    dtype: int64




```python
obj.rank()
obj.rank(method='first')
```




    0    6.0
    1    1.0
    2    7.0
    3    4.0
    4    3.0
    5    2.0
    6    5.0
    dtype: float64




```python
obj.rank(ascending=False)
```




    0    1.5
    1    7.0
    2    1.5
    3    3.5
    4    5.0
    5    6.0
    6    3.5
    dtype: float64




```python
frame = pd.DataFrame({"b": [4.3, 7, -3, 2], "a": [0, 1, 0, 1],
                      "c": [-2, 5, 8, -2.5]})
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
      <th>b</th>
      <th>a</th>
      <th>c</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>4.3</td>
      <td>0</td>
      <td>-2.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>7.0</td>
      <td>1</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-3.0</td>
      <td>0</td>
      <td>8.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2.0</td>
      <td>1</td>
      <td>-2.5</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame.rank() # frame.rank(axis=0)
frame.rank(axis=1)
frame.rank(axis='columns')
# axis=0 : index, axis=1 : columns
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
      <th>b</th>
      <th>a</th>
      <th>c</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>3.0</td>
      <td>2.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3.0</td>
      <td>1.0</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1.0</td>
      <td>2.0</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3.0</td>
      <td>2.0</td>
      <td>1.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame.rank(axis=1, ascending=False)
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
      <th>b</th>
      <th>a</th>
      <th>c</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1.0</td>
      <td>2.0</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1.0</td>
      <td>3.0</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3.0</td>
      <td>2.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1.0</td>
      <td>2.0</td>
      <td>3.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
obj = pd.Series(np.arange(5), index=["a", "a", "b", "b", "c"])
obj
```




    a    0
    a    1
    b    2
    b    3
    c    4
    dtype: int32




```python
obj.index.is_unique
```




    False




```python
df = pd.DataFrame(np.random.standard_normal((5, 3)),
                  index=["a", "a", "b", "b", "c"])
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
      <th>0</th>
      <th>1</th>
      <th>2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>-0.068547</td>
      <td>-0.064012</td>
      <td>0.869298</td>
    </tr>
    <tr>
      <th>a</th>
      <td>0.616236</td>
      <td>2.222751</td>
      <td>0.272216</td>
    </tr>
    <tr>
      <th>b</th>
      <td>-0.251076</td>
      <td>-0.762235</td>
      <td>-0.521090</td>
    </tr>
    <tr>
      <th>b</th>
      <td>-0.367095</td>
      <td>-1.141942</td>
      <td>-0.535416</td>
    </tr>
    <tr>
      <th>c</th>
      <td>1.416959</td>
      <td>-0.109812</td>
      <td>-0.707217</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.loc['b']
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
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>b</th>
      <td>-0.251076</td>
      <td>-0.762235</td>
      <td>-0.521090</td>
    </tr>
    <tr>
      <th>b</th>
      <td>-0.367095</td>
      <td>-1.141942</td>
      <td>-0.535416</td>
    </tr>
  </tbody>
</table>
</div>




```python
df = pd.DataFrame([[1.4, np.nan], [7.1, -4.5],
                   [np.nan, np.nan], [0.75, -1.3]],
                  index=["a", "b", "c", "d"],
                  columns=["one", "two"])
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
      <th>one</th>
      <th>two</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>1.40</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>b</th>
      <td>7.10</td>
      <td>-4.5</td>
    </tr>
    <tr>
      <th>c</th>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>d</th>
      <td>0.75</td>
      <td>-1.3</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.sum()
# axis=0 : index, axis=1 : columns
```




    one    9.25
    two   -5.80
    dtype: float64




```python
df.sum(axis=0)
df.sum(axis='index')
df.sum(axis=1)
```




    a    1.40
    b    2.60
    c    0.00
    d   -0.55
    dtype: float64




```python
df.sum(axis='index', skipna=False)
```




    one   NaN
    two   NaN
    dtype: float64




```python
df
df.mean()
```




    one    3.083333
    two   -2.900000
    dtype: float64




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
      <th>one</th>
      <th>two</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>1.40</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>b</th>
      <td>7.10</td>
      <td>-4.5</td>
    </tr>
    <tr>
      <th>c</th>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>d</th>
      <td>0.75</td>
      <td>-1.3</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.idxmax()
```




    one    b
    two    d
    dtype: object




```python
df.cumsum()
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
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>1.40</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>b</th>
      <td>8.50</td>
      <td>-4.5</td>
    </tr>
    <tr>
      <th>c</th>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>d</th>
      <td>9.25</td>
      <td>-5.8</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.describe() # 기술통계
df.info()
```

    <class 'pandas.core.frame.DataFrame'>
    Index: 4 entries, a to d
    Data columns (total 2 columns):
     #   Column  Non-Null Count  Dtype  
    ---  ------  --------------  -----  
     0   one     3 non-null      float64
     1   two     2 non-null      float64
    dtypes: float64(2)
    memory usage: 268.0+ bytes
    


```python
pd.read_csv('data/datasets/titanic/train.csv')
# pd.read_csv('../data/datasets/titanic/train.csv') 현재 파일 위치 기준으로 한단계 상위폴더로 이동한 다음 data 폴더로 이동
# pd.read_csv('../../data/datasets/titanic/train.csv') 두단계 상위폴더로 이동 후
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
df = pd.read_csv('pew.csv')
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
      <th>&lt;$10k</th>
      <th>$10-20k</th>
      <th>$20-30k</th>
      <th>$30-40k</th>
      <th>$40-50k</th>
      <th>$50-75k</th>
      <th>$75-100k</th>
      <th>$100-150k</th>
      <th>&gt;150k</th>
      <th>Don't know/refused</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>18.000000</td>
      <td>18.000000</td>
      <td>18.000000</td>
      <td>18.000000</td>
      <td>18.000000</td>
      <td>18.000000</td>
      <td>18.000000</td>
      <td>18.000000</td>
      <td>18.000000</td>
      <td>18.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>107.222222</td>
      <td>154.500000</td>
      <td>186.500000</td>
      <td>183.444444</td>
      <td>171.388889</td>
      <td>288.055556</td>
      <td>221.666667</td>
      <td>177.611111</td>
      <td>144.888889</td>
      <td>340.055556</td>
    </tr>
    <tr>
      <th>std</th>
      <td>168.931784</td>
      <td>255.172433</td>
      <td>309.891869</td>
      <td>291.470354</td>
      <td>271.144446</td>
      <td>458.442436</td>
      <td>345.078849</td>
      <td>275.679724</td>
      <td>205.224952</td>
      <td>530.523878</td>
    </tr>
    <tr>
      <th>min</th>
      <td>1.000000</td>
      <td>2.000000</td>
      <td>3.000000</td>
      <td>4.000000</td>
      <td>2.000000</td>
      <td>7.000000</td>
      <td>3.000000</td>
      <td>4.000000</td>
      <td>4.000000</td>
      <td>8.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>12.250000</td>
      <td>14.750000</td>
      <td>17.000000</td>
      <td>15.750000</td>
      <td>15.000000</td>
      <td>34.250000</td>
      <td>25.250000</td>
      <td>22.500000</td>
      <td>23.750000</td>
      <td>41.250000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>20.000000</td>
      <td>27.000000</td>
      <td>33.500000</td>
      <td>40.000000</td>
      <td>34.000000</td>
      <td>66.500000</td>
      <td>65.500000</td>
      <td>48.500000</td>
      <td>53.500000</td>
      <td>74.500000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>170.000000</td>
      <td>193.000000</td>
      <td>192.000000</td>
      <td>198.750000</td>
      <td>166.750000</td>
      <td>201.500000</td>
      <td>128.750000</td>
      <td>103.500000</td>
      <td>134.250000</td>
      <td>294.750000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>575.000000</td>
      <td>869.000000</td>
      <td>1064.000000</td>
      <td>982.000000</td>
      <td>881.000000</td>
      <td>1486.000000</td>
      <td>949.000000</td>
      <td>792.000000</td>
      <td>634.000000</td>
      <td>1529.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
# tesla_stock_quandl
df = pd.read_csv('tesla_stock_quandl.csv')
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
      <th>Date</th>
      <th>Open</th>
      <th>High</th>
      <th>Low</th>
      <th>Close</th>
      <th>Volume</th>
      <th>ExDividend</th>
      <th>SplitRatio</th>
      <th>AdjOpen</th>
      <th>AdjHigh</th>
      <th>AdjLow</th>
      <th>AdjClose</th>
      <th>AdjVolume</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2018-03-27</td>
      <td>304.00</td>
      <td>304.2700</td>
      <td>277.18</td>
      <td>279.18</td>
      <td>13696168.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>304.00</td>
      <td>304.2700</td>
      <td>277.18</td>
      <td>279.18</td>
      <td>13696168.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2018-03-26</td>
      <td>307.34</td>
      <td>307.5900</td>
      <td>291.36</td>
      <td>304.18</td>
      <td>8324639.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>307.34</td>
      <td>307.5900</td>
      <td>291.36</td>
      <td>304.18</td>
      <td>8324639.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2018-03-23</td>
      <td>311.25</td>
      <td>311.6100</td>
      <td>300.45</td>
      <td>301.54</td>
      <td>6600538.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>311.25</td>
      <td>311.6100</td>
      <td>300.45</td>
      <td>301.54</td>
      <td>6600538.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2018-03-22</td>
      <td>313.89</td>
      <td>318.8200</td>
      <td>308.18</td>
      <td>309.10</td>
      <td>4914307.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>313.89</td>
      <td>318.8200</td>
      <td>308.18</td>
      <td>309.10</td>
      <td>4914307.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2018-03-21</td>
      <td>310.25</td>
      <td>322.4400</td>
      <td>310.19</td>
      <td>316.53</td>
      <td>5927881.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>310.25</td>
      <td>322.4400</td>
      <td>310.19</td>
      <td>316.53</td>
      <td>5927881.0</td>
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
      <td>...</td>
    </tr>
    <tr>
      <th>1944</th>
      <td>2010-07-06</td>
      <td>20.00</td>
      <td>20.0000</td>
      <td>15.83</td>
      <td>16.11</td>
      <td>6866900.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>20.00</td>
      <td>20.0000</td>
      <td>15.83</td>
      <td>16.11</td>
      <td>6866900.0</td>
    </tr>
    <tr>
      <th>1945</th>
      <td>2010-07-02</td>
      <td>23.00</td>
      <td>23.1000</td>
      <td>18.71</td>
      <td>19.20</td>
      <td>5139800.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>23.00</td>
      <td>23.1000</td>
      <td>18.71</td>
      <td>19.20</td>
      <td>5139800.0</td>
    </tr>
    <tr>
      <th>1946</th>
      <td>2010-07-01</td>
      <td>25.00</td>
      <td>25.9200</td>
      <td>20.27</td>
      <td>21.96</td>
      <td>8218800.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>25.00</td>
      <td>25.9200</td>
      <td>20.27</td>
      <td>21.96</td>
      <td>8218800.0</td>
    </tr>
    <tr>
      <th>1947</th>
      <td>2010-06-30</td>
      <td>25.79</td>
      <td>30.4192</td>
      <td>23.30</td>
      <td>23.83</td>
      <td>17187100.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>25.79</td>
      <td>30.4192</td>
      <td>23.30</td>
      <td>23.83</td>
      <td>17187100.0</td>
    </tr>
    <tr>
      <th>1948</th>
      <td>2010-06-29</td>
      <td>19.00</td>
      <td>25.0000</td>
      <td>17.54</td>
      <td>23.89</td>
      <td>18766300.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>19.00</td>
      <td>25.0000</td>
      <td>17.54</td>
      <td>23.89</td>
      <td>18766300.0</td>
    </tr>
  </tbody>
</table>
<p>1949 rows × 13 columns</p>
</div>




```python
df = pd.read_csv('gapminder.tsv', sep='\t')
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
      <th>country</th>
      <th>continent</th>
      <th>year</th>
      <th>lifeExp</th>
      <th>pop</th>
      <th>gdpPercap</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Afghanistan</td>
      <td>Asia</td>
      <td>1952</td>
      <td>28.801</td>
      <td>8425333</td>
      <td>779.445314</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Afghanistan</td>
      <td>Asia</td>
      <td>1957</td>
      <td>30.332</td>
      <td>9240934</td>
      <td>820.853030</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Afghanistan</td>
      <td>Asia</td>
      <td>1962</td>
      <td>31.997</td>
      <td>10267083</td>
      <td>853.100710</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Afghanistan</td>
      <td>Asia</td>
      <td>1967</td>
      <td>34.020</td>
      <td>11537966</td>
      <td>836.197138</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Afghanistan</td>
      <td>Asia</td>
      <td>1972</td>
      <td>36.088</td>
      <td>13079460</td>
      <td>739.981106</td>
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
      <th>1699</th>
      <td>Zimbabwe</td>
      <td>Africa</td>
      <td>1987</td>
      <td>62.351</td>
      <td>9216418</td>
      <td>706.157306</td>
    </tr>
    <tr>
      <th>1700</th>
      <td>Zimbabwe</td>
      <td>Africa</td>
      <td>1992</td>
      <td>60.377</td>
      <td>10704340</td>
      <td>693.420786</td>
    </tr>
    <tr>
      <th>1701</th>
      <td>Zimbabwe</td>
      <td>Africa</td>
      <td>1997</td>
      <td>46.809</td>
      <td>11404948</td>
      <td>792.449960</td>
    </tr>
    <tr>
      <th>1702</th>
      <td>Zimbabwe</td>
      <td>Africa</td>
      <td>2002</td>
      <td>39.989</td>
      <td>11926563</td>
      <td>672.038623</td>
    </tr>
    <tr>
      <th>1703</th>
      <td>Zimbabwe</td>
      <td>Africa</td>
      <td>2007</td>
      <td>43.487</td>
      <td>12311143</td>
      <td>469.709298</td>
    </tr>
  </tbody>
</table>
<p>1704 rows × 6 columns</p>
</div>




```python
# df.head()
# df.tail()
# df.info()
# df.columns
df.dtypes
```




    country       object
    continent     object
    year           int64
    lifeExp      float64
    pop            int64
    gdpPercap    float64
    dtype: object




```python
# Zimbabwe 데이터만 추출하시오
# df[df['country'] == 'Zimbabwe'].info()
df[df['continent'] == 'Africa'].shape[0]/12
```




    52.0




```python
df[df['continent'] == 'Africa']
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
      <th>country</th>
      <th>continent</th>
      <th>year</th>
      <th>lifeExp</th>
      <th>pop</th>
      <th>gdpPercap</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>24</th>
      <td>Algeria</td>
      <td>Africa</td>
      <td>1952</td>
      <td>43.077</td>
      <td>9279525</td>
      <td>2449.008185</td>
    </tr>
    <tr>
      <th>25</th>
      <td>Algeria</td>
      <td>Africa</td>
      <td>1957</td>
      <td>45.685</td>
      <td>10270856</td>
      <td>3013.976023</td>
    </tr>
    <tr>
      <th>26</th>
      <td>Algeria</td>
      <td>Africa</td>
      <td>1962</td>
      <td>48.303</td>
      <td>11000948</td>
      <td>2550.816880</td>
    </tr>
    <tr>
      <th>27</th>
      <td>Algeria</td>
      <td>Africa</td>
      <td>1967</td>
      <td>51.407</td>
      <td>12760499</td>
      <td>3246.991771</td>
    </tr>
    <tr>
      <th>28</th>
      <td>Algeria</td>
      <td>Africa</td>
      <td>1972</td>
      <td>54.518</td>
      <td>14760787</td>
      <td>4182.663766</td>
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
      <th>1699</th>
      <td>Zimbabwe</td>
      <td>Africa</td>
      <td>1987</td>
      <td>62.351</td>
      <td>9216418</td>
      <td>706.157306</td>
    </tr>
    <tr>
      <th>1700</th>
      <td>Zimbabwe</td>
      <td>Africa</td>
      <td>1992</td>
      <td>60.377</td>
      <td>10704340</td>
      <td>693.420786</td>
    </tr>
    <tr>
      <th>1701</th>
      <td>Zimbabwe</td>
      <td>Africa</td>
      <td>1997</td>
      <td>46.809</td>
      <td>11404948</td>
      <td>792.449960</td>
    </tr>
    <tr>
      <th>1702</th>
      <td>Zimbabwe</td>
      <td>Africa</td>
      <td>2002</td>
      <td>39.989</td>
      <td>11926563</td>
      <td>672.038623</td>
    </tr>
    <tr>
      <th>1703</th>
      <td>Zimbabwe</td>
      <td>Africa</td>
      <td>2007</td>
      <td>43.487</td>
      <td>12311143</td>
      <td>469.709298</td>
    </tr>
  </tbody>
</table>
<p>624 rows × 6 columns</p>
</div>




```python
# 1. 기대수명 데이터셋으로 아래의 작업을 수행하시오.
# 1) iloc 속성으로 행 데이터 추출하기
df.iloc[-1]
# 2) loc 속성으로 행 단위 데이터 추출하기
df.loc[:]
# 3) 열 단위로 데이터 추출하기
df['country']
df.country
# 4) 'year', 'pop' 데이터 추출하기
df[['year', 'pop']]
# 5) country continent  year 데이터 추출하기
df[['country', 'continent', 'year']]
# 6) country  year       pop 데이터 추출하기
df[['country', 'year', 'pop']]
# 7) loc, iloc 속성 자유자재로 사용하기
# 출력예시)
#          country  lifeExp    gdpPercap
# 0    Afghanistan   28.801   779.445314
# 99    Bangladesh   43.453   721.186086
# 999     Mongolia   51.253  1226.041130
df.loc[[0, 99, 999], ['country', 'lifeExp', 'gdpPercap']]
# 출력예시)
#         country  lifeExp    gdpPercap
# 10  Afghanistan   42.129   726.734055
# 11  Afghanistan   43.828   974.580338
# 12      Albania   55.230  1601.056136
# 13      Albania   59.280  1942.284244
df[['country', 'lifeExp', 'gdpPercap']].loc[10:13]
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
      <th>country</th>
      <th>lifeExp</th>
      <th>gdpPercap</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>10</th>
      <td>Afghanistan</td>
      <td>42.129</td>
      <td>726.734055</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Afghanistan</td>
      <td>43.828</td>
      <td>974.580338</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Albania</td>
      <td>55.230</td>
      <td>1601.056136</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Albania</td>
      <td>59.280</td>
      <td>1942.284244</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 2. 행과 열에 라벨을 가지는 5 x 5 이상의 크기를 가지는 데이터프레임을 만든다.
# - 10가지 이상의 방법으로 특정한 행과 열을 선택한다.
dfex = pd.DataFrame(np.random.random_sample(25).reshape(5,5), index=['a', 'b', 'c', 'd', 'e'], columns=['ㄱ', 'ㄴ', 'ㄷ', 'ㄹ', 'ㅁ'])
dfex
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
      <th>ㄱ</th>
      <th>ㄴ</th>
      <th>ㄷ</th>
      <th>ㄹ</th>
      <th>ㅁ</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>0.356027</td>
      <td>0.866776</td>
      <td>0.848089</td>
      <td>0.526779</td>
      <td>0.845292</td>
    </tr>
    <tr>
      <th>b</th>
      <td>0.501531</td>
      <td>0.830766</td>
      <td>0.397069</td>
      <td>0.699946</td>
      <td>0.121947</td>
    </tr>
    <tr>
      <th>c</th>
      <td>0.973153</td>
      <td>0.943707</td>
      <td>0.414888</td>
      <td>0.587642</td>
      <td>0.877279</td>
    </tr>
    <tr>
      <th>d</th>
      <td>0.405518</td>
      <td>0.508717</td>
      <td>0.881222</td>
      <td>0.536392</td>
      <td>0.863088</td>
    </tr>
    <tr>
      <th>e</th>
      <td>0.126383</td>
      <td>0.947403</td>
      <td>0.394199</td>
      <td>0.432448</td>
      <td>0.481610</td>
    </tr>
  </tbody>
</table>
</div>




```python
dfex.loc['b']
dfex.iloc[1]
dfex.max()
dfex.min()
dfex.loc[['c','e']]
dfex.loc['a']['ㄱ']
dfex.loc[['a'],['ㄱ', 'ㄴ']]
dfex.iloc[[1,2]]
dfex.mean()
dfex.iloc[1:4].loc['b']
```




    ㄱ    0.501531
    ㄴ    0.830766
    ㄷ    0.397069
    ㄹ    0.699946
    ㅁ    0.121947
    Name: b, dtype: float64




```python

```
