```python
import numpy as np
```


```python
arr = np.array([1,2,3,4])
arr
```




    array([1, 2, 3, 4])




```python
arr.dtype
```




    dtype('int32')




```python
type(arr) # arr 은 배열이고 arr에 저장되어 있는게 정수
```




    numpy.ndarray




```python
type(arr[0])
```




    numpy.int32




```python
arr = np.array(['APPLE', 'CHERRY', 'BANANA'])
arr.dtype # <U6 : unicode, 6은 최대크기(BANANA)
```




    dtype('<U6')




```python
arr = np.array([1,2,3], dtype=np.float64)
arr.dtype
```




    dtype('float64')




```python
arr = np.array([1,2,3], dtype=np.float16) # 16bit
arr.dtype
```




    dtype('float16')




```python
arr = np.array([1,2,3], dtype=np.int16) # 16bit
arr.dtype
```




    dtype('int16')




```python
arr = np.array([1,2,3], dtype=np.int8) # 8bit
arr.dtype
```




    dtype('int8')




```python
arr = np.array([1,2,3], dtype=np.float64)
arr.dtype
arr
```




    array([1., 2., 3.])




```python
arr = np.array([1,2,3], dtype='i1') # i바이트수
arr
```




    array([1, 2, 3], dtype=int8)




```python
arr = np.array([1,2,3])
arr
arr.dtype
```




    dtype('int32')




```python
farr = arr.astype(np.float32)
farr
```




    array([1., 2., 3.], dtype=float32)




```python
arr = np.array([1,2,3])
arr
```




    array([1, 2, 3])




```python
myList = [1,2,'3']
myList
```




    [1, 2, '3']




```python
type(myList)
type(myList[0])
type(myList[2])
```




    str




```python
imyList = [1,2,3]
cmyList = [1,2,'3']
```


```python
np.array(imyList)
```




    array([1, 2, 3])




```python
np.array(cmyList)
# 배열 : 동일한 타입(동일한 크기)의 데이터를 여러개 나열한 것
```




    array(['1', '2', '3'], dtype='<U11')




```python
arr1 = np.array(list(range(10, 14))).reshape(2,2)
arr2 = np.array(list(range(10, 14))).reshape(2,2)
```


```python
arr1
arr2
```




    array([[10, 11],
           [12, 13]])




```python
arr1-arr2 # 넘파이 배열은 요소간 연산 => 동일한 크기의 배열
```




    array([[0, 0],
           [0, 0]])




```python
arr1*2 # 숫자와 연산시 모든 항목에 동일한 연산
```




    array([[20, 22],
           [24, 26]])




```python
arr1*arr2 # 행렬의 곱셈(matrix multiply, matmul) x, 요소간 곱셈(element-wise product)
```




    array([[100, 121],
           [144, 169]])




```python
arr1 = np.array(list(range(10,14))).reshape(2,2)
arr1
```




    array([[10, 11],
           [12, 13]])




```python
arr2 = np.array(list(range(13,17))).reshape(2,2)
arr2
```




    array([[13, 14],
           [15, 16]])




```python
arr1>arr2
arr1>10
```




    array([[False,  True],
           [ True,  True]])




```python
arr1==arr2
```




    array([[False, False],
           [False, False]])




```python
~(arr1==arr2) # ~는 not 연산자
```




    array([[ True,  True],
           [ True,  True]])




```python
arr1 != arr2 # != : 같지 않다
```




    array([[ True,  True],
           [ True,  True]])




```python
arr1==arr2
~(arr1==arr2)
```




    array([[ True,  True],
           [ True,  True]])




```python
arr1!=arr2
~(arr1!=arr2)
```




    array([[False, False],
           [False, False]])




```python
(~(arr1==arr2)) | (~(arr1!=arr2))
#     행렬      OR       행렬    => 요소간 or 연산
# or 연산자는 둘 중 하나 이상이 True -> True
```




    array([[ True,  True],
           [ True,  True]])




```python
np.arange(8)
```




    array([0, 1, 2, 3, 4, 5, 6, 7])




