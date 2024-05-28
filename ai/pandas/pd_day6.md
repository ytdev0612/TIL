```python
import pandas as pd
import numpy as np
```


```python
# 멀티 인덱스
data = pd.Series(np.random.uniform(size=9),
                 index=[["a", "a", "a", "b", "b", "c", "c", "d", "d"],
                        [1, 2, 3, 1, 3, 1, 2, 2, 3]])
data
```




    a  1    0.647321
       2    0.458013
       3    0.672327
    b  1    0.581817
       3    0.427490
    c  1    0.338228
       2    0.131536
    d  2    0.351324
       3    0.186348
    dtype: float64




```python
data.index
```




    MultiIndex([('a', 1),
                ('a', 2),
                ('a', 3),
                ('b', 1),
                ('b', 3),
                ('c', 1),
                ('c', 2),
                ('d', 2),
                ('d', 3)],
               )




```python
data['b']
```




    1    0.581817
    3    0.427490
    dtype: float64




```python
data['b':'c']
```




    b  1    0.581817
       3    0.427490
    c  1    0.338228
       2    0.131536
    dtype: float64




```python
data[['b', 'd']]
```




    b  1    0.581817
       3    0.427490
    d  2    0.351324
       3    0.186348
    dtype: float64




```python
data
```




    a  1    0.647321
       2    0.458013
       3    0.672327
    b  1    0.581817
       3    0.427490
    c  1    0.338228
       2    0.131536
    d  2    0.351324
       3    0.186348
    dtype: float64




```python
data.loc[:, 2] # 상위 인덱스 전체, 하위 인덱스 2번 라벨
```




    a    0.458013
    c    0.131536
    d    0.351324
    dtype: float64




```python
data
```




    a  1    0.647321
       2    0.458013
       3    0.672327
    b  1    0.581817
       3    0.427490
    c  1    0.338228
       2    0.131536
    d  2    0.351324
       3    0.186348
    dtype: float64




```python
data.unstack() # 행 인덱스 -> 열 인덱스
data.unstack().stack() # 열 인덱스 -> 행 인덱스
```




    a  1    0.647321
       2    0.458013
       3    0.672327
    b  1    0.581817
       3    0.427490
    c  1    0.338228
       2    0.131536
    d  2    0.351324
       3    0.186348
    dtype: float64




```python
np.random.seed(0)
df1 = pd.DataFrame(np.vstack([list('ABCDE'),
                              np.round(np.random.rand(3, 5), 2)]).T,
                   columns=["C1", "C2", "C3", "C4"])
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
      <th>C1</th>
      <th>C2</th>
      <th>C3</th>
      <th>C4</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>A</td>
      <td>0.55</td>
      <td>0.65</td>
      <td>0.79</td>
    </tr>
    <tr>
      <th>1</th>
      <td>B</td>
      <td>0.72</td>
      <td>0.44</td>
      <td>0.53</td>
    </tr>
    <tr>
      <th>2</th>
      <td>C</td>
      <td>0.6</td>
      <td>0.89</td>
      <td>0.57</td>
    </tr>
    <tr>
      <th>3</th>
      <td>D</td>
      <td>0.54</td>
      <td>0.96</td>
      <td>0.93</td>
    </tr>
    <tr>
      <th>4</th>
      <td>E</td>
      <td>0.42</td>
      <td>0.38</td>
      <td>0.07</td>
    </tr>
  </tbody>
</table>
</div>




```python
# set_index : 특정 데이터 열 -> 행 인덱스로 설정
df2 = df1.set_index("C1")
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
      <th>C2</th>
      <th>C3</th>
      <th>C4</th>
    </tr>
    <tr>
      <th>C1</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A</th>
      <td>0.55</td>
      <td>0.65</td>
      <td>0.79</td>
    </tr>
    <tr>
      <th>B</th>
      <td>0.72</td>
      <td>0.44</td>
      <td>0.53</td>
    </tr>
    <tr>
      <th>C</th>
      <td>0.6</td>
      <td>0.89</td>
      <td>0.57</td>
    </tr>
    <tr>
      <th>D</th>
      <td>0.54</td>
      <td>0.96</td>
      <td>0.93</td>
    </tr>
    <tr>
      <th>E</th>
      <td>0.42</td>
      <td>0.38</td>
      <td>0.07</td>
    </tr>
  </tbody>
</table>
</div>




```python
# reset_index : 행 인덱스 -> 데이터 열로 설정
df2.reset_index()
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
      <th>C1</th>
      <th>C2</th>
      <th>C3</th>
      <th>C4</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>A</td>
      <td>0.55</td>
      <td>0.65</td>
      <td>0.79</td>
    </tr>
    <tr>
      <th>1</th>
      <td>B</td>
      <td>0.72</td>
      <td>0.44</td>
      <td>0.53</td>
    </tr>
    <tr>
      <th>2</th>
      <td>C</td>
      <td>0.6</td>
      <td>0.89</td>
      <td>0.57</td>
    </tr>
    <tr>
      <th>3</th>
      <td>D</td>
      <td>0.54</td>
      <td>0.96</td>
      <td>0.93</td>
    </tr>
    <tr>
      <th>4</th>
      <td>E</td>
      <td>0.42</td>
      <td>0.38</td>
      <td>0.07</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 행 인덱스 제거
df2.reset_index(drop=True)
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
      <th>C2</th>
      <th>C3</th>
      <th>C4</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.55</td>
      <td>0.65</td>
      <td>0.79</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.72</td>
      <td>0.44</td>
      <td>0.53</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.6</td>
      <td>0.89</td>
      <td>0.57</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.54</td>
      <td>0.96</td>
      <td>0.93</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.42</td>
      <td>0.38</td>
      <td>0.07</td>
    </tr>
  </tbody>
</table>
</div>




```python
np.random.seed(0)
df3 = pd.DataFrame(np.round(np.random.randn(5, 4), 2),
                   columns=[["A", "A", "B", "B"],
                            ["C1", "C2", "C1", "C2"]])
df3
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
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th colspan="2" halign="left">A</th>
      <th colspan="2" halign="left">B</th>
    </tr>
    <tr>
      <th></th>
      <th>C1</th>
      <th>C2</th>
      <th>C1</th>
      <th>C2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1.76</td>
      <td>0.40</td>
      <td>0.98</td>
      <td>2.24</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1.87</td>
      <td>-0.98</td>
      <td>0.95</td>
      <td>-0.15</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-0.10</td>
      <td>0.41</td>
      <td>0.14</td>
      <td>1.45</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.76</td>
      <td>0.12</td>
      <td>0.44</td>
      <td>0.33</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1.49</td>
      <td>-0.21</td>
      <td>0.31</td>
      <td>-0.85</td>
    </tr>
  </tbody>
</table>
</div>




```python
df3.columns
```




    MultiIndex([('A', 'C1'),
                ('A', 'C2'),
                ('B', 'C1'),
                ('B', 'C2')],
               )




```python
df3.columns.names = ["Cidx1", "Cidx2"]
df3
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
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th>Cidx1</th>
      <th colspan="2" halign="left">A</th>
      <th colspan="2" halign="left">B</th>
    </tr>
    <tr>
      <th>Cidx2</th>
      <th>C1</th>
      <th>C2</th>
      <th>C1</th>
      <th>C2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1.76</td>
      <td>0.40</td>
      <td>0.98</td>
      <td>2.24</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1.87</td>
      <td>-0.98</td>
      <td>0.95</td>
      <td>-0.15</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-0.10</td>
      <td>0.41</td>
      <td>0.14</td>
      <td>1.45</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.76</td>
      <td>0.12</td>
      <td>0.44</td>
      <td>0.33</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1.49</td>
      <td>-0.21</td>
      <td>0.31</td>
      <td>-0.85</td>
    </tr>
  </tbody>
</table>
</div>




```python
np.random.seed(0)
df4 = pd.DataFrame(np.round(np.random.randn(6, 4), 2),
                   columns=[["A", "A", "B", "B"],
                            ["C", "D", "C", "D"]],
                   index=[["M", "M", "M", "F", "F", "F"],
                          ["id_" + str(i + 1) for i in range(3)] * 2])
df4.columns.names = ["Cidx1", "Cidx2"]
df4.index.names = ["Ridx1", "Ridx2"]
df4
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
      <th>Cidx1</th>
      <th colspan="2" halign="left">A</th>
      <th colspan="2" halign="left">B</th>
    </tr>
    <tr>
      <th></th>
      <th>Cidx2</th>
      <th>C</th>
      <th>D</th>
      <th>C</th>
      <th>D</th>
    </tr>
    <tr>
      <th>Ridx1</th>
      <th>Ridx2</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="3" valign="top">M</th>
      <th>id_1</th>
      <td>1.76</td>
      <td>0.40</td>
      <td>0.98</td>
      <td>2.24</td>
    </tr>
    <tr>
      <th>id_2</th>
      <td>1.87</td>
      <td>-0.98</td>
      <td>0.95</td>
      <td>-0.15</td>
    </tr>
    <tr>
      <th>id_3</th>
      <td>-0.10</td>
      <td>0.41</td>
      <td>0.14</td>
      <td>1.45</td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">F</th>
      <th>id_1</th>
      <td>0.76</td>
      <td>0.12</td>
      <td>0.44</td>
      <td>0.33</td>
    </tr>
    <tr>
      <th>id_2</th>
      <td>1.49</td>
      <td>-0.21</td>
      <td>0.31</td>
      <td>-0.85</td>
    </tr>
    <tr>
      <th>id_3</th>
      <td>-2.55</td>
      <td>0.65</td>
      <td>0.86</td>
      <td>-0.74</td>
    </tr>
  </tbody>
</table>
</div>




