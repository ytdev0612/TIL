## 상자의 높이가 주어지고 가장 높은 곳에서 가장 낮은 곳으로 평탄화 작업하기

```py
box = [5, 8, 3, 1, 5, 6, 9, 9, 2, 2, 4]   # 상자높이
dump_count = 5      # 가장 높은 값 -1 -> 가장 낮은 값 + 1


for i in range(dump_count):
    min_n = min(box)        # 가장 작은 수
    max_n = max(box)        # 가장 큰 수
    box[box.index(min_n)] = min_n + 1       # 가장 작은 수 +1
    box[box.index(max_n)] = max_n - 1       # 가장 큰 수 -1

res = max(box) - min(box)
print(res)

# 코드 개선 방안 -> 현재 min, max 함수를 매번 호출 중, 이걸 현재 가장 작은 수, 가장 큰 수의 개수를 세서 해보는거 찾아보기
```


## question

```py
building = [0, 0, 3, 5, 2, 4, 8, 0, 6, 4, 0, 6, 0, 0]   # 좌,우 양쪽 끝 2칸은 빌딩 x

res = 0             # 조망권이 확보된 층

# 함수 사용안하고 풀어볼 때
# for i in range(2, len(building) - 2):
#     high = 0
#
#     for j in (building[i-2:i] + building[i+1:i+3]):
#         if j > high:
#             high = j
#
#     if high < building[i]:
#         res += (building[i] - high)
#
# print(res)

for i in range(2, len(building) - 2):
    high = (max(building[i-2:i]) if max(building[i-2:i]) > max(building[i+1:i+3]) else max(building[i+1:i+3]))

    if high < building[i]:
        res += (building[i] - high)

print(res)

# 0층일경우에는 연산을 안한다 등의 방법도 있음
```


## 선택 정렬
- 주어진 자료들 중 가장 작은 값의 원소부터 차례대로 선택하여 위치를 교환하는 방식

```py
n_list = [64, 25, 10, 22, 11]

for i in range(len(n_list)-1):
    low_num = i             # 가장 작은 수의 인덱스
    for j in range(i+1, len(n_list)):
        if n_list[j] < n_list[low_num]:
            low_num = j
    if i != low_num:        # low_num의 값이 바뀌면 i 인덱스에 있는 값보다 작은 수가 있으므로 두 개의 위치를 교환
        n_list[i], n_list[low_num] = n_list[low_num], n_list[i]

print(n_list)
```


## 2차원 배열 리스트 
- 가로, 세로, 대각선 합 비교해서 가장 큰 수 찾기

```py
# 파일 불러오기
with open('sum_arr.txt') as f:
    content = f.read()

content = content.split('\n')
content = content[:-1]

for i in range(len(content)):
    content[i] = content[i].split(' ')

# 리스트 안의 값 숫자로 변경
content = [[int(num) for num in i] for i in content]

# for i in content:
#     print(i, end='\n')

# 가로 합의 최대 값
# 세로 합의 최대 값
# 대각선 합의 값들
garo = (sum(content[i][j] for i in range(5)) for j in range(5))
sero = (sum(content[i][j] for j in range(5)) for i in range(5))
degak = sum(content[i][i] for i in range(5))
degak2 = sum(content[4-i][i] for i in range(5))

res_list = [max(garo), max(sero), degak, degak2]
print(max(res_list))
```
