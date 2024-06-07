```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
```


```python
col = ['X','Y']
data1 = [[-6,-3],[-4,-1],[-2,-3],[0,1],[2,2]]
data2 = [[7,-4],[4,-1],[2,0],[-1,3],[-4,9]]
data3 = [[3,-4],[3,-1],[3,0],[3,3],[3,9]]
df1 = pd.DataFrame(data=data1, columns=col)
df2 = pd.DataFrame(data=data2, columns=col)
df3 = pd.DataFrame(data=data3, columns=col)
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
      <th>X</th>
      <th>Y</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>-6</td>
      <td>-3</td>
    </tr>
    <tr>
      <th>1</th>
      <td>-4</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-2</td>
      <td>-3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>




```python
df1.cov() # 공분산
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>X</th>
      <th>Y</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>X</th>
      <td>10.0</td>
      <td>6.0</td>
    </tr>
    <tr>
      <th>Y</th>
      <td>6.0</td>
      <td>5.2</td>
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
      <th>X</th>
      <th>Y</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>7</td>
      <td>-4</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>-1</td>
      <td>3</td>
    </tr>
    <tr>
      <th>4</th>
      <td>-4</td>
      <td>9</td>
    </tr>
  </tbody>
</table>
</div>




```python
df2.cov() # 음의 상관관계
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>X</th>
      <th>Y</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>X</th>
      <td>18.30</td>
      <td>-20.55</td>
    </tr>
    <tr>
      <th>Y</th>
      <td>-20.55</td>
      <td>24.30</td>
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

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>X</th>
      <th>Y</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>3</td>
      <td>-4</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>3</td>
    </tr>
    <tr>
      <th>4</th>
      <td>3</td>
      <td>9</td>
    </tr>
  </tbody>
</table>
</div>




```python
df3.cov()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>X</th>
      <th>Y</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>X</th>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>Y</th>
      <td>0.0</td>
      <td>24.3</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 첨도(kurtosis, kurt) : 데이터 분포의 뾰족한 정도
# 정규분포 : 평균=0, 표준편차=1
# 정규분포 : 0, 정규분포보다 뾰족한 경우 : >0, 정규분포보다 완만한 경우 : <0
l = [-9,-5,-1,-1,0,0,0,0,0,1,1,5,9] 
m = np.random.normal(0,1,13) 
p = [-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6] 
data = {"col1":l,"col2":m,"col3":p}
df = pd.DataFrame(data)
print(df)
```

        col1      col2  col3
    0     -9  1.143091    -6
    1     -5 -0.011953    -5
    2     -1 -0.532272    -4
    3     -1 -0.164728    -3
    4      0  0.988523    -2
    5      0  0.460258    -1
    6      0 -0.044893     0
    7      0  0.501859     1
    8      0  0.004275     2
    9      1 -0.206938     3
    10     1 -0.836073     4
    11     5 -0.161500     5
    12     9 -0.626104     6
    


```python
df['col1'].kurt() # 첨도
```




    2.190460157126824




```python
df['col1'].mean() # 0
df['col1'].std() # 4.2
```




    4.242640687119285




```python
df['col2'].mean() # 0.03
df['col2'].std() # 0.59
```




    0.5915942461102468




```python
df['col2'].kurt() # 첨도
```




    -0.24698264119826163




```python
df['col3'].mean() # 0
df['col3'].std() # 3.89
df['col3'].kurt() # 첨도
```




    -1.2000000000000002




```python
# 왜도(skew) : 비대칭도
# 정규분포=왜도=0, 왼쪽으로 치우침=왜도>0, 오른쪽으로 치우침=왜도<0
```


```python
a = [-5,-4,-3,-3,-2,-2,-1,-1,-1,0,0,0,0,0,1,1,1,2]
b = [-3,-2,-1,-1,-1,-1,0,0,0,0,0,0,1,1,1,1,2,3]
c = [-2,-1,-1,-1,0,0,0,0,0,1,1,1,2,2,3,3,4,5,]
data = {"col1":a,"col2":b,"col3":c}
df = pd.DataFrame(data)
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
      <th>col1</th>
      <th>col2</th>
      <th>col3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>-5</td>
      <td>-3</td>
      <td>-2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>-4</td>
      <td>-2</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-3</td>
      <td>-1</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>-3</td>
      <td>-1</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>-2</td>
      <td>-1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>-2</td>
      <td>-1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>-1</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>-1</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>-1</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>0</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>10</th>
      <td>0</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>11</th>
      <td>0</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>12</th>
      <td>0</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>13</th>
      <td>0</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>14</th>
      <td>1</td>
      <td>1</td>
      <td>3</td>
    </tr>
    <tr>
      <th>15</th>
      <td>1</td>
      <td>1</td>
      <td>3</td>
    </tr>
    <tr>
      <th>16</th>
      <td>1</td>
      <td>2</td>
      <td>4</td>
    </tr>
    <tr>
      <th>17</th>
      <td>2</td>
      <td>3</td>
      <td>5</td>
    </tr>
  </tbody>
