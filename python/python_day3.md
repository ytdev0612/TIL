# 함수

```python
y = ax + b
def function_name():
    code ...
    # return 생략되어 있다.
```

## 함수의 유형

- 입력이 없는 함수, 리턴이 없는 함수, 둘다 없는 함수
- 매개변수를 지정하여 호출 하는 함수

### 함수의 주석
- 권장하는 방법 : `"""주석"""`


## map 함수
- int()는 문자 -> 숫자 1개만 가능한데 map함수를 이용하면 한번에 여러개를 바꿀수 있음

```python
map(int, ['1', '2', '3'])

def my_func():
    x, y = map(int, input('두 수를 입력하세요:').split(' '))
    print('합:', x+y)   # print(f'합:{x+y}')
    print('차:', x-y)
    print('곱:', x*y)
    print('나눔:', x/y)
```
- def add(*v):  # (*v) : 인수 개수가 정확하지 않아도 받을 수 있다. 받을 때 튜플로 받게 된다.