# 클래스

- 클래스 예제
```py
class Person:
    bag=[]  # 가방은 여러가지 물건들 저장, 클래스 속성
    def put_bag(self, stuff):
        # self.bag.append(stuff)  # 클래스 속성 접근할때는 클래스 이름으로 접근
        Person.bag.append(stuff)

hgd = Person()
hgd.put_bag('wallet')
hgd.bag
# ['wallet']
```
- 해당 방식은 다른 객체를 만들어도 속성을 모든 객체가 공유한다.

```py
class Person:
    def __init__(self):
        self.bag = []       # 인스턴스(객체) 속성
    def put_bag(self, stuff):
        self.bag.append(stuff) # 객체가 가지고 있는 bag에 stuff 추가
```

- 이렇게 만들면 각각의 객체가 각자의 속성을 같게된다.


# 예외(exception)

- 코드가 실행중에 발생한 에러

```py
def mydiv(a):
    try:
        return 5/a  # 예외가 발생할 여지가 있는 코드
    except: # 예외가 발생했을 때 실행
        print('예외 상황이 발생했습니다. 입력값을 확인해보세요.')

mydiv(0)    # 실행중인 코드에서 에러 발생(예외)
```

- try문 수행중에 오류 발생-> except 수행, 그렇지 않으면 else 수행

```py
try:
    age = int(input('나이 입력 : '))
except:
    print('숫자만 입력해주세요.')
else:
    print('반갑습니다.')
print('안녕')
```

- `finally` : 예외 발생 여부와 상관없이 무조건 실행

```py
try:
    x = int(input())
    y = 1/x
except:
    print('0으로 나누지 못함')
else:
    print(y)
finally:
    print('코드 실행 종료')

# 어떤 값을 x에 입력하든 '코드 실행 종료'는 실행된다.
```


## 내장함수, 외장함수

- 내장 함수 : 기본적으로 메모리에 적재되는 함수
  - map, filter, max, len ...

- 외장 함수 : 메모리에 적재(import)한 다음 사용할 수 있는 함수

```py
random.random() 
# random모듈.random함수()

# 모듈 : 특정 기능과 관련된 함수, 클래스들로 구성된 파일
```

- `any` : 리스트(튜플)의 요소 중에서 하나라도 참 -> 참, 모두 거짓->거짓
- `chr` : # 유니코드(전세계문자 코드) -> 문자
- `ord` : # 문자 -> 유니코드(전세계문자 코드)

- `eval()` : 문자열로된 수식, 함수 등

```py
eval('1+2')
eval('abs(-5)')
```

- `filter()` : filter(함수, x(변수))

```py
x2 = list(filter(lambda k: k>0, x))
print(x2)

# [1, 3, 5]


def f_func(k):   # [1, -2, 3, -4, 0, 5]
    return k>0   # [True, False, ...]

list(filter(f_func, x)) # [1, -2, 3, -4, 0, 5]
# x에 저장된 각각의 요소를 f_func함수로 전달, 조건에 부합되는 요소만 추출

# [1, 3, 5]
```

- `glob.glob("c:/")` : c드라이브에 있는 파일/폴더 검색