</table>
</div>




```python
# col1은 최빈값이 우측으로 치우쳐져 있음 왜도<0
df['col1'].skew()
```




    -0.6157739556801386




```python
df['col2'].mean()
df['col2'].skew() # 정규분포(대칭구조), 왜도=0
```




    0.0




```python
# col1은 최빈값이 좌측으로 치우쳐져 있음 왜도>0
df['col3'].mean()
df['col3'].skew()
```




    0.6157739556801384




```python
"""
상관계수
1) 피어슨 상관계수 : 두 변수가 연속형, 선형관계, ex: 딥러님 점수와 데이터분석 점수 간의 상관관계,
연속형 자료가 정규분포를 따른다고 가정하는 모수적 추론 기법
2) 스피어만 상관계수 : 순위가 있는 서열척도 간의 상관관계, ex: 딥러닝 등수와 데이터분석 등수의 상관관계,
두 변수간의 관계가 비선형적(곡선)일 때 사용가능
3) 켄달(kendall)의 타우(tau) : 두 변수간의 관계가 비선형적이거나 서열척도의 변수일때, 표본이 작을 때 사용가능
"""
```




    '\n상관계수\n1) 피어슨 상관계수 : 두 변수가 연속형, 선형관계, ex: 딥러님 점수와 데이터분석 점수 간의 상관관계,\n연속형 자료가 정규분포를 따른다고 가정하는 모수적 추론 기법\n2) 스피어만 상관계수 : 순위가 있는 서열척도 간의 상관관계, ex: 딥러닝 등수와 데이터분석 등수의 상관관계,\n두 변수간의 관계가 비선형적(곡선)일 때 사용가능\n3) 켄달(kendall)의 타우(tau) : 두 변수간의 관계가 비선형적이거나 서열척도의 변수일때, 표본이 작을 때 사용가능\n'




```python
'''
Phi 상관계수, Cramer's 상관계수 : 범주형 변수간 상관관계
1) Phi 상관계수(변수가 갖는 값의 범주가 2개)
- ex) 성별 : 남/여, 합격여부 : 합/불합
- 성별과 합격여부와의 상관관계 궁금? Phi 상관계수

2) Cramer's 상관계수(변수가 갖는 값의 범주가 3개 이상)
- ex) 나이대: 10대/20대/30대/40대, 거주형태 : 단독/빌라/아파트/복합
- 나이대와 거주형태간의 관계? Cramer's 상관계수
'''
```




    "\nPhi 상관계수, Cramer's 상관계수 : 범주형 변수간 상관관계\n1) Phi 상관계수(변수가 갖는 값의 범주가 2개)\n- ex) 성별 : 남/여, 합격여부 : 합/불합\n- 성별과 합격여부와의 상관관계 궁금? Phi 상관계수\n\n2) Cramer's 상관계수(변수가 갖는 값의 범주가 3개 이상)\n- ex) 나이대: 10대/20대/30대/40대, 거주형태 : 단독/빌라/아파트/복합\n- 나이대와 거주형태간의 관계? Cramer's 상관계수\n"




```python
"""
Point biseral 상관계수 : 연속형 변수와 범주형 변수간 상관관계
ex) 성별과 시험점수간의 상관관계
"""
```




    '\nPoint biseral 상관계수 : 연속형 변수와 범주형 변수간 상관관계\nex) 성별과 시험점수간의 상관관계\n'




```python
z = [-3, -2, -1, 0, 1, 2, 3]
w = [9, 4, 1, 0, 1, 4, 9]

np.corrcoef(z, w)[0, 1] # 피어슨 상관계수, w=z**2, 비선형 
```




    0.0




```python
# 스피어만 상관계수
import scipy.stats as ss
```


```python
x = [8, 3, 6, 6, 9, 4, 3, 9, 3, 4]
y = [6, 2, 4, 6, 10, 5, 1, 8, 4, 5]
```


```python
ss.spearmanr(x,y).correlation
```




    0.9000703207408192




```python
col1 = [1,2,3,4,5,6]
col2 = [1,4,2,8,16,32]
col3 = [6,5,4,3,2,1]
data = {"col1":col1,"col2":col2,"col3":col3}
df = pd.DataFrame(data)
print(df)
```

       col1  col2  col3
    0     1     1     6
    1     2     4     5
    2     3     2     4
    3     4     8     3
    4     5    16     2
    5     6    32     1
    


```python
# col1 변수의 순위와 col2 변수의 순위가 대체로 일치 -> 스피어만 상관계수가 양수
# 스피어만 상관계수 : 두 변수의 순위에 대한 피어슨 상관계수
```


