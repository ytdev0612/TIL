- `char_length()` : 문자열의 길이를 반환한다.
- `length()` : 문자열의 길이를 바이트 단위로 반환한다.
- `concat()` : 문자열들을 입력하면 결합해준다.
- `concat_ws()` : 제일 앞에 구분자를 넣어서 구분자로 연결할 수 있다.
- `left(), right()` : (문자열, 5), 각 방향에서 5글자만큼만 출력한다.

- `substr()`
```sql
substr()` : `('안녕하세요', 2, 4) -> 녕하세
/*3번째 수는 생략 가능하며 생략하면 가운데 수부터 끝까지 추출된다.*/
```

- `substring_index()`
```sql
substring_index('서울특별시 강남구 역삼동', ' ', 2); -> 서울특별시 강남구 
/*왼쪽에서 2번째 공백 이후를 모두 제거한다, `서울특별시 강남구`까지 추출*/

select substring_index('강북구강남구영등포구', '구', 2); -> 강북구강남

/*마지막을 음수로 주면 오른쪽에서 부터 2번째 공백 이전을 모두 제거한다*/

select substring_index('서울특별시 강남구 역삼동', ' ', -2); -> 강남구 역삼동
```

- `lpad(), rpad()` : 특정문자로 채우기
```sql
lpad('sql', 5, '#') -> ##sql
rpad('sql', 5, '#') -> sql##
```

- `ltrim(), rtrim()` : 공백제거
```sql
ltrim('   sql  ') -> 'sql  '
rtrim('   sql  ') -> '   sql'
trim('   sql  ') -> 'sql'
/* 양쪽, 왼쪽, 오른쪽 동일 문자열을 제거할 수도 있다. */
select trim(both 'ab' from 'ababcdab'); -> cd
elect trim(leading 'ab' from 'ababcdab'); -> cdab
select trim(trailing 'ab' from 'ababcdab'); -> ababcd
```

- `field(찾고자하는문자열, 문자열1, ...)`
```sql
select field('java', 'sql', 'java', 'c'); -> 2
```

- `find_in_set()`
```sql
select find_in_set('java', 'sql,java,c'); -> 2
```

- `instr(문자열, 찾고자하는 문자열)`, `locate(찾고자하는 문자열, 문자열)`
```sql
select instr('네 인생을 살아라', '인생'); -> 3(인생의 시작위치)
```

- `elt(찾을문자열위치, '문자열1', ...)`
```sql
select elt(2, 'sql', 'java', 'c'); -> java
```

- `repeat(문자열,횟수)` : 문자열 반복 함수
```sql
select repeat('ㅋ', 5); -> ㅋㅋㅋㅋㅋ
```

- `replace('문자열', '원래문자열', '바꿀문자열')` : 문자열 치환 함수
```sql
select replace('010.1234.5678', '.', '-'); -> 010-1234-5678
```

- `reverse('문자열')` : 문자열 뒤집기 함수
```sql
select reverse('abcd'); -> dcba
```

- 자릿수 지정함수 
```sql
select ceiling(123.56);	/*올림*/
select floor(123.56); /*버림*/
select round(123.56); /*반올림*/
select round(123.356, 2) /*반올림*/
select truncate(123.56, 1) /*버림*/
```

- `abs()`
```sql
select abs(-3); -> 3
select abs(3); -> 3
```

- `sign()` : 음수면 -1, 양수면 +1
```sql
select sign(-3);
select sign(3);
```

- 나머지 구하는 함수
```sql
select mod(10, 4); /*나머지*/
select 10%4;
select 10 mod 4;
```

- `power()`, `sqrt()`
```sql
select power(2,3); -> 8(2의3제곱)
select sqrt(9); -> 3(제곱근)
```

- `rand()`
```sql
select rand();
select rand(20240405); /* seed */

select rand()*2; /* 0 <= rand() < 1 */
```

- `now()`, `sysdate()`  : 현재의 날짜, 시간 반환
- `curdate()`, `curtime()`
```sql
/*연도나 달만을 출력할 수도 있음*/
select year(now()), month(now());
/*분기 출력도 가능하다*/
select quarter(now());

select hour(now());
select minute(now());
select day(now());
```

- `datediff(끝일자, 시작일자)`
```sql
select datediff('2024-05-01', '2024-04-05'); -> 26
select datediff('2024-04-05', '2024-05-01'); -> -26
```

- `timestamp(단위, 시작, 끝)`
```sql
select timestampdiff(day, now(), '2024-04-30'); -> 24 (24년4월5일 기준)

/*달, 연도도 가능*/
select timestampdiff(month, now(), '2024-12-30'); -> 8
select timestampdiff(year, now(), '2025-12-30'); -> 1
```

- `adddate()`
```sql
select adddate(now(), 20); -> 4/25일로 변경됨 (24년4월5일 기준)

select adddate(now(), interval 20 day);
select adddate(now(), interval 20 month);
select adddate(now(), interval 20 hour);

/*이전*/
select subdate(now(), interval 20 day);
```

- `last_day()`
```sql
select last_day(now()); /*현재 월의 마지막 일자*/
select dayofyear(now()); /* 올해가 지금 며칠 경과일 */
select weekday(now()); /* 요일(0-6) */
```

- 데이터 형 변환 : `cast(값 as 변환타입), convert()`
```sql
select cast('1' as unsigned); -> 1 /*unsigned : 부호가 없는 숫자 형식, signed : 부호가 있는 숫자 형식*/
/* 1byte -> 8bit => 1bit: 부호(0 or 1(음수 or 양수)), 7bit: 숫자
7bit = -128 ... 0, ... 127
1byte = 8bit => 8bit 숫자 = 0~255
*/

select cast(1 as char(1)); -> 문자 1로 변환
select convert(1, char(1)); -> 문자 1로 변환
```

- `if(조건식, 참, 거짓)`
```sql
select if (1+2 > 0, '앙수', '음수'); -> 양수

/* ifnull함수의 1번째 인수가 null이 아니면 1번째 인수가 리턴, null이면 두번째 인수가 리턴된다. */
select ifnull(null, 0); -> 0
select ifnull(5, 10); -> 5

/* 두 값이 같으면 null, 다르면 1번째 인수가 리턴 */
select nullif(3, 3); -> null
select nullif(3, 5); -> 3
```

- case문
``` sql
/* when 조건1 then 값1 when 조건2 then 값2 ... */
select case when 100*2 > 150 then '합격' 
when 100*2 > 500 then '불합격' 
else '재시험'
end;
```

- 집계함수
```sql
sum(), count()/* null 제외 */, avg(), min(), max()  

/* group by절 : 그룹별로 묶어서 요약 */
/*
select 그룹으로 묶을 열, 집계함수
from 테이블명
where 조건절(옵션, 없으면 안써도 됨)
group by 그룹으로 묶을 열(번호)
*/
/* 도시 단위로 그룹화 -> 그룹별 마일리지의 합계 */
select 도시, sum(마일리지) as 마일리지 합계 from 고객
group by 도시;

/* having 절 : group by 결과에 대한 조건 

select 그룹으로 묶을 열, 집계함수
from 테이블명
where 조건절(옵션, 없으면 안써도 됨)
group by 그룹으로 묶을 열(번호)
having 절;(옵션, 없으면 안써도 됨)
*/
```

- ` with rollup` : 그룹별 소계, 전체 총계 구하고자 할 때 사용하며 , group by 다음에 사용
- 
