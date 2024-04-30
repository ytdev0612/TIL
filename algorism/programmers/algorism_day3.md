- 시간/공간 복잡도가 낮도록 설계

## ex1 n을 입력받아 1~n 까지 연속된 숫자의 제곱의 합을 출력하는 프로그램을 작성
```py
def solution(n):
    return sum(i**2 for i in range(1, n+1))

print(solution(4))
# 시간 복잡도 : O(n)

n = 5
print(int((n*(n+1)*(2*n+1)) / 6))
# 시간 복잡도 : O(1)

# 결과는 동일
```

## ex2 숫자 n개를 리스트로 전달 받아 최소값을 출력하는 프로그램 작성(min 사용 불가)
```py
def solution(n):
    res = n[0]
    for i in n:
        if res > i:
            res = i

    return res

print(solution([19, 34, 3, 18, 23]))
# 시간 복잡도 : O(n)
```


## ex3 name과 name2 각각에 대해 중복 이름을 출력
```py
name = ["Tom", "Jerry", "Mike", "Tom"]
name2 = ["Tom", "Jerry", "Mike", "Tom", "Mike"]
# name과 name2 각각에 대해 중복 이름을 출력

# print(','.join(name[i] for i in range(len(name)-1) if name[i] in name[i+1:]))
# print(','.join(name2[i] for i in range(len(name2)-1) if name2[i] in name2[i+1:]))

# 만약 이름이 3번이상 나오면 그 이름이 여러번 출력되므로 그 부분을 확인하는게 필요하다.

def check_name(name):
    res = []
    for i in range(len(name) - 1):
        if name[i] in name[i + 1:] and name[i] not in res:
            res.append(name[i])
    return res

print(','.join(check_name(name)))
print(','.join(check_name(name2)))
```


## ex4 n명 중 두명을 뽑아 짝을 지을 수 있는 모든 조합을 출력
```py
# ["Tom", "Jerry", "Mike"]
# n명 중 두명을 뽑아 짝을 지을 수 있는 모든 조합을 출력
# 'Tom' - 'Jerry', ... 3가지 조합
name3 = ["Tom", "Jerry", "Mike"]

print([name[i] + '-' + j for i in range(len(name3)-1) for j in name3[i+1:]])
```

---

```py
# 팩토리얼
def fact(n):
    if n <= 1:
        return 1
    return n * fact(n-1)    # 함수 호출이 먼저, 5 * 4 * 3 ... 1이 될 때 까지

print(fact(5))
```


## ex5 1~10까지의 합을 재귀호출로 작성하여 출력
```py
def hap(n):
    if n == 1:
        return 1
    return n + hap(n-1)

print(hap(10))
```


## ex6 myList 에서 최대값을 return, 재귀 호출을 활용
```py
a = 0
b = 0
def recursion_max(myList):
    # myList 에서 최대값을 return, 재귀 호출을 활용
    global a, b
    if len(myList[b:]) == 0:
        return a
    if a < myList[b]:
        a = myList[b]
    return recursion_max(myList[b+1:])


print(recursion_max([37,24,56,15,16,23,100,12,13]))

# ex2
li=[37,24,56,15,16,23,100,12,13]
#print(min(li[0], li[1]))
# li.remove(min(li[0], li[1]))
# print(li)


def recursion_max(myList):
    if len(myList) == 1:
        return myList[0]
    myList.remove(min(myList[0], myList[1]))
    return recursion_max(myList)

print(recursion_max(li)) # 100
```