```python
df.corr() # 피어슨
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>col1</th>
      <th>col2</th>
      <th>col3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>col1</th>
      <td>1.000000</td>
      <td>0.887739</td>
      <td>-1.000000</td>
    </tr>
    <tr>
      <th>col2</th>
      <td>0.887739</td>
      <td>1.000000</td>
      <td>-0.887739</td>
    </tr>
    <tr>
      <th>col3</th>
      <td>-1.000000</td>
      <td>-0.887739</td>
      <td>1.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.corr(method='pearson') # 위와동일, defalut:피어슨 상관계수
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>col1</th>
      <th>col2</th>
      <th>col3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>col1</th>
      <td>1.000000</td>
      <td>0.887739</td>
      <td>-1.000000</td>
    </tr>
    <tr>
      <th>col2</th>
      <td>0.887739</td>
      <td>1.000000</td>
      <td>-0.887739</td>
    </tr>
    <tr>
      <th>col3</th>
      <td>-1.000000</td>
      <td>-0.887739</td>
      <td>1.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.corr(method='spearman') # 스피어만 상관계수, 비선형적, 표본이 많을 때
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>col1</th>
      <th>col2</th>
      <th>col3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>col1</th>
      <td>1.000000</td>
      <td>0.942857</td>
      <td>-1.000000</td>
    </tr>
    <tr>
      <th>col2</th>
      <td>0.942857</td>
      <td>1.000000</td>
      <td>-0.942857</td>
    </tr>
    <tr>
      <th>col3</th>
      <td>-1.000000</td>
      <td>-0.942857</td>
      <td>1.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
ss.kendalltau(df['col1'], df['col2']).correlation # 비선형적, 표본이 적을 때
```




    0.8666666666666666




```python
df.corr(method='kendall')
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>col1</th>
      <th>col2</th>
      <th>col3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>col1</th>
      <td>1.000000</td>
      <td>0.866667</td>
      <td>-1.000000</td>
    </tr>
    <tr>
      <th>col2</th>
      <td>0.866667</td>
      <td>1.000000</td>
      <td>-0.866667</td>
    </tr>
    <tr>
      <th>col3</th>
      <td>-1.000000</td>
      <td>-0.866667</td>
      <td>1.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
data1 = {"col1":[1,2,3,4,5,6],"col2":[1,4,2,8,16,32]}
data2 = {"col1":[6,5,4,3,2,1],"col3":[3,6,1,2,5,9]}
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
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
      <th>col1</th>
      <th>col2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>4</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>8</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>16</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>32</td>
    </tr>
  </tbody>
</table>
</div>




```python
df1.corr()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>col1</th>
      <th>col2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>col1</th>
      <td>1.000000</td>
      <td>0.887739</td>
    </tr>
    <tr>
      <th>col2</th>
      <td>0.887739</td>
      <td>1.000000</td>
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
      <th>col1</th>
      <th>col3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>6</td>
      <td>3</td>
    </tr>
    <tr>
      <th>1</th>
      <td>5</td>
      <td>6</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2</td>
      <td>5</td>
    </tr>
    <tr>
      <th>5</th>
      <td>1</td>
      <td>9</td>
    </tr>
  </tbody>
</table>
</div>




```python
df2.corr()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>col1</th>
      <th>col3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>col1</th>
      <td>1.000000</td>
      <td>-0.508391</td>
    </tr>
    <tr>
      <th>col3</th>
      <td>-0.508391</td>
      <td>1.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 절대적 x, 참고용
# 0~0.2
# 0.2~0.5
# 0.5~0.7
# 0.7~1.0
```


```python
# df1의 col1과 df2의 col2간의 상관관계
df1.corrwith(df2)
```




    col1   -1.0
    col2    NaN
    col3    NaN
    dtype: float64




```python
df1.corrwith(df2, method='pearson')
```




    col1   -1.0
    col2    NaN
    col3    NaN
    dtype: float64




```python
df1.corrwith(df2, method='pearson', drop=True)
```




    col1   -1.0
    dtype: float64




```python
'''
표본에서 구한 상관계수
동일한 모집단에서 추출된 표본에 따라 상관계수도 달라짐
=> 상관계수에 대해 통계적 검증(p-value) => p-value < 0.05 인 경우에는 '통계적으로 유의미하다'
'''
```


```python
x = [8, 3, 6, 6, 9, 4, 3, 9, 3, 4]
y = [6, 2, 4, 6, 10, 5, 1, 8, 4, 5]
```


```python
ss.pearsonr(x,y) # ss.pearsonr(x,y).correlation
np.corrcoef(x, y)[0, 1]
```




    0.862517279213578




```python
ss.pearsonr(x,y) # statistic, pvalue, 상관계수 : 0.86, pvalue=0.001
```




    (0.8625172792135781, 0.0013196539141999974)




