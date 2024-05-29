```python
import pandas as pd
import numpy as np
import seaborn as sns
```


```python
data = {
    "도시": ["서울", "서울", "서울", "부산", "부산", "부산", "인천", "인천"],
    "연도": ["2015", "2010", "2005", "2015", "2010", "2005", "2015", "2010"],
    "인구": [9904312, 9631482, 9762546, 3448737, 3393191, 3512547, 2890451, 263203],
    "지역": ["수도권", "수도권", "수도권", "경상권", "경상권", "경상권", "수도권", "수도권"]
}
columns = ["도시", "연도", "인구", "지역"]
df1 = pd.DataFrame(data, columns=columns)
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
      <th>도시</th>
      <th>연도</th>
      <th>인구</th>
      <th>지역</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>서울</td>
      <td>2015</td>
      <td>9904312</td>
      <td>수도권</td>
    </tr>
    <tr>
      <th>1</th>
      <td>서울</td>
      <td>2010</td>
      <td>9631482</td>
      <td>수도권</td>
    </tr>
    <tr>
      <th>2</th>
      <td>서울</td>
      <td>2005</td>
      <td>9762546</td>
      <td>수도권</td>
    </tr>
    <tr>
      <th>3</th>
      <td>부산</td>
      <td>2015</td>
      <td>3448737</td>
      <td>경상권</td>
    </tr>
    <tr>
      <th>4</th>
      <td>부산</td>
      <td>2010</td>
      <td>3393191</td>
      <td>경상권</td>
    </tr>
    <tr>
      <th>5</th>
      <td>부산</td>
      <td>2005</td>
      <td>3512547</td>
      <td>경상권</td>
    </tr>
    <tr>
      <th>6</th>
      <td>인천</td>
      <td>2015</td>
      <td>2890451</td>
      <td>수도권</td>
    </tr>
    <tr>
      <th>7</th>
      <td>인천</td>
      <td>2010</td>
      <td>263203</td>
      <td>수도권</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 피봇테이블 : 데이터프레임의 특정 열들을 각각 행/열 인덱스로 만들고, 
# 또 다른 특정 열은 데이터로 구성해놓은 테이블
# pivot, pivot_table
```


```python
df1
df1.pivot('도시', '연도', '인구') # 행, 열, 데이터
df1.pivot(index='도시',columns='연도',values='인구')
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
      <th>연도</th>
      <th>2005</th>
      <th>2010</th>
      <th>2015</th>
    </tr>
    <tr>
      <th>도시</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>부산</th>
      <td>3512547.0</td>
      <td>3393191.0</td>
      <td>3448737.0</td>
    </tr>
    <tr>
      <th>서울</th>
      <td>9762546.0</td>
      <td>9631482.0</td>
      <td>9904312.0</td>
    </tr>
    <tr>
      <th>인천</th>
      <td>NaN</td>
      <td>263203.0</td>
      <td>2890451.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
df1.set_index(['도시', '연도'])[['인구']].unstack()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead tr th {
        text-align: left;
    }

    .dataframe thead tr:last-of-type th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th colspan="3" halign="left">인구</th>
    </tr>
    <tr>
      <th>연도</th>
      <th>2005</th>
      <th>2010</th>
      <th>2015</th>
    </tr>
    <tr>
      <th>도시</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>부산</th>
      <td>3512547.0</td>
      <td>3393191.0</td>
      <td>3448737.0</td>
    </tr>
    <tr>
      <th>서울</th>
      <td>9762546.0</td>
      <td>9631482.0</td>
      <td>9904312.0</td>
    </tr>
    <tr>
      <th>인천</th>
      <td>NaN</td>
      <td>263203.0</td>
      <td>2890451.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
# df1.pivot(index='지역', columns='연도', values='인구') # 서울과 인천이 지역과 연도에 대한 인구 데이터가 중복되어 버림, 에러
df1.pivot(index=['지역', '도시'], columns='연도', values='인구')
# 행/열 인덱스는 데이터를 검색하기 위한 기준 -> 값으로 데이터가 1개만 있어야 한다
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
      <th>연도</th>
      <th>2005</th>
      <th>2010</th>
      <th>2015</th>
    </tr>
    <tr>
      <th>지역</th>
      <th>도시</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>경상권</th>
      <th>부산</th>
      <td>3512547.0</td>
      <td>3393191.0</td>
      <td>3448737.0</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">수도권</th>
      <th>서울</th>
      <td>9762546.0</td>
      <td>9631482.0</td>
      <td>9904312.0</td>
    </tr>
    <tr>
      <th>인천</th>
      <td>NaN</td>
      <td>263203.0</td>
      <td>2890451.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
np.random.seed(0)
df2 = pd.DataFrame({
    'key1': ['A', 'A', 'B', 'B', 'A'],
    'key2': ['one', 'two', 'one', 'two', 'one'],
    'data1': [1, 2, 3, 4, 5],
    'data2': [10, 20, 30, 40, 50]
})
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
      <th>key1</th>
      <th>key2</th>
      <th>data1</th>
      <th>data2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>A</td>
      <td>one</td>
      <td>1</td>
      <td>10</td>
    </tr>
    <tr>
      <th>1</th>
      <td>A</td>
      <td>two</td>
      <td>2</td>
      <td>20</td>
    </tr>
    <tr>
      <th>2</th>
      <td>B</td>
      <td>one</td>
      <td>3</td>
      <td>30</td>
    </tr>
    <tr>
      <th>3</th>
      <td>B</td>
      <td>two</td>
      <td>4</td>
      <td>40</td>
    </tr>
    <tr>
      <th>4</th>
      <td>A</td>
      <td>one</td>
      <td>5</td>
      <td>50</td>
    </tr>
  </tbody>
</table>
</div>




```python
myGroup = df2.groupby(df2.key1)
myGroup
```




    <pandas.core.groupby.generic.DataFrameGroupBy object at 0x00000231D0770700>




```python
myGroup.groups
```




    {'A': [0, 1, 4], 'B': [2, 3]}




```python
myGroup.sum()
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
      <th>data1</th>
      <th>data2</th>
    </tr>
    <tr>
      <th>key1</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A</th>
      <td>8</td>
      <td>80</td>
    </tr>
    <tr>
      <th>B</th>
      <td>7</td>
      <td>70</td>
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
      <th>key1</th>
      <th>key2</th>
      <th>data1</th>
      <th>data2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>A</td>
      <td>one</td>
      <td>1</td>
      <td>10</td>
    </tr>
    <tr>
      <th>1</th>
      <td>A</td>
      <td>two</td>
      <td>2</td>
      <td>20</td>
    </tr>
    <tr>
      <th>2</th>
      <td>B</td>
      <td>one</td>
      <td>3</td>
      <td>30</td>
    </tr>
    <tr>
      <th>3</th>
      <td>B</td>
      <td>two</td>
      <td>4</td>
      <td>40</td>
    </tr>
    <tr>
      <th>4</th>
      <td>A</td>
      <td>one</td>
      <td>5</td>
      <td>50</td>
    </tr>
  </tbody>
</table>
</div>




```python
df2.groupby(df2.key1)['data1'].sum() # 가장 일반적인 방식
# df2.groupby(df2.key1).sum()['data1']
```




    key1
    A    8
    B    7
    Name: data1, dtype: int64




```python
df2.data1.groupby(df2.key1).sum()
```




    key1
    A    8
    B    7
    Name: data1, dtype: int64




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
      <th>key1</th>
      <th>key2</th>
      <th>data1</th>
      <th>data2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>A</td>
      <td>one</td>
      <td>1</td>
      <td>10</td>
    </tr>
    <tr>
      <th>1</th>
      <td>A</td>
      <td>two</td>
      <td>2</td>
      <td>20</td>
    </tr>
    <tr>
      <th>2</th>
      <td>B</td>
      <td>one</td>
      <td>3</td>
      <td>30</td>
    </tr>
    <tr>
      <th>3</th>
      <td>B</td>
      <td>two</td>
      <td>4</td>
      <td>40</td>
    </tr>
    <tr>
      <th>4</th>
      <td>A</td>
      <td>one</td>
      <td>5</td>
      <td>50</td>
    </tr>
  </tbody>
</table>
</div>




```python
df2.groupby([df2.key1, df2.key2]).data1.sum()
df2.groupby([df2.key1, df2.key2]).sum()['data1']
df2.data1.groupby([df2.key1, df2.key2]).sum()

# df2.groupby(df2.key1)['data1'].sum() # 가장 일반적인 방식
# df2.groupby(df2.key1).sum()['data1']
# df2.data1.groupby(df2.key1).sum()
```




    key1  key2
    A     one     6
          two     2
    B     one     3
          two     4
    Name: data1, dtype: int64




```python
df2.groupby([df2.key1, df2.key2]).data1.sum().unstack()
# df2.groupby([df2.key1, df2.key2]).data1.sum().unstack('key2')
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
      <th>key2</th>
      <th>one</th>
      <th>two</th>
    </tr>
    <tr>
      <th>key1</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A</th>
      <td>6</td>
      <td>2</td>
    </tr>
    <tr>
      <th>B</th>
      <td>3</td>
      <td>4</td>
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
      <th>도시</th>
      <th>연도</th>
      <th>인구</th>
      <th>지역</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>서울</td>
      <td>2015</td>
      <td>9904312</td>
      <td>수도권</td>
    </tr>
    <tr>
      <th>1</th>
      <td>서울</td>
      <td>2010</td>
      <td>9631482</td>
      <td>수도권</td>
    </tr>
    <tr>
      <th>2</th>
      <td>서울</td>
      <td>2005</td>
      <td>9762546</td>
      <td>수도권</td>
    </tr>
    <tr>
      <th>3</th>
      <td>부산</td>
      <td>2015</td>
      <td>3448737</td>
      <td>경상권</td>
    </tr>
    <tr>
      <th>4</th>
      <td>부산</td>
      <td>2010</td>
      <td>3393191</td>
      <td>경상권</td>
    </tr>
    <tr>
      <th>5</th>
      <td>부산</td>
      <td>2005</td>
      <td>3512547</td>
      <td>경상권</td>
    </tr>
    <tr>
      <th>6</th>
      <td>인천</td>
      <td>2015</td>
      <td>2890451</td>
      <td>수도권</td>
    </tr>
    <tr>
      <th>7</th>
      <td>인천</td>
      <td>2010</td>
      <td>263203</td>
      <td>수도권</td>
    </tr>
  </tbody>
</table>
</div>




```python
df1.groupby([df1.지역, df1.연도]).인구.sum().unstack()
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
      <th>연도</th>
      <th>2005</th>
      <th>2010</th>
      <th>2015</th>
    </tr>
    <tr>
      <th>지역</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>경상권</th>
      <td>3512547</td>
      <td>3393191</td>
      <td>3448737</td>
    </tr>
    <tr>
      <th>수도권</th>
      <td>9762546</td>
      <td>9894685</td>
      <td>12794763</td>
    </tr>
  </tbody>