```python
# data.unstack() # 행 인덱스 -> 열 인덱스
# data.unstack().stack() # 열 인덱스 -> 행 인덱스
df4.stack()
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
      <th>Cidx1</th>
      <th>A</th>
      <th>B</th>
    </tr>
    <tr>
      <th>Ridx1</th>
      <th>Ridx2</th>
      <th>Cidx2</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="6" valign="top">M</th>
      <th rowspan="2" valign="top">id_1</th>
      <th>C</th>
      <td>1.76</td>
      <td>0.98</td>
    </tr>
    <tr>
      <th>D</th>
      <td>0.40</td>
      <td>2.24</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">id_2</th>
      <th>C</th>
      <td>1.87</td>
      <td>0.95</td>
    </tr>
    <tr>
      <th>D</th>
      <td>-0.98</td>
      <td>-0.15</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">id_3</th>
      <th>C</th>
      <td>-0.10</td>
      <td>0.14</td>
    </tr>
    <tr>
      <th>D</th>
      <td>0.41</td>
      <td>1.45</td>
    </tr>
    <tr>
      <th rowspan="6" valign="top">F</th>
      <th rowspan="2" valign="top">id_1</th>
      <th>C</th>
      <td>0.76</td>
      <td>0.44</td>
    </tr>
    <tr>
      <th>D</th>
      <td>0.12</td>
      <td>0.33</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">id_2</th>
      <th>C</th>
      <td>1.49</td>
      <td>0.31</td>
    </tr>
    <tr>
      <th>D</th>
      <td>-0.21</td>
      <td>-0.85</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">id_3</th>
      <th>C</th>
      <td>-2.55</td>
      <td>0.86</td>
    </tr>
    <tr>
      <th>D</th>
      <td>0.65</td>
      <td>-0.74</td>
    </tr>
  </tbody>
</table>
</div>




```python
df4.stack('Cidx1')
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
      <th>Cidx2</th>
      <th>C</th>
      <th>D</th>
    </tr>
    <tr>
      <th>Ridx1</th>
      <th>Ridx2</th>
      <th>Cidx1</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="6" valign="top">M</th>
      <th rowspan="2" valign="top">id_1</th>
      <th>A</th>
      <td>1.76</td>
      <td>0.40</td>
    </tr>
    <tr>
      <th>B</th>
      <td>0.98</td>
      <td>2.24</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">id_2</th>
      <th>A</th>
      <td>1.87</td>
      <td>-0.98</td>
    </tr>
    <tr>
      <th>B</th>
      <td>0.95</td>
      <td>-0.15</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">id_3</th>
      <th>A</th>
      <td>-0.10</td>
      <td>0.41</td>
    </tr>
    <tr>
      <th>B</th>
      <td>0.14</td>
      <td>1.45</td>
    </tr>
    <tr>
      <th rowspan="6" valign="top">F</th>
      <th rowspan="2" valign="top">id_1</th>
      <th>A</th>
      <td>0.76</td>
      <td>0.12</td>
    </tr>
    <tr>
      <th>B</th>
      <td>0.44</td>
      <td>0.33</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">id_2</th>
      <th>A</th>
      <td>1.49</td>
      <td>-0.21</td>
    </tr>
    <tr>
      <th>B</th>
      <td>0.31</td>
      <td>-0.85</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">id_3</th>
      <th>A</th>
      <td>-2.55</td>
      <td>0.65</td>
    </tr>
    <tr>
      <th>B</th>
      <td>0.86</td>
      <td>-0.74</td>
    </tr>
  </tbody>
</table>
</div>




```python
df4.stack(0)
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
      <th>Cidx2</th>
      <th>C</th>
      <th>D</th>
    </tr>
    <tr>
      <th>Ridx1</th>
      <th>Ridx2</th>
      <th>Cidx1</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="6" valign="top">M</th>
      <th rowspan="2" valign="top">id_1</th>
      <th>A</th>
      <td>1.76</td>
      <td>0.40</td>
    </tr>
    <tr>
      <th>B</th>
      <td>0.98</td>
      <td>2.24</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">id_2</th>
      <th>A</th>
      <td>1.87</td>
      <td>-0.98</td>
    </tr>
    <tr>
      <th>B</th>
      <td>0.95</td>
      <td>-0.15</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">id_3</th>
      <th>A</th>
      <td>-0.10</td>
      <td>0.41</td>
    </tr>
    <tr>
      <th>B</th>
      <td>0.14</td>
      <td>1.45</td>
    </tr>
    <tr>
      <th rowspan="6" valign="top">F</th>
      <th rowspan="2" valign="top">id_1</th>
      <th>A</th>
      <td>0.76</td>
      <td>0.12</td>
    </tr>
    <tr>
      <th>B</th>
      <td>0.44</td>
      <td>0.33</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">id_2</th>
      <th>A</th>
      <td>1.49</td>
      <td>-0.21</td>
    </tr>
    <tr>
      <th>B</th>
      <td>0.31</td>
      <td>-0.85</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">id_3</th>
      <th>A</th>
      <td>-2.55</td>
      <td>0.65</td>
    </tr>
    <tr>
      <th>B</th>
      <td>0.86</td>
      <td>-0.74</td>
    </tr>
  </tbody>
</table>
</div>




```python
df4
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
      <th>Cidx1</th>
      <th colspan="2" halign="left">A</th>
      <th colspan="2" halign="left">B</th>
    </tr>
    <tr>
      <th></th>
      <th>Cidx2</th>
      <th>C</th>
      <th>D</th>
      <th>C</th>
      <th>D</th>
    </tr>
    <tr>
      <th>Ridx1</th>
      <th>Ridx2</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="3" valign="top">M</th>
      <th>id_1</th>
      <td>1.76</td>
      <td>0.40</td>
      <td>0.98</td>
      <td>2.24</td>
    </tr>
    <tr>
      <th>id_2</th>
      <td>1.87</td>
      <td>-0.98</td>
      <td>0.95</td>
      <td>-0.15</td>
    </tr>
    <tr>
      <th>id_3</th>
      <td>-0.10</td>
      <td>0.41</td>
      <td>0.14</td>
      <td>1.45</td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">F</th>
      <th>id_1</th>
      <td>0.76</td>
      <td>0.12</td>
      <td>0.44</td>
      <td>0.33</td>
    </tr>
    <tr>
      <th>id_2</th>
      <td>1.49</td>
      <td>-0.21</td>
      <td>0.31</td>
      <td>-0.85</td>
    </tr>
    <tr>
      <th>id_3</th>
      <td>-2.55</td>
      <td>0.65</td>
      <td>0.86</td>
      <td>-0.74</td>
    </tr>
  </tbody>
</table>
</div>




```python
df4.stack() # 'Cidx2'가 행 인덱스
df4.stack('Cidx2') # 'Cidx2'가 행 인덱스
df4.stack(1) # 'Cidx2'가 행 인덱스
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
      <th>Cidx1</th>
      <th>A</th>
      <th>B</th>
    </tr>
    <tr>
      <th>Ridx1</th>
      <th>Ridx2</th>
      <th>Cidx2</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="6" valign="top">M</th>
      <th rowspan="2" valign="top">id_1</th>
      <th>C</th>
      <td>1.76</td>
      <td>0.98</td>
    </tr>
    <tr>
      <th>D</th>
      <td>0.40</td>
      <td>2.24</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">id_2</th>
      <th>C</th>
      <td>1.87</td>
      <td>0.95</td>
    </tr>
    <tr>
      <th>D</th>
      <td>-0.98</td>
      <td>-0.15</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">id_3</th>
      <th>C</th>
      <td>-0.10</td>
      <td>0.14</td>
    </tr>
    <tr>
      <th>D</th>
      <td>0.41</td>
      <td>1.45</td>
    </tr>
    <tr>
      <th rowspan="6" valign="top">F</th>
      <th rowspan="2" valign="top">id_1</th>
      <th>C</th>
      <td>0.76</td>
      <td>0.44</td>
    </tr>
    <tr>
      <th>D</th>
      <td>0.12</td>
      <td>0.33</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">id_2</th>
      <th>C</th>
      <td>1.49</td>
      <td>0.31</td>
    </tr>
    <tr>
      <th>D</th>
      <td>-0.21</td>
      <td>-0.85</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">id_3</th>
      <th>C</th>
      <td>-2.55</td>
      <td>0.86</td>
    </tr>
    <tr>
      <th>D</th>
      <td>0.65</td>
      <td>-0.74</td>
    </tr>
  </tbody>
</table>
</div>




```python
df4
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
      <th>Cidx1</th>
      <th colspan="2" halign="left">A</th>
      <th colspan="2" halign="left">B</th>
    </tr>
    <tr>
      <th></th>
      <th>Cidx2</th>
      <th>C</th>
      <th>D</th>
      <th>C</th>
      <th>D</th>
    </tr>
    <tr>
      <th>Ridx1</th>
      <th>Ridx2</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="3" valign="top">M</th>
      <th>id_1</th>
      <td>1.76</td>
      <td>0.40</td>
      <td>0.98</td>
      <td>2.24</td>
    </tr>
    <tr>
      <th>id_2</th>
      <td>1.87</td>
      <td>-0.98</td>
      <td>0.95</td>
      <td>-0.15</td>
    </tr>
    <tr>
      <th>id_3</th>
      <td>-0.10</td>
      <td>0.41</td>
      <td>0.14</td>
      <td>1.45</td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">F</th>
      <th>id_1</th>
      <td>0.76</td>
      <td>0.12</td>
      <td>0.44</td>
      <td>0.33</td>
    </tr>
    <tr>
      <th>id_2</th>
      <td>1.49</td>
      <td>-0.21</td>
      <td>0.31</td>
      <td>-0.85</td>
    </tr>
    <tr>
      <th>id_3</th>
      <td>-2.55</td>
      <td>0.65</td>
      <td>0.86</td>
      <td>-0.74</td>
    </tr>
  </tbody>
</table>
</div>