```python
# 연속형 변수, 정규분포(이상치가 거의 없음), 선형관계
# 가설
# 귀무가설 : 기존의 입장(H0)
# 대립가설 : 귀무가설의 상반된 입장(H1)

# 가설검정
# 1) 귀무/대립가설 수립
# 2) 표분추출, 확률실험
# 3) 유의수준 설정 -> 의사결정 기준

# 남학생들의 평균 성적이 여학생들보다 높을 것이다(가정)
# 귀무가설 : 일반적인 사람들이 알고 있는 통념
# - 모집단이 어떤 특징을 가질 것으로 여겨지는 가설, 실험을 통해 기각하고자 하는 가설
# - 남학생들의 평균 성적이 여학생들보다 낮거나 같다
# 대립가설 : 일반적인 사람들이 알고 있는 통념에 반하는 새로운 주
# - 귀무가설의 반대되는 가설, 실험을 통해 귀무가설이 틀리다고 증명해야 하는 가설
# - 남학생들의 평균 성적이 여학생들보다 높다

# 귀무가설을 먼저 수립하고 이것을 기각할 수 있는 증거를 찾아내고, 주장하고 싶은 가설인 대립가설을 채택

# 상관계수에서의 귀무가설이 '상관계수가 0이다'(상관관계가 없다)
# 대립가설은 '상관계수가 0이 아니다'(상관관계가 있다)

# p-value는 모집단에서 상관계수가 0일때, 표본에 대한 상관계수(0.86)보다 더 극단적인 상관계수가 관찰된 확률

```


```python
# 유클리디안 거리
```


```python
# 표준화, 정규화
# 표준화 : 평균이 0, 표준편차가 1인 표준정규분포로 표준화하는 것
```


```python
data = np.random.randint(30, size=(6, 5))
data
```




    array([[17, 23,  6, 19, 27],
           [10,  4,  5, 15, 12],
           [ 6, 27,  4,  1, 28],
           [14, 25, 25, 29, 29],
           [ 7, 12,  9, 22, 23],
           [ 5, 11,  5,  5,  8]])




```python
# 표준화값=(각 데이터 - 데이터평균)# 편차 / 표준편차 
```


```python
np.mean(data)
np.mean(data, axis=0)
```




    array([ 9.83333333, 17.        ,  9.        , 15.16666667, 21.16666667])




```python
(data - np.mean(data, axis=0)) / np.std(data, axis=0) # 표준화값
```




    array([[ 1.63816953,  0.70874931, -0.40951418,  0.39791435,  0.71191758],
           [ 0.03809697, -1.5356235 , -0.54601891, -0.01730062, -1.11872763],
           [-0.87623022,  1.18124885, -0.68252363, -1.47055302,  0.8339606 ],
           [ 0.95242415,  0.94499908,  2.18407562,  1.43595177,  0.95600361],
           [-0.64764842, -0.59062442,  0.        ,  0.70932558,  0.22374553],
           [-1.10481201, -0.70874931, -0.54601891, -1.05533805, -1.60689969]])




```python
ss.zscore(data)
```




    array([[ 1.63816953,  0.70874931, -0.40951418,  0.39791435,  0.71191758],
           [ 0.03809697, -1.5356235 , -0.54601891, -0.01730062, -1.11872763],
           [-0.87623022,  1.18124885, -0.68252363, -1.47055302,  0.8339606 ],
           [ 0.95242415,  0.94499908,  2.18407562,  1.43595177,  0.95600361],
           [-0.64764842, -0.59062442,  0.        ,  0.70932558,  0.22374553],
           [-1.10481201, -0.70874931, -0.54601891, -1.05533805, -1.60689969]])




```python
from sklearn.preprocessing import StandardScaler
```


```python
StandardScaler().fit_transform(data)
```




    array([[ 1.63816953,  0.70874931, -0.40951418,  0.39791435,  0.71191758],
           [ 0.03809697, -1.5356235 , -0.54601891, -0.01730062, -1.11872763],
           [-0.87623022,  1.18124885, -0.68252363, -1.47055302,  0.8339606 ],
           [ 0.95242415,  0.94499908,  2.18407562,  1.43595177,  0.95600361],
           [-0.64764842, -0.59062442,  0.        ,  0.70932558,  0.22374553],
           [-1.10481201, -0.70874931, -0.54601891, -1.05533805, -1.60689969]])




```python
# 평균값은 이상치에 민감
# 원본 데이터 -> 이상치 검색 -> 제거 -> 정제된 데이터의 표준화
# ex) 
# 근로자 연봉 데이터 -> 극단 고액/소액 연봉 검색 -> 제거 -> 정제된 연봉 데이터의 표준화
# 평균값 대신에 중위수로 대체

# 표준화(StandardScaler) : (data-mean) / std
# 표준화(RobustScaler, 극단값에 강인함) : (data-median) / IQR
```


```python
from sklearn.preprocessing import StandardScaler, RobustScaler
```


```python
mu, sigma = 10, 2
```


```python
x = mu + sigma*np.random.randn(100)
```


```python
plt.hist(x)
```




    (array([ 1.,  5.,  7., 13., 19., 21., 20.,  8.,  4.,  2.]),
     array([ 4.09709936,  5.30369489,  6.51029042,  7.71688596,  8.92348149,
            10.13007702, 11.33667255, 12.54326808, 13.74986361, 14.95645914,
            16.16305468]),
     <BarContainer object of 10 artists>)




    
![png](output_60_1.png)
    



```python
x[98:100]=100 # 극단치를 임의로 저장
```


