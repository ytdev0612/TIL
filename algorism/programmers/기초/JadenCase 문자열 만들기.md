# JadenCase 문자열 만들기 
- JadenCase란 모든 단어의 첫 문자가 대문자이고, 그 외의 알파벳은 소문자인 문자열입니다.
- 단, 첫 문자가 알파벳이 아닐 때에는 이어지는 알파벳은 소문자로 쓰면 됩니다.
- 문자열 s가 주어졌을 때, s를 JadenCase로 바꾼 문자열을 리턴하는 함수, solution을 완성해주세요.

``` py
def solution(s):
    answer = ''
    
    for i in range(len(s)):
        if i == 0 or s[i-1] == ' ':
            answer += s[i].upper()
        else:
            answer += s[i].lower()
    
    return answer
```
- 숫자는 upper, lower 사용하면 에러 발생하지만 str 타입이면 변화없이 사용가능
- 파이썬 내장 함수 2개에 대해 새로 학습
    - title() : 여러 단어가 있는 경우 각 단어의 첫글자를 대문자로 만들기
    - capitalize() : 문자열의 첫글자만 대문자로 만들기