```python
df4.unstack()
df4.unstack(1)
df4.unstack('Ridx2')
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
      <th>Cidx1</th>
      <th colspan="6" halign="left">A</th>
      <th colspan="6" halign="left">B</th>
    </tr>
    <tr>
      <th>Cidx2</th>
      <th colspan="3" halign="left">C</th>
      <th colspan="3" halign="left">D</th>
      <th colspan="3" halign="left">C</th>
      <th colspan="3" halign="left">D</th>
    </tr>
    <tr>
      <th>Ridx2</th>
      <th>id_1</th>
      <th>id_2</th>
      <th>id_3</th>
      <th>id_1</th>
      <th>id_2</th>
      <th>id_3</th>
      <th>id_1</th>
      <th>id_2</th>
      <th>id_3</th>
      <th>id_1</th>
      <th>id_2</th>
      <th>id_3</th>
    </tr>
    <tr>
      <th>Ridx1</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
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
      <th>F</th>
      <td>0.76</td>
      <td>1.49</td>
      <td>-2.55</td>
      <td>0.12</td>
      <td>-0.21</td>
      <td>0.65</td>
      <td>0.44</td>
      <td>0.31</td>
      <td>0.86</td>
      <td>0.33</td>
      <td>-0.85</td>
      <td>-0.74</td>
    </tr>
    <tr>
      <th>M</th>
      <td>1.76</td>
      <td>1.87</td>
      <td>-0.10</td>
      <td>0.40</td>
      <td>-0.98</td>
      <td>0.41</td>
      <td>0.98</td>
      <td>0.95</td>
      <td>0.14</td>
      <td>2.24</td>
      <td>-0.15</td>
      <td>1.45</td>
    </tr>
  </tbody>
</table>
</div>




```python
df4.unstack(0)
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
      <th>Cidx1</th>
      <th colspan="4" halign="left">A</th>
      <th colspan="4" halign="left">B</th>
    </tr>
    <tr>
      <th>Cidx2</th>
      <th colspan="2" halign="left">C</th>
      <th colspan="2" halign="left">D</th>
      <th colspan="2" halign="left">C</th>
      <th colspan="2" halign="left">D</th>
    </tr>
    <tr>
      <th>Ridx1</th>
      <th>F</th>
      <th>M</th>
      <th>F</th>
      <th>M</th>
      <th>F</th>
      <th>M</th>
      <th>F</th>
      <th>M</th>
    </tr>
    <tr>
      <th>Ridx2</th>
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
      <th>id_1</th>
      <td>0.76</td>
      <td>1.76</td>
      <td>0.12</td>
      <td>0.40</td>
      <td>0.44</td>
      <td>0.98</td>
      <td>0.33</td>
      <td>2.24</td>
    </tr>
    <tr>
      <th>id_2</th>
      <td>1.49</td>
      <td>1.87</td>
      <td>-0.21</td>
      <td>-0.98</td>
      <td>0.31</td>
      <td>0.95</td>
      <td>-0.85</td>
      <td>-0.15</td>
    </tr>
    <tr>
      <th>id_3</th>
      <td>-2.55</td>
      <td>-0.10</td>
      <td>0.65</td>
      <td>0.41</td>
      <td>0.86</td>
      <td>0.14</td>
      <td>-0.74</td>
      <td>1.45</td>
    </tr>
  </tbody>
</table>
</div>




```python
df3
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
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th>Cidx1</th>
      <th colspan="2" halign="left">A</th>
      <th colspan="2" halign="left">B</th>
    </tr>
    <tr>
      <th>Cidx2</th>
      <th>C1</th>
      <th>C2</th>
      <th>C1</th>
      <th>C2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1.76</td>
      <td>0.40</td>
      <td>0.98</td>
      <td>2.24</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1.87</td>
      <td>-0.98</td>
      <td>0.95</td>
      <td>-0.15</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-0.10</td>
      <td>0.41</td>
      <td>0.14</td>
      <td>1.45</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.76</td>
      <td>0.12</td>
      <td>0.44</td>
      <td>0.33</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1.49</td>
      <td>-0.21</td>
      <td>0.31</td>
      <td>-0.85</td>
    </tr>
  </tbody>
</table>
</div>




```python
df3[('B')]
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
      <th>Cidx2</th>
      <th>C1</th>
      <th>C2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.98</td>
      <td>2.24</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.95</td>
      <td>-0.15</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.14</td>
      <td>1.45</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.44</td>
      <td>0.33</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.31</td>
      <td>-0.85</td>
    </tr>
  </tbody>
</table>
</div>




```python
df3[('B', 'C1')]
```




    0    0.98
    1    0.95
    2    0.14
    3    0.44
    4    0.31
    Name: (B, C1), dtype: float64




```python
df3['B', 'C1']
```




    0    0.98
    1    0.95
    2    0.14
    3    0.44
    4    0.31
    Name: (B, C1), dtype: float64




```python
df3
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
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th>Cidx1</th>
      <th colspan="2" halign="left">A</th>
      <th colspan="2" halign="left">B</th>
    </tr>
    <tr>
      <th>Cidx2</th>
      <th>C1</th>
      <th>C2</th>
      <th>C1</th>
      <th>C2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1.76</td>
      <td>0.40</td>
      <td>0.98</td>
      <td>2.24</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1.87</td>
      <td>-0.98</td>
      <td>0.95</td>
      <td>-0.15</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-0.10</td>
      <td>0.41</td>
      <td>0.14</td>
      <td>1.45</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.76</td>
      <td>0.12</td>
      <td>0.44</td>
      <td>0.33</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1.49</td>
      <td>-0.21</td>
      <td>0.31</td>
      <td>-0.85</td>
    </tr>
  </tbody>
</table>
</div>




```python
df3.loc[0,('B','C1')]
# df3.loc[0,['B','C1']] 에러
```




    0.98




```python
df3.loc[0,('B','C1')] = 1
```


```python
df3
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
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th>Cidx1</th>
      <th colspan="2" halign="left">A</th>
      <th colspan="2" halign="left">B</th>
    </tr>
    <tr>
      <th>Cidx2</th>
      <th>C1</th>
      <th>C2</th>
      <th>C1</th>
      <th>C2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1.76</td>
      <td>0.40</td>
      <td>1.00</td>
      <td>2.24</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1.87</td>
      <td>-0.98</td>
      <td>0.95</td>
      <td>-0.15</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-0.10</td>
      <td>0.41</td>
      <td>0.14</td>
      <td>1.45</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.76</td>
      <td>0.12</td>
      <td>0.44</td>
      <td>0.33</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1.49</td>
      <td>-0.21</td>
      <td>0.31</td>
      <td>-0.85</td>
    </tr>
  </tbody>
</table>
</div>




```python
df3.iloc[0,2]
```




    1.0




```python
df3
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
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th>Cidx1</th>
      <th colspan="2" halign="left">A</th>
      <th colspan="2" halign="left">B</th>
    </tr>
    <tr>
      <th>Cidx2</th>
      <th>C1</th>
      <th>C2</th>
      <th>C1</th>
      <th>C2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1.76</td>
      <td>0.40</td>
      <td>1.00</td>
      <td>2.24</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1.87</td>
      <td>-0.98</td>
      <td>0.95</td>
      <td>-0.15</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-0.10</td>
      <td>0.41</td>
      <td>0.14</td>
      <td>1.45</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.76</td>
      <td>0.12</td>
      <td>0.44</td>
      <td>0.33</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1.49</td>
      <td>-0.21</td>
      <td>0.31</td>
      <td>-0.85</td>
    </tr>
  </tbody>
</table>
</div>




```python
df3['A']
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
      <th>Cidx2</th>
      <th>C1</th>
      <th>C2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1.76</td>
      <td>0.40</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1.87</td>
      <td>-0.98</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-0.10</td>
      <td>0.41</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.76</td>
      <td>0.12</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1.49</td>
      <td>-0.21</td>
    </tr>
  </tbody>
</table>
</div>




```python
df4
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
      <th>Cidx1</th>
      <th colspan="2" halign="left">A</th>
      <th colspan="2" halign="left">B</th>
    </tr>
    <tr>
      <th></th>
      <th>Cidx2</th>
      <th>C</th>
      <th>D</th>
      <th>C</th>
      <th>D</th>
    </tr>
    <tr>
      <th>Ridx1</th>
      <th>Ridx2</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="3" valign="top">M</th>
      <th>id_1</th>
      <td>1.76</td>
      <td>0.40</td>
      <td>0.98</td>
      <td>2.24</td>
    </tr>
    <tr>
      <th>id_2</th>
      <td>1.87</td>
      <td>-0.98</td>
      <td>0.95</td>
      <td>-0.15</td>
    </tr>
    <tr>
      <th>id_3</th>
      <td>-0.10</td>
      <td>0.41</td>
      <td>0.14</td>
      <td>1.45</td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">F</th>
      <th>id_1</th>
      <td>0.76</td>
      <td>0.12</td>
      <td>0.44</td>
      <td>0.33</td>
    </tr>
    <tr>
      <th>id_2</th>
      <td>1.49</td>
      <td>-0.21</td>
      <td>0.31</td>
      <td>-0.85</td>
    </tr>
    <tr>
      <th>id_3</th>
      <td>-2.55</td>
      <td>0.65</td>
      <td>0.86</td>
      <td>-0.74</td>
    </tr>
  </tbody>
</table>
</div>




```python
df4.loc['M']
df4.loc['M', 'id_1']
df4.loc[('M', 'id_1'), 'A']
df4.loc[('M', 'id_1'), ('A', 'C')]
```




    1.76




```python
df4.loc[:, 'A']
df4.loc[:, ('A', 'D')]
```




    Ridx1  Ridx2
    M      id_1     0.40
           id_2    -0.98
           id_3     0.41
    F      id_1     0.12
           id_2    -0.21
           id_3     0.65
    Name: (A, D), dtype: float64




```python
df4.loc[:, [('A', 'C'), ('B', 'C')]]
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
      <th>Cidx1</th>
      <th>A</th>
      <th>B</th>
    </tr>
    <tr>
      <th></th>
      <th>Cidx2</th>
      <th>C</th>
      <th>C</th>
    </tr>
    <tr>
      <th>Ridx1</th>
      <th>Ridx2</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="3" valign="top">M</th>
      <th>id_1</th>
      <td>1.76</td>
      <td>0.98</td>
    </tr>
    <tr>
      <th>id_2</th>
      <td>1.87</td>
      <td>0.95</td>
    </tr>
    <tr>
      <th>id_3</th>
      <td>-0.10</td>
      <td>0.14</td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">F</th>
      <th>id_1</th>
      <td>0.76</td>
      <td>0.44</td>
    </tr>
    <tr>
      <th>id_2</th>
      <td>1.49</td>
      <td>0.31</td>
    </tr>
    <tr>
      <th>id_3</th>
      <td>-2.55</td>
      <td>0.86</td>
    </tr>
  </tbody>
</table>
</div>




```python
df4.loc[('M','id_1'), : ]
```




    Cidx1  Cidx2
    A      C        1.76
           D        0.40
    B      C        0.98
           D        2.24
    Name: (M, id_1), dtype: float64