</table>
</div>




```python
iris = sns.load_dataset("iris")
iris
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
      <th>sepal_length</th>
      <th>sepal_width</th>
      <th>petal_length</th>
      <th>petal_width</th>
      <th>species</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>5.1</td>
      <td>3.5</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>setosa</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4.9</td>
      <td>3.0</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>setosa</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4.7</td>
      <td>3.2</td>
      <td>1.3</td>
      <td>0.2</td>
      <td>setosa</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4.6</td>
      <td>3.1</td>
      <td>1.5</td>
      <td>0.2</td>
      <td>setosa</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5.0</td>
      <td>3.6</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>setosa</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>145</th>
      <td>6.7</td>
      <td>3.0</td>
      <td>5.2</td>
      <td>2.3</td>
      <td>virginica</td>
    </tr>
    <tr>
      <th>146</th>
      <td>6.3</td>
      <td>2.5</td>
      <td>5.0</td>
      <td>1.9</td>
      <td>virginica</td>
    </tr>
    <tr>
      <th>147</th>
      <td>6.5</td>
      <td>3.0</td>
      <td>5.2</td>
      <td>2.0</td>
      <td>virginica</td>
    </tr>
    <tr>
      <th>148</th>
      <td>6.2</td>
      <td>3.4</td>
      <td>5.4</td>
      <td>2.3</td>
      <td>virginica</td>
    </tr>
    <tr>
      <th>149</th>
      <td>5.9</td>
      <td>3.0</td>
      <td>5.1</td>
      <td>1.8</td>
      <td>virginica</td>
    </tr>
  </tbody>
</table>
<p>150 rows × 5 columns</p>
</div>




```python
iris.groupby(iris.species).sum()
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
      <th>sepal_length</th>
      <th>sepal_width</th>
      <th>petal_length</th>
      <th>petal_width</th>
    </tr>
    <tr>
      <th>species</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>setosa</th>
      <td>250.3</td>
      <td>171.4</td>
      <td>73.1</td>
      <td>12.3</td>
    </tr>
    <tr>
      <th>versicolor</th>
      <td>296.8</td>
      <td>138.5</td>
      <td>213.0</td>
      <td>66.3</td>
    </tr>
    <tr>
      <th>virginica</th>
      <td>329.4</td>
      <td>148.7</td>
      <td>277.6</td>
      <td>101.3</td>
    </tr>
  </tbody>
</table>
</div>




```python
iris.groupby(iris.species).mean()
iris.groupby(iris.species).median() # 중위수
iris.groupby(iris.species).min()
iris.groupby(iris.species).max()
iris.groupby(iris.species).std() # 표준편차
iris.groupby(iris.species).var() # 분산
iris.groupby(iris.species).first() # 그룹 데이터의 첫번째 위치에 있는 데이터
iris.groupby(iris.species).last()
iris.groupby(iris.species).count() # 그룹에 속한 데이터 개수, 데이터프레임의 각 열별로 데이터 개수
iris.groupby(iris.species).size() # 그룹에 속한 데이터 개수, species 별로 데이터의 개수
# count, size함수의 공통점 : 그룹에 속한 데이터 개수
# 차이점 : 각 열별로 계산, 그룹별로 계산
# size함수 : NaN을 포함하여 데이터 개수 계산, count : NaN 포함하지 않고 데이터 계산
```




    species
    setosa        50
    versicolor    50
    virginica     50
    dtype: int64




```python
iris.groupby(iris.species).groups
```




    {'setosa': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49], 'versicolor': [50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99], 'virginica': [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149]}




```python
titanic = sns.load_dataset("titanic")
titanic.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 891 entries, 0 to 890
    Data columns (total 15 columns):
     #   Column       Non-Null Count  Dtype   
    ---  ------       --------------  -----   
     0   survived     891 non-null    int64   
     1   pclass       891 non-null    int64   
     2   sex          891 non-null    object  
     3   age          714 non-null    float64 
     4   sibsp        891 non-null    int64   
     5   parch        891 non-null    int64   
     6   fare         891 non-null    float64 
     7   embarked     889 non-null    object  
     8   class        891 non-null    category
     9   who          891 non-null    object  
     10  adult_male   891 non-null    bool    
     11  deck         203 non-null    category
     12  embark_town  889 non-null    object  
     13  alive        891 non-null    object  
     14  alone        891 non-null    bool    
    dtypes: bool(2), category(2), float64(2), int64(4), object(5)
    memory usage: 80.7+ KB
    


```python
# size함수 : NaN을 포함하여 데이터 개수 계산, count : NaN 포함하지 않고 데이터 계산
titanic.groupby('survived')
titanic.groupby('survived').age.count() # 714건(NaN 포함 x)
```




    survived
    0    424
    1    290
    Name: age, dtype: int64




```python
titanic.groupby('survived').age.size() # 891건(NaN 포함)
```




    survived
    0    549
    1    342
    Name: age, dtype: int64




```python
iris
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
      <th>sepal_length</th>
      <th>sepal_width</th>
      <th>petal_length</th>
      <th>petal_width</th>
      <th>species</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>5.1</td>
      <td>3.5</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>setosa</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4.9</td>
      <td>3.0</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>setosa</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4.7</td>
      <td>3.2</td>
      <td>1.3</td>
      <td>0.2</td>
      <td>setosa</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4.6</td>
      <td>3.1</td>
      <td>1.5</td>
      <td>0.2</td>
      <td>setosa</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5.0</td>
      <td>3.6</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>setosa</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>145</th>
      <td>6.7</td>
      <td>3.0</td>
      <td>5.2</td>
      <td>2.3</td>
      <td>virginica</td>
    </tr>
    <tr>
      <th>146</th>
      <td>6.3</td>
      <td>2.5</td>
      <td>5.0</td>
      <td>1.9</td>
      <td>virginica</td>
    </tr>
    <tr>
      <th>147</th>
      <td>6.5</td>
      <td>3.0</td>
      <td>5.2</td>
      <td>2.0</td>
      <td>virginica</td>
    </tr>
    <tr>
      <th>148</th>
      <td>6.2</td>
      <td>3.4</td>
      <td>5.4</td>
      <td>2.3</td>
      <td>virginica</td>
    </tr>
    <tr>
      <th>149</th>
      <td>5.9</td>
      <td>3.0</td>
      <td>5.1</td>
      <td>1.8</td>
      <td>virginica</td>
    </tr>
  </tbody>
</table>
<p>150 rows × 5 columns</p>
</div>




```python
iris.groupby(iris.species).max()
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
      <th>sepal_length</th>
      <th>sepal_width</th>
      <th>petal_length</th>
      <th>petal_width</th>
    </tr>
    <tr>
      <th>species</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>setosa</th>
      <td>5.8</td>
      <td>4.4</td>
      <td>1.9</td>
      <td>0.6</td>
    </tr>
    <tr>
      <th>versicolor</th>
      <td>7.0</td>
      <td>3.4</td>
      <td>5.1</td>
      <td>1.8</td>
    </tr>
    <tr>
      <th>virginica</th>
      <td>7.9</td>
      <td>3.8</td>
      <td>6.9</td>
      <td>2.5</td>
    </tr>
  </tbody>
</table>
</div>




```python
iris.groupby(iris.species).min()
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
      <th>sepal_length</th>
      <th>sepal_width</th>
      <th>petal_length</th>
      <th>petal_width</th>
    </tr>
    <tr>
      <th>species</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>setosa</th>
      <td>4.3</td>
      <td>2.3</td>
      <td>1.0</td>
      <td>0.1</td>
    </tr>
    <tr>
      <th>versicolor</th>
      <td>4.9</td>
      <td>2.0</td>
      <td>3.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>virginica</th>
      <td>4.9</td>
      <td>2.2</td>
      <td>4.5</td>
      <td>1.4</td>
    </tr>
  </tbody>
</table>
</div>




```python
iris.groupby(iris.species).max()-iris.groupby(iris.species).min()
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
      <th>sepal_length</th>
      <th>sepal_width</th>
      <th>petal_length</th>
      <th>petal_width</th>
    </tr>
    <tr>
      <th>species</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>setosa</th>
      <td>1.5</td>
      <td>2.1</td>
      <td>0.9</td>
      <td>0.5</td>
    </tr>
    <tr>
      <th>versicolor</th>
      <td>2.1</td>
      <td>1.4</td>
      <td>2.1</td>
      <td>0.8</td>
    </tr>
    <tr>
      <th>virginica</th>
      <td>3.0</td>
      <td>1.6</td>
      <td>2.4</td>
      <td>1.1</td>
    </tr>
  </tbody>
</table>
</div>




```python
def cha(x):
    return x.max()-x.min()
