# Java Script
- `<script></script>` 안에 작성한다.
- `let` : 변수, 변수 재선언이 불가능하다.
- `const` : 상수, 값 변경이 불가능하다.
- `var` : 변수, 변수 재선언이 가능하다.
- `alert` : 웹 브라우저에서 팝업 알림 창을 생성한다.
- `prompt` : prompt('message', '_default')
- `confirm` : confirm('가입하시겠습니까?'), 네, 아니오 선택으로 True, False 반환한다.
- 
```js
if(조건){
    문장
}else if(조건){
    문장
}else{
    문장
}
```

- `&&` : and
- `==` : 같은지 확인, 만약 두개의 타입이 다르면 피연산자의 타입을 강제로 변경해 비교한다.
  - ex) 1=='1' -> True
  - `===` : 타입 변경없이 비교
- `typeof()` : 타입 확인

```js
console.log(`1+2는 3입니다`)
// 1+2는 3입니다
console.log(`1+2는 ${1+2}입니다`)
// 1+2는 3입니다
```

```js
switch('hello'){
case 0:
alert('짝수')
break
case 1:
alert('홀수')
break
default:
alert('숫자가 아닙니다.')
break
}
```

## 삼항 연산자

- ( ?   : )
  - `(조건 ? 참일 때 식 : 거짓일 때 식)`