```python
df4
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
      <th>Cidx1</th>
      <th colspan="2" halign="left">A</th>
      <th colspan="2" halign="left">B</th>
    </tr>
    <tr>
      <th></th>
      <th>Cidx2</th>
      <th>C</th>
      <th>D</th>
      <th>C</th>
      <th>D</th>
    </tr>
    <tr>
      <th>Ridx1</th>
      <th>Ridx2</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="3" valign="top">M</th>
      <th>id_1</th>
      <td>1.76</td>
      <td>0.40</td>
      <td>0.98</td>
      <td>2.24</td>
    </tr>
    <tr>
      <th>id_2</th>
      <td>1.87</td>
      <td>-0.98</td>
      <td>0.95</td>
      <td>-0.15</td>
    </tr>
    <tr>
      <th>id_3</th>
      <td>-0.10</td>
      <td>0.41</td>
      <td>0.14</td>
      <td>1.45</td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">F</th>
      <th>id_1</th>
      <td>0.76</td>
      <td>0.12</td>
      <td>0.44</td>
      <td>0.33</td>
    </tr>
    <tr>
      <th>id_2</th>
      <td>1.49</td>
      <td>-0.21</td>
      <td>0.31</td>
      <td>-0.85</td>
    </tr>
    <tr>
      <th>id_3</th>
      <td>-2.55</td>
      <td>0.65</td>
      <td>0.86</td>
      <td>-0.74</td>
    </tr>
  </tbody>
</table>
</div>




```python
df4.sum() # 위 -> 아래 방향으로 합산한 결과, df4.sum(axis=0)
```




    Cidx1  Cidx2
    A      C        3.23
           D        0.39
    B      C        3.68
           D        2.28
    dtype: float64




```python
df4.sum(axis=1) # 좌 -> 우 방향으로 합산한 결과
```




    Ridx1  Ridx2
    M      id_1     5.38
           id_2     1.69
           id_3     1.90
    F      id_1     1.65
           id_2     0.74
           id_3    -1.78
    dtype: float64




```python
df4.loc[('aoa', 'all'), :] = df4.sum()
df4
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
      <th>Cidx1</th>
      <th colspan="2" halign="left">A</th>
      <th colspan="2" halign="left">B</th>
    </tr>
    <tr>
      <th></th>
      <th>Cidx2</th>
      <th>C</th>
      <th>D</th>
      <th>C</th>
      <th>D</th>
    </tr>
    <tr>
      <th>Ridx1</th>
      <th>Ridx2</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="3" valign="top">M</th>
      <th>id_1</th>
      <td>1.76</td>
      <td>0.40</td>
      <td>0.98</td>
      <td>2.24</td>
    </tr>
    <tr>
      <th>id_2</th>
      <td>1.87</td>
      <td>-0.98</td>
      <td>0.95</td>
      <td>-0.15</td>
    </tr>
    <tr>
      <th>id_3</th>
      <td>-0.10</td>
      <td>0.41</td>
      <td>0.14</td>
      <td>1.45</td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">F</th>
      <th>id_1</th>
      <td>0.76</td>
      <td>0.12</td>
      <td>0.44</td>
      <td>0.33</td>
    </tr>
    <tr>
      <th>id_2</th>
      <td>1.49</td>
      <td>-0.21</td>
      <td>0.31</td>
      <td>-0.85</td>
    </tr>
    <tr>
      <th>id_3</th>
      <td>-2.55</td>
      <td>0.65</td>
      <td>0.86</td>
      <td>-0.74</td>
    </tr>
    <tr>
      <th>aoa</th>
      <th>all</th>
      <td>3.23</td>
      <td>0.39</td>
      <td>3.68</td>
      <td>2.28</td>
    </tr>
  </tbody>
</table>
</div>




```python
df4.loc[ : ,('aoa','all')] = df4.sum(axis=1)
df4
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
      <th>Cidx1</th>
      <th colspan="2" halign="left">A</th>
      <th colspan="2" halign="left">B</th>
      <th>aoa</th>
    </tr>
    <tr>
      <th></th>
      <th>Cidx2</th>
      <th>C</th>
      <th>D</th>
      <th>C</th>
      <th>D</th>
      <th>all</th>
    </tr>
    <tr>
      <th>Ridx1</th>
      <th>Ridx2</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="3" valign="top">M</th>
      <th>id_1</th>
      <td>1.76</td>
      <td>0.40</td>
      <td>0.98</td>
      <td>2.24</td>
      <td>5.38</td>
    </tr>
    <tr>
      <th>id_2</th>
      <td>1.87</td>
      <td>-0.98</td>
      <td>0.95</td>
      <td>-0.15</td>
      <td>1.69</td>
    </tr>
    <tr>
      <th>id_3</th>
      <td>-0.10</td>
      <td>0.41</td>
      <td>0.14</td>
      <td>1.45</td>
      <td>1.90</td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">F</th>
      <th>id_1</th>
      <td>0.76</td>
      <td>0.12</td>
      <td>0.44</td>
      <td>0.33</td>
      <td>1.65</td>
    </tr>
    <tr>
      <th>id_2</th>
      <td>1.49</td>
      <td>-0.21</td>
      <td>0.31</td>
      <td>-0.85</td>
      <td>0.74</td>
    </tr>
    <tr>
      <th>id_3</th>
      <td>-2.55</td>
      <td>0.65</td>
      <td>0.86</td>
      <td>-0.74</td>
      <td>-1.78</td>
    </tr>
    <tr>
      <th>aoa</th>
      <th>all</th>
      <td>3.23</td>
      <td>0.39</td>
      <td>3.68</td>
      <td>2.28</td>
      <td>9.58</td>
    </tr>
  </tbody>
</table>
</div>




```python
df4.swaplevel('Ridx1', 'Ridx2')
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
      <th>Cidx1</th>
      <th colspan="2" halign="left">A</th>
      <th colspan="2" halign="left">B</th>
      <th>aoa</th>
    </tr>
    <tr>
      <th></th>
      <th>Cidx2</th>
      <th>C</th>
      <th>D</th>
      <th>C</th>
      <th>D</th>
      <th>all</th>
    </tr>
    <tr>
      <th>Ridx2</th>
      <th>Ridx1</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>id_1</th>
      <th>M</th>
      <td>1.76</td>
      <td>0.40</td>
      <td>0.98</td>
      <td>2.24</td>
      <td>5.38</td>
    </tr>
    <tr>
      <th>id_2</th>
      <th>M</th>
      <td>1.87</td>
      <td>-0.98</td>
      <td>0.95</td>
      <td>-0.15</td>
      <td>1.69</td>
    </tr>
    <tr>
      <th>id_3</th>
      <th>M</th>
      <td>-0.10</td>
      <td>0.41</td>
      <td>0.14</td>
      <td>1.45</td>
      <td>1.90</td>
    </tr>
    <tr>
      <th>id_1</th>
      <th>F</th>
      <td>0.76</td>
      <td>0.12</td>
      <td>0.44</td>
      <td>0.33</td>
      <td>1.65</td>
    </tr>
    <tr>
      <th>id_2</th>
      <th>F</th>
      <td>1.49</td>
      <td>-0.21</td>
      <td>0.31</td>
      <td>-0.85</td>
      <td>0.74</td>
    </tr>
    <tr>
      <th>id_3</th>
      <th>F</th>
      <td>-2.55</td>
      <td>0.65</td>
      <td>0.86</td>
      <td>-0.74</td>
      <td>-1.78</td>
    </tr>
    <tr>
      <th>all</th>
      <th>aoa</th>
      <td>3.23</td>
      <td>0.39</td>
      <td>3.68</td>
      <td>2.28</td>
      <td>9.58</td>
    </tr>
  </tbody>
</table>
</div>