iris.groupby('species').agg(cha)
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
      <th>sepal_length</th>
      <th>sepal_width</th>
      <th>petal_length</th>
      <th>petal_width</th>
    </tr>
    <tr>
      <th>species</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>setosa</th>
      <td>1.5</td>
      <td>2.1</td>
      <td>0.9</td>
      <td>0.5</td>
    </tr>
    <tr>
      <th>versicolor</th>
      <td>2.1</td>
      <td>1.4</td>
      <td>2.1</td>
      <td>0.8</td>
    </tr>
    <tr>
      <th>virginica</th>
      <td>3.0</td>
      <td>1.6</td>
      <td>2.4</td>
      <td>1.1</td>
    </tr>
  </tbody>
</table>
</div>




```python
iris.describe()
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
      <th>sepal_length</th>
      <th>sepal_width</th>
      <th>petal_length</th>
      <th>petal_width</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>150.000000</td>
      <td>150.000000</td>
      <td>150.000000</td>
      <td>150.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>5.843333</td>
      <td>3.057333</td>
      <td>3.758000</td>
      <td>1.199333</td>
    </tr>
    <tr>
      <th>std</th>
      <td>0.828066</td>
      <td>0.435866</td>
      <td>1.765298</td>
      <td>0.762238</td>
    </tr>
    <tr>
      <th>min</th>
      <td>4.300000</td>
      <td>2.000000</td>
      <td>1.000000</td>
      <td>0.100000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>5.100000</td>
      <td>2.800000</td>
      <td>1.600000</td>
      <td>0.300000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>5.800000</td>
      <td>3.000000</td>
      <td>4.350000</td>
      <td>1.300000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>6.400000</td>
      <td>3.300000</td>
      <td>5.100000</td>
      <td>1.800000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>7.900000</td>
      <td>4.400000</td>
      <td>6.900000</td>
      <td>2.500000</td>
    </tr>
  </tbody>
</table>
</div>




```python
iris.groupby(iris.species).describe().T
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
      <th>species</th>
      <th>setosa</th>
      <th>versicolor</th>
      <th>virginica</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="8" valign="top">sepal_length</th>
      <th>count</th>
      <td>50.000000</td>
      <td>50.000000</td>
      <td>50.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>5.006000</td>
      <td>5.936000</td>
      <td>6.588000</td>
    </tr>
    <tr>
      <th>std</th>
      <td>0.352490</td>
      <td>0.516171</td>
      <td>0.635880</td>
    </tr>
    <tr>
      <th>min</th>
      <td>4.300000</td>
      <td>4.900000</td>
      <td>4.900000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>4.800000</td>
      <td>5.600000</td>
      <td>6.225000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>5.000000</td>
      <td>5.900000</td>
      <td>6.500000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>5.200000</td>
      <td>6.300000</td>
      <td>6.900000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>5.800000</td>
      <td>7.000000</td>
      <td>7.900000</td>
    </tr>
    <tr>
      <th rowspan="8" valign="top">sepal_width</th>
      <th>count</th>
      <td>50.000000</td>
      <td>50.000000</td>
      <td>50.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>3.428000</td>
      <td>2.770000</td>
      <td>2.974000</td>
    </tr>
    <tr>
      <th>std</th>
      <td>0.379064</td>
      <td>0.313798</td>
      <td>0.322497</td>
    </tr>
    <tr>
      <th>min</th>
      <td>2.300000</td>
      <td>2.000000</td>
      <td>2.200000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>3.200000</td>
      <td>2.525000</td>
      <td>2.800000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>3.400000</td>
      <td>2.800000</td>
      <td>3.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>3.675000</td>
      <td>3.000000</td>
      <td>3.175000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>4.400000</td>
      <td>3.400000</td>
      <td>3.800000</td>
    </tr>
    <tr>
      <th rowspan="8" valign="top">petal_length</th>
      <th>count</th>
      <td>50.000000</td>
      <td>50.000000</td>
      <td>50.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>1.462000</td>
      <td>4.260000</td>
      <td>5.552000</td>
    </tr>
    <tr>
      <th>std</th>
      <td>0.173664</td>
      <td>0.469911</td>
      <td>0.551895</td>
    </tr>
    <tr>
      <th>min</th>
      <td>1.000000</td>
      <td>3.000000</td>
      <td>4.500000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>1.400000</td>
      <td>4.000000</td>
      <td>5.100000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>1.500000</td>
      <td>4.350000</td>
      <td>5.550000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>1.575000</td>
      <td>4.600000</td>
      <td>5.875000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>1.900000</td>
      <td>5.100000</td>
      <td>6.900000</td>
    </tr>
    <tr>
      <th rowspan="8" valign="top">petal_width</th>
      <th>count</th>
      <td>50.000000</td>
      <td>50.000000</td>
      <td>50.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>0.246000</td>
      <td>1.326000</td>
      <td>2.026000</td>
    </tr>
    <tr>
      <th>std</th>
      <td>0.105386</td>
      <td>0.197753</td>
      <td>0.274650</td>
    </tr>
    <tr>
      <th>min</th>
      <td>0.100000</td>
      <td>1.000000</td>
      <td>1.400000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>0.200000</td>
      <td>1.200000</td>
      <td>1.800000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>0.200000</td>
      <td>1.300000</td>
      <td>2.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>0.300000</td>
      <td>1.500000</td>
      <td>2.300000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>0.600000</td>
      <td>1.800000</td>
      <td>2.500000</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 종별로 그룹화한 다음, 꽃입 길이(petal_length)가 가장 큰 3개의 데이터를 추출하시오
def myTop3(df):
    return df.sort_values(by='petal_length', ascending=False)[:3]
    # print(df.sort_values(by='petal_length', ascending=False)[:3])
    # print(df)
    # print("="*50)
iris.groupby(iris.species).apply(myTop3)
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
      <th>sepal_length</th>
      <th>sepal_width</th>
      <th>petal_length</th>
      <th>petal_width</th>
      <th>species</th>
    </tr>
    <tr>
      <th>species</th>
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
      <th rowspan="3" valign="top">setosa</th>
      <th>24</th>
      <td>4.8</td>
      <td>3.4</td>
      <td>1.9</td>
      <td>0.2</td>
      <td>setosa</td>
    </tr>
    <tr>
      <th>44</th>
      <td>5.1</td>
      <td>3.8</td>
      <td>1.9</td>
      <td>0.4</td>
      <td>setosa</td>
    </tr>
    <tr>
      <th>23</th>
      <td>5.1</td>
      <td>3.3</td>
      <td>1.7</td>
      <td>0.5</td>
      <td>setosa</td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">versicolor</th>
      <th>83</th>
      <td>6.0</td>
      <td>2.7</td>
      <td>5.1</td>
      <td>1.6</td>
      <td>versicolor</td>
    </tr>
    <tr>
      <th>77</th>
      <td>6.7</td>
      <td>3.0</td>
      <td>5.0</td>
      <td>1.7</td>
      <td>versicolor</td>
    </tr>
    <tr>
      <th>72</th>
      <td>6.3</td>
      <td>2.5</td>
      <td>4.9</td>
      <td>1.5</td>
      <td>versicolor</td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">virginica</th>
      <th>118</th>
      <td>7.7</td>
      <td>2.6</td>
      <td>6.9</td>
      <td>2.3</td>
      <td>virginica</td>
    </tr>
    <tr>
      <th>117</th>
      <td>7.7</td>
      <td>3.8</td>
      <td>6.7</td>
      <td>2.2</td>
      <td>virginica</td>
    </tr>
    <tr>
      <th>122</th>
      <td>7.7</td>
      <td>2.8</td>
      <td>6.7</td>
      <td>2.0</td>
      <td>virginica</td>
    </tr>
  </tbody>
</table>
</div>




```python
iris.groupby(iris.species).apply(lambda x: x.sort_values(by='petal_length', ascending=False).head(3))
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
      <th>sepal_length</th>
      <th>sepal_width</th>
      <th>petal_length</th>
      <th>petal_width</th>
      <th>species</th>
    </tr>
    <tr>
      <th>species</th>
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
      <th rowspan="3" valign="top">setosa</th>
      <th>24</th>
      <td>4.8</td>
      <td>3.4</td>
      <td>1.9</td>
      <td>0.2</td>
      <td>setosa</td>
    </tr>
    <tr>
      <th>44</th>
      <td>5.1</td>
      <td>3.8</td>
      <td>1.9</td>
      <td>0.4</td>
      <td>setosa</td>
    </tr>
    <tr>
      <th>23</th>
      <td>5.1</td>
      <td>3.3</td>
      <td>1.7</td>
      <td>0.5</td>
      <td>setosa</td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">versicolor</th>
      <th>83</th>
      <td>6.0</td>
      <td>2.7</td>
      <td>5.1</td>
      <td>1.6</td>
      <td>versicolor</td>
    </tr>
    <tr>
      <th>77</th>
      <td>6.7</td>
      <td>3.0</td>
      <td>5.0</td>
      <td>1.7</td>
      <td>versicolor</td>
    </tr>
    <tr>
      <th>72</th>
      <td>6.3</td>
      <td>2.5</td>
      <td>4.9</td>
      <td>1.5</td>
      <td>versicolor</td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">virginica</th>
      <th>118</th>
      <td>7.7</td>
      <td>2.6</td>
      <td>6.9</td>
      <td>2.3</td>
      <td>virginica</td>
    </tr>
    <tr>
      <th>117</th>
      <td>7.7</td>
      <td>3.8</td>
      <td>6.7</td>
      <td>2.2</td>
      <td>virginica</td>
    </tr>
    <tr>
      <th>122</th>
      <td>7.7</td>
      <td>2.8</td>
      <td>6.7</td>
      <td>2.0</td>
      <td>virginica</td>
    </tr>
  </tbody>
</table>
</div>




```python
# transform : 그룹화 연산에 따른 데이터프레임의 변환
def q3(s):
    return pd.cut(s, 3, labels=['소', '중', '대'])

