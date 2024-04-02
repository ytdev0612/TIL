# 정규표현식

- 복잡한 문자열을 처리한다.
- (정규식, regular experssions;re)
- `import re`

- `re.match(패턴식, 문자열)`
  - 문자열에 패턴이 있는지 판단한다.
  - 문자열의 왼쪽에서 부터 패턴이 있는지를 판단한다.

```py
import re

re.match("h", 'hello')  # 문자열에 패턴이 존재, hello문자열에 h문자 패턴 존재 여부 확인
re.match("s", 'hello')  # 패턴이 존재하지 않으면 아무것도 출력 안됨
re.match("e", 'hello')  # hello문자열에 e문자 패턴 존재 여부 확인, 출력 안됨

re.match("he", 'hello')
re.match("hi", 'hellohi')   # 처음 발견안되면 x
```

- `re.search(패턴식, 문자열)`
  - 문자열에 패턴이 있는지 판단한다.
  - 문자열의 왼쪽에서 시작해 패턴이 있는지 판단한다.

```py
re.search("h", 'hello')  # 문자열에 패턴이 존재, hello문자열에 h문자 패턴 존재 여부 확인
re.search("s", 'hello')  # 패턴이 존재하지 않으면 아무것도 출력 안됨
re.search("e", 'hellohello')  # hello문자열에 e문자 패턴 존재 여부 확인, 출력, 뒤에 패턴이 또 잇어도 그건 출력x

re.search("he", 'hello')
re.search("hi", 'hellohi')  # 전체적으로 검색
```

- `^문자열`
  - 특정 문자열로 시작
- `문자열$`
  - 특정 문자열로 끝

```py
re.search("^he", 'hello world') # 출력
re.search("he", 'hello world')  # 출력
re.search("^he", 'hi, hello world') # 출력 x
re.search("he", 'hi, hello world')  # 출력

re.search('world$', 'hi, hello world')  # 출력
re.search('world$', 'hi, hello world bye')  # 출력x
```

- `|` : 여러 패턴 중에 어느 하나의 패턴에 매칭된다.(or)
- `+` : 문자가 1개 이상 있으면 매칭된다.

```py
re.match('h+', 'hhhi')
re.match('h+', 'hhhhhhhi')

re.match('h+i', 'hhhi') # h문자가 1개 이상 있으며, 이어서 i문자가 등장하면 패턴 존재
re.match('h+i+k', 'hhhiikkk')   # 출력, 'hhhiik'까지 출력
```

- `*` : 문자가 0개 이상 있으면 매칭된다.

```py
re.match('h*', 'hhhi')
re.match('h*', 'ahhhi') # h문자가 없어도 매치가됨 -> 0개가 매치
```

- `"."` : 모든 문자 1개
- `"[.]"` : 마침표
