```python
import numpy as np
```


```python
arr = np.arange(12).reshape(3,4)
arr
```




    array([[ 0,  1,  2,  3],
           [ 4,  5,  6,  7],
           [ 8,  9, 10, 11]])




```python
arr.reshape(12)
arr.reshape(3*4)
```




    array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11])




```python
arr.flatten()
arr.ravel()
```




    array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11])




```python

```


```python

```


```python
x = np.arange(3)
x # 1차원 배열
```




    array([0, 1, 2])




```python
x.reshape(1,3)
x # 2차원 배열(행렬) (1*3)
```




    array([0, 1, 2])




```python
x.reshape(3, 1)
x # 2차원 배열(행렬) )
```




    array([[0],
           [1],
           [2]])




```python
x = np.arange(3)
x
```




    array([0, 1, 2])




```python
x[ : , np.newaxis].shape # (3,1)
x[ : , np.newaxis]
```




    array([[0],
           [1],
           [2]])




```python
arr = arr.flatten()
arr
```




    array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11])




```python
for i in arr:
    print(i)
```

    0
    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    


```python
arr
```




    array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11])




```python
arr = arr.reshape(4,3)
arr
```




    array([[ 0,  1,  2],
           [ 3,  4,  5],
           [ 6,  7,  8],
           [ 9, 10, 11]])




```python
for i in arr:
    print(i)
```

    [0 1 2]
    [3 4 5]
    [6 7 8]
    [ 9 10 11]
    


```python
for i in arr:
    for j in i:
        print(j)
```

    0
    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    


```python
arr
```




    array([[ 0,  1,  2],
           [ 3,  4,  5],
           [ 6,  7,  8],
           [ 9, 10, 11]])




```python
arr = arr.reshape(2,3,2)
arr
```




    array([[[ 0,  1],
            [ 2,  3],
            [ 4,  5]],
    
           [[ 6,  7],
            [ 8,  9],
            [10, 11]]])




```python
for i in arr:
    for j in i:
        for k in j:
            print(k)
```

    0
    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    


```python
# 파이썬 : 리스트, 튜플, 딕셔너리, 집합
# 넘파이 : 배열(ndarray)
# 판다스 : 데이터프레임, 시리즈
# 데이터 수집(크롤링, db) -> 전처리(넘파이, 판다스) -> 분석(판다스)
# matplotlib, seaborn, plotly, tableau ...
```


```python
a1 = np.ones((2,3))
a1
```




    array([[1., 1., 1.],
           [1., 1., 1.]])




```python
a2 = np.zeros((2,2))
a2
```




    array([[0., 0.],
           [0., 0.]])




```python
np.hstack([a1, a2]) # 행이 같지않으면 error
```




    array([[1., 1., 1., 0., 0.],
           [1., 1., 1., 0., 0.]])




```python
a1 = np.ones((2,3))
a2 = np.zeros((3,3))
np.vstack([a1,a2]) # 열이 같지 않으면 error
```




    array([[1., 1., 1.],
           [1., 1., 1.],
           [0., 0., 0.],
           [0., 0., 0.],
           [0., 0., 0.]])




```python
# dstack(depth) : 행, 열이 아닌 깊이 방향으로 배열을 합침
```


```python
a1 = np.ones((3,4))
a2 = np.zeros((3,4))
```


```python
a1
```




    array([[1., 1., 1., 1.],
           [1., 1., 1., 1.],
           [1., 1., 1., 1.]])




```python
a2
```




    array([[0., 0., 0., 0.],
           [0., 0., 0., 0.],
           [0., 0., 0., 0.]])




```python
# 3*4*2
np.dstack([a1,a2])
np.dstack([a1,a2]).shape
# dstack([a1,a2]) => 2개의 3*4배열 => 1개의 3*4*2 배열
```




    (3, 4, 2)




```python
# dstack은 잘 사용되지 않으며, stack 주로 사용
```