iris['p_l_class'] = iris.groupby(iris.species).petal_length.transform(q3)
# species를 그루핑 -> 각 그룹에 대해 꽃입 길이를 기준으로 3개 서브그룹으로 나눔 -> 각각 소,중,대 라벨부여
```


```python
iris[['petal_length', 'p_l_class']]
#특성공학(feature engineering) : 데이터프레임의 열에 대한 가공처리를 한 결과로 새로운 열을 생성(추가)
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
      <th>petal_length</th>
      <th>p_l_class</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1.4</td>
      <td>중</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1.4</td>
      <td>중</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1.3</td>
      <td>소</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1.5</td>
      <td>중</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1.4</td>
      <td>중</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>145</th>
      <td>5.2</td>
      <td>소</td>
    </tr>
    <tr>
      <th>146</th>
      <td>5.0</td>
      <td>소</td>
    </tr>
    <tr>
      <th>147</th>
      <td>5.2</td>
      <td>소</td>
    </tr>
    <tr>
      <th>148</th>
      <td>5.4</td>
      <td>중</td>
    </tr>
    <tr>
      <th>149</th>
      <td>5.1</td>
      <td>소</td>
    </tr>
  </tbody>
</table>
<p>150 rows × 2 columns</p>
</div>




```python
# pivot_table : pivot(피봇테이블) + groupby(그룹 분석)
```


```python
df1
#df1.pivot_table(데이터, 행, 열)
#df1.pivot(행, 열, 데이터)
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
      <th>도시</th>
      <th>연도</th>
      <th>인구</th>
      <th>지역</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>서울</td>
      <td>2015</td>
      <td>9904312</td>
      <td>수도권</td>
    </tr>
    <tr>
      <th>1</th>
      <td>서울</td>
      <td>2010</td>
      <td>9631482</td>
      <td>수도권</td>
    </tr>
    <tr>
      <th>2</th>
      <td>서울</td>
      <td>2005</td>
      <td>9762546</td>
      <td>수도권</td>
    </tr>
    <tr>
      <th>3</th>
      <td>부산</td>
      <td>2015</td>
      <td>3448737</td>
      <td>경상권</td>
    </tr>
    <tr>
      <th>4</th>
      <td>부산</td>
      <td>2010</td>
      <td>3393191</td>
      <td>경상권</td>
    </tr>
    <tr>
      <th>5</th>
      <td>부산</td>
      <td>2005</td>
      <td>3512547</td>
      <td>경상권</td>
    </tr>
    <tr>
      <th>6</th>
      <td>인천</td>
      <td>2015</td>
      <td>2890451</td>
      <td>수도권</td>
    </tr>
    <tr>
      <th>7</th>
      <td>인천</td>
      <td>2010</td>
      <td>263203</td>
      <td>수도권</td>
    </tr>
  </tbody>
</table>
</div>




```python
df1.pivot_table('인구', '도시', '연도')
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
      <th>연도</th>
      <th>2005</th>
      <th>2010</th>
      <th>2015</th>
    </tr>
    <tr>
      <th>도시</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>부산</th>
      <td>3512547.0</td>
      <td>3393191.0</td>
      <td>3448737.0</td>
    </tr>
    <tr>
      <th>서울</th>
      <td>9762546.0</td>
      <td>9631482.0</td>
      <td>9904312.0</td>
    </tr>
    <tr>
      <th>인천</th>
      <td>NaN</td>
      <td>263203.0</td>
      <td>2890451.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.options.display.float_format = '{:.2f}'.format
# pd.options.display.float_format = '{:.0f}'.format
```


```python
# pivot_table : pivot(피봇테이블) + groupby(그룹 분석)
# df1.pivot_table('인구', '도시', '연도', margins=True)
# df1.pivot_table('인구', '도시', '연도', margins=True, aggfunc='mean')
df1.pivot_table('인구', '도시', '연도', margins=True, aggfunc='mean', fill_value=0)
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
      <th>연도</th>
      <th>2005</th>
      <th>2010</th>
      <th>2015</th>
      <th>All</th>
    </tr>
    <tr>
      <th>도시</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>부산</th>
      <td>3512547.00</td>
      <td>3393191</td>
      <td>3448737</td>
      <td>3451491.67</td>
    </tr>
    <tr>
      <th>서울</th>
      <td>9762546.00</td>
      <td>9631482</td>
      <td>9904312</td>
      <td>9766113.33</td>
    </tr>
    <tr>
      <th>인천</th>
      <td>0.00</td>
      <td>263203</td>
      <td>2890451</td>
      <td>1576827.00</td>
    </tr>
    <tr>
      <th>All</th>
      <td>6637546.50</td>
      <td>4429292</td>
      <td>5414500</td>
      <td>5350808.62</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 3.451492e+06 == 3.451492 * 10의 6승
# 3.451492 * 10 **6
```


```python
# df1.pivot_table('인구', '도시', '연도', margins=True, aggfunc='max')
df1.pivot_table('인구', '도시', '연도', margins=True, aggfunc='max', fill_value=0)
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
      <th>연도</th>
      <th>2005</th>
      <th>2010</th>
      <th>2015</th>
      <th>All</th>
    </tr>
    <tr>
      <th>도시</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>부산</th>
      <td>3512547</td>
      <td>3393191</td>
      <td>3448737</td>
      <td>3512547</td>
    </tr>
    <tr>
      <th>서울</th>
      <td>9762546</td>
      <td>9631482</td>
      <td>9904312</td>
      <td>9904312</td>
    </tr>
    <tr>
      <th>인천</th>
      <td>0</td>
      <td>263203</td>
      <td>2890451</td>
      <td>2890451</td>
    </tr>
    <tr>
      <th>All</th>
      <td>9762546</td>
      <td>9631482</td>
      <td>9904312</td>
      <td>9904312</td>
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
      <th>도시</th>
      <th>연도</th>
      <th>인구</th>
      <th>지역</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>서울</td>
      <td>2015</td>
      <td>9904312</td>
      <td>수도권</td>
    </tr>
    <tr>
      <th>1</th>
      <td>서울</td>
      <td>2010</td>
      <td>9631482</td>
      <td>수도권</td>
    </tr>
    <tr>
      <th>2</th>
      <td>서울</td>
      <td>2005</td>
      <td>9762546</td>
      <td>수도권</td>
    </tr>
    <tr>
      <th>3</th>
      <td>부산</td>
      <td>2015</td>
      <td>3448737</td>
      <td>경상권</td>
    </tr>
    <tr>
      <th>4</th>
      <td>부산</td>
      <td>2010</td>
      <td>3393191</td>
      <td>경상권</td>
    </tr>
    <tr>
      <th>5</th>
      <td>부산</td>
      <td>2005</td>
      <td>3512547</td>
      <td>경상권</td>
    </tr>
    <tr>
      <th>6</th>
      <td>인천</td>
      <td>2015</td>
      <td>2890451</td>
      <td>수도권</td>
    </tr>
    <tr>
      <th>7</th>
      <td>인천</td>
      <td>2010</td>
      <td>263203</td>
      <td>수도권</td>
    </tr>
  </tbody>
</table>
</div>




```python
df1.pivot_table('인구', '연도', '도시')
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
      <th>도시</th>
      <th>부산</th>
      <th>서울</th>
      <th>인천</th>
      <th>All</th>
    </tr>
    <tr>
      <th>연도</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2005</th>
      <td>3512547.00</td>
      <td>9762546.00</td>
      <td>NaN</td>
      <td>6637546.50</td>
    </tr>
    <tr>
      <th>2010</th>
      <td>3393191.00</td>
      <td>9631482.00</td>
      <td>263203.00</td>
      <td>4429292.00</td>
    </tr>
    <tr>
      <th>2015</th>
      <td>3448737.00</td>
      <td>9904312.00</td>
      <td>2890451.00</td>
      <td>5414500.00</td>
    </tr>
    <tr>
      <th>All</th>
      <td>3451491.67</td>
      <td>9766113.33</td>
      <td>1576827.00</td>
      <td>5350808.62</td>
    </tr>
  </tbody>
</table>
</div>




```python
df1.pivot_table('인구', ['연도', '도시'])
type(df1.pivot_table('인구', ['연도', '도시']))
```




    pandas.core.frame.DataFrame




```python
tips=sns.load_dataset("tips")
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
# tip 열 값을 total_bill 열 값으로 나눈 결과를 tip_pct라는 새로운 열에 추가
tips['tip_pct'] = tips.tip / tips.total_bill
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
      <th>tip_pct</th>
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
      <td>0.06</td>
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
      <td>0.16</td>
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
      <td>0.17</td>
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
      <td>0.14</td>
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
      <td>0.15</td>
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
      <td>0.20</td>
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
      <td>0.07</td>
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
      <td>0.09</td>
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
      <td>0.10</td>
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
      <td>0.16</td>
    </tr>
  </tbody>
</table>
<p>244 rows × 8 columns</p>
</div>




```python
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
      <th>tip_pct</th>
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
      <td>0.06</td>
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
      <td>0.16</td>
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
      <td>0.17</td>
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
      <td>0.14</td>
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
      <td>0.15</td>
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
      <td>0.20</td>
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
      <td>0.07</td>
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
      <td>0.09</td>
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
      <td>0.10</td>
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
      <td>0.16</td>
    </tr>
  </tbody>
</table>
<p>244 rows × 8 columns</p>
</div>




```python
# 성별(sex)로 나누어 데이터 개수 출력
tips.groupby('sex').count()
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
      <th>smoker</th>
      <th>day</th>
      <th>time</th>
      <th>size</th>
      <th>tip_pct</th>
    </tr>
    <tr>
      <th>sex</th>
      <th></th>
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
      <th>Male</th>
      <td>157</td>
      <td>157</td>
      <td>157</td>
      <td>157</td>
      <td>157</td>
      <td>157</td>
      <td>157</td>
    </tr>
    <tr>
      <th>Female</th>
      <td>87</td>
      <td>87</td>
      <td>87</td>
      <td>87</td>
      <td>87</td>
      <td>87</td>
      <td>87</td>
    </tr>
  </tbody>
