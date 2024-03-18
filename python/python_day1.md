# 1일차 내용 정리

- 화면에 출력하기 : `print('Hello, python.')`
  - 구분자 : `sep=" "`
  - end 옵션 : `end=" "`
- 사용자가 입력하기 : `input('숫자를 입력하세요 : ')`


## Escape
- `\n` : 줄바꾸기
- `\t` : 탭(Tab)
- `\\` : '\' 출력하기
- `\'` : 작은따옴표 출력하기
- `\"` : 큰따옴표 출력하기
- `\b` : 백스페이스


## 산술 연산자
- `+` : 더하기
- `-' : 빼기
- `*` : 곱하기
- `**` : 제곱
- `/` : 나누기
- `//` : 나누기(나눈 몫 출력)
- `%` : 나누기(나눈 나머지 출력)

```python
x = 5
y = 3
print(x + y)    # 8
print(x - y)    # 2
print(x * y)    # 15
print(x / y)    # 1.666..
print(x ** y)   # 125
print(5 % 3)    # 2
print(5 // 3)   # 1
```

- 몫, 나머지 출력 : `divmod(x, y)`
- 개수 세는 함수 : `count()`
- 타입 확인 : `type()`
- 문자 찾기 : `find(찾을문자, 시작, 끝)`
- 변수 생성
  - 대소문자, 숫자 가능
  - 숫자로 시작, 특수문자 x
- 아무것도 없는 상태 : `x = None`


## 논리 연산자
  - `and` : 둘다 참이여야 True
  - `or` : 둘 중 하나이상이 참이여야 True
  - `not` : 둘다 거짓이여야 True
  - 논리연산자의 우선순위는 `not>and>or` 이다.
  - 비교연산자 > 논리연산자
- 여러줄에 걸쳐 문자열을 작성할 때 사용 : `'''  '''`
- 길이 : `len()` 문자열의 길이를 반환한다.


## 문자열 포멧팅

```python
num = 2
name = Tomas

print('I eat %d apples.' %2)
print('I eat %s apples" % 'two')
print('I eat %s apples %d times %%' % ('two', 2))

print('I eat {0} apples'.format(2))
print('I {0} eat {1} apples'.format(2, 5))
print('l {num} eat {su} apples'.format(su = 2,num = 5))

print(f'I eat {num} apples.')
print(f'I eat {num} apples with {name}.')

print("%10s" % 'hi')    #         hi
print("%10s" % 'hello') #      hello

print('{0:>10}'.format('hi')) #         hi
print('{0:<10}'.format('hi')) # hi        
print('{0:^10}'.format('hi')) #     hi    
print('{0:=^10}'.format('hi')) # ====hi====

x = 3.141592
print("{0}".format(x)) # 3.141592
print("{0:0.3f}".format(x)) # 3.142
```

---


- 문자열 쪼개기 : `.split(',')` # split() 값으로 구분해서 분리한다. 아무것도 안넣으면 공백 기준
- 여러 개의 데이터를 각각 적용하기 : `.map(function, iterable)` # iterable 각각의 요소에 function 함수를 적용한 결과를  새로운 iterator로 반환한다.
- 리스트 문자열로 합치기 : `"구분자".join(list)`

```python
x_list = ['a', 'b', 'c']
res = ','.join(x_list)
print(res) # a,b,c
```

- 정렬하기
  - `upper()` : 대문자로 전환하기
  - `lower()` : 소문자로 전환하기
  - `strip()` : 공백 제거하기

```python
x = '   hello   '
x.strip()   # hello
x.rstrip()  #    hello
x.lstrip()  # hello   
```

- 문자열 변경하기 : `replace(old, new, [count])`


## 자료구조
데이터(자료)를 저장 및 관리하는 방법

파이썬 자료구조 : 리스트, 튜플, 딕셔너리, 집합(set)
```python
# 리스트
x = list()
x = []
x = [1, 2, 'life', ['python', 3, 4, 5], 6, [7, 8]] # 다중 리스트도 가능하다.

del x[0]            # 삭제 가능하다.

x.append(10)
x.append([20, 30])  # 추가도 가능하다.
x.extend([40, 50])  # append는 리스트 끝에 그대로 넣으며 extend는 가장 바깥쪽 iterable 의 모든 항목을 넣는다.
x.append('ping')    # ping 그대로 추가
x.extend('ping')    # p, i, n, g 각각 추가

x.pop()             # 제일 마지막 값을 추출 후 제거한다.

# 튜플
x = (10, 20, 30)    # 변경이 불가능하다. 읽기로 주로 사용, 리스트로 변환하여 값 변경이 가능하다.
```