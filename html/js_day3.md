## 상속
- 부모클래스가 가지고 있는 메서드, 속성을 자식클래스가 물려주는 것

## stringify()
- javascript 객체를 json 문자열로 변환

```js
//함수 선언 방법 : function(){}, () => {}
const test={
    a:function(){
    console.log(this)
    },
    b:()=>{
    console.log(this)
    }
}
test.a()
test.b()
```

```js
// 객체 자료형: 속성, 메서드를 갖는 객체가 갖는 자료형으로는 배열, 함수
// (배열도 객체)
const arr=[]
arr.age=35
console.log(arr)
// 함수도 객체
function f(){}
f.age=20
console.log(f.age)
```

```js
// 기본 자료형(객체 아님, 속성을 가질 수 없다): 숫자, 문자, 불린(참/거짓)
const x= 100
// x.name='홍길동, 속성이 만들어지지 않는다
// console.log(x.name), undefined

// 기본 자료형이지만 객체로 정의
//숫자->숫자객체(Number), 문자->문자객체(String), 불린->불린객체(Boolean)
const obj_num = new Number(100)
console.log(typeof obj_num)
obj_num.data=7
console.log(obj_num.data)
```

```js
// 객체자료형.prototype.매서드명=function(){}
// prototype 객체에 속성 또는 매서드를 추가하면, 모든 객체(기본자료형 포함)에서
// 추가한 속성과 매서드를 사용할 수 있다.

// Number 클래스(객체)에 power 메소드 추가하면,
// 숫자(객체)들은 power 메서드를 호출할 수 있다.
Number.prototype.power=function(n){
return this.valueOf()**n    // this.valueOf()=3, n=2
}
const a=3
console.log(a.power(2))
```

- `toFixed(n)` : 소수이하n번째자리까지 출력 n+1번쨰 자리에서 반올림 한다.
- `.trim()` :  문자열 앞/뒤 공백제거한다.

## js 파일을 따로 저장해서 그걸 가져올 때 
- `<script src="jsfile.js"></script>`

```js
const obj={
name:'자바스크립트',
r_lang:'R언어'
}

obj.addr= obj.addr!=undefined ? obj.addr:'서울시'
// 변수 = 조건식 ? 참 : 거짓
console.log(obj)

// obj에 'python' 속성이 있으면 속성 값을 그대로 사용,
// 없으면 'python' 속성에 '파이썬' 값을 추가하시오
obj.python = obj.python != undefined ? obj.python: obj.python = '파이썬'
console.log(obj)
```