</table>
</div>




```python
tips.sex.value_counts()
tips.groupby('sex').size()
```




    sex
    Male      157
    Female     87
    dtype: int64




```python
# 성별(sex), 흡연자(smoker) 열로 나누어 데이터의 개수
tips.groupby(['sex', 'smoker']).count()
tips.groupby(['sex', 'smoker']).size()
```




    sex     smoker
    Male    Yes       60
            No        97
    Female  Yes       33
            No        54
    dtype: int64




```python
tips.groupby(['sex', 'smoker']).size().unstack()
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
      <th>smoker</th>
      <th>Yes</th>
      <th>No</th>
    </tr>
    <tr>
      <th>sex</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Male</th>
      <td>60</td>
      <td>97</td>
    </tr>
    <tr>
      <th>Female</th>
      <td>33</td>
      <td>54</td>
    </tr>
  </tbody>
</table>
</div>




```python
tips.pivot_table('tip','sex','smoker',margins=True, aggfunc='count')
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
      <th>smoker</th>
      <th>Yes</th>
      <th>No</th>
      <th>All</th>
    </tr>
    <tr>
      <th>sex</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Male</th>
      <td>60</td>
      <td>97</td>
      <td>157</td>
    </tr>
    <tr>
      <th>Female</th>
      <td>33</td>
      <td>54</td>
      <td>87</td>
    </tr>
    <tr>
      <th>All</th>
      <td>93</td>
      <td>151</td>
      <td>244</td>
    </tr>
  </tbody>
</table>
</div>




```python
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
      <th>tip_pct</th>
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
      <td>0.06</td>
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
      <td>0.16</td>
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
      <td>0.17</td>
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
      <td>0.14</td>
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
      <td>0.15</td>
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
      <td>0.20</td>
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
      <td>0.07</td>
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
      <td>0.09</td>
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
      <td>0.10</td>
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
      <td>0.16</td>
    </tr>
  </tbody>
</table>
<p>244 rows × 8 columns</p>
</div>




```python
# 성별과 흡연 여부에 따른 평균 팁 비율
# - 성별에 따른 평균 팁비율
# - 흡연여부에 따른 평균 팁비율
tips.groupby(['sex','smoker'])['tip_pct'].mean()
tips.groupby('smoker')['tip_pct'].mean()
tips.groupby('sex')['tip_pct'].mean()

tips.pivot_table('tip_pct', 'sex', 'smoker')
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
      <th>smoker</th>
      <th>Yes</th>
      <th>No</th>
    </tr>
    <tr>
      <th>sex</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Male</th>
      <td>0.15</td>
      <td>0.16</td>
    </tr>
    <tr>
      <th>Female</th>
      <td>0.18</td>
      <td>0.16</td>
    </tr>
  </tbody>
</table>
</div>




```python
tips.groupby('sex')[['tip_pct']].describe()
tips.groupby(['sex', 'smoker'])[['tip_pct']].describe()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead tr th {
        text-align: left;
    }

    .dataframe thead tr:last-of-type th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th colspan="8" halign="left">tip_pct</th>
    </tr>
    <tr>
      <th></th>
      <th></th>
      <th>count</th>
      <th>mean</th>
      <th>std</th>
      <th>min</th>
      <th>25%</th>
      <th>50%</th>
      <th>75%</th>
      <th>max</th>
    </tr>
    <tr>
      <th>sex</th>
      <th>smoker</th>
      <th></th>
      <th></th>
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
      <th rowspan="2" valign="top">Male</th>
      <th>Yes</th>
      <td>60.00</td>
      <td>0.15</td>
      <td>0.09</td>
      <td>0.04</td>
      <td>0.10</td>
      <td>0.14</td>
      <td>0.19</td>
      <td>0.71</td>
    </tr>
    <tr>
      <th>No</th>
      <td>97.00</td>
      <td>0.16</td>
      <td>0.04</td>
      <td>0.07</td>
      <td>0.13</td>
      <td>0.16</td>
      <td>0.19</td>
      <td>0.29</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">Female</th>
      <th>Yes</th>
      <td>33.00</td>
      <td>0.18</td>
      <td>0.07</td>
      <td>0.06</td>
      <td>0.15</td>
      <td>0.17</td>
      <td>0.20</td>
      <td>0.42</td>
    </tr>
    <tr>
      <th>No</th>
      <td>54.00</td>
      <td>0.16</td>
      <td>0.04</td>
      <td>0.06</td>
      <td>0.14</td>
      <td>0.15</td>
      <td>0.18</td>
      <td>0.25</td>
    </tr>
  </tbody>
</table>
</div>




```python
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
      <th>tip_pct</th>
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
      <td>0.06</td>
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
      <td>0.16</td>
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
      <td>0.17</td>
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
      <td>0.14</td>
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
      <td>0.15</td>
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
      <td>0.20</td>
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
      <td>0.07</td>
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
      <td>0.09</td>
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
      <td>0.10</td>
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
      <td>0.16</td>
    </tr>
  </tbody>
</table>
<p>244 rows × 8 columns</p>
</div>




```python
# - 어느 요일에 손님이 많은가?
tips.groupby('day').size()
# tips.groupby('day')['tip'].count().sort_values()
# tips.groupby('day').size().max()
# - 단체 손님 중 가장 많은 인원?
tips['size'].max() # 6명
tips.groupby('size').size() # 2명으로 온 사람이 젤 많음
# - 성별에 따라 팁의 최대값
tips.pivot_table('tip', 'sex', aggfunc='max')
tips.groupby('sex')['tip'].max()
# - 성별에 따라 팁의 최소값
tips.pivot_table('tip', 'sex', aggfunc='min')
tips.groupby('sex')['tip'].min()
```




    sex
    Male     1.00
    Female   1.00
    Name: tip, dtype: float64




```python
# 1.두 개의 데이터프레임을 만들고 merge 명령으로 합친다. 단 데이터프레임은 다음 조건을 만족해야 한다.
# 각각 5 x 5 이상의 크기를 가진다.
# 공통 열을 하나 이상 가진다. 다만 공통 열의 이름은 서로 다르다.
# 데이터프레임 1
df1 = pd.DataFrame({
    'A': np.random.randint(0, 100, 5),
    'B': np.random.randint(0, 100, 5),
    'C': np.random.randint(0, 100, 5),
    'D': np.random.randint(0, 100, 5),
    'same1': [1,2,3,4,5]
})

# 데이터프레임 2
df2 = pd.DataFrame({
    'W': np.random.randint(0, 100, 5),
    'X': np.random.randint(0, 100, 5),
    'Y': np.random.randint(0, 100, 5),
    'Z': np.random.randint(0, 100, 5),
    'same2': [1,2,3,4,5]
})
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
      <th>B</th>
      <th>C</th>
      <th>D</th>
      <th>same1</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>59</td>
      <td>94</td>
      <td>20</td>
      <td>41</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>67</td>
      <td>81</td>
      <td>58</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>98</td>
      <td>82</td>
      <td>50</td>
      <td>65</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>62</td>
      <td>46</td>
      <td>27</td>
      <td>36</td>
      <td>4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>35</td>
      <td>99</td>
      <td>14</td>
      <td>10</td>
      <td>5</td>
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
      <th>W</th>
      <th>X</th>
      <th>Y</th>
      <th>Z</th>
      <th>same2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>86</td>
      <td>80</td>
      <td>19</td>
      <td>77</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>43</td>
      <td>32</td>
      <td>46</td>
      <td>30</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>11</td>
      <td>54</td>
      <td>42</td>
      <td>24</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2</td>
      <td>0</td>
      <td>56</td>
      <td>2</td>
      <td>4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>51</td>
      <td>38</td>
      <td>60</td>
      <td>3</td>
      <td>5</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.merge(df1, df2, left_on='same1', right_on='same2')
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
      <th>D</th>
      <th>same1</th>
      <th>W</th>
      <th>X</th>
      <th>Y</th>
      <th>Z</th>
      <th>same2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>59</td>
      <td>94</td>
      <td>20</td>
      <td>41</td>
      <td>1</td>
      <td>86</td>
      <td>80</td>
      <td>19</td>
      <td>77</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>67</td>
      <td>81</td>
      <td>58</td>
      <td>2</td>
      <td>43</td>
      <td>32</td>
      <td>46</td>
      <td>30</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>98</td>
      <td>82</td>
      <td>50</td>
      <td>65</td>
      <td>3</td>
      <td>11</td>
      <td>54</td>
      <td>42</td>
      <td>24</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>62</td>
      <td>46</td>
      <td>27</td>
      <td>36</td>
      <td>4</td>
      <td>2</td>
      <td>0</td>
      <td>56</td>
      <td>2</td>
      <td>4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>35</td>
      <td>99</td>
      <td>14</td>
      <td>10</td>
      <td>5</td>
      <td>51</td>
      <td>38</td>
      <td>60</td>
      <td>3</td>
      <td>5</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 2.어느 회사의 전반기(1월 ~ 6월) 실적을 나타내는 데이터프레임과 후반기(7월 ~ 12월) 실적을 나타내는 데이터프레임을 만든 뒤 합친다. 
# 실적 정보는 “매출”, “비용”, “이익” 으로 이루어진다. (이익 = 매출 - 비용).
# 또한 1년간의 총 실적을 마지막 행으로 덧붙인다.
df1 = pd.DataFrame({
    '1월': np.random.randint(1, 1000, 2),
    '2월': np.random.randint(1, 1000, 2),
    '3월': np.random.randint(1, 1000, 2),
    '4월': np.random.randint(1, 1000, 2),
    '5월': np.random.randint(1, 1000, 2),
    '6월': np.random.randint(1, 1000, 2),
}, index=['매출', '비용'])

df2 = pd.DataFrame({
    '7월': np.random.randint(1, 1000, 2),
    '8월': np.random.randint(1, 1000, 2),
    '9월': np.random.randint(1, 1000, 2),
    '10월': np.random.randint(1, 1000, 2),
    '11월': np.random.randint(1, 1000, 2),
    '12월': np.random.randint(1, 1000, 2),
}, index=['매출', '비용'])
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
      <th>1월</th>
      <th>2월</th>
      <th>3월</th>
      <th>4월</th>
      <th>5월</th>
      <th>6월</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>매출</th>
      <td>208</td>
      <td>167</td>
      <td>350</td>
      <td>736</td>
      <td>813</td>
      <td>382</td>
    </tr>
    <tr>
      <th>비용</th>
      <td>780</td>
      <td>112</td>
      <td>130</td>
      <td>887</td>
      <td>217</td>
      <td>25</td>
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
      <th>7월</th>
      <th>8월</th>
      <th>9월</th>
      <th>10월</th>
      <th>11월</th>
      <th>12월</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>매출</th>
      <td>68</td>
      <td>772</td>
      <td>717</td>
      <td>292</td>
      <td>702</td>
      <td>728</td>
    </tr>
    <tr>
      <th>비용</th>
      <td>979</td>
      <td>235</td>
      <td>999</td>
      <td>727</td>
      <td>710</td>
      <td>556</td>
    </tr>
  </tbody>
</table>
</div>




```python
df1.loc['이익'] = df1.loc['매출'] - df1.loc['비용']
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
      <th>1월</th>
      <th>2월</th>
      <th>3월</th>
      <th>4월</th>
      <th>5월</th>
      <th>6월</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>매출</th>
      <td>208</td>
      <td>167</td>
      <td>350</td>
      <td>736</td>
      <td>813</td>
      <td>382</td>
    </tr>
    <tr>
      <th>비용</th>
      <td>780</td>
      <td>112</td>
      <td>130</td>
      <td>887</td>
      <td>217</td>
      <td>25</td>
    </tr>
    <tr>
      <th>이익</th>
      <td>-572</td>
      <td>55</td>
      <td>220</td>
      <td>-151</td>
      <td>596</td>
      <td>357</td>
    </tr>
  </tbody>
