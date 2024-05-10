```python
import numpy as np
```


```python
# 시드(seed)를 이용하여 난수 발생
```


```python
np.random.rand()
```




    0.591835038038944




```python
np.random.seed(20240510)
```


```python
np.random.rand()
```




    0.24432338459661196




```python
np.random.rand(10)
```




    array([0.63551756, 0.67221731, 0.8370985 , 0.3230404 , 0.66728613,
           0.99852928, 0.95145872, 0.36059922, 0.68687786, 0.21542222])




```python
x = np.arange(10)
x
```




    array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])




```python
np.random.shuffle(x)
x
```




    array([9, 3, 4, 6, 5, 0, 7, 1, 2, 8])




```python
# choice : 표본 추출 함수
np.random.choice(x)
```




    1




```python
np.random.choice(5,3, p=[0.1, 0, 0.3, 0.6, 0])
```




    array([2, 3, 2])




```python
# np.random.rand() : 0 <= 난수 < 1
# np.random.randn() : 표준정규분포(평균 : 0, 표준편차 : 1)
# np.random.randint() : 균등분포, 정수난수
```


```python
np.random.rand(15)
```




    array([0.16554452, 0.17774328, 0.03386804, 0.9700636 , 0.7731069 ,
           0.68283439, 0.93101806, 0.33355784, 0.05890293, 0.22177769,
           0.03126138, 0.17330544, 0.17744193, 0.59640132, 0.34261491])




```python
np.random.rand(3,5)
```




    array([[0.20056924, 0.8142382 , 0.50216399, 0.62280608, 0.88084442],
           [0.17058259, 0.87232319, 0.08994572, 0.70349292, 0.93155618],
           [0.23852116, 0.01922331, 0.50562618, 0.13863753, 0.10726334]])




```python
np.random.randn(10)
```




    array([ 1.5818164 , -0.62391063, -0.12153732,  0.56207896, -0.6880638 ,
            0.63919372, -0.21095508, -1.01603034, -1.51825887, -0.98392414])




```python
np.mean(np.random.randn(10))
np.std(np.random.randn(10))
```




    0.9122711489913216




```python
np.random.randint(3)
```




    2




```python
np.random.randint(5,11, size=10)
```




    array([ 9,  8,  8,  9, 10,  8,  7,  8,  5, 10])




```python
np.random.randint(5,11, size=(2,5))
```




    array([[ 9, 10,  6,  5, 10],
           [ 6,  7,  7,  5,  8]])




```python
data = np.random.randint(5,11, size=10)
```


```python
data
```




    array([ 5,  9,  6, 10,  7,  8,  6,  5,  8,  9])




```python
np.unique(data)
```




    array([ 5,  6,  7,  8,  9, 10])




```python
np.unique(data, return_counts=True)
```




    (array([ 5,  6,  7,  8,  9, 10]), array([2, 2, 1, 2, 2, 1], dtype=int64))




```python
np.unique(data, return_counts=True)[0]
np.unique(data, return_counts=True)[1]
```




    array([2, 2, 1, 2, 2, 1], dtype=int64)




```python
np.bincount(data, minlength=11) 
# minlength : 0부터 설정된 값-1까지 수를 범위로 설정하여 빈도수 조사
# minlength=11 이면 0~10까지 수를 범위로 설정하여 빈도수 조사
# 결과 : array([0, 0, 0, 0, 0, 2, 2, 1, 2, 2, 1], dtype=int64)
```




    array([0, 0, 0, 0, 0, 2, 2, 1, 2, 2, 1], dtype=int64)




```python
np.sort(data)
```




    array([ 5,  5,  6,  6,  7,  8,  8,  9,  9, 10])




```python
# 로또 수 5개 출력
```


```python
lotto = np.arange(1,46)
for _ in range(5):
    print(np.random.choice(lotto,6, replace=False))
```

    [20  6  9 43  7 16]
    [ 4  7 43 22 17 12]
    [17 13 11 36 32 12]
    [ 1 28 30 34 17 18]
    [ 5 30 31 28 14  9]
    


```python
# 동전을 10번 던져 앞면(숫자 1)과 뒷면(숫자 0)이 나오는 가상 실험을 파이썬으로 작성
```


```python
np.random.randint(2, size=10)
```




    array([1, 0, 0, 0, 0, 1, 0, 1, 1, 1])




```python
# 주사위를 100번 던져서 나오는 숫자의 평균
```


```python
dice = np.random.randint(1,7, size=100)
```


```python
dice
```




    array([5, 6, 4, 3, 1, 1, 2, 4, 2, 2, 5, 2, 4, 6, 2, 1, 4, 5, 2, 6, 6, 4,
           2, 3, 5, 6, 6, 3, 3, 3, 4, 4, 1, 4, 1, 2, 6, 6, 6, 4, 2, 3, 6, 4,
           6, 1, 3, 5, 3, 2, 4, 4, 4, 6, 1, 5, 2, 2, 5, 6, 1, 3, 3, 4, 4, 6,
           4, 3, 2, 1, 3, 4, 5, 1, 4, 2, 6, 6, 6, 2, 4, 2, 6, 3, 1, 2, 4, 4,
           3, 3, 3, 3, 5, 1, 3, 5, 1, 6, 4, 2])




```python
np.mean(dice)
```




    3.67




```python

```
