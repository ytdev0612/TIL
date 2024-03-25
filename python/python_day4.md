# 파일 입출력

```python
myfile = open('newfile.txt', 'w')     # w: 쓰기, r: 읽기, a: 추가

myfile.close()
```

다른 형태로도 가능하다. 이때는 자동으로 닫히므로 close()를 사용할 필요가 없다.

```
with open('newfile.txt', 'r') as myfile:
    s = myfile.read()
    print(s)
```


## python 객체 저장

- `class()` : 틀, 템플릿, 사람, 자동차 ...
- 객체() : 실체, 홍길동, 마티즈, ...

- 피클링 : 파이썬 객체를 파일로 저장한다.
- 언피클링 : 파일로부터 파이썬 객체를 읽는다.

```python
import pickle

with open('hgd.p', 'wb') as f:
    pickle.dump(name, f)    # dump 함수로 객체 저장
    pickle.dump(age, f)
    pickle.dump(addr, f)
    pickle.dump(job, f)

with open('hgd.p', 'rb') as f:
    name = pickle.load(f)
    age = pickle.load(f)
    addr = pickle.load(f)
    job = pickle.load(f)
```

- `reverse` : 리스트에서 제공하는 함수로 `list.reverse()`로 사용할 수 있다.
- `reversed` : 내장함수로 리스트에서 제공함수는 아니다.


### n-gram 기법

- 문자열에서 n개의 연속된 문자를 추출한다.

```python
txt = 'hello'
for i in range(len(txt) -1):
        print(txt[i:i+2], end='')
        print()

# he
# el
# ll
# lo

# gram_2 = [txt[i:i+2]for i in range(len(txt)-1)]
# print(gram_2)
```

- 이러한 n-gram 방식으로 다른 두 문장간의 유사도를 구할 수 있다.

```python
txt1 = '나는 오늘 파이썬 문자열 공부를 했습니다'
txt2 = '오늘에서야 파이썬 문자열관련 함수를 공부 했습니다'

# Create bigrams
bigrams_txt1 = [txt1[i:i+2] for i in range(len(txt1) - 1)]
bigrams_txt2 = [txt2[i:i+2] for i in range(len(txt2) - 1)]

# Count bigrams
counter_txt1 = {i: bigrams_txt1.count(i) for i in bigrams_txt1}
counter_txt2 = {i: bigrams_txt2.count(i) for i in bigrams_txt2}

# Calculate similarity
intersection = {i: min(counter_txt1.get(i, 0), counter_txt2.get(i, 0)) for i in set(counter_txt1) | set(counter_txt2)}
similarity = sum(intersection.values()) / min(sum(counter_txt1.values()), sum(counter_txt2.values()))

print(f'Similarity: {similarity}')
```