</table>
</div>




```python
df2.loc['이익'] = df2.loc['매출'] - df2.loc['비용']
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
      <th>7월</th>
      <th>8월</th>
      <th>9월</th>
      <th>10월</th>
      <th>11월</th>
      <th>12월</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>매출</th>
      <td>68</td>
      <td>772</td>
      <td>717</td>
      <td>292</td>
      <td>702</td>
      <td>728</td>
    </tr>
    <tr>
      <th>비용</th>
      <td>979</td>
      <td>235</td>
      <td>999</td>
      <td>727</td>
      <td>710</td>
      <td>556</td>
    </tr>
    <tr>
      <th>이익</th>
      <td>-911</td>
      <td>537</td>
      <td>-282</td>
      <td>-435</td>
      <td>-8</td>
      <td>172</td>
    </tr>
  </tbody>
</table>
</div>




```python
company = pd.concat([df1, df2], axis=1)
company
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
      <th>1월</th>
      <th>2월</th>
      <th>3월</th>
      <th>4월</th>
      <th>5월</th>
      <th>6월</th>
      <th>7월</th>
      <th>8월</th>
      <th>9월</th>
      <th>10월</th>
      <th>11월</th>
      <th>12월</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>매출</th>
      <td>208</td>
      <td>167</td>
      <td>350</td>
      <td>736</td>
      <td>813</td>
      <td>382</td>
      <td>68</td>
      <td>772</td>
      <td>717</td>
      <td>292</td>
      <td>702</td>
      <td>728</td>
    </tr>
    <tr>
      <th>비용</th>
      <td>780</td>
      <td>112</td>
      <td>130</td>
      <td>887</td>
      <td>217</td>
      <td>25</td>
      <td>979</td>
      <td>235</td>
      <td>999</td>
      <td>727</td>
      <td>710</td>
      <td>556</td>
    </tr>
    <tr>
      <th>이익</th>
      <td>-572</td>
      <td>55</td>
      <td>220</td>
      <td>-151</td>
      <td>596</td>
      <td>357</td>
      <td>-911</td>
      <td>537</td>
      <td>-282</td>
      <td>-435</td>
      <td>-8</td>
      <td>172</td>
    </tr>
  </tbody>
</table>
</div>




```python
company['총 실적'] = company.sum(axis=1)
company
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
      <th>1월</th>
      <th>2월</th>
      <th>3월</th>
      <th>4월</th>
      <th>5월</th>
      <th>6월</th>
      <th>7월</th>
      <th>8월</th>
      <th>9월</th>
      <th>10월</th>
      <th>11월</th>
      <th>12월</th>
      <th>총 실적</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>매출</th>
      <td>208</td>
      <td>167</td>
      <td>350</td>
      <td>736</td>
      <td>813</td>
      <td>382</td>
      <td>68</td>
      <td>772</td>
      <td>717</td>
      <td>292</td>
      <td>702</td>
      <td>728</td>
      <td>5935</td>
    </tr>
    <tr>
      <th>비용</th>
      <td>780</td>
      <td>112</td>
      <td>130</td>
      <td>887</td>
      <td>217</td>
      <td>25</td>
      <td>979</td>
      <td>235</td>
      <td>999</td>
      <td>727</td>
      <td>710</td>
      <td>556</td>
      <td>6357</td>
    </tr>
    <tr>
      <th>이익</th>
      <td>-572</td>
      <td>55</td>
      <td>220</td>
      <td>-151</td>
      <td>596</td>
      <td>357</td>
      <td>-911</td>
      <td>537</td>
      <td>-282</td>
      <td>-435</td>
      <td>-8</td>
      <td>172</td>
      <td>-422</td>
    </tr>
  </tbody>
</table>
</div>




```python
iris
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
      <th>sepal_length</th>
      <th>sepal_width</th>
      <th>petal_length</th>
      <th>petal_width</th>
      <th>species</th>
      <th>p_l_class</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>5.10</td>
      <td>3.50</td>
      <td>1.40</td>
      <td>0.20</td>
      <td>setosa</td>
      <td>중</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4.90</td>
      <td>3.00</td>
      <td>1.40</td>
      <td>0.20</td>
      <td>setosa</td>
      <td>중</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4.70</td>
      <td>3.20</td>
      <td>1.30</td>
      <td>0.20</td>
      <td>setosa</td>
      <td>소</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4.60</td>
      <td>3.10</td>
      <td>1.50</td>
      <td>0.20</td>
      <td>setosa</td>
      <td>중</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5.00</td>
      <td>3.60</td>
      <td>1.40</td>
      <td>0.20</td>
      <td>setosa</td>
      <td>중</td>
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
      <th>145</th>
      <td>6.70</td>
      <td>3.00</td>
      <td>5.20</td>
      <td>2.30</td>
      <td>virginica</td>
      <td>소</td>
    </tr>
    <tr>
      <th>146</th>
      <td>6.30</td>
      <td>2.50</td>
      <td>5.00</td>
      <td>1.90</td>
      <td>virginica</td>
      <td>소</td>
    </tr>
    <tr>
      <th>147</th>
      <td>6.50</td>
      <td>3.00</td>
      <td>5.20</td>
      <td>2.00</td>
      <td>virginica</td>
      <td>소</td>
    </tr>
    <tr>
      <th>148</th>
      <td>6.20</td>
      <td>3.40</td>
      <td>5.40</td>
      <td>2.30</td>
      <td>virginica</td>
      <td>중</td>
    </tr>
    <tr>
      <th>149</th>
      <td>5.90</td>
      <td>3.00</td>
      <td>5.10</td>
      <td>1.80</td>
      <td>virginica</td>
      <td>소</td>
    </tr>
  </tbody>
</table>
<p>150 rows × 6 columns</p>
</div>




```python
# 3. 붓꽃(iris) 데이터에서 붓꽃 종(species)별로 꽃잎길이(sepal_length), 꽃잎폭(sepal_width) 등의 평균을 구하라.
iris.groupby(iris.species).mean()
# 만약 붓꽃 종(species)이 표시되지 않았을 때 이 수치들을 이용하여 붓꽃 종을 찾아낼 수 있을지 생각하라. 어떤 방법이 있을까?텍스트로 답변
# 가지고 있는 데이터를 pd.cut해서 3종류로 분류?
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
      <th>sepal_length</th>
      <th>sepal_width</th>
      <th>petal_length</th>
      <th>petal_width</th>
    </tr>
    <tr>
      <th>species</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>setosa</th>
      <td>5.01</td>
      <td>3.43</td>
      <td>1.46</td>
      <td>0.25</td>
    </tr>
    <tr>
      <th>versicolor</th>
      <td>5.94</td>
      <td>2.77</td>
      <td>4.26</td>
      <td>1.33</td>
    </tr>
    <tr>
      <th>virginica</th>
      <td>6.59</td>
      <td>2.97</td>
      <td>5.55</td>
      <td>2.03</td>
    </tr>
  </tbody>
</table>
</div>




```python
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
      <th>tip_pct</th>
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
      <td>0.06</td>
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
      <td>0.16</td>
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
      <td>0.17</td>
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
      <td>0.14</td>
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
      <td>0.15</td>
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
      <td>0.20</td>
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
      <td>0.07</td>
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
      <td>0.09</td>
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
      <td>0.10</td>
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
      <td>0.16</td>
    </tr>
  </tbody>
</table>
<p>244 rows × 8 columns</p>
</div>