```python
df4.swaplevel('Cidx1', 'Cidx2', axis=1)
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
      <th>Cidx2</th>
      <th>C</th>
      <th>D</th>
      <th>C</th>
      <th>D</th>
      <th>all</th>
    </tr>
    <tr>
      <th></th>
      <th>Cidx1</th>
      <th>A</th>
      <th>A</th>
      <th>B</th>
      <th>B</th>
      <th>aoa</th>
    </tr>
    <tr>
      <th>Ridx1</th>
      <th>Ridx2</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="3" valign="top">M</th>
      <th>id_1</th>
      <td>1.76</td>
      <td>0.40</td>
      <td>0.98</td>
      <td>2.24</td>
      <td>5.38</td>
    </tr>
    <tr>
      <th>id_2</th>
      <td>1.87</td>
      <td>-0.98</td>
      <td>0.95</td>
      <td>-0.15</td>
      <td>1.69</td>
    </tr>
    <tr>
      <th>id_3</th>
      <td>-0.10</td>
      <td>0.41</td>
      <td>0.14</td>
      <td>1.45</td>
      <td>1.90</td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">F</th>
      <th>id_1</th>
      <td>0.76</td>
      <td>0.12</td>
      <td>0.44</td>
      <td>0.33</td>
      <td>1.65</td>
    </tr>
    <tr>
      <th>id_2</th>
      <td>1.49</td>
      <td>-0.21</td>
      <td>0.31</td>
      <td>-0.85</td>
      <td>0.74</td>
    </tr>
    <tr>
      <th>id_3</th>
      <td>-2.55</td>
      <td>0.65</td>
      <td>0.86</td>
      <td>-0.74</td>
      <td>-1.78</td>
    </tr>
    <tr>
      <th>aoa</th>
      <th>all</th>
      <td>3.23</td>
      <td>0.39</td>
      <td>3.68</td>
      <td>2.28</td>
      <td>9.58</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame = pd.DataFrame(np.arange(12).reshape((4, 3)),
                     index=[["a", "a", "b", "b"], [1, 2, 1, 2]],
                     columns=[["Ohio", "Ohio", "Colorado"],
                              ["Green", "Red", "Green"]])
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

    .dataframe thead tr th {
        text-align: left;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th colspan="2" halign="left">Ohio</th>
      <th>Colorado</th>
    </tr>
    <tr>
      <th></th>
      <th></th>
      <th>Green</th>
      <th>Red</th>
      <th>Green</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">a</th>
      <th>1</th>
      <td>0</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>4</td>
      <td>5</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">b</th>
      <th>1</th>
      <td>6</td>
      <td>7</td>
      <td>8</td>
    </tr>
    <tr>
      <th>2</th>
      <td>9</td>
      <td>10</td>
      <td>11</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame.index.names = ["key1", "key2"]
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
      <th colspan="2" halign="left">Ohio</th>
      <th>Colorado</th>
    </tr>
    <tr>
      <th></th>
      <th></th>
      <th>Green</th>
      <th>Red</th>
      <th>Green</th>
    </tr>
    <tr>
      <th>key1</th>
      <th>key2</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">a</th>
      <th>1</th>
      <td>0</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>4</td>
      <td>5</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">b</th>
      <th>1</th>
      <td>6</td>
      <td>7</td>
      <td>8</td>
    </tr>
    <tr>
      <th>2</th>
      <td>9</td>
      <td>10</td>
      <td>11</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame.columns.names = ["state", "color"]
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
      <th>state</th>
      <th colspan="2" halign="left">Ohio</th>
      <th>Colorado</th>
    </tr>
    <tr>
      <th></th>
      <th>color</th>
      <th>Green</th>
      <th>Red</th>
      <th>Green</th>
    </tr>
    <tr>
      <th>key1</th>
      <th>key2</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">a</th>
      <th>1</th>
      <td>0</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>4</td>
      <td>5</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">b</th>
      <th>1</th>
      <td>6</td>
      <td>7</td>
      <td>8</td>
    </tr>
    <tr>
      <th>2</th>
      <td>9</td>
      <td>10</td>
      <td>11</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame.index
frame.index.nlevels
```




    2




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
      <th>state</th>
      <th colspan="2" halign="left">Ohio</th>
      <th>Colorado</th>
    </tr>
    <tr>
      <th></th>
      <th>color</th>
      <th>Green</th>
      <th>Red</th>
      <th>Green</th>
    </tr>
    <tr>
      <th>key1</th>
      <th>key2</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">a</th>
      <th>1</th>
      <td>0</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>4</td>
      <td>5</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">b</th>
      <th>1</th>
      <td>6</td>
      <td>7</td>
      <td>8</td>
    </tr>
    <tr>
      <th>2</th>
      <td>9</td>
      <td>10</td>
      <td>11</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame["Ohio"]
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
      <th>color</th>
      <th>Green</th>
      <th>Red</th>
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
      <th rowspan="2" valign="top">a</th>
      <th>1</th>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>4</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">b</th>
      <th>1</th>
      <td>6</td>
      <td>7</td>
    </tr>
    <tr>
      <th>2</th>
      <td>9</td>
      <td>10</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame.swaplevel("key1", "key2")
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
      <th>state</th>
      <th colspan="2" halign="left">Ohio</th>
      <th>Colorado</th>
    </tr>
    <tr>
      <th></th>
      <th>color</th>
      <th>Green</th>
      <th>Red</th>
      <th>Green</th>
    </tr>
    <tr>
      <th>key2</th>
      <th>key1</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <th>a</th>
      <td>0</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <th>a</th>
      <td>3</td>
      <td>4</td>
      <td>5</td>
    </tr>
    <tr>
      <th>1</th>
      <th>b</th>
      <td>6</td>
      <td>7</td>
      <td>8</td>
    </tr>
    <tr>
      <th>2</th>
      <th>b</th>
      <td>9</td>
      <td>10</td>
      <td>11</td>
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
      <th>state</th>
      <th colspan="2" halign="left">Ohio</th>
      <th>Colorado</th>
    </tr>
    <tr>
      <th></th>
      <th>color</th>
      <th>Green</th>
      <th>Red</th>
      <th>Green</th>
    </tr>
    <tr>
      <th>key1</th>
      <th>key2</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">a</th>
      <th>1</th>
      <td>0</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>4</td>
      <td>5</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">b</th>
      <th>1</th>
      <td>6</td>
      <td>7</td>
      <td>8</td>
    </tr>
    <tr>
      <th>2</th>
      <td>9</td>
      <td>10</td>
      <td>11</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame.sort_index(level=1)
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
      <th>state</th>
      <th colspan="2" halign="left">Ohio</th>
      <th>Colorado</th>
    </tr>
    <tr>
      <th></th>
      <th>color</th>
      <th>Green</th>
      <th>Red</th>
      <th>Green</th>
    </tr>
    <tr>
      <th>key1</th>
      <th>key2</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <th>1</th>
      <td>0</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>b</th>
      <th>1</th>
      <td>6</td>
      <td>7</td>
      <td>8</td>
    </tr>
    <tr>
      <th>a</th>
      <th>2</th>
      <td>3</td>
      <td>4</td>
      <td>5</td>
    </tr>
    <tr>
      <th>b</th>
      <th>2</th>
      <td>9</td>
      <td>10</td>
      <td>11</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame.sort_index(level=0)
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
      <th>state</th>
      <th colspan="2" halign="left">Ohio</th>
      <th>Colorado</th>
    </tr>
    <tr>
      <th></th>
      <th>color</th>
      <th>Green</th>
      <th>Red</th>
      <th>Green</th>
    </tr>
    <tr>
      <th>key1</th>
      <th>key2</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">a</th>
      <th>1</th>
      <td>0</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>4</td>
      <td>5</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">b</th>
      <th>1</th>
      <td>6</td>
      <td>7</td>
      <td>8</td>
    </tr>
    <tr>
      <th>2</th>
      <td>9</td>
      <td>10</td>
      <td>11</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame.swaplevel(0, 1)
frame.swaplevel(0, 1).sort_index(level=0)
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
      <th>state</th>
      <th colspan="2" halign="left">Ohio</th>
      <th>Colorado</th>
    </tr>
    <tr>
      <th></th>
      <th>color</th>
      <th>Green</th>
      <th>Red</th>
      <th>Green</th>
    </tr>
    <tr>
      <th>key2</th>
      <th>key1</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">1</th>
      <th>a</th>
      <td>0</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>b</th>
      <td>6</td>
      <td>7</td>
      <td>8</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">2</th>
      <th>a</th>
      <td>3</td>
      <td>4</td>
      <td>5</td>
    </tr>
    <tr>
      <th>b</th>
      <td>9</td>
      <td>10</td>
      <td>11</td>
    </tr>
  </tbody>
</table>
</div>




```python
df1 = pd.DataFrame({
    '고객번호': [1001, 1002, 1003, 1004, 1005, 1006, 1007],
    '이름': ['둘리', '도우너', '또치', '길동', '희동', '마이콜', '영희']
}, columns=['고객번호', '이름'])
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
      <th>고객번호</th>
      <th>이름</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1001</td>
      <td>둘리</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1002</td>
      <td>도우너</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1003</td>
      <td>또치</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1004</td>
      <td>길동</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1005</td>
      <td>희동</td>
    </tr>
    <tr>
      <th>5</th>
      <td>1006</td>
      <td>마이콜</td>
    </tr>
    <tr>
      <th>6</th>
      <td>1007</td>
      <td>영희</td>
    </tr>
  </tbody>
</table>
</div>




```python
df2 = pd.DataFrame({
    '고객번호': [1001, 1001, 1005, 1006, 1008, 1001],
    '금액': [10000, 20000, 15000, 5000, 100000, 30000]
}, columns=['고객번호', '금액'])
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
      <th>고객번호</th>
      <th>금액</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1001</td>
      <td>10000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1001</td>
      <td>20000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1005</td>
      <td>15000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1006</td>
      <td>5000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1008</td>
      <td>100000</td>
    </tr>
    <tr>
      <th>5</th>
      <td>1001</td>
      <td>30000</td>
    </tr>
  </tbody>
</table>
</div>




```python
# merge 함수 : 공통된 열/행 인덱스 기준으로 합침
pd.merge(df1, df2) # 양쪽 모두 공통으로 존재하는 열 값을 기준으로 
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
      <th>고객번호</th>
      <th>이름</th>
      <th>금액</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1001</td>
      <td>둘리</td>
      <td>10000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1001</td>
      <td>둘리</td>
      <td>20000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1001</td>
      <td>둘리</td>
      <td>30000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1005</td>
      <td>희동</td>
      <td>15000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1006</td>
      <td>마이콜</td>
      <td>5000</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.merge(df1, df2, how='outer')
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
      <th>고객번호</th>
      <th>이름</th>
      <th>금액</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1001</td>
      <td>둘리</td>
      <td>10000.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1001</td>
      <td>둘리</td>
      <td>20000.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1001</td>
      <td>둘리</td>
      <td>30000.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1002</td>
      <td>도우너</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1003</td>
      <td>또치</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>5</th>
      <td>1004</td>
      <td>길동</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>6</th>
      <td>1005</td>
      <td>희동</td>
      <td>15000.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>1006</td>
      <td>마이콜</td>
      <td>5000.0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>1007</td>
      <td>영희</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>9</th>
      <td>1008</td>
      <td>NaN</td>
      <td>100000.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.merge(df1, df2, how='left')
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
      <th>고객번호</th>
      <th>이름</th>
      <th>금액</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1001</td>
      <td>둘리</td>
      <td>10000.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1001</td>
      <td>둘리</td>
      <td>20000.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1001</td>
      <td>둘리</td>
      <td>30000.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1002</td>
      <td>도우너</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1003</td>
      <td>또치</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>5</th>
      <td>1004</td>
      <td>길동</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>6</th>
      <td>1005</td>
      <td>희동</td>
      <td>15000.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>1006</td>
      <td>마이콜</td>
      <td>5000.0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>1007</td>
      <td>영희</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.merge(df1, df2, how='right')
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
      <th>고객번호</th>
      <th>이름</th>
      <th>금액</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1001</td>
      <td>둘리</td>
      <td>10000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1001</td>
      <td>둘리</td>
      <td>20000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1005</td>
      <td>희동</td>
      <td>15000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1006</td>
      <td>마이콜</td>
      <td>5000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1008</td>
      <td>NaN</td>
      <td>100000</td>
    </tr>
    <tr>
      <th>5</th>
      <td>1001</td>
      <td>둘리</td>
      <td>30000</td>
    </tr>
  </tbody>
</table>
</div>




```python
df1 = pd.DataFrame({
    '품종': ['setosa', 'setosa', 'virginica', 'virginica'],
    '꽃잎길이': [1.4, 1.3, 1.5, 1.3]},
    columns=['품종', '꽃잎길이'])
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
      <th>품종</th>
      <th>꽃잎길이</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>setosa</td>
      <td>1.4</td>
    </tr>
    <tr>
      <th>1</th>
      <td>setosa</td>
      <td>1.3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>virginica</td>
      <td>1.5</td>
    </tr>
    <tr>
      <th>3</th>
      <td>virginica</td>
      <td>1.3</td>
    </tr>
  </tbody>
</table>
</div>




