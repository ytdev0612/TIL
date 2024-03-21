- driver.find_element("css selector", seoul_btn) # css selector를 이용해 뒤의 내용을 찾음
- .attrs : 속성을 참고 할 때(생략도 가능)

- string 과 text 모두 특정 태그로 감싸져있는 내용을 추출한다.

- 차이는 특정 태그로 감싸져 있는 부분 내에 또 다른 태그가 있는 경우 string에서는 에러 발생
- text에서는 텍스트 추출이 정상적으로 수행된다. -> text를 쓰는게 더 편리하다.

- `input_pw.submit()` : # 패스워드 입력 후 엔터 키 입력과 동일

```
1)driver.get("사이트주소")
2-1)driver.find_element('css selector', "추출 대상 셀렉터")
2-2)driver.page_source
3)BeautifulSoup()
4)select, ... 내용추출
```