```python
np.arange(8).reshape(4,2)
```




    array([[0, 1],
           [2, 3],
           [4, 5],
           [6, 7]])




```python
np.arange(8).reshape(2,2,2)
```




    array([[[0, 1],
            [2, 3]],
    
           [[4, 5],
            [6, 7]]])




```python
# 1~24까지의 값, 2*3*4 행렬
# arange, range
np.array(list(range(1,25))).reshape(2,3,4)
np.arange(1,25).reshape(2,3,4)
```




    array([[[ 1,  2,  3,  4],
            [ 5,  6,  7,  8],
            [ 9, 10, 11, 12]],
    
           [[13, 14, 15, 16],
            [17, 18, 19, 20],
            [21, 22, 23, 24]]])




```python
data = np.arange(200)
data
data2 = data.reshape(4,-1)
data2
```




    array([[  0,   1,   2,   3,   4,   5,   6,   7,   8,   9,  10,  11,  12,
             13,  14,  15,  16,  17,  18,  19,  20,  21,  22,  23,  24,  25,
             26,  27,  28,  29,  30,  31,  32,  33,  34,  35,  36,  37,  38,
             39,  40,  41,  42,  43,  44,  45,  46,  47,  48,  49],
           [ 50,  51,  52,  53,  54,  55,  56,  57,  58,  59,  60,  61,  62,
             63,  64,  65,  66,  67,  68,  69,  70,  71,  72,  73,  74,  75,
             76,  77,  78,  79,  80,  81,  82,  83,  84,  85,  86,  87,  88,
             89,  90,  91,  92,  93,  94,  95,  96,  97,  98,  99],
           [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112,
            113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125,
            126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138,
            139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149],
           [150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162,
            163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175,
            176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188,
            189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199]])




```python
data3 = data.reshape(-1, 10)
data3
```




    array([[  0,   1,   2,   3,   4,   5,   6,   7,   8,   9],
           [ 10,  11,  12,  13,  14,  15,  16,  17,  18,  19],
           [ 20,  21,  22,  23,  24,  25,  26,  27,  28,  29],
           [ 30,  31,  32,  33,  34,  35,  36,  37,  38,  39],
           [ 40,  41,  42,  43,  44,  45,  46,  47,  48,  49],
           [ 50,  51,  52,  53,  54,  55,  56,  57,  58,  59],
           [ 60,  61,  62,  63,  64,  65,  66,  67,  68,  69],
           [ 70,  71,  72,  73,  74,  75,  76,  77,  78,  79],
           [ 80,  81,  82,  83,  84,  85,  86,  87,  88,  89],
           [ 90,  91,  92,  93,  94,  95,  96,  97,  98,  99],
           [100, 101, 102, 103, 104, 105, 106, 107, 108, 109],
           [110, 111, 112, 113, 114, 115, 116, 117, 118, 119],
           [120, 121, 122, 123, 124, 125, 126, 127, 128, 129],
           [130, 131, 132, 133, 134, 135, 136, 137, 138, 139],
           [140, 141, 142, 143, 144, 145, 146, 147, 148, 149],
           [150, 151, 152, 153, 154, 155, 156, 157, 158, 159],
           [160, 161, 162, 163, 164, 165, 166, 167, 168, 169],
           [170, 171, 172, 173, 174, 175, 176, 177, 178, 179],
           [180, 181, 182, 183, 184, 185, 186, 187, 188, 189],
           [190, 191, 192, 193, 194, 195, 196, 197, 198, 199]])




