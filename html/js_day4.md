```js
//DOMContentLoaded 이벤트는 웹 문서를 모두 읽고 나서 발생됨
html - 요소(html, head,...body,...span)
js - 문서객체 -> 조합 -> 문서 객체 모델(DOM)
head 태그 내부에 script 태그는 body 태그에 있는 문서 객체에 접근할 수 없다.
head 태그 내부에 script 태그에서 body 태그에 있는 문서 객체에 접근하려면?
화면에 body 태그에 있는 문서 객체를 모두 읽을때까지 기다려야 함
```

`.textContent` : 단순히 텍스트를 출력할 때 사용

```js
 태그, #아이디, .클래스, [속성=값],
선택자 조상 선택자 후손, 선택자 부모 > 선택자 자손
```

`.addEventListener()` : (이벤트명,이벤트발생시수행할작업)