```python
np.stack([a1, a2]) # axis(축)를 지정, 기본값 0
np.stack([a1, a2], axis=0)
```




    array([[[1., 1., 1., 1.],
            [1., 1., 1., 1.],
            [1., 1., 1., 1.]],
    
           [[0., 0., 0., 0.],
            [0., 0., 0., 0.],
            [0., 0., 0., 0.]]])




```python
np.stack([a1, a2]).shape
# 2개 3*4 => 1개의 2*3*4
```




    (2, 3, 4)




```python
r1 = np.stack([a1,a2], axis=1)
r1.shape
```




    (3, 2, 4)




```python
r2 = np.stack([a1,a2], axis=2)
r2.shape
```




    (3, 4, 2)




```python
# 두 행렬 (3,4),(3,4)를 stack 함수로 연결할 때 axis 값에 따라 shape이 달라짐
# axis = 0 => 2,3,4
# axis = 1 => 3,2,4
# axis = 2 => 3,4,2 (dstack과 같음)
```


```python
a1 = np.array([1,2,3])
a2 = np.array([11,12,13])
```


```python
# array[1,2,3,11,12,13]
np.hstack([a1,a2])
```




    array([ 1,  2,  3, 11, 12, 13])




```python
np.r_[a1,a2] # 특별한 함수, 인덱서 함수, r(row)
```




    array([ 1,  2,  3, 11, 12, 13])




```python
np.c_[a1,a2] 특별한 함수, 인덱서 함수, c(column)
# np.c_[a1,a2] == np.vstack([a1,a2]).T
```




    array([[ 1, 11],
           [ 2, 12],
           [ 3, 13]])




```python
a1 = np.array([1,2,3])
a2 = np.array([11,12,13])
np.vstack([a1,a2])
```




    array([[ 1,  2,  3],
           [11, 12, 13]])




```python
# tile : 동일한 배열을 반복해서 연결
arr = np.arange(6).reshape(2,3)
arr
```




    array([[0, 1, 2],
           [3, 4, 5]])




```python
np.tile(arr,3) # 좌우 방향으로 3번 반복
```




    array([[0, 1, 2, 0, 1, 2, 0, 1, 2],
           [3, 4, 5, 3, 4, 5, 3, 4, 5]])




```python
np.tile(arr, (3, 1)) # 위아래로 3번 반복, 좌우 방향으로 1번 반복
```




    array([[0, 1, 2],
           [3, 4, 5],
           [0, 1, 2],
           [3, 4, 5],
           [0, 1, 2],
           [3, 4, 5]])




```python
np.tile(arr, (3, 2)) # 위아래로 3번 반복, 좌우 방향으로 2번 반복
```




    array([[0, 1, 2, 0, 1, 2],
           [3, 4, 5, 3, 4, 5],
           [0, 1, 2, 0, 1, 2],
           [3, 4, 5, 3, 4, 5],
           [0, 1, 2, 0, 1, 2],
           [3, 4, 5, 3, 4, 5]])




```python
# [ [ 0., 0., 0., 1., 1,],
#   [ 0., 0., 0., 1., 1,],
#   [ 0., 0., 0., 1., 1,] ]
arr = np.array([0, 0, 0, 1, 1])
np.tile(arr, (3,1))
```




    array([[0, 0, 0, 1, 1],
           [0, 0, 0, 1, 1],
           [0, 0, 0, 1, 1]])




```python
arr1=np.ones((3,2))

arr2=np.zeros((3,3))

np.hstack([arr2,arr1])
```




    array([[0., 0., 0., 1., 1.],
           [0., 0., 0., 1., 1.],
           [0., 0., 0., 1., 1.]])




```python
x = np.arange(3)
y = np.arange(5)
# (x,y) = (0,0),(0,1), ... (2,4)
```


```python
x,y = np.meshgrid(x,y)
```


```python
x
```




    array([[0, 1, 2],
           [0, 1, 2],
           [0, 1, 2],
           [0, 1, 2],
           [0, 1, 2]])