```python
df2 = pd.DataFrame({
    '품종': ['setosa', 'virginica', 'virginica', 'versicolor'],
    '꽃잎너비': [0.4, 0.3, 0.5, 0.3]},
    columns=['품종', '꽃잎너비'])
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
      <th>품종</th>
      <th>꽃잎너비</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>setosa</td>
      <td>0.4</td>
    </tr>
    <tr>
      <th>1</th>
      <td>virginica</td>
      <td>0.3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>virginica</td>
      <td>0.5</td>
    </tr>
    <tr>
      <th>3</th>
      <td>versicolor</td>
      <td>0.3</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.merge(df1,df2) # inner join -> 6 = 2*1+2*2, 이름이 같은 열들이 키(합치기 기준 열)가 됨
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
      <th>품종</th>
      <th>꽃잎길이</th>
      <th>꽃잎너비</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>setosa</td>
      <td>1.4</td>
      <td>0.4</td>
    </tr>
    <tr>
      <th>1</th>
      <td>setosa</td>
      <td>1.3</td>
      <td>0.4</td>
    </tr>
    <tr>
      <th>2</th>
      <td>virginica</td>
      <td>1.5</td>
      <td>0.3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>virginica</td>
      <td>1.5</td>
      <td>0.5</td>
    </tr>
    <tr>
      <th>4</th>
      <td>virginica</td>
      <td>1.3</td>
      <td>0.3</td>
    </tr>
    <tr>
      <th>5</th>
      <td>virginica</td>
      <td>1.3</td>
      <td>0.5</td>
    </tr>
  </tbody>
</table>
</div>




```python
# on : 합치기 기준 열 이름 지정
```


```python
df1 = pd.DataFrame({
    '고객명': ['춘향', '춘향', '몽룡'],
    '날짜': ['2018-01-01', '2018-01-02', '2018-01-01'],
    '데이터': ['20000', '30000', '100000']})
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
      <th>고객명</th>
      <th>날짜</th>
      <th>데이터</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>춘향</td>
      <td>2018-01-01</td>
      <td>20000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>춘향</td>
      <td>2018-01-02</td>
      <td>30000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>몽룡</td>
      <td>2018-01-01</td>
      <td>100000</td>
    </tr>
  </tbody>
</table>
</div>




```python
df2 = pd.DataFrame({
    '고객명': ['춘향', '몽룡'],
    '데이터': ['여자', '남자']})
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
      <th>고객명</th>
      <th>데이터</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>춘향</td>
      <td>여자</td>
    </tr>
    <tr>
      <th>1</th>
      <td>몽룡</td>
      <td>남자</td>
    </tr>
  </tbody>
</table>
</div>




```python
# pd.merge(df1, df2) 고객명과 데이터를 기준으로 합치기
merged_df = pd.merge(df1, df2, on='고객명')
merged_df
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
      <th>고객명</th>
      <th>날짜</th>
      <th>데이터_x</th>
      <th>데이터_y</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>춘향</td>
      <td>2018-01-01</td>
      <td>20000</td>
      <td>여자</td>
    </tr>
    <tr>
      <th>1</th>
      <td>춘향</td>
      <td>2018-01-02</td>
      <td>30000</td>
      <td>여자</td>
    </tr>
    <tr>
      <th>2</th>
      <td>몽룡</td>
      <td>2018-01-01</td>
      <td>100000</td>
      <td>남자</td>
    </tr>
  </tbody>
</table>
</div>




```python
merged_df.rename(columns={'데이터_x':'데이터', '데이터_y':'성별'}, inplace=True)
```


```python
merged_df
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
      <th>고객명</th>
      <th>날짜</th>
      <th>데이터</th>
      <th>성별</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>춘향</td>
      <td>2018-01-01</td>
      <td>20000</td>
      <td>여자</td>
    </tr>
    <tr>
      <th>1</th>
      <td>춘향</td>
      <td>2018-01-02</td>
      <td>30000</td>
      <td>여자</td>
    </tr>
    <tr>
      <th>2</th>
      <td>몽룡</td>
      <td>2018-01-01</td>
      <td>100000</td>
      <td>남자</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 전체 열 이름 변경
merged_df.columns=['고객이름', '연월일', '데이터값', '성별']
merged_df
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
      <th>고객이름</th>
      <th>연월일</th>
      <th>데이터값</th>
      <th>성별</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>춘향</td>
      <td>2018-01-01</td>
      <td>20000</td>
      <td>여자</td>
    </tr>
    <tr>
      <th>1</th>
      <td>춘향</td>
      <td>2018-01-02</td>
      <td>30000</td>
      <td>여자</td>
    </tr>
    <tr>
      <th>2</th>
      <td>몽룡</td>
      <td>2018-01-01</td>
      <td>100000</td>
      <td>남자</td>
    </tr>
  </tbody>
</table>
</div>




```python
merged_df.columns
```




    Index(['고객이름', '연월일', '데이터값', '성별'], dtype='object')




```python
# 일부 열 이름 변경

```


```python
df1 = pd.DataFrame({
    '이름': ['영희', '철수', '철수'],
    '성적': [1, 2, 3]})
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
      <th>이름</th>
      <th>성적</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>영희</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>철수</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>철수</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>




```python
df2 = pd.DataFrame({
    '성명': ['영희', '영희', '철수'],
    '성적2': [4, 5, 6]})
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
      <th>성명</th>
      <th>성적2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>영희</td>
      <td>4</td>
    </tr>
    <tr>
      <th>1</th>
      <td>영희</td>
      <td>5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>철수</td>
      <td>6</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.merge(df1, df2, left_on='이름', right_on = '성명') # 4건 : 1*2 + 2*1
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
      <th>이름</th>
      <th>성적</th>
      <th>성명</th>
      <th>성적2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>영희</td>
      <td>1</td>
      <td>영희</td>
      <td>4</td>
    </tr>
    <tr>
      <th>1</th>
      <td>영희</td>
      <td>1</td>
      <td>영희</td>
      <td>5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>철수</td>
      <td>2</td>
      <td>철수</td>
      <td>6</td>
    </tr>
    <tr>
      <th>3</th>
      <td>철수</td>
      <td>3</td>
      <td>철수</td>
      <td>6</td>
    </tr>
  </tbody>
</table>
</div>




```python
df1 = pd.DataFrame({
    '도시': ['서울', '서울', '서울', '부산', '부산'],
    '연도': [2000, 2005, 2010, 2000, 2005],
    '인구': [9853972, 9762546, 9631482, 3655437, 3512547]})
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
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>서울</td>
      <td>2000</td>
      <td>9853972</td>
    </tr>
    <tr>
      <th>1</th>
      <td>서울</td>
      <td>2005</td>
      <td>9762546</td>
    </tr>
    <tr>
      <th>2</th>
      <td>서울</td>
      <td>2010</td>
      <td>9631482</td>
    </tr>
    <tr>
      <th>3</th>
      <td>부산</td>
      <td>2000</td>
      <td>3655437</td>
    </tr>
    <tr>
      <th>4</th>
      <td>부산</td>
      <td>2005</td>
      <td>3512547</td>
    </tr>
  </tbody>
</table>
</div>




```python
df2 = pd.DataFrame(
    np.arange(12).reshape((6, 2)),
    index=[['부산', '부산', '서울', '서울', '서울', '서울'],
           [2000, 2005, 2000, 2005, 2010, 2015]],
    columns=['데이터1', '데이터2'])
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
      <th></th>
      <th>데이터1</th>
      <th>데이터2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">부산</th>
      <th>2000</th>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2005</th>
      <td>2</td>
      <td>3</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">서울</th>
      <th>2000</th>
      <td>4</td>
      <td>5</td>
    </tr>
    <tr>
      <th>2005</th>
      <td>6</td>
      <td>7</td>
    </tr>
    <tr>
      <th>2010</th>
      <td>8</td>
      <td>9</td>
    </tr>
    <tr>
      <th>2015</th>
      <td>10</td>
      <td>11</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.merge(df1, df2, left_on=['도시','연도'], right_index=True)
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
      <th>데이터1</th>
      <th>데이터2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>서울</td>
      <td>2000</td>
      <td>9853972</td>
      <td>4</td>
      <td>5</td>
    </tr>
    <tr>
      <th>1</th>
      <td>서울</td>
      <td>2005</td>
      <td>9762546</td>
      <td>6</td>
      <td>7</td>
    </tr>
    <tr>
      <th>2</th>
      <td>서울</td>
      <td>2010</td>
      <td>9631482</td>
      <td>8</td>
      <td>9</td>
    </tr>
    <tr>
      <th>3</th>
      <td>부산</td>
      <td>2000</td>
      <td>3655437</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>부산</td>
      <td>2005</td>
      <td>3512547</td>
      <td>2</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>




```python
df1 = pd.DataFrame(
    [[1., 2.], [3., 4.], [5., 6.]],
    index=['a', 'c', 'e'],
    columns=['서울', '부산'])
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
      <th>서울</th>
      <th>부산</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>1.0</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>c</th>
      <td>3.0</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>e</th>
      <td>5.0</td>
      <td>6.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
df2 = pd.DataFrame(
    [[7., 8.], [9., 10.], [11., 12.], [13, 14]],
    index=['b', 'c', 'd', 'e'],
    columns=['대구', '광주'])
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
      <th>대구</th>
      <th>광주</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>b</th>
      <td>7.0</td>
      <td>8.0</td>
    </tr>
    <tr>
      <th>c</th>
      <td>9.0</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>d</th>
      <td>11.0</td>
      <td>12.0</td>
    </tr>
    <tr>
      <th>e</th>
      <td>13.0</td>
      <td>14.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.merge(df1, df2, left_index=True, right_index=True, how='outer')
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
      <th>서울</th>
      <th>부산</th>
      <th>대구</th>
      <th>광주</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>1.0</td>
      <td>2.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>b</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>7.0</td>
      <td>8.0</td>
    </tr>
    <tr>
      <th>c</th>
      <td>3.0</td>
      <td>4.0</td>
      <td>9.0</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>d</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>11.0</td>
      <td>12.0</td>
    </tr>
    <tr>
      <th>e</th>
      <td>5.0</td>
      <td>6.0</td>
      <td>13.0</td>
      <td>14.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
df1.join(df2)
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
      <th>서울</th>
      <th>부산</th>
      <th>대구</th>
      <th>광주</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>1.0</td>
      <td>2.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>c</th>
      <td>3.0</td>
      <td>4.0</td>
      <td>9.0</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>e</th>
      <td>5.0</td>
      <td>6.0</td>
      <td>13.0</td>
      <td>14.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