```python
x
```




    array([  6.75367431,   8.6916238 ,  13.13013887,  11.50865573,
            10.03882296,   9.61072092,  11.67471176,  13.13619522,
             9.93958823,  11.13623581,   8.15965253,  11.6312179 ,
             5.78852807,   8.78954742,  11.81411717,   7.37237436,
            14.46355935,  11.96894169,  11.29380781,   7.84239038,
             7.33517507,   9.02174574,   8.58718621,  14.61151688,
            11.57381765,  12.81300819,   7.82529612,  10.14595888,
             8.28886658,  13.00003026,  12.22301317,   9.23146048,
            10.66171318,   8.30263825,   7.26707257,   9.31796017,
             6.36345329,   7.16732203,  11.98722374,   9.98337737,
            11.41480681,  10.50244595,  10.74286547,   9.38327124,
             8.53514829,  11.7904759 ,   8.68500554,   9.49484341,
            10.2405496 ,  10.2590472 ,  12.03551281,   9.54267053,
            10.22167387,   6.92138011,  10.29276575,  11.00541803,
            13.79810115,  12.17768567,  10.91864395,  10.78675616,
             8.17464197,   9.162774  ,  12.0361553 ,  12.5719665 ,
             9.28299504,   6.42276888,  12.93750518,  13.34638551,
            12.2369531 ,   5.47085639,  11.13599622,   4.09709936,
             6.35389177,  10.14602691,  12.37774515,   9.88705379,
            16.16305468,   8.06304598,   9.34007069,   9.52011811,
            11.11980708,  14.45338105,  12.84067804,  10.52270565,
            10.12475464,  11.58051493,   8.33714478,  10.74561586,
             9.8419679 ,  11.61138035,   7.67127646,  15.88183723,
             9.28588925,  11.42286331,  11.66328023,  10.92234116,
             9.56584995,  12.0900795 , 100.        , 100.        ])




```python
np.mean(x)
```




    12.07609879421928




```python
np.std(x)
```




    12.758986534220911




```python
plt.hist(x)
```




    (array([92.,  6.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  2.]),
     array([  4.09709936,  13.68738942,  23.27767949,  32.86796955,
             42.45825962,  52.04854968,  61.63883974,  71.22912981,
             80.81941987,  90.40970994, 100.        ]),
     <BarContainer object of 10 artists>)




    
![png](output_65_1.png)
    



```python
pd.DataFrame(x).describe()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
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
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>100.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>12.076099</td>
    </tr>
    <tr>
      <th>std</th>
      <td>12.823264</td>
    </tr>
    <tr>
      <th>min</th>
      <td>4.097099</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>8.765067</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>10.275906</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>11.852823</td>
    </tr>
    <tr>
      <th>max</th>
      <td>100.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
q1 = pd.DataFrame(x).describe().iloc[4]
q3 = pd.DataFrame(x).describe().iloc[6]
```


```python
iqr = q3-q1
```


```python
q3 + iqr*1.5 # high boundary
```




    0    16.484458
    dtype: float64




```python
q1 - iqr*1.5 # low boundary
# 정상범위 : 4.13~16.48
```




    0    4.133431
    dtype: float64




```python
# outliers = 
# (q3 + iqr*1.5) < data
# or 
# (q1 - iqr*1.5) > data
```


```python
x[((q3 + iqr*1.5).values >= x) & ((q1 - iqr*1.5).values < x)  ]
x[((q3 + iqr*1.5).values >= x) & ((q1 - iqr*1.5).values < x)  ].mean()
```




    10.345492577956588




```python
x
```




    array([  6.75367431,   8.6916238 ,  13.13013887,  11.50865573,
            10.03882296,   9.61072092,  11.67471176,  13.13619522,
             9.93958823,  11.13623581,   8.15965253,  11.6312179 ,
             5.78852807,   8.78954742,  11.81411717,   7.37237436,
            14.46355935,  11.96894169,  11.29380781,   7.84239038,
             7.33517507,   9.02174574,   8.58718621,  14.61151688,
            11.57381765,  12.81300819,   7.82529612,  10.14595888,
             8.28886658,  13.00003026,  12.22301317,   9.23146048,
            10.66171318,   8.30263825,   7.26707257,   9.31796017,
             6.36345329,   7.16732203,  11.98722374,   9.98337737,
            11.41480681,  10.50244595,  10.74286547,   9.38327124,
             8.53514829,  11.7904759 ,   8.68500554,   9.49484341,
            10.2405496 ,  10.2590472 ,  12.03551281,   9.54267053,
            10.22167387,   6.92138011,  10.29276575,  11.00541803,
            13.79810115,  12.17768567,  10.91864395,  10.78675616,
             8.17464197,   9.162774  ,  12.0361553 ,  12.5719665 ,
             9.28299504,   6.42276888,  12.93750518,  13.34638551,
            12.2369531 ,   5.47085639,  11.13599622,   4.09709936,
             6.35389177,  10.14602691,  12.37774515,   9.88705379,
            16.16305468,   8.06304598,   9.34007069,   9.52011811,
            11.11980708,  14.45338105,  12.84067804,  10.52270565,
            10.12475464,  11.58051493,   8.33714478,  10.74561586,
             9.8419679 ,  11.61138035,   7.67127646,  15.88183723,
             9.28588925,  11.42286331,  11.66328023,  10.92234116,
             9.56584995,  12.0900795 , 100.        , 100.        ])




