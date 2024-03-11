# git 기초

## 개념
- VCS(Version Control System)
- Git VS Github
- Open source
- Git
  - Working Directory
  - Stage
  - Commit

## 명령어
'''
$ git init : 프로젝트 최초 1회(폴더 -> 리포)

$ git config --global user.name 'NAME'
$ git config --global user.email 'EMAIL' : 컴퓨터(계정)당 1회 위의 2개

$ git add <file> : 스테이징

$ git commit -m 'MESSAGE' : 커밋 생성
'''

- `git status` : 현재 상태 확인
- `git log` : 전체 로그 확인, `git log --oneline`
- `git add` : 저장소에 코드 추가, `git add .`
- `git add -A` : 커밋에 파일의 변경 사항을 한번에 모두 포함
- `git commit -m ''message` : 커밋 생성 '메세지'
- 