```python
data.reshape(-1,5,10) # 4*5*10
data.reshape(4,-1,10)
```




    array([[[  0,   1,   2,   3,   4,   5,   6,   7,   8,   9],
            [ 10,  11,  12,  13,  14,  15,  16,  17,  18,  19],
            [ 20,  21,  22,  23,  24,  25,  26,  27,  28,  29],
            [ 30,  31,  32,  33,  34,  35,  36,  37,  38,  39],
            [ 40,  41,  42,  43,  44,  45,  46,  47,  48,  49]],
    
           [[ 50,  51,  52,  53,  54,  55,  56,  57,  58,  59],
            [ 60,  61,  62,  63,  64,  65,  66,  67,  68,  69],
            [ 70,  71,  72,  73,  74,  75,  76,  77,  78,  79],
            [ 80,  81,  82,  83,  84,  85,  86,  87,  88,  89],
            [ 90,  91,  92,  93,  94,  95,  96,  97,  98,  99]],
    
           [[100, 101, 102, 103, 104, 105, 106, 107, 108, 109],
            [110, 111, 112, 113, 114, 115, 116, 117, 118, 119],
            [120, 121, 122, 123, 124, 125, 126, 127, 128, 129],
            [130, 131, 132, 133, 134, 135, 136, 137, 138, 139],
            [140, 141, 142, 143, 144, 145, 146, 147, 148, 149]],
    
           [[150, 151, 152, 153, 154, 155, 156, 157, 158, 159],
            [160, 161, 162, 163, 164, 165, 166, 167, 168, 169],
            [170, 171, 172, 173, 174, 175, 176, 177, 178, 179],
            [180, 181, 182, 183, 184, 185, 186, 187, 188, 189],
            [190, 191, 192, 193, 194, 195, 196, 197, 198, 199]]])




```python
# 2차원 배열
# 10부터 시작하여 2씩 증가시킨 값으로 초기화
# shape은 3행 4열
np.arange(10,34,2).reshape(3,4)
```




    array([[10, 12, 14, 16],
           [18, 20, 22, 24],
           [26, 28, 30, 32]])




```python
# 불린참조(팬시)

arr = np.array([1,2,3,4])
idx = np.array([True,False,False,True])
```


```python
arr[idx]
```




    array([1, 4])




```python
np.min(arr)
np.max(arr)
```




    4




```python
(arr==np.min(arr)) | (arr==np.max(arr)) # 최소값, 최대값 위치에서 True
```




    array([ True, False, False,  True])




```python
arr[np.array([True, False, False, True])]
```




    array([1, 4])




```python
arr[(arr==np.min(arr)) | (arr==np.max(arr))]
```




    array([1, 4])




```python
# 11~20까지의 수가 저장된 배열 arr을 생성하시오.
arr = np.arange(11,21)
arr
```




    array([11, 12, 13, 14, 15, 16, 17, 18, 19, 20])




```python
arr % 2
```




    array([1, 0, 1, 0, 1, 0, 1, 0, 1, 0], dtype=int32)




```python
arr[arr % 2 == 0]
```




    array([12, 14, 16, 18, 20])




```python
arr[1]
# arr[1,3] error
arr[np.array([1,3])]
arr[np.array([1,3,5,7,9])]
arr[np.array([1,3,5,7,9,9,9,9,9])]
```




    array([12, 14, 16, 18, 20, 20, 20, 20, 20])




```python
idx = np.array([0,0,0,1,1,1,3,3,3])
idx
```




    array([0, 0, 0, 1, 1, 1, 3, 3, 3])




```python
arr
```




    array([11, 12, 13, 14, 15, 16, 17, 18, 19, 20])




```python
arr[idx]
```




    array([11, 11, 11, 12, 12, 12, 14, 14, 14])




```python
arr = np.arange(10, 40).reshape(5, -1)
arr
```




    array([[10, 11, 12, 13, 14, 15],
           [16, 17, 18, 19, 20, 21],
           [22, 23, 24, 25, 26, 27],
           [28, 29, 30, 31, 32, 33],
           [34, 35, 36, 37, 38, 39]])




```python
arr[:] # 전체행 추출
arr[:,:] # 전체행에 대해 전체열을 추출
arr[:,[True, True, True, False, False, False]]
```




    array([[10, 11, 12],
           [16, 17, 18],
           [22, 23, 24],
           [28, 29, 30],
           [34, 35, 36]])




```python
idx = np.array([True, True, True, False, False, False])
idx
```




    array([ True,  True,  True, False, False, False])




```python
arr[:,idx]
```




    array([[10, 11, 12],
           [16, 17, 18],
           [22, 23, 24],
           [28, 29, 30],
           [34, 35, 36]])