```python
# RobustScaler().fit_transform(x)
RobustScaler().fit_transform(pd.DataFrame(x))
```




    array([[-1.14070907e+00],
           [-5.13085320e-01],
           [ 9.24370862e-01],
           [ 3.99237811e-01],
           [-7.67817976e-02],
           [-2.15426797e-01],
           [ 4.53016669e-01],
           [ 9.26332271e-01],
           [-1.08919927e-01],
           [ 2.78626004e-01],
           [-6.85369378e-01],
           [ 4.38930758e-01],
           [-1.45328105e+00],
           [-4.81371803e-01],
           [ 4.98164462e-01],
           [-9.40337054e-01],
           [ 1.35621203e+00],
           [ 5.48305885e-01],
           [ 3.29657225e-01],
           [-7.88117805e-01],
           [-9.52384404e-01],
           [-4.06172125e-01],
           [-5.46908446e-01],
           [ 1.40412951e+00],
           [ 4.20341130e-01],
           [ 8.21665012e-01],
           [-7.93653947e-01],
           [-4.20847899e-02],
           [-6.43522155e-01],
           [ 8.82233925e-01],
           [ 6.30589401e-01],
           [-3.38253971e-01],
           [ 1.24947246e-01],
           [-6.39062065e-01],
           [-9.74440059e-01],
           [-3.10240207e-01],
           [-1.26708593e+00],
           [-1.00674524e+00],
           [ 5.54226706e-01],
           [-9.47383892e-02],
           [ 3.68843927e-01],
           [ 7.33670074e-02],
           [ 1.51229202e-01],
           [-2.89088583e-01],
           [-5.63761431e-01],
           [ 4.90508007e-01],
           [-5.15228708e-01],
           [-2.52954853e-01],
           [-1.14506652e-02],
           [-5.46004014e-03],
           [ 5.69865589e-01],
           [-2.37465575e-01],
           [-1.75637556e-02],
           [-1.08639592e+00],
           [ 5.46004014e-03],
           [ 2.36259396e-01],
           [ 1.14069693e+00],
           [ 6.15909650e-01],
           [ 2.08156770e-01],
           [ 1.65443630e-01],
           [-6.80514901e-01],
           [-3.60498754e-01],
           [ 5.70073666e-01],
           [ 7.43601323e-01],
           [-3.21564005e-01],
           [-1.24787601e+00],
           [ 8.61984572e-01],
           [ 9.94404435e-01],
           [ 6.35103982e-01],
           [-1.55616210e+00],
           [ 2.78548412e-01],
           [-2.00106665e+00],
           [-1.27018252e+00],
           [-4.20627575e-02],
           [ 6.80700854e-01],
           [-1.25933715e-01],
           [ 1.90661008e+00],
           [-7.16656346e-01],
           [-3.03079501e-01],
           [-2.44769396e-01],
           [ 2.73305400e-01],
           [ 1.35291568e+00],
           [ 8.30626163e-01],
           [ 7.99283077e-02],
           [-4.89519892e-02],
           [ 4.22510110e-01],
           [-6.27886788e-01],
           [ 1.52119944e-01],
           [-1.40535219e-01],
           [ 4.32506175e-01],
           [-8.43534709e-01],
           [ 1.81553508e+00],
           [-3.20626686e-01],
           [ 3.71453102e-01],
           [ 4.49314456e-01],
           [ 2.09354145e-01],
           [-2.29958696e-01],
           [ 5.87537540e-01],
           [ 2.90580185e+01],
           [ 2.90580185e+01]])




```python
from sklearn.preprocessing import MinMaxScaler
# 0~1 사이로 변환

```


```python
data
```




    array([[17, 23,  6, 19, 27],
           [10,  4,  5, 15, 12],
           [ 6, 27,  4,  1, 28],
           [14, 25, 25, 29, 29],
           [ 7, 12,  9, 22, 23],
           [ 5, 11,  5,  5,  8]])




```python
# 0 <= (각 열 데이터 - 각 열 최소값) / (각 열 최대값 - 각 열 최소값) <= 1
# (17-5) / (17-5)
# (10-5) / (17-5)
# ...
# (5-5) / (17-5)

(data - data.min(axis=0))/ (data.max(axis=0) - data.min(axis=0))
```




    array([[1.        , 0.82608696, 0.0952381 , 0.64285714, 0.9047619 ],
           [0.41666667, 0.        , 0.04761905, 0.5       , 0.19047619],
           [0.08333333, 1.        , 0.        , 0.        , 0.95238095],
           [0.75      , 0.91304348, 1.        , 1.        , 1.        ],
           [0.16666667, 0.34782609, 0.23809524, 0.75      , 0.71428571],
           [0.        , 0.30434783, 0.04761905, 0.14285714, 0.        ]])




