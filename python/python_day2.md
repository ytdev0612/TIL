# 2일차 내용 정리

## 딕셔너리
`dict = {}, {key, value}`
```
dic.keys()
dic.get('key')
dic.values()
dic.clear()
```


## set
- {}, 집합, 중복이 허용되지 않으며 정렬되서 출력된다. -> index 불가능하다.


## 집합 기호
- `s1&s2`,`s1.intersection(s2)`  : 교집합
- `s1 | s2`, `s1.union(s2)` : 합집합
- `s1 - s2`, `s1.difference(s2)` : 차집합

- `add()` : add()는 인수가 1개만 가능하다.
- `remove()`

```
if 조건식:
    조건식이 참일 때 수행할 문장
else:
    조건식이 거짓일 때 수행할 문장

for 변수 in range(반복횟수):
    반복수행할 코드

while 조건식:   # 탈출하는 조건이 필요하다.
    반복수행할 코드
```


## 리스트 컴프리헨션(리스트 내포)
리스트 내부에 for문 작성 -> 리스트 초기

`[표현식 for 항목 in 반복대상 if 조건]`

`[표현식 for 항목 in 반복대상 if 조건 for 항복 in 반복대상 if 조건 ...]`
```
ex)
x = [1, 2, 3]
res = [n*2 for n in x]
res
->
x = [1, 2, 3]
res2 = [n for n in x if n >= 2]     # [2, 3]
res2
```


## 모듈
- 특정 기능을 수행하기 위한 함수
- 클래스 등으로 구성된 파일이다.
