# DBMS, DB

파일 시스템 -> 데이터베이스

- 데이터 레이크(lake) : 정형/비정형 다양한 형태의 데이터 저장소 집합
  - 정형(데이터베이스)데이터
  - 비정형(이미지, 동영상, 센서, ...)데이터
- 데이터 웨어하우스(warehouse) : 데이터 창고
- 데이터 마트 : 데이터 웨어하우스의 부분(특정 목적/작업/부서에서 사용)


## 데이터 베이스의 종류

- 관계형, 계층형, 그래프형, ...
  - 관계형 : 데이터를 관계로 나타낸 데이터베이스(일반적인 데이터베이스)
    - SQLite : IoT, 데이터분석, 임베디드, 적은 규모 웹사이트에서 주로 사용되는 데이터베이스
    - 오라클, PostgreSQL, MariaDB ...
  - 계층형 : 데이터를 트리구조(계층)로 표현
  - 그래프형 : 데이터를 그래프로 표현
  - NoSQL : MongoDB, 카산드라, ...

---

- 테이블 = 관계 = 릴레이션(relation)
- 레코드 = 행 = 로우(low) = 튜플(tuple)
- 필드(field) = 열 = 컬럼(column) = 속성(attribute)
- SQL을 사용하여 DB접근(검색, 추가, 수정, 삭제)
- SQL은 RDBMS 구조의 데이터를 다루기 위해 사용하는 언어
- DDL(Data Define Language) : 데이터 정의어
- DML(Data Manipulation Language) : 데이터 조작어
- DCL(Data Control Language) : 데이터 제어어

```sql
-- 데이터 추가
INSERT INTO Person(ID, Name, Birthday) -- id는 기본키, not null
VALUES (1, '홍길동', '1997-01-02');	
/* id는 기본키,
 not null*/

INSERT INTO Person VALUES (2, '임꺽정', '1999-01-01')

DELETE (*) from Person;	-- 데이터 삭제, 데이터 구조는 남아있다.

select * from Person;	-- 데이터 선택

UPDATE Person SET name='이순신';    -- 데이터 변경

SELECT * FROM Person;   -- 데이터 모두 출력
```