```python
mms = MinMaxScaler()
```


```python
mms.fit_transform(data)
```




    array([[1.        , 0.82608696, 0.0952381 , 0.64285714, 0.9047619 ],
           [0.41666667, 0.        , 0.04761905, 0.5       , 0.19047619],
           [0.08333333, 1.        , 0.        , 0.        , 0.95238095],
           [0.75      , 0.91304348, 1.        , 1.        , 1.        ],
           [0.16666667, 0.34782609, 0.23809524, 0.75      , 0.71428571],
           [0.        , 0.30434783, 0.04761905, 0.14285714, 0.        ]])




```python
from sklearn.preprocessing import Binarizer
```


```python
data
```




    array([[17, 23,  6, 19, 27],
           [10,  4,  5, 15, 12],
           [ 6, 27,  4,  1, 28],
           [14, 25, 25, 29, 29],
           [ 7, 12,  9, 22, 23],
           [ 5, 11,  5,  5,  8]])




```python
bnr = Binarizer(threshold=10) # threshold 보다 작거나 같으면 0, 크면 1, 데이터를 2진화
```


```python
bnr.transform(data)
```




    array([[1, 1, 0, 1, 1],
           [0, 0, 0, 1, 1],
           [0, 1, 0, 0, 1],
           [1, 1, 1, 1, 1],
           [0, 1, 0, 1, 1],
           [0, 1, 0, 0, 0]])




```python
# Binarizer : 연속형 변수 -> 0/1
# OneHotEncoder : 범주형 변수 -> 0/1
```


```python
from sklearn.preprocessing import OneHotEncoder
```


```python
train = np.array([[0, 0, 0],
               [0, 1, 1],
               [0, 2, 2],
               [1, 0, 3],
               [1, 1, 4]])
train
# 성별(0:M, 1:F), 연령(20:0, 30:1, 40:2), 성적(0:S, 4:D)
```




    array([[0, 0, 0],
           [0, 1, 1],
           [0, 2, 2],
           [1, 0, 3],
           [1, 1, 4]])




```python
ohe = OneHotEncoder()
```


```python
# ohe.fit(데이터변수) # 범주형 변수 -> 이항변수
ohe.fit(train)
```




    OneHotEncoder()




```python
ohe.categories_
```




    [array([0, 1]), array([0, 1, 2]), array([0, 1, 2, 3, 4])]




```python
ohe.n_features_in_
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    ~\AppData\Local\Temp/ipykernel_4980/3171561689.py in <module>
    ----> 1 ohe.n_features_in_
    

    AttributeError: 'OneHotEncoder' object has no attribute 'n_features_in_'



```python
ohe.transform(train)
```




    <5x10 sparse matrix of type '<class 'numpy.float64'>'
    	with 15 stored elements in Compressed Sparse Row format>




```python
ohe.transform(train).toarray() 
```




    array([[1., 0., 1., 0., 0., 1., 0., 0., 0., 0.],
           [1., 0., 0., 1., 0., 0., 1., 0., 0., 0.],
           [1., 0., 0., 0., 1., 0., 0., 1., 0., 0.],
           [0., 1., 1., 0., 0., 0., 0., 0., 1., 0.],
           [0., 1., 0., 1., 0., 0., 0., 0., 0., 1.]])




```python
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
# std / min, max
# 1. 표준화,정규화를 수행하시오.
# 나이, 운임(fare)
# 2. parch + sibsp = family 열 추가
# 3. family 열을 5명 기준으로 1과 0으로 변환
# 4. fare와 age 열 간의 상관관계
# 5. fare와 survived 열 간의 상관관계
# 6. embark_town에서 첫번째 글자만 추출하여 embark_town_name에 저장
# 캐글 가입, remind
```


```python
1. 표준화,정규화를 수행하시오.
```


```python
ss.zscore(titanic[['age', 'fare']]) # 표준화
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>age</th>
      <th>fare</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>NaN</td>
      <td>-0.502445</td>
    </tr>
    <tr>
      <th>1</th>
      <td>NaN</td>
      <td>0.786845</td>
    </tr>
    <tr>
      <th>2</th>
      <td>NaN</td>
      <td>-0.488854</td>
    </tr>
    <tr>
      <th>3</th>
      <td>NaN</td>
      <td>0.420730</td>
    </tr>
    <tr>
      <th>4</th>
      <td>NaN</td>
      <td>-0.486337</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>886</th>
      <td>NaN</td>
      <td>-0.386671</td>
    </tr>
    <tr>
      <th>887</th>
      <td>NaN</td>
      <td>-0.044381</td>
    </tr>
    <tr>
      <th>888</th>
      <td>NaN</td>
      <td>-0.176263</td>
    </tr>
    <tr>
      <th>889</th>
      <td>NaN</td>
      <td>-0.044381</td>
    </tr>
    <tr>
      <th>890</th>
      <td>NaN</td>
      <td>-0.492378</td>
    </tr>
  </tbody>
