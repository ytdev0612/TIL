# Q1 6자리 숫자를 입력 받아 Baby-gin 여부 확인하기

```
0-9 사이의 숫자 카드에서 임의의 카드 6장을 뽑아 3장의 카드가 연속적인 번호를 갖는 경우를 run, 3장의 카드가 동일한 번호를 갖는 경우를 triplet이라고 한다. 
6장의카드가 run과 triplet으로만 구성된 경우를 구하시오
```

```py
# 다른 방법으로 해야 정확할 거 같음
# import random
def triplet(num):
    if num[0] == num[1] == num[2]:
        return True


def run(num):
    if num[0] + 1 == num[1] and num[1] + 1 == num[2]:
        return True


def remain_check(num):
    if len(set(num)) == 2:
        return True
    elif len(set(num)) == 3:
        if run(list(set(num))):
            return True


# random_num = [random.randint(1, 9) for i in range(6)]
# random_num = sorted(random_num)
# print(random_num)
# print(random_num[::2])
random_num = [3,4,4,4,4,5]
random_num = sorted(random_num)

if run(random_num[:3]) or triplet(random_num[:3]):
    if run(random_num[3:]) or triplet(random_num[3:]):
        cnt = 2
    else:
        cnt = 1
else:
    cnt = 0

if cnt == 2 or remain_check(random_num):
    print('Baby-gin')
else:
    print('Not Baby-gin')

# 배열 활용해서 해보기
```


## 버블 정렬
- 인접한 두 개의 원소를 비교하며 자리를 계속 교환하는 방식
- 한 단계가 끝나면 가장 큰 원소가 마지막 자리로 정렬된다.
- 시간 복잡도 : O(n**2)

```py
num_list = [55, 7, 78, 12, 42]

for i in range(len(num_list)-1):
    for j in range(len(num_list)-(i+1)):    # 한번 루프를 돌면 가장큰 수가 오른쪽에 도착
        if num_list[j] > num_list[j+1]:
            num_list[j], num_list[j+1] = num_list[j+1], num_list[j]
        # print(num_list)
    # print(num_list)
print(num_list)

```

## 카운팅 정렬
- 항목들의 순서를 결정하기 위해 집합에 각 항목이 몇 개씩 있는지 세는 작업을 해 선형 시간에 정렬하는 효율적인 알고리즘
- 정수나 정수로 표현할 수 있는 자료에 대해서만 적용 가능하다
- 카운트를 위한 충분한 공간을 할당하려면 집합 내의 가장 큰 정수를 알아야 한다
- 시간 복잡도 : O(n + k): n은 리스트 길이, k는 정수의 최대값

```py
num_list = [0, 4, 1, 3, 1, 2, 4, 1]

counts = [0] * (max(num_list)+1)

for i in num_list:
    counts[i] = counts[i] + 1

# print(count)

for i in range(1, len(counts)):
    counts[i] += counts[i-1]

# print(count)

temp = [0] * len(num_list)
# print(temp)

for i in range(len(num_list)-1, -1, -1):
    counts[num_list[i]] -= 1
    temp[counts[num_list[i]]] = num_list[i]

print(temp)
```


## 2차원 배열 활용

```
5*5 2차 배열에 무작위로 25개의 숫자로 초기화 한 후 각 요소에 대해서 그 요소와 이웃한 요소와의 차의 절대값을 구하시오
벽에 있는 요소는 이웃한 요소가 없을 수 있음
```

```py
import random

array = [[random.randint(1, 10) for _ in range(5)] for _ in range(5)]

res = 0
for i in range(len(array)):
    for j in range(len(array[i])):
        factor = array[i][j]
        hap = 0
        # 북
        if i > 0:
            hap += abs(factor - array[i - 1][j])
        # 남
        if i < len(array) - 1:
            hap += abs(factor - array[i + 1][j])
        # 서
        if j > 0:
            hap += abs(factor - array[i][j - 1])
        # 동
        if j < len(array[i]) - 1:
            hap += abs(factor - array[i][j + 1])

        res += hap

print(res)
```