```python
arr
# arr에서 1(10~), 3(12~), 5(14~)번째 열을 출력하시오.
arr[:,[0,2,4]]
```




    array([[10, 12, 14],
           [16, 18, 20],
           [22, 24, 26],
           [28, 30, 32],
           [34, 36, 38]])




```python
idx = np.array([0,2,4])
idx
arr[:, idx]
```




    array([[10, 12, 14],
           [16, 18, 20],
           [22, 24, 26],
           [28, 30, 32],
           [34, 36, 38]])




```python
arr[:, np.array([0, 2, 4])]
arr[:, np.arange(0, 5, 2)]
```




    array([[10, 12, 14],
           [16, 18, 20],
           [22, 24, 26],
           [28, 30, 32],
           [34, 36, 38]])




```python
arr[:,[4,1,3,0]]
```




    array([[14, 11, 13, 10],
           [20, 17, 19, 16],
           [26, 23, 25, 22],
           [32, 29, 31, 28],
           [38, 35, 37, 34]])




```python
# arr에서 3번째행, 2번째행, 4번째행 순서로 데이터 추출하시오. arr[행, 열]
arr[[2,1,3]]
```




    array([[22, 23, 24, 25, 26, 27],
           [16, 17, 18, 19, 20, 21],
           [28, 29, 30, 31, 32, 33]])




```python
# 무한대(infinity) : np.inf
# 숫자아님(not a number) : np.nan
```


```python
np.array([1])/np.array([0])
np.log(0)
```

    C:\Users\ryun1\AppData\Local\Temp/ipykernel_35668/878147698.py:1: RuntimeWarning: divide by zero encountered in true_divide
      np.array([1])/np.array([0])
    C:\Users\ryun1\AppData\Local\Temp/ipykernel_35668/878147698.py:2: RuntimeWarning: divide by zero encountered in log
      np.log(0)
    




    -inf




```python
# 0/0
np.array([0])/np.array([0])
```

    C:\Users\ryun1\AppData\Local\Temp/ipykernel_35668/1436990704.py:2: RuntimeWarning: invalid value encountered in true_divide
      np.array([0])/np.array([0])
    




    array([nan])




```python
np.zeros(3)
```




    array([0., 0., 0.])




```python
np.zeros((3,2))
```




    array([[0., 0.],
           [0., 0.],
           [0., 0.]])




```python
np.zeros((3,2)).dtype
```




    dtype('float64')




```python
np.zeros((3,2), dtype='i')
```




    array([[0, 0],
           [0, 0],
           [0, 0]], dtype=int32)




```python
np.ones((3,2))
```




    array([[1., 1.],
           [1., 1.],
           [1., 1.]])




```python
arr = np.ones((3,2))*2
arr
```




    array([[2., 2.],
           [2., 2.],
           [2., 2.]])




```python
np.ones_like(arr)
```




    array([[1., 1.],
           [1., 1.],
           [1., 1.]])




```python
np.zeros_like(arr)
```




    array([[0., 0.],
           [0., 0.],
           [0., 0.]])




```python
np.arange(2,31,2).reshape(-1,3)
```




    array([[ 2,  4,  6],
           [ 8, 10, 12],
           [14, 16, 18],
           [20, 22, 24],
           [26, 28, 30]])




```python
np.linspace(0,10,5)
```




    array([ 0. ,  2.5,  5. ,  7.5, 10. ])




```python
arr = np.arange(1,7).reshape(2,3)
arr
```




    array([[1, 2, 3],
           [4, 5, 6]])




```python
# transpose : 전치행렬(행과 열을 바꾼 행렬)
arr.transpose()
arr.T
```




    array([[1, 4],
           [2, 5],
           [3, 6]])




```python
arr.transpose().transpose()
arr.T.T
```




    array([[1, 2, 3],
           [4, 5, 6]])




```python
# (사과, 배, 딸기)
data = np.array([[1,5,0],
                [5,3,0],
                [1,2,0]])
data
price = np.array([[1000],
                  [5000],
                  [8000]])
price
```




    array([[1000],
           [5000],
           [8000]])




```python
data.shape # 3행 3열
price.shape # 3행 1열
```




    (3, 1)