</table>
<p>891 rows × 2 columns</p>
</div>




```python
from sklearn.preprocessing import MinMaxScaler
# 0~1 사이로 변환
mms = MinMaxScaler()
```


```python
mms.fit_transform(titanic[['age', 'fare']]) # 정규화
```




    array([[0.27117366, 0.01415106],
           [0.4722292 , 0.13913574],
           [0.32143755, 0.01546857],
           ...,
           [       nan, 0.04577135],
           [0.32143755, 0.0585561 ],
           [0.39683338, 0.01512699]])




```python
2. parch + sibsp = family 열 추가
```


```python
titanic['family'] = titanic['parch'] + titanic['sibsp']
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
      <th>family</th>
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
      <td>1</td>
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
      <td>1</td>
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
      <td>0</td>
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
      <td>1</td>
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
      <td>0</td>
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
      <td>0</td>
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
      <td>0</td>
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
      <td>3</td>
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
      <td>0</td>
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
      <td>0</td>
    </tr>
  </tbody>
</table>
<p>891 rows × 16 columns</p>
</div>




```python
3. family 열을 5명 기준으로 1과 0으로 변환
```


```python
titanic['family']
```




    0      1
    1      1
    2      0
    3      1
    4      0
          ..
    886    0
    887    0
    888    3
    889    0
    890    0
    Name: family, Length: 891, dtype: int64




```python
bnr = Binarizer(threshold=5)
```


```python
bnr.transform(pd.DataFrame(titanic['family']))
```




    array([[0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [1],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [1],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [1],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [1],
           [0],
           [0],
           [1],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [1],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [1],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [1],
           [0],
           [1],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [1],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [1],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [1],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [1],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [1],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [1],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [1],
           [1],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [1],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [1],
           [0],
           [0],
           [0],
           [0],
           [1],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [1],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [1],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [1],
           [0],
           [0],
           [0],
           [1],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [1],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0]], dtype=int64)




```python
4. fare와 age 열 간의 상관관계
```


```python
titanic[['fare', 'age']]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>fare</th>
      <th>age</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>7.2500</td>
      <td>22.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>71.2833</td>
      <td>38.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>7.9250</td>
      <td>26.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>53.1000</td>
      <td>35.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>8.0500</td>
      <td>35.0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>886</th>
      <td>13.0000</td>
      <td>27.0</td>
    </tr>
    <tr>
      <th>887</th>
      <td>30.0000</td>
      <td>19.0</td>
    </tr>
    <tr>
      <th>888</th>
      <td>23.4500</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>889</th>
      <td>30.0000</td>
      <td>26.0</td>
    </tr>
    <tr>
      <th>890</th>
      <td>7.7500</td>
      <td>32.0</td>
    </tr>
  </tbody>
</table>
<p>891 rows × 2 columns</p>
</div>




```python
titanic[['fare','age']].cov()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>fare</th>
      <th>age</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>fare</th>
      <td>2469.436846</td>
      <td>73.849030</td>
    </tr>
    <tr>
      <th>age</th>
      <td>73.849030</td>
      <td>211.019125</td>
    </tr>
  </tbody>
</table>
</div>




```python
titanic[['fare','age']].corr()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>fare</th>
      <th>age</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>fare</th>
      <td>1.000000</td>
      <td>0.096067</td>
    </tr>
    <tr>
      <th>age</th>
      <td>0.096067</td>
      <td>1.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
5. fare와 survived 열 간의 상관관계
```


```python
titanic[['fare','survived']].cov()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>fare</th>
      <th>survived</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>fare</th>
      <td>2469.436846</td>
      <td>6.221787</td>
    </tr>
    <tr>
      <th>survived</th>
      <td>6.221787</td>
      <td>0.236772</td>
    </tr>
  </tbody>
</table>
</div>




```python
titanic[['fare','survived']].corr()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>fare</th>
      <th>survived</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>fare</th>
      <td>1.000000</td>
      <td>0.257307</td>
    </tr>
    <tr>
      <th>survived</th>
      <td>0.257307</td>
      <td>1.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
embark_town에서 첫번째 글자만 추출하여 embark_town_name에 저장
```


```python
titanic['embark_town_name'] = titanic['embark_town'].str[0]
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
      <th>family</th>
      <th>embark_town_name</th>
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
      <td>1</td>
      <td>S</td>
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
      <td>1</td>
      <td>C</td>
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
      <td>0</td>
      <td>S</td>
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
      <td>1</td>
      <td>S</td>
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
      <td>0</td>
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
      <td>0</td>
      <td>S</td>
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
      <td>0</td>
      <td>S</td>
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
      <td>3</td>
      <td>S</td>
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
      <td>0</td>
      <td>C</td>
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
      <td>0</td>
      <td>Q</td>
    </tr>
  </tbody>
</table>
<p>891 rows × 17 columns</p>
</div>




```python

```


```python

```


```python

```
