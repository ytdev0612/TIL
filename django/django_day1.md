- django 설치
  - cd\
  - mkdir venvs
  - cd venvs
  - python -m venv mysite
  - cd mysite
  - cd Scripts
  - activate/deactivate
  - pip install django==4.0.3

- django 실행
  - cd\
  - mkdir projects
  - cd projects
  - c:\venvs\mysite\Scripts\activate
  - mkdir mysite
  - cd mysite
  - django-admin startproject config .
  - python manage.py runserver
  - http://127.0.0.1:8000/ 접속해서 확인


- 환경변수에 c:\venvs 추가
- mysite.bat파일을 통해서 어디서든 `mysite`만 치면 바로 가상환경이 실행되도록 설정
```
@echo off
cd c:/projects/mysite
c:/venvs/mysite/scripts/activate
```

1. cmd
2. cd\
3. mkdir venvs
4.cd venvs
5. python -m venv mysite

---------------------가상환경 생성---------------

6.cd my*
7.cd Scr*
8.activate
(mysite) C:\venvs\mysite\Scripts>

--------------------가상환경에 입장--------------

9.pip install django==3.1.3
1.  python -m pip install --upgrade pip

------------------장고설치&pip업그레이드-------

1.  cd\
2.  mkdir project
3.  cd project

------------프로젝트 디렉토리 생성----------------

1.  exit
2.  cmd
3.  C:\Users\i>cd\project
4.  C:\project>C:\venvs\mysite\Scripts\activate
18.(mysite) C:\project>mkdir mysite
19.(mysite) C:\project>cd mysite
20.(mysite) C:\project\mysite>django-admin startproject config .
21.(mysite) C:\project\mysite>deactivate
1.  C:\project\mysite>dir/w 명령 수행시, [config]와 manage.py가 있어야 함.
2.  cd con*
3.  C:\project\mysite\config>dir/w

--------------프로젝트 구성 완료----------------------

===============================================
장고 웹 서버 구동
1. C:\venvs\mysite\Scripts\activate
2. (mysite) C:\project\mysite\config>cd..
3. (mysite) C:\project\mysite>python manage.py runserver
Watching for...
You have 18 unapplied migration(s)....
Django version 3.1.3, using settings 'config.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.


4. 웹브라우저를 띄운 후 
http://127.0.0.1:8000/ 주소를 입력