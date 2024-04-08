- `order by asc|desc` : asc는 오름차순, desc는 내림차순으로 정렬한다.
- asc는 기본 값으로 생략해도 자동으로 적용되며 열 이름 대신에 별명 or 컬럼의 순서를 넣어도 작동한다.

- `UPDATE 테이블명 SET 열 = 값 WHERE 조건식`

```sql
/* % : 문자 여러개, _ : 문자 1개 */

select * from 고객
where 도시 like '대전광역시';
/* like만 사용된 경우에는 = 기호와 같은 의미 
select * from 고객
where 도시 = '대전광역시';
*/

select * from 고객
where 도시 like '%인천%';

select * from 고객
where 도시 like '__특%';
```

