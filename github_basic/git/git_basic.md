# git 기초

## 개념
- VCS(Version Control System)
- Git 과 Github는 다르다
- Open Source
- Git
  - Woring Directory
  - Stage
  - Commit


## 기초 명령어
```

$ git init
$ git config --global user.name 'Name'
$ git config --global user.email 'Email'
  (PC마다 1번만 등록(Name, Email)하면 계속 사용가능하다.)
$ git add <file>
$ git commit -m 'Message'

```

- `git status` : 현재 상태 확인
- `git log` : 전체 로그 확인, `git log --oneline`
- `git add` : 저장소에 코드 추가, `git add .`
- `git add -A` : 커밋에 파일의 변경 사항을 한번에 모두 포함
- `git commit -m ''message` : 커밋 생성 '메세지'
- `touch <file>` : 해당 위치에 파일 생성

```
Ex)
1. d.md 를 생성한다.
    - $ touch d.md

2. commit 한다 (creadte d.md)
    - $ git add d.md
    - $ git commit -m'create d.md'

3. 모든 마크다운 파일들을 수정한다(내용은 따로)
4. a.md, b.md 만 커밋한다.(a, b)
    - $ git commit -m'a, b'
5. c.md, d.md 만 커밋한다. (c, d)
    = $ git commit -m'c, d'
6. 모든 마크다운 파일들을 수정한다.
7. 모든 파일들을 한번에 커밋한다. 

```
