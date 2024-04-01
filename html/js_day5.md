```js
<!--이벤트 모델 : 이벤트를 연결하는 방법-->
document.body.addEventListener(이벤트명, () => {
이벤트 발생 시 처리할 구문
키보드 이벤트 : keydown, keypress, keyup
})
```

```js
css position:
1) position 속성 : 문서에서 요소를 배치하는 방법 지정
2) top, right, left, bottom : 문서에서 요소의 위치를 지정
참고 : block, inline

1) 요소를 옮기기 위해 기준점을 설정
static, relative, absolute, ...
- relative : 자기 자신의 원래 위치를 기준으로 배치
2) 기준점에서 옮기고자 하는 요소의 위치를 설정
top, right, left, bottom
```

```js
    /*
    //document.addEventListener(이벤트명, 이벤트발생시처리구문)
    //1번째 방식(예전방식)
    document.addEventListener("DOMContentLoaded",() => {
        const textarea=document.querySelector('textarea')
        const h1=document.querySelector('h1')
        textarea.addEventListener('keyup',(e)=>{
            const length=textarea.value.length
            h1.textContent=`{length}`
        })
    })
    //2번째 방식(요즘방식)
    myListener = (e)=>{
       // const length=textarea.value.length //에러발생(리스너 내부에서 textarea참조 못함)
        const length=e.currentTarget.value.length
        h1.textContent=`{length}`
    }
    document.addEventListener("DOMContentLoaded",() => {
        const textarea=document.querySelector('textarea')
        const h1=document.querySelector('h1')
        textarea.addEventListener('keyup',myListener)
    })
    
    */
```