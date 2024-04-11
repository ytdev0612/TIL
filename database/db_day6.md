## 서브쿼리(Subquery)
- sql 내부에서 사용되는 select문
- 괄호 안에 기술, 복잡한 데이터 추출
- 서브쿼리가 먼저 실행된 후 메인 쿼리 실행

```sql
select * 
from 테이블명
where 컬럼=(select 컬럼명 from 테이블명);
```

- IN
- ANY
  -  서브쿼리의 각 결과에 대해 비교 했을때 최소 1건 이상 조건이 만족되는 자료를 추출
-  All
   -  여러 개의 조건 모두에 대해서 부합하면 추출


## DML(데이터 조작어)

- INSERT : 데이터를 추가
  - `INSERT INTO 테이블명 values()`
  - `INSERT INTO 테이블명(열) values (열)`

- UPDATE : 데이터를 변경
  - `UPDATE 테이블명 SET 컬럼 = 값, 컬럼 = 값 where 조건`

- DELETE : 데이터를 삭제
  - `DELETE FROM 테이블명 [WHERE 조건]`

```sql
/*
SELECT 문 수행 결과를 다른 테이블에 추가 
INSERT INTO 테이블명(컬럼1, 컬럼2, ...)
VALUES(값1, 값2, ...) 

insert into 테이블명(컬럼1, 컬럼2, ...)
select 컬럼1, 컬럼2, ...
from 테이블명
where 조건;
*/
```