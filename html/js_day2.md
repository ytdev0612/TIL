## 함수
```js
// 익명함수
const myfunc=function(){
        
}

// 선언적함수
function myfunc(){

}
```
- 예시
```js
const myfunc = function(){
    console.log('함수입니다.1');
    console.log('함수입니다.2');
}
myfunc()
console.log(myfunc)
console.log(typeof myfunc)
```

```js
function var_arg(...items){// 매개변수 개수가 일정치 않을 때 사용
}

function var_arg(x, ...items){// 매개변수 개수가 일정치 않을 때 사용. 처음은 x에 들어가게 된다.
}
```

- 콜백함수 : 매개변수로 전달되는 함수

```
function f(cb){
for (i=0; i<3; i++){
    cb(i)
    }
}
function myPrint(i){
    console.log(`${i+1}번째 콜백함수가 호출되었습니다.`)
}
f(myPrint)

f(function(i){
    console.log(`${i+1}번째 콜백함수가 호출되었습니다.`)
})
```

```js
//forEach: 배열이 가지고 있는 함수, 배열 내부 요소를 이용해서 콜백함수 호출
const num = [10, 20, 30]
num.forEach(function(value, index, array){
console.log(`${index}번째 요소: ${value}`)
})
```

```js
// map: 배열이 가지고 있는 함수, 콜백 함수의 리턴 결과로 새로운 배열 생성
const num2 = [10, 20, 30]
res = num2.map(function(value, index, array){
    return 2*value
})
console.log(res)
```

```js
//filter: 배열이 가지고 있는 함수, 콜백 함수의 리턴값이 true에 해당하는 값들로 새로운 배열 생성
const num3 = [10, 20, 30]
res = num3.filter(function(value, index, array){
    return value%20==0
})
console.log(res)
```

- 타이머 함수
```js
// setTimeout(콜백함수, 시간(밀리초, 1000밀리초 = 1초)) : 특정 시간 후에 함수를 1번 호출
// clearTimeout(타이머id):setTimeout 함수로 설정한 타이머 제거
setTimeout(()=>{
console.log('5초후에 타이머 종료')
clearInterval(interValId)
}, 5*1000)

// setInterval(콜백함수, 시간(밀리초)) : 특정 시간 간격으로 콜백함수 호출
// clearInterval(타이머id) : setInterval 함수로 설정한 타이머 제거
cnt=0
interValId=setInterval(() => {
console.log(`1초마다 실행(${cnt}번째)`)
cnt++
},1*1000)

console.log('5초후 타이머 종료');
setTimeout(() => {
    clearInterval(intervalId);
}, 5 * 1000)
sec = 1
cnt = 0;
intervalId = setInterval(() => {
    console.log(`${sec}초후에 실행 - ${cnt}번째`); cnt++;
}, sec*1000)
```