```python
y
```




    array([[0, 0, 0],
           [1, 1, 1],
           [2, 2, 2],
           [3, 3, 3],
           [4, 4, 4]])




```python
[list(zip(x,y)) for x,y in zip(x,y)]
```




    [[(0, 0), (1, 0), (2, 0)],
     [(0, 1), (1, 1), (2, 1)],
     [(0, 2), (1, 2), (2, 2)],
     [(0, 3), (1, 3), (2, 3)],
     [(0, 4), (1, 4), (2, 4)]]




```python
arr1 = np.array([1,2,3])
arr2 = np.array([11,21,31])
```


```python
np.concatenate([arr1,arr2]) # ((arr1,arr2))도 가능,결과 동일
```




    array([ 1,  2,  3, 11, 21, 31])




```python
# array([ [0,1,2,3,4,5],
#         [10,11,12,13,14,15],
#          ...
#         [50,51,52,53,54,55] ])
```


```python
arr1 = np.arange(6)
arr2 = [0,10,20,30,40,50] # np.arange(0,51,10)
x,y = np.meshgrid(arr1, arr2)
```


```python
x
y
x + y
```




    array([[ 0,  1,  2,  3,  4,  5],
           [10, 11, 12, 13, 14, 15],
           [20, 21, 22, 23, 24, 25],
           [30, 31, 32, 33, 34, 35],
           [40, 41, 42, 43, 44, 45],
           [50, 51, 52, 53, 54, 55]])




```python
arr = np.arange(6)
arr_f = [arr+i*10 for i in range(6)]
arr_f = np.array(arr_f)
arr_f
```




    array([[ 0,  1,  2,  3,  4,  5],
           [10, 11, 12, 13, 14, 15],
           [20, 21, 22, 23, 24, 25],
           [30, 31, 32, 33, 34, 35],
           [40, 41, 42, 43, 44, 45],
           [50, 51, 52, 53, 54, 55]])




```python
a = np.arange(1,5)
b = np.array([4,2,2,4])
```


```python
a
```




    array([1, 2, 3, 4])




```python
b
```




    array([4, 2, 2, 4])




```python
a >= b
```




    array([False,  True,  True,  True])




```python
np.all(a>=b) # 각 요소들을 일일히 비교하는게 아니라, 배열의 모든 요소에 대해 조건을 확인
```




    False




```python
# 벡터(행렬)끼리 연산하려면 크기가 동일해야 함
# 브로드캐스팅 : 벡터(행렬)의 크기가 다르더라도 연산이 가능하도록 크기를 동일하게 해주는 작업
# 벡터      스칼라
# 1                   11
# 2                   12
# 3     +     10   =  13
# 4                   14

```


```python
x = np.arange(1,5)
x
```




    array([1, 2, 3, 4])




```python
y = 10
```


```python
x + y
```




    array([11, 12, 13, 14])




```python
# 행렬         벡터
# 0 1 2         10
# 1 2 3    +    11
# 3 4 5         12
```


```python
# 행렬(2)      벡터(1) -> 행렬(2)
# 0 1 2         10 10 10    10 11 12
# 1 2 3    +    11 11 11  = ...
# 3 4 5         12 12 12
```


```python
# 행렬(2)      벡터(1) -> 행렬(2)
# 0 1 2        
# 1 2 3    +   [10 11 12] = ...
# 3 4 5      
```


```python
# 행렬(2)      벡터(1) -> 행렬(2)
# 0 1 2        [10 11 12]    
# 1 2 3    +   [10 11 12] = ...
# 3 4 5        [10 11 12]  
```


```python
x = np.arange(5)
x
```




    array([0, 1, 2, 3, 4])




```python
y = 1
```


```python
x+y
```




    array([1, 2, 3, 4, 5])




```python
y = np.ones_like(x)
y
```




    array([1, 1, 1, 1, 1])




```python
arr1 = np.arange(6)
arr2 = np.arange(0,56,10)
```


```python
# array([0, 1, 2],
#       [1, 2, 3],
#       [2, 3, 4],
#       [3, 4, 5],
#       [4, 5, 6])
```