```python
# 4. tips 데이터에서,
# - 팁의 비율이 요일과 점심/저녁 여부, 인원수에 어떤 영향을 받는지 살펴본다.
tips.groupby('day')['tip_pct'].describe()
# tips.groupby('time')['tip_pct'].describe()
# tips.groupby('size')['tip_pct'].describe()
# - 어떤 요인이 가장 크게 작용하는지 판단할 수 있는 방법이 있는가?텍스트로 답변
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
      <th>count</th>
      <th>mean</th>
      <th>std</th>
      <th>min</th>
      <th>25%</th>
      <th>50%</th>
      <th>75%</th>
      <th>max</th>
    </tr>
    <tr>
      <th>day</th>
      <th></th>
      <th></th>
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
      <th>Thur</th>
      <td>62.00</td>
      <td>0.16</td>
      <td>0.04</td>
      <td>0.07</td>
      <td>0.14</td>
      <td>0.15</td>
      <td>0.19</td>
      <td>0.27</td>
    </tr>
    <tr>
      <th>Fri</th>
      <td>19.00</td>
      <td>0.17</td>
      <td>0.05</td>
      <td>0.10</td>
      <td>0.13</td>
      <td>0.16</td>
      <td>0.20</td>
      <td>0.26</td>
    </tr>
    <tr>
      <th>Sat</th>
      <td>87.00</td>
      <td>0.15</td>
      <td>0.05</td>
      <td>0.04</td>
      <td>0.12</td>
      <td>0.15</td>
      <td>0.19</td>
      <td>0.33</td>
    </tr>
    <tr>
      <th>Sun</th>
      <td>76.00</td>
      <td>0.17</td>
      <td>0.08</td>
      <td>0.06</td>
      <td>0.12</td>
      <td>0.16</td>
      <td>0.19</td>
      <td>0.71</td>
    </tr>
  </tbody>
</table>
</div>




```python
tips.groupby('time')['tip_pct'].describe()
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
      <th>count</th>
      <th>mean</th>
      <th>std</th>
      <th>min</th>
      <th>25%</th>
      <th>50%</th>
      <th>75%</th>
      <th>max</th>
    </tr>
    <tr>
      <th>time</th>
      <th></th>
      <th></th>
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
      <th>Lunch</th>
      <td>68.00</td>
      <td>0.16</td>
      <td>0.04</td>
      <td>0.07</td>
      <td>0.14</td>
      <td>0.15</td>
      <td>0.19</td>
      <td>0.27</td>
    </tr>
    <tr>
      <th>Dinner</th>
      <td>176.00</td>
      <td>0.16</td>
      <td>0.07</td>
      <td>0.04</td>
      <td>0.12</td>
      <td>0.16</td>
      <td>0.19</td>
      <td>0.71</td>
    </tr>
  </tbody>
</table>
</div>




```python
tips.groupby('size')['tip_pct'].describe()
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
      <th>count</th>
      <th>mean</th>
      <th>std</th>
      <th>min</th>
      <th>25%</th>
      <th>50%</th>
      <th>75%</th>
      <th>max</th>
    </tr>
    <tr>
      <th>size</th>
      <th></th>
      <th></th>
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
      <th>1</th>
      <td>4.00</td>
      <td>0.22</td>
      <td>0.08</td>
      <td>0.14</td>
      <td>0.17</td>
      <td>0.20</td>
      <td>0.25</td>
      <td>0.33</td>
    </tr>
    <tr>
      <th>2</th>
      <td>156.00</td>
      <td>0.17</td>
      <td>0.07</td>
      <td>0.04</td>
      <td>0.14</td>
      <td>0.16</td>
      <td>0.20</td>
      <td>0.71</td>
    </tr>
    <tr>
      <th>3</th>
      <td>38.00</td>
      <td>0.15</td>
      <td>0.05</td>
      <td>0.06</td>
      <td>0.12</td>
      <td>0.16</td>
      <td>0.19</td>
      <td>0.23</td>
    </tr>
    <tr>
      <th>4</th>
      <td>37.00</td>
      <td>0.15</td>
      <td>0.04</td>
      <td>0.08</td>
      <td>0.12</td>
      <td>0.15</td>
      <td>0.17</td>
      <td>0.28</td>
    </tr>
    <tr>
      <th>5</th>
      <td>5.00</td>
      <td>0.14</td>
      <td>0.07</td>
      <td>0.07</td>
      <td>0.11</td>
      <td>0.12</td>
      <td>0.17</td>
      <td>0.24</td>
    </tr>
    <tr>
      <th>6</th>
      <td>4.00</td>
      <td>0.16</td>
      <td>0.04</td>
      <td>0.10</td>
      <td>0.13</td>
      <td>0.16</td>
      <td>0.19</td>
      <td>0.20</td>
    </tr>
  </tbody>
</table>
</div>




```python
tips.groupby(['day', 'time'])['tip_pct'].describe()
tips.groupby(['day', 'time', 'size'])['tip_pct'].describe()
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
      <th></th>
      <th>count</th>
      <th>mean</th>
      <th>std</th>
      <th>min</th>
      <th>25%</th>
      <th>50%</th>
      <th>75%</th>
      <th>max</th>
    </tr>
    <tr>
      <th>day</th>
      <th>time</th>
      <th>size</th>
      <th></th>
      <th></th>
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
      <th rowspan="7" valign="top">Thur</th>
      <th rowspan="6" valign="top">Lunch</th>
      <th>1</th>
      <td>1.00</td>
      <td>0.18</td>
      <td>NaN</td>
      <td>0.18</td>
      <td>0.18</td>
      <td>0.18</td>
      <td>0.18</td>
      <td>0.18</td>
    </tr>
    <tr>
      <th>2</th>
      <td>47.00</td>
      <td>0.16</td>
      <td>0.04</td>
      <td>0.08</td>
      <td>0.14</td>
      <td>0.15</td>
      <td>0.19</td>
      <td>0.27</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4.00</td>
      <td>0.14</td>
      <td>0.07</td>
      <td>0.07</td>
      <td>0.09</td>
      <td>0.15</td>
      <td>0.20</td>
      <td>0.21</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5.00</td>
      <td>0.15</td>
      <td>0.03</td>
      <td>0.12</td>
      <td>0.12</td>
      <td>0.15</td>
      <td>0.15</td>
      <td>0.19</td>
    </tr>
    <tr>
      <th>5</th>
      <td>1.00</td>
      <td>0.12</td>
      <td>NaN</td>
      <td>0.12</td>
      <td>0.12</td>
      <td>0.12</td>
      <td>0.12</td>
      <td>0.12</td>
    </tr>
    <tr>
      <th>6</th>
      <td>3.00</td>
      <td>0.17</td>
      <td>0.03</td>
      <td>0.14</td>
      <td>0.16</td>
      <td>0.18</td>
      <td>0.19</td>
      <td>0.20</td>
    </tr>
    <tr>
      <th>Dinner</th>
      <th>2</th>
      <td>1.00</td>
      <td>0.16</td>
      <td>NaN</td>
      <td>0.16</td>
      <td>0.16</td>
      <td>0.16</td>
      <td>0.16</td>
      <td>0.16</td>
    </tr>
    <tr>
      <th rowspan="5" valign="top">Fri</th>
      <th rowspan="3" valign="top">Lunch</th>
      <th>1</th>
      <td>1.00</td>
      <td>0.22</td>
      <td>NaN</td>
      <td>0.22</td>
      <td>0.22</td>
      <td>0.22</td>
      <td>0.22</td>
      <td>0.22</td>
    </tr>
    <tr>
      <th>2</th>
      <td>5.00</td>
      <td>0.18</td>
      <td>0.05</td>
      <td>0.12</td>
      <td>0.15</td>
      <td>0.18</td>
      <td>0.20</td>
      <td>0.26</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1.00</td>
      <td>0.19</td>
      <td>NaN</td>
      <td>0.19</td>
      <td>0.19</td>
      <td>0.19</td>
      <td>0.19</td>
      <td>0.19</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">Dinner</th>
      <th>2</th>
      <td>11.00</td>
      <td>0.16</td>
      <td>0.05</td>
      <td>0.10</td>
      <td>0.13</td>
      <td>0.15</td>
      <td>0.18</td>
      <td>0.26</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1.00</td>
      <td>0.12</td>
      <td>NaN</td>
      <td>0.12</td>
      <td>0.12</td>
      <td>0.12</td>
      <td>0.12</td>
      <td>0.12</td>
    </tr>
    <tr>
      <th rowspan="5" valign="top">Sat</th>
      <th rowspan="5" valign="top">Dinner</th>
      <th>1</th>
      <td>2.00</td>
      <td>0.23</td>
      <td>0.13</td>
      <td>0.14</td>
      <td>0.18</td>
      <td>0.23</td>
      <td>0.28</td>
      <td>0.33</td>
    </tr>
    <tr>
      <th>2</th>
      <td>53.00</td>
      <td>0.16</td>
      <td>0.05</td>
      <td>0.04</td>
      <td>0.13</td>
      <td>0.16</td>
      <td>0.19</td>
      <td>0.29</td>
    </tr>
    <tr>
      <th>3</th>
      <td>18.00</td>
      <td>0.15</td>
      <td>0.04</td>
      <td>0.06</td>
      <td>0.13</td>
      <td>0.15</td>
      <td>0.18</td>
      <td>0.23</td>
    </tr>
    <tr>
      <th>4</th>
      <td>13.00</td>
      <td>0.14</td>
      <td>0.05</td>
      <td>0.08</td>
      <td>0.10</td>
      <td>0.14</td>
      <td>0.19</td>
      <td>0.21</td>
    </tr>
    <tr>
      <th>5</th>
      <td>1.00</td>
      <td>0.11</td>
      <td>NaN</td>
      <td>0.11</td>
      <td>0.11</td>
      <td>0.11</td>
      <td>0.11</td>
      <td>0.11</td>
    </tr>
    <tr>
      <th rowspan="5" valign="top">Sun</th>
      <th rowspan="5" valign="top">Dinner</th>
      <th>2</th>
      <td>39.00</td>
      <td>0.18</td>
      <td>0.11</td>
      <td>0.06</td>
      <td>0.12</td>
      <td>0.17</td>
      <td>0.20</td>
      <td>0.71</td>
    </tr>
    <tr>
      <th>3</th>
      <td>15.00</td>
      <td>0.15</td>
      <td>0.04</td>
      <td>0.07</td>
      <td>0.13</td>
      <td>0.16</td>
      <td>0.17</td>
      <td>0.23</td>
    </tr>
    <tr>
      <th>4</th>
      <td>18.00</td>
      <td>0.15</td>
      <td>0.04</td>
      <td>0.08</td>
      <td>0.13</td>
      <td>0.15</td>
      <td>0.17</td>
      <td>0.28</td>
    </tr>
    <tr>
      <th>5</th>
      <td>3.00</td>
      <td>0.16</td>
      <td>0.09</td>
      <td>0.07</td>
      <td>0.12</td>
      <td>0.17</td>
      <td>0.21</td>
      <td>0.24</td>
    </tr>
    <tr>
      <th>6</th>
      <td>1.00</td>
      <td>0.10</td>
      <td>NaN</td>
      <td>0.10</td>
      <td>0.10</td>
      <td>0.10</td>
      <td>0.10</td>
      <td>0.10</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 5. 타이타닉 승객 데이터를 이용하여 다음 분석을 실시하라. 데이터는 다음과 같이 받을 수 있다.