df1.join(df2, how='outer')
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
      <th>서울</th>
      <th>부산</th>
      <th>대구</th>
      <th>광주</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>1.0</td>
      <td>2.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>b</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>7.0</td>
      <td>8.0</td>
    </tr>
    <tr>
      <th>c</th>
      <td>3.0</td>
      <td>4.0</td>
      <td>9.0</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>d</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>11.0</td>
      <td>12.0</td>
    </tr>
    <tr>
      <th>e</th>
      <td>5.0</td>
      <td>6.0</td>
      <td>13.0</td>
      <td>14.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
df1.join(df2, how='left')
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
      <th>서울</th>
      <th>부산</th>
      <th>대구</th>
      <th>광주</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>1.0</td>
      <td>2.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>c</th>
      <td>3.0</td>
      <td>4.0</td>
      <td>9.0</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>e</th>
      <td>5.0</td>
      <td>6.0</td>
      <td>13.0</td>
      <td>14.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
df1.join(df2, how='right')
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
      <th>서울</th>
      <th>부산</th>
      <th>대구</th>
      <th>광주</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>b</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>7.0</td>
      <td>8.0</td>
    </tr>
    <tr>
      <th>c</th>
      <td>3.0</td>
      <td>4.0</td>
      <td>9.0</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>d</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>11.0</td>
      <td>12.0</td>
    </tr>
    <tr>
      <th>e</th>
      <td>5.0</td>
      <td>6.0</td>
      <td>13.0</td>
      <td>14.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
# concat : 기준열 없이 단순 데이터 연결, 기본적으로 위아래(행) 연결
```


```python
s1 = pd.Series([0, 1], index=['A', 'B'])
s2 = pd.Series([2, 3, 4], index=['A', 'B', 'C'])
```


```python
s1
```




    A    0
    B    1
    dtype: int64




```python
s2
```




    A    2
    B    3
    C    4
    dtype: int64




```python
pd.concat([s1, s2])
```




    A    0
    B    1
    A    2
    B    3
    C    4
    dtype: int64




```python
df1 = pd.DataFrame(
    np.arange(6).reshape(3, 2),
    index=['a', 'b', 'c'],
    columns=['데이터1', '데이터2'])
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
      <th>데이터1</th>
      <th>데이터2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>b</th>
      <td>2</td>
      <td>3</td>
    </tr>
    <tr>
      <th>c</th>
      <td>4</td>
      <td>5</td>
    </tr>
  </tbody>
</table>
</div>




```python
df2 = pd.DataFrame(
    5 + np.arange(4).reshape(2, 2),
    index=['a', 'c'],
    columns=['데이터3', '데이터4'])
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
      <th>데이터3</th>
      <th>데이터4</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>5</td>
      <td>6</td>
    </tr>
    <tr>
      <th>c</th>
      <td>7</td>
      <td>8</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.concat([df1, df2], axis=1)
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
      <th>데이터1</th>
      <th>데이터2</th>
      <th>데이터3</th>
      <th>데이터4</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>0</td>
      <td>1</td>
      <td>5.0</td>
      <td>6.0</td>
    </tr>
    <tr>
      <th>b</th>
      <td>2</td>
      <td>3</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>c</th>
      <td>4</td>
      <td>5</td>
      <td>7.0</td>
      <td>8.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame = pd.DataFrame({"a": range(7), "b": range(7, 0, -1),
                      "c": ["one", "one", "one", "two", "two",
                            "two", "two"],
                      "d": [0, 1, 2, 0, 1, 2, 3]})
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
      <th>a</th>
      <th>b</th>
      <th>c</th>
      <th>d</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>7</td>
      <td>one</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>6</td>
      <td>one</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>5</td>
      <td>one</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>4</td>
      <td>two</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>3</td>
      <td>two</td>
      <td>1</td>
    </tr>
    <tr>
      <th>5</th>
      <td>5</td>
      <td>2</td>
      <td>two</td>
      <td>2</td>
    </tr>
    <tr>
      <th>6</th>
      <td>6</td>
      <td>1</td>
      <td>two</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame2 = frame.set_index(["c", "d"])
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
      <th></th>
      <th>a</th>
      <th>b</th>
    </tr>
    <tr>
      <th>c</th>
      <th>d</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="3" valign="top">one</th>
      <th>0</th>
      <td>0</td>
      <td>7</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>6</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>5</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">two</th>
      <th>0</th>
      <td>3</td>
      <td>4</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4</td>
      <td>3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>5</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>6</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame.set_index(["c", "d"], drop=False)
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
      <th>a</th>
      <th>b</th>
      <th>c</th>
      <th>d</th>
    </tr>
    <tr>
      <th>c</th>
      <th>d</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="3" valign="top">one</th>
      <th>0</th>
      <td>0</td>
      <td>7</td>
      <td>one</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>6</td>
      <td>one</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>5</td>
      <td>one</td>
      <td>2</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">two</th>
      <th>0</th>
      <td>3</td>
      <td>4</td>
      <td>two</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4</td>
      <td>3</td>
      <td>two</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>5</td>
      <td>2</td>
      <td>two</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>6</td>
      <td>1</td>
      <td>two</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame.set_index(["c", "d"], drop=True)
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
      <th>a</th>
      <th>b</th>
    </tr>
    <tr>
      <th>c</th>
      <th>d</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="3" valign="top">one</th>
      <th>0</th>
      <td>0</td>
      <td>7</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>6</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>5</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">two</th>
      <th>0</th>
      <td>3</td>
      <td>4</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4</td>
      <td>3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>5</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>6</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>




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
      <th></th>
      <th>a</th>
      <th>b</th>
    </tr>
    <tr>
      <th>c</th>
      <th>d</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="3" valign="top">one</th>
      <th>0</th>
      <td>0</td>
      <td>7</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>6</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>5</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">two</th>
      <th>0</th>
      <td>3</td>
      <td>4</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4</td>
      <td>3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>5</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>6</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame2.reset_index()
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
      <th>c</th>
      <th>d</th>
      <th>a</th>
      <th>b</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>one</td>
      <td>0</td>
      <td>0</td>
      <td>7</td>
    </tr>
    <tr>
      <th>1</th>
      <td>one</td>
      <td>1</td>
      <td>1</td>
      <td>6</td>
    </tr>
    <tr>
      <th>2</th>
      <td>one</td>
      <td>2</td>
      <td>2</td>
      <td>5</td>
    </tr>
    <tr>
      <th>3</th>
      <td>two</td>
      <td>0</td>
      <td>3</td>
      <td>4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>two</td>
      <td>1</td>
      <td>4</td>
      <td>3</td>
    </tr>
    <tr>
      <th>5</th>
      <td>two</td>
      <td>2</td>
      <td>5</td>
      <td>2</td>
    </tr>
    <tr>
      <th>6</th>
      <td>two</td>
      <td>3</td>
      <td>6</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>




```python
#1. df1과 df2에 대해 merge 연습, on, left_on, right_on, how
df1 = pd.DataFrame({"key": ["b", "b", "a", "c", "a", "a", "b"],
                    "data1": pd.Series(range(7), dtype="Int64")})
df2 = pd.DataFrame({"key": ["a", "b", "d"],
                    "data2": pd.Series(range(3), dtype="Int64")})
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
      <th>key</th>
      <th>data1</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>b</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>b</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>a</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>c</td>
      <td>3</td>
    </tr>
    <tr>
      <th>4</th>
      <td>a</td>
      <td>4</td>
    </tr>
    <tr>
      <th>5</th>
      <td>a</td>
      <td>5</td>
    </tr>
    <tr>
      <th>6</th>
      <td>b</td>
      <td>6</td>
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
      <th>key</th>
      <th>data2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>a</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>b</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>d</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.merge(df1,df2, how='left')
pd.merge(df1, df2, how='right')
pd.merge(df1, df2)
pd.merge(df1, df2, on='key')
pd.merge(df1, df2, how='outer')
pd.merge(df2, df1, how='outer')
pd.merge(df1,df2, left_on='key', right_on='key')
pd.merge(df1,df2, left_on='data1', right_on='data2')
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
      <th>key_x</th>
      <th>data1</th>
      <th>key_y</th>
      <th>data2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>b</td>
      <td>0</td>
      <td>a</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>b</td>
      <td>1</td>
      <td>b</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>a</td>
      <td>2</td>
      <td>d</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>




```python
#2. left과 right에 대해 merge 연습, on, left_on, right_on, how
left = pd.DataFrame({"key1": ["foo", "foo", "bar"],
                     "key2": ["one", "two", "one"],
                     "lval": pd.Series([1, 2, 3], dtype='Int64')})
right = pd.DataFrame({"key1": ["foo", "foo", "bar", "bar"],
                      "key2": ["one", "one", "one", "two"],
                      "rval": pd.Series([4, 5, 6, 7], dtype='Int64')})
pd.merge(left, right, on=["key1", "key2"], how="outer")
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
      <th>lval</th>
      <th>rval</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>foo</td>
      <td>one</td>
      <td>1</td>
      <td>4</td>
    </tr>
    <tr>
      <th>1</th>
      <td>foo</td>
      <td>one</td>
      <td>1</td>
      <td>5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>foo</td>
      <td>two</td>
      <td>2</td>
      <td>&lt;NA&gt;</td>
    </tr>
    <tr>
      <th>3</th>
      <td>bar</td>
      <td>one</td>
      <td>3</td>
      <td>6</td>
    </tr>
    <tr>
      <th>4</th>
      <td>bar</td>
      <td>two</td>
      <td>&lt;NA&gt;</td>
      <td>7</td>
    </tr>
  </tbody>
</table>
</div>




```python
left
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
      <th>lval</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>foo</td>
      <td>one</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>foo</td>
      <td>two</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>bar</td>
      <td>one</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>