```python
arr1 = np.arange(3)
arr2 = np.arange(5)
x, y = np.meshgrid(arr1, arr2)
x
```




    array([[0, 1, 2],
           [0, 1, 2],
           [0, 1, 2],
           [0, 1, 2],
           [0, 1, 2]])




```python
y
```




    array([[0, 0, 0],
           [1, 1, 1],
           [2, 2, 2],
           [3, 3, 3],
           [4, 4, 4]])




```python
x+y
```




    array([[0, 1, 2],
           [1, 2, 3],
           [2, 3, 4],
           [3, 4, 5],
           [4, 5, 6]])




```python
x = np.arange(3)
x
```




    array([0, 1, 2])




```python
y=np.arange(5).reshape(5,1)
y
```




    array([[0],
           [1],
           [2],
           [3],
           [4]])




```python
x+y
```




    array([[0, 1, 2],
           [1, 2, 3],
           [2, 3, 4],
           [3, 4, 5],
           [4, 5, 6]])




```python
arr = np.arange(3)
arr2 = [arr + i for i in range(5)]
arr2 = np.array(arr2)
arr2
```




    array([[0, 1, 2],
           [1, 2, 3],
           [2, 3, 4],
           [3, 4, 5],
           [4, 5, 6]])




```python
np.vstack([range(7)[i:i+3] for i in range(5)])
```




    array([[0, 1, 2],
           [1, 2, 3],
           [2, 3, 4],
           [3, 4, 5],
           [4, 5, 6]])




```python
# 1. 
# 지금까지 공부한 명령어를 사용하여 다음과 같은 배열을 다양한 방법으로 만드시오.
# - tile사용, tile 미사용,...
# array([[   0.,    0.,    0.,    1.,    1.],
#        [   0.,    0.,    0.,    1.,    1.],
#        [   0.,    0.,    0.,    1.,    1.],
#        [  10.,   20.,   30.,   40.,   50.],
#        [  60.,   70.,   80.,   90.,  100.],
#        [ 110.,  120.,  130.,  140.,  150.],
#        [   0.,    0.,    0.,    1.,    1.],
#        [   0.,    0.,    0.,    1.,    1.],
#        [   0.,    0.,    0.,    1.,    1.],
#        [  10.,   20.,   30.,   40.,   50.],
#        [  60.,   70.,   80.,   90.,  100.],
#        [ 110.,  120.,  130.,  140.,  150.]])
```


```python
arr1 = np.hstack([np.zeros((12, 3)), np.ones((12, 2))])

arr2 = np.arange(10, 151, 10).reshape(3, 5)
arr1[3:6, :], arr1[9:12, :] = arr2, arr2
arr1
```




    array([[  0.,   0.,   0.,   1.,   1.],
           [  0.,   0.,   0.,   1.,   1.],
           [  0.,   0.,   0.,   1.,   1.],
           [ 10.,  20.,  30.,  40.,  50.],
           [ 60.,  70.,  80.,  90., 100.],
           [110., 120., 130., 140., 150.],
           [  0.,   0.,   0.,   1.,   1.],
           [  0.,   0.,   0.,   1.,   1.],
           [  0.,   0.,   0.,   1.,   1.],
           [ 10.,  20.,  30.,  40.,  50.],
           [ 60.,  70.,  80.,  90., 100.],
           [110., 120., 130., 140., 150.]])




```python
# 2.  아래와 같은 구조의 배열을 생성하시오
# 1 2 3 4 5
# 10 9 8 7 6
# 11 12 13 14 15
# 20 19 18 17 16
# 21 22 23 24 25
x = np.arange(1,26).reshape(5,5)
y = np.array([i if i[0] % 2 != 0 else i[::-1] for i in x])
y
```




    array([[ 1,  2,  3,  4,  5],
           [10,  9,  8,  7,  6],
           [11, 12, 13, 14, 15],
           [20, 19, 18, 17, 16],
           [21, 22, 23, 24, 25]])




```python

```
