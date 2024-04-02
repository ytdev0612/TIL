```py
re.match("^[A-Z]+", 'Hi') # ^를 [] 앞에 붙이면 특정 문자(범위)로 시작하는 패턴식
# ^[A-Z]+:1개 이상의 대문자로 시작하는 문자열인 경우 매치됨

# [범위]*$ #특정 문자(숫자) 범위로 끝나는지 확인
# [범위]+$ #특정 문자(숫자) 범위로 끝나는지 확인

# \s:공백, 줄바꿈, 탭

res.groups() #패턴에 매치된 문자열을 튜플형식으로 리턴
```

- 패턴 그룹에 대한 이름을 부여한다.
- `(?P<그룹이름>정규식)`

```py
res=re.match("(?P<func>[a-z]+)\((?P<arg>\d+)\)", "print(100)")

res.group('func')#'func' 그룹 이름에 해당되는 패턴에 매치된 문자열을 리턴

res.group('arg')
```

- `re.sub("정규식","바꿀문자열", "문자열", "변경횟수" )`
  - 자연어처리에서 문자열 전처리시 많이 사용되는 함수
  - 변경횟수는 생략시 매칭된 문자열을 모두 변경

```py
re.sub("orange", "fruit", "orange banana tree box apple orange orange")

re.sub("orange", "fruit", "orange banana tree box apple orange orange", 2)

re.sub("orange|apple|banana", "fruit", "orange banana tree box apple orange orange")
```

```py
# 변경함수(매치된객체):
#     변경할 수식
#re.sub("패턴", 변경함수, "문자열", "변경횟수")

def func_db(res):
#변경할 수식
    return str(int(res.group())*2)

re.sub("\d+",func_db,"10 20 sky 50 100 bird 200")
```