```python
right
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
      <th>rval</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>foo</td>
      <td>one</td>
      <td>4</td>
    </tr>
    <tr>
      <th>1</th>
      <td>foo</td>
      <td>one</td>
      <td>5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>bar</td>
      <td>one</td>
      <td>6</td>
    </tr>
    <tr>
      <th>3</th>
      <td>bar</td>
      <td>two</td>
      <td>7</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.merge(left,right, how='left')
pd.merge(left,right, how='right')
pd.merge(left,right, on=['key1', 'key2'])
pd.merge(left, right, left_on='key1', right_on='key1')
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
      <th>key2_x</th>
      <th>lval</th>
      <th>key2_y</th>
      <th>rval</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>foo</td>
      <td>one</td>
      <td>1</td>
      <td>one</td>
      <td>4</td>
    </tr>
    <tr>
      <th>1</th>
      <td>foo</td>
      <td>one</td>
      <td>1</td>
      <td>one</td>
      <td>5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>foo</td>
      <td>two</td>
      <td>2</td>
      <td>one</td>
      <td>4</td>
    </tr>
    <tr>
      <th>3</th>
      <td>foo</td>
      <td>two</td>
      <td>2</td>
      <td>one</td>
      <td>5</td>
    </tr>
    <tr>
      <th>4</th>
      <td>bar</td>
      <td>one</td>
      <td>3</td>
      <td>one</td>
      <td>6</td>
    </tr>
    <tr>
      <th>5</th>
      <td>bar</td>
      <td>one</td>
      <td>3</td>
      <td>two</td>
      <td>7</td>
    </tr>
  </tbody>
</table>
</div>




```python
#3. merge 열 이름과 행 인덱스를 기준으로 병합 연습
left1 = pd.DataFrame({"key": ["a", "b", "a", "a", "b", "c"],
                      "value": pd.Series(range(6), dtype="Int64")})
right1 = pd.DataFrame({"group_val": [3.5, 7]}, index=["a", "b"])
left1
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
      <th>key</th>
      <th>value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>a</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>b</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>a</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>a</td>
      <td>3</td>
    </tr>
    <tr>
      <th>4</th>
      <td>b</td>
      <td>4</td>
    </tr>
    <tr>
      <th>5</th>
      <td>c</td>
      <td>5</td>
    </tr>
  </tbody>
</table>
</div>




```python
right1
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
      <th>group_val</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>3.5</td>
    </tr>
    <tr>
      <th>b</th>
      <td>7.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.merge(left1,right1, left_on='key', right_index=True)
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
      <th>key</th>
      <th>value</th>
      <th>group_val</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>a</td>
      <td>0</td>
      <td>3.5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>a</td>
      <td>2</td>
      <td>3.5</td>
    </tr>
    <tr>
      <th>3</th>
      <td>a</td>
      <td>3</td>
      <td>3.5</td>
    </tr>
    <tr>
      <th>1</th>
      <td>b</td>
      <td>1</td>
      <td>7.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>b</td>
      <td>4</td>
      <td>7.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
#4. merge 연습, index 기준
left2 = pd.DataFrame([[1., 2.], [3., 4.], [5., 6.]],
                     index=["a", "c", "e"],
                     columns=["Ohio", "Nevada"]).astype("Int64")
right2 = pd.DataFrame([[7., 8.], [9., 10.], [11., 12.], [13, 14]],
                      index=["b", "c", "d", "e"],
                      columns=["Missouri", "Alabama"]).astype("Int64")
left2
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
      <th>a</th>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>c</th>
      <td>3</td>
      <td>4</td>
    </tr>
    <tr>
      <th>e</th>
      <td>5</td>
      <td>6</td>
    </tr>
  </tbody>
</table>
</div>




```python
right2
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
      <th>Missouri</th>
      <th>Alabama</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>b</th>
      <td>7</td>
      <td>8</td>
    </tr>
    <tr>
      <th>c</th>
      <td>9</td>
      <td>10</td>
    </tr>
    <tr>
      <th>d</th>
      <td>11</td>
      <td>12</td>
    </tr>
    <tr>
      <th>e</th>
      <td>13</td>
      <td>14</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.merge(left2, right2, left_index=True, right_index=True)
pd.merge(left2, right2, left_index=True, right_index=True, how='outer')
pd.merge(left2, right2, left_index=True, right_index=True, how='left')
pd.merge(left2, right2, left_index=True, right_index=True, how='right')
merged_df = pd.merge(left2, right2, left_index=True, right_index=True)
merged_df.rename(columns={'Ohio': '오하이오'})
merged_df.rename(columns={'Ohio': '오하이오', 'Nevada':'네바다'}, inplace=True)
merged_df
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
      <th>오하이오</th>
      <th>네바다</th>
      <th>Missouri</th>
      <th>Alabama</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>c</th>
      <td>3</td>
      <td>4</td>
      <td>9</td>
      <td>10</td>
    </tr>
    <tr>
      <th>e</th>
      <td>5</td>
      <td>6</td>
      <td>13</td>
      <td>14</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 5. concat 연습, axis, join 속성 값 변경 설정
s1 = pd.Series([0, 1], index=["a", "b"], dtype="Int64")
s2 = pd.Series([2, 3, 4], index=["c", "d", "e"], dtype="Int64")
s3 = pd.Series([5, 6], index=["f", "g"], dtype="Int64")
```


```python
s1
```




    a    0
    b    1
    dtype: Int64




```python
s2
```




    c    2
    d    3
    e    4
    dtype: Int64




```python
s3
```




    f    5
    g    6
    dtype: Int64




```python
pd.concat([s1,s2])
pd.concat([s1,s2,s3])
pd.concat([s1,s2,s3], axis=1)
pd.concat([s1,s2], axis=1)
pd.concat([s1, s2, s3], axis=1, join='inner')
pd.concat([s1, s2, s3], axis=1, join='outer')
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
      <td>0</td>
      <td>&lt;NA&gt;</td>
      <td>&lt;NA&gt;</td>
    </tr>
    <tr>
      <th>b</th>
      <td>1</td>
      <td>&lt;NA&gt;</td>
      <td>&lt;NA&gt;</td>
    </tr>
    <tr>
      <th>c</th>
      <td>&lt;NA&gt;</td>
      <td>2</td>
      <td>&lt;NA&gt;</td>
    </tr>
    <tr>
      <th>d</th>
      <td>&lt;NA&gt;</td>
      <td>3</td>
      <td>&lt;NA&gt;</td>
    </tr>
    <tr>
      <th>e</th>
      <td>&lt;NA&gt;</td>
      <td>4</td>
      <td>&lt;NA&gt;</td>
    </tr>
    <tr>
      <th>f</th>
      <td>&lt;NA&gt;</td>
      <td>&lt;NA&gt;</td>
      <td>5</td>
    </tr>
    <tr>
      <th>g</th>
      <td>&lt;NA&gt;</td>
      <td>&lt;NA&gt;</td>
      <td>6</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 6. concat 연습, axis, join 속성 값 변경 설정
df1 = pd.DataFrame(np.arange(6).reshape(3, 2), index=["a", "b", "c"],
                   columns=["one", "two"])
df2 = pd.DataFrame(5 + np.arange(4).reshape(2, 2), index=["a", "c"],
                   columns=["three", "four"])
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
      <th>one</th>
      <th>two</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>b</th>
      <td>2</td>
      <td>3</td>
    </tr>
    <tr>
      <th>c</th>
      <td>4</td>
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
      <th>three</th>
      <th>four</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>5</td>
      <td>6</td>
    </tr>
    <tr>
      <th>c</th>
      <td>7</td>
      <td>8</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.concat([df1, df2])
pd.concat([df1, df2], axis=1)
pd.concat([df1, df2], axis=1, join='inner')
pd.concat([df1, df2], axis=1, join='outer')
df1.join(df2)
df1.join(df2, how='outer')
df1.join(df2, how='left')
df1.join(df2, how='right')
df2.join(df1)
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
      <th>four</th>
      <th>one</th>
      <th>two</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>5</td>
      <td>6</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>c</th>
      <td>7</td>
      <td>8</td>
      <td>4</td>
      <td>5</td>
    </tr>
  </tbody>
</table>
</div>




```python
#7. stack, unstack 연습
data = pd.DataFrame(np.arange(6).reshape((2, 3)),
                    index=pd.Index(["Ohio", "Colorado"], name="state"),
                    columns=pd.Index(["one", "two", "three"],
                    name="number"))
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
      <th>number</th>
      <th>one</th>
      <th>two</th>
      <th>three</th>
    </tr>
    <tr>
      <th>state</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Ohio</th>
      <td>0</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>Colorado</th>
      <td>3</td>
      <td>4</td>
      <td>5</td>
    </tr>
  </tbody>
</table>
</div>




```python
data.unstack()
data.stack().unstack()
data.stack()
```




    state     number
    Ohio      one       0
              two       1
              three     2
    Colorado  one       3
              two       4
              three     5
    dtype: int32




```python
import seaborn as sns
titanic = sns.load_dataset("titanic")
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
      <td>22.0</td>
      <td>1</td>
      <td>0</td>
      <td>7.2500</td>
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
      <td>38.0</td>
      <td>1</td>
      <td>0</td>
      <td>71.2833</td>
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
      <td>26.0</td>
      <td>0</td>
      <td>0</td>
      <td>7.9250</td>
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
      <td>35.0</td>
      <td>1</td>
      <td>0</td>
      <td>53.1000</td>
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
      <td>35.0</td>
      <td>0</td>
      <td>0</td>
      <td>8.0500</td>
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
      <td>27.0</td>
      <td>0</td>
      <td>0</td>
      <td>13.0000</td>
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
      <td>19.0</td>
      <td>0</td>
      <td>0</td>
      <td>30.0000</td>
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
      <td>23.4500</td>
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
      <td>26.0</td>
      <td>0</td>
      <td>0</td>
      <td>30.0000</td>
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
      <td>32.0</td>
      <td>0</td>
      <td>0</td>
      <td>7.7500</td>
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
# 8. 타이타닉
# - survived 열 값으로 전체 생존율 출력
# len(titanic.survived)
# titanic.survived.value_counts()
titanic.survived[titanic.survived == 1].value_counts() / len(titanic.survived) * 100
# - pclass 열 값이 1인 자료의 개수를 출력
titanic.pclass[titanic.pclass == 1].value_counts()
# - age가 10보다 작은 승객에 대한 생존율 출력
titanic.survived[(titanic.survived[titanic.survived == 1]) & (titanic.age < 10)].value_counts() / len(titanic.survived) * 100
# - embarked(embark_town)에서 각 항구별 승선인원 출력
titanic.embark_town.value_counts()
```




    Southampton    644
    Cherbourg      168
    Queenstown      77
    Name: embark_town, dtype: int64




```python

```