titanic = sns.load_dataset("titanic")
# qcut 명령으로 세 개의 나이 그룹을 만든다.
# 성별, 선실, 나이 그룹에 의한 생존율을 데이터프레임으로 계산한다. 행에는 성별 및 나이 그룹에 대한 다중 인덱스를 사용하고 열에는 선실 인덱스를 사용한다. 생존률은 해당 그룹의 생존 인원수를 전체 인원수로 나눈 값이다.
# 성별 및 선실에 의한 생존율을 피봇 데이터 형태로 만든다.
titanic
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
      <th>survived</th>
      <th>pclass</th>
      <th>sex</th>
      <th>age</th>
      <th>sibsp</th>
      <th>parch</th>
      <th>fare</th>
      <th>embarked</th>
      <th>class</th>
      <th>who</th>
      <th>adult_male</th>
      <th>deck</th>
      <th>embark_town</th>
      <th>alive</th>
      <th>alone</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>3</td>
      <td>male</td>
      <td>22.00</td>
      <td>1</td>
      <td>0</td>
      <td>7.25</td>
      <td>S</td>
      <td>Third</td>
      <td>man</td>
      <td>True</td>
      <td>NaN</td>
      <td>Southampton</td>
      <td>no</td>
      <td>False</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>1</td>
      <td>female</td>
      <td>38.00</td>
      <td>1</td>
      <td>0</td>
      <td>71.28</td>
      <td>C</td>
      <td>First</td>
      <td>woman</td>
      <td>False</td>
      <td>C</td>
      <td>Cherbourg</td>
      <td>yes</td>
      <td>False</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>3</td>
      <td>female</td>
      <td>26.00</td>
      <td>0</td>
      <td>0</td>
      <td>7.92</td>
      <td>S</td>
      <td>Third</td>
      <td>woman</td>
      <td>False</td>
      <td>NaN</td>
      <td>Southampton</td>
      <td>yes</td>
      <td>True</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1</td>
      <td>1</td>
      <td>female</td>
      <td>35.00</td>
      <td>1</td>
      <td>0</td>
      <td>53.10</td>
      <td>S</td>
      <td>First</td>
      <td>woman</td>
      <td>False</td>
      <td>C</td>
      <td>Southampton</td>
      <td>yes</td>
      <td>False</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0</td>
      <td>3</td>
      <td>male</td>
      <td>35.00</td>
      <td>0</td>
      <td>0</td>
      <td>8.05</td>
      <td>S</td>
      <td>Third</td>
      <td>man</td>
      <td>True</td>
      <td>NaN</td>
      <td>Southampton</td>
      <td>no</td>
      <td>True</td>
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
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>886</th>
      <td>0</td>
      <td>2</td>
      <td>male</td>
      <td>27.00</td>
      <td>0</td>
      <td>0</td>
      <td>13.00</td>
      <td>S</td>
      <td>Second</td>
      <td>man</td>
      <td>True</td>
      <td>NaN</td>
      <td>Southampton</td>
      <td>no</td>
      <td>True</td>
    </tr>
    <tr>
      <th>887</th>
      <td>1</td>
      <td>1</td>
      <td>female</td>
      <td>19.00</td>
      <td>0</td>
      <td>0</td>
      <td>30.00</td>
      <td>S</td>
      <td>First</td>
      <td>woman</td>
      <td>False</td>
      <td>B</td>
      <td>Southampton</td>
      <td>yes</td>
      <td>True</td>
    </tr>
    <tr>
      <th>888</th>
      <td>0</td>
      <td>3</td>
      <td>female</td>
      <td>NaN</td>
      <td>1</td>
      <td>2</td>
      <td>23.45</td>
      <td>S</td>
      <td>Third</td>
      <td>woman</td>
      <td>False</td>
      <td>NaN</td>
      <td>Southampton</td>
      <td>no</td>
      <td>False</td>
    </tr>
    <tr>
      <th>889</th>
      <td>1</td>
      <td>1</td>
      <td>male</td>
      <td>26.00</td>
      <td>0</td>
      <td>0</td>
      <td>30.00</td>
      <td>C</td>
      <td>First</td>
      <td>man</td>
      <td>True</td>
      <td>C</td>
      <td>Cherbourg</td>
      <td>yes</td>
      <td>True</td>
    </tr>
    <tr>
      <th>890</th>
      <td>0</td>
      <td>3</td>
      <td>male</td>
      <td>32.00</td>
      <td>0</td>
      <td>0</td>
      <td>7.75</td>
      <td>Q</td>
      <td>Third</td>
      <td>man</td>
      <td>True</td>
      <td>NaN</td>
      <td>Queenstown</td>
      <td>no</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
<p>891 rows × 15 columns</p>
</div>




```python
titanic['age_group'] = pd.qcut(titanic.age, 3, labels=['젊음', '중간', '늙음'])
titanic.head()
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
      <th>survived</th>
      <th>pclass</th>
      <th>sex</th>
      <th>age</th>
      <th>sibsp</th>
      <th>parch</th>
      <th>fare</th>
      <th>embarked</th>
      <th>class</th>
      <th>who</th>
      <th>adult_male</th>
      <th>deck</th>
      <th>embark_town</th>
      <th>alive</th>
      <th>alone</th>
      <th>age_group</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>3</td>
      <td>male</td>
      <td>22.00</td>
      <td>1</td>
      <td>0</td>
      <td>7.25</td>
      <td>S</td>
      <td>Third</td>
      <td>man</td>
      <td>True</td>
      <td>NaN</td>
      <td>Southampton</td>
      <td>no</td>
      <td>False</td>
      <td>젊음</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>1</td>
      <td>female</td>
      <td>38.00</td>
      <td>1</td>
      <td>0</td>
      <td>71.28</td>
      <td>C</td>
      <td>First</td>
      <td>woman</td>
      <td>False</td>
      <td>C</td>
      <td>Cherbourg</td>
      <td>yes</td>
      <td>False</td>
      <td>늙음</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>3</td>
      <td>female</td>
      <td>26.00</td>
      <td>0</td>
      <td>0</td>
      <td>7.92</td>
      <td>S</td>
      <td>Third</td>
      <td>woman</td>
      <td>False</td>
      <td>NaN</td>
      <td>Southampton</td>
      <td>yes</td>
      <td>True</td>
      <td>중간</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1</td>
      <td>1</td>
      <td>female</td>
      <td>35.00</td>
      <td>1</td>
      <td>0</td>
      <td>53.10</td>
      <td>S</td>
      <td>First</td>
      <td>woman</td>
      <td>False</td>
      <td>C</td>
      <td>Southampton</td>
      <td>yes</td>
      <td>False</td>
      <td>늙음</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0</td>
      <td>3</td>
      <td>male</td>
      <td>35.00</td>
      <td>0</td>
      <td>0</td>
      <td>8.05</td>
      <td>S</td>
      <td>Third</td>
      <td>man</td>
      <td>True</td>
      <td>NaN</td>
      <td>Southampton</td>
      <td>no</td>
      <td>True</td>
      <td>늙음</td>
    </tr>
  </tbody>
</table>
</div>




```python
titanic.pivot_table('survived', ['age_group', 'sex'], 'class', margins=True)
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
      <th>class</th>
      <th>First</th>
      <th>Second</th>
      <th>Third</th>
      <th>All</th>
    </tr>
    <tr>
      <th>age_group</th>
      <th>sex</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">젊음</th>
      <th>female</th>
      <td>0.95</td>
      <td>1.00</td>
      <td>0.51</td>
      <td>0.70</td>
    </tr>
    <tr>
      <th>male</th>
      <td>0.50</td>
      <td>0.36</td>
      <td>0.16</td>
      <td>0.22</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">중간</th>
      <th>female</th>
      <td>0.95</td>
      <td>0.91</td>
      <td>0.48</td>
      <td>0.77</td>
    </tr>
    <tr>
      <th>male</th>
      <td>0.50</td>
      <td>0.08</td>
      <td>0.20</td>
      <td>0.21</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">늙음</th>
      <th>female</th>
      <td>0.98</td>
      <td>0.86</td>
      <td>0.25</td>
      <td>0.80</td>
    </tr>
    <tr>
      <th>male</th>
      <td>0.35</td>
      <td>0.06</td>
      <td>0.06</td>
      <td>0.19</td>
    </tr>
    <tr>
      <th>All</th>
      <th></th>
      <td>0.66</td>
      <td>0.48</td>
      <td>0.24</td>
      <td>0.41</td>
    </tr>
  </tbody>
</table>
</div>




```python

```
