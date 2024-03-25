## 재귀호출
- 자기 자신을 호출하는 함수

```python
def hi(cnt):
    if cnt == 0:
        return
    print('(before)hi', cnt)
    cnt -= 1
    hi(cnt)
    print('(after)hi', cnt)
    # return 생략되어 있음
"""
hi(3) -> hi(2) -> hi(1) -> hi(0) -> return -> 6번째 줄로 되돌아감 ->
 7열 실행 -> 이전 시점으로 되돌아감 (hi(0) -> hi(1) -> hi(2))
"""

def star(s):
    if s == 0:
        return
    print('*'*(5-s))    # 5->4->...->1(****)-> 0(return)->0(*****)->...->5
    s -= 1
    star(s)
    print('*'*(5-s))
    # return

star(5)

# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *
```


## 리스트, 딕셔너리 내포

`[i ** 2 for i in a if ~ ] { }`

## 함수, 람다 표현식

```python
# def 함수명():
def func1(x):
    return x + 1

# 람다식(익명)으로 함수 정의 , lambda
# lambda
lambda x: x+1

# 람다식(명명)으로 함수 정의
func2 = lambda x: x+1

# 람다식 기본 형식
# (lambda 매개변수들 : 수식)(인수들)
# 람다식 내부에 새로운 변수를 생성할 수 없음
```

```python
# 람다식을 인수로 사용, 대표적으로 map 함수에서 사용
def add_one(x):
    res = [ ]
    for i in x:
        res.append(i+1)
    return x+1

l = [10, 20, 30]
def add_one_2(x):
    return x+1
list(map(add_one_2, l))

list(map(lambda x: x+1, l))
```

- 람다식에 조건식도 사용 가능하다.

```python
a = list(range(1, 11))

list(map(lambda x: x+1, a))      # map(함수, 변수)
list(map(lambda x: str(x), a))      # map(함수, 변수)


list(map(lambda x: str(x) if x%2==0 else x, a))
# a에 저장된 리스트의 각 요소를 x에 전달,
# 짝수면 str, 홀수면 x값 출력

# [1, '2', 3, '4', 5, '6', 7, '8', 9, '10']


# a에 저장된 값이 5보다 크면 2를 곱하고, 아니면 저장된 값 그대로 출력
list(map(lambda x: x*2 if x>5 else x, a))

# [1, 2, 3, 4, 5, 12, 14, 16, 18, 20]


# # a에 저장된 값이 3이면 3.0으로 변경, 나머지는 그대로
list(map(lambda x: float(x) if x==3 else x, a))

# [1, 2, 3.0, 4, 5, 6, 7, 8, 9, 10]
```

- `lambda 매개변수들 : 식1 if 조건식1 else 식2 if 조건식2 else 식3`, 이런 형식도 가능하다.

```python
# 1은 문자로 변환, 2는 실수로 변환, 3이상은 10을 더하시오
list(map(lambda x: str(x) if x==1 else float(x) if x==2 else x+10, a))

# ['1', 2.0, 13, 14, 15, 16, 17, 18, 19, 20]
```

- 리스트 2개를 입력해 람다함수 연산을 통해 리스트 1개로 출력할 수 도 있다.

```py
a= list(range(1, 6))
b = list(range(11, 16))

# [12, 14, , ... , 20]
list(map(lambda x, y : x+y, a, b))
list(map(lambda x, y : x*y, a, b))
```

## filter 함수

- 조건에 맞는 데이터 요소만 추출한다.
- `filter(함수, 리스트, ...)`
- `map(함수, 리스트, ...)`

```py
a = [1,2,3,4,5]

list(filter(lambda x: x>1 and x<4, a))
# filter는 조건이 참인 요소만 추출하고 나머지(거짓)는 버린다.

# [2, 3]
```

## reduce 함수

- `reduce()` : 누적된 결과를 저장한다.

```py
def cum(x, y):
    return x+y
from functools import reduce

reduce(cum, a)  # a에 저장된 데이터에 대해 cum함수를 수행한 누적 결과를 구하시오

# 1 2 -> 3 3 -> 6 4 -> 10 5 ->15
```

## 전역 변수, 지역 변수
- 전역 변수
  - 함수 바깥에서 선언된 변수로 전체 코드에서 참조가 가능하다.
  - 함수 내부에서도 사용 가능하다.
- 지역 변수
  - 함수 내부에서 선언된 변수로 함수 밖에서 접근이 불가능하다.
  - `global`로 함수 내부에서 전역 변수로 선언할 수 있다.


# 클래스

- 클래스 : 공통된 특성(바퀴, 색상, 마력, 배기량, ...)
- 동작(달린다, 멈춘다, ...)을 갖는 객체들의 모임
- ex) 동물 : 사람, 사자, ...

```py
# 클래스 정의
class Car:
    def drive(self):    # self : 현재 객체(자기 자신)
        print('자동차가 달립니다.')
    def print_msg(self):
        self.drive()    #
    hp = 3000

gran = Car()    # 자동차 클래스로부터 객체가 만들어짐

gran.drive()
gran.print_msg()
```