```python
# data 배열과 price 배열간에 행렬의 곱셈 연산 가능? o
data.dot(price) # 내적
```




    array([[26000],
           [20000],
           [11000]])




```python
data@price # 행렬의 곱셈, 3차원 부터는 달라짐
```




    array([[26000],
           [20000],
           [11000]])




```python
arr = np.arange(10,15)
arr
```




    array([10, 11, 12, 13, 14])




```python
arr2 = arr # 데이터를 공유한다는 의미(뷰)
arr2
```




    array([10, 11, 12, 13, 14])




```python
arr2[1]=99
arr2
```




    array([10, 99, 12, 13, 14])




```python
arr
```




    array([10, 99, 12, 13, 14])




```python
arr=np.arange(10,15)
arr3=arr.copy()
arr3
```




    array([10, 11, 12, 13, 14])




```python
arr3[1] = 99
arr3
```




    array([10, 99, 12, 13, 14])




```python
arr
```




    array([10, 11, 12, 13, 14])




```python
# 1. 1차원 numpy 배열을 만들어 결과와 같이 출력하기
# [ 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
np.arange(0,30,2)
```




    array([ 0,  2,  4,  6,  8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28])




```python
# 2. 2차원 numpy 배열을 만들어 결과와 같이 출력하기
# [[10, 20, 30, 40],
# 50, 60, 70, 80]]
np.array(list(range(10,90,10))).reshape(2,4)
```




    array([[10, 20, 30, 40],
           [50, 60, 70, 80]])




```python
# 3. 3차원 numpy 배열을 만들어 결과와 같이 출력하기
# [[[ 1, 2, 3],
# [ 4, 5, 6]],
# [[ 7, 8, 9],
# [10, 11, 12]],
# [[13, 14, 15],
# [16, 17, 18]],
# [[19, 20, 21],
# [22, 23, 24]]]
np.arange(1,25).reshape(4, 2, 3)
```




    array([[[ 1,  2,  3],
            [ 4,  5,  6]],
    
           [[ 7,  8,  9],
            [10, 11, 12]],
    
           [[13, 14, 15],
            [16, 17, 18]],
    
           [[19, 20, 21],
            [22, 23, 24]]])




```python
# 4. 아래와 같은 행렬을 이용하여 조건에 맞는 코드 작성
vector = np.array(range(0, 30, 2))

# 값 24 인덱싱
#  값 6 인덱싱
vector[12]
vector[3]

idx = np.array([12,3])
idx
vector[idx]
```




    array([24,  6])




```python
# 5. 아래와 같은 행렬을 이용하여 조건에 맞는 코드 작성
matrix = np.array([
[1, 2, 3, 4],
[5, 6, 7, 8],
[9, 10, 11, 12],
[13, 14, 15, 16]
])

# - 값 8 인덱싱
# - 값 2 인덱싱
# - 값 9 인덱싱
# - 값 15 인덱싱

matrix[1,3]
matrix[0,1]
matrix[2,0]
matrix[-1, -2]
```




    15




```python
# 6. 아래와 같은 행렬을 작성해보세요
# [-1, -2, -3, -4, -5]
np.arange(1,6) * -1
```




    array([-1, -2, -3, -4, -5])




```python
# 7.다음 행렬과 같은 배열이 있다.

x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
             11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
# 이 배열에서 3의 배수를 찾아라.
# 이 배열에서 4로 나누면 1이 남는 수를 찾아라.
# 이 배열에서 3으로 나누면 나누어지고 4로 나누면 1이 남는 수를 찾아라.

x[x % 3 == 0]
x[x % 4 == 1]

a = x[x%3 == 0]
a[a%4 == 1]
x[(x % 3 == 0) & (x % 4 == 1)]
```




    array([9])




```python
# 8. 다음 배열을 만들고 슬라이싱, 인덱싱 연습하세요
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
arr2d[:, 2:]
arr2d[1:3]
arr2d[0,2]
arr2d[1:,2]
arr2d + 2
```




    array([[ 3,  4,  5],
           [ 6,  7,  8],
           [ 9, 10, 11]])




```python

```
