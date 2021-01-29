# skinfosec_python_project
sk인포섹 - 파이썬 모듈프로젝트
작성자 : 

< 필독사항 >

0. cmd 실행 명령어
 - Mysql
	- mysql_dockerfile 폴더로 이동 (dockerfile이 존재하는 곳)
	- docker build -t hyomin_mysql:8.0
	- docker run -d -p 13306:3306 --name hyomin_mysql hyomin_mysql:8.0
 - Python
	- python_dockerfile 폴더로 이동 (dockerfile이 존재하는 곳)
	- docker build -t hyomin_python:3.8 .
	- docker run -it hyomin_python:3.8


1. 도커 허브 사이트 각 url 및 커맨드 pull 명령어
 - mysql
	- https://hub.docker.com/r/bigjoy22/hyomin_mysql
	- docker pull bigjoy22/hyomin_mysql:8.0
 - Python
	- https://hub.docker.com/r/bigjoy22/hyomin_python
	- docker pull bigjoy22/hyomin_python:3.8


2. 포트 및 ip주소
	- mysql은 13306:3306으로 실행

	- python에서 mysql로 접속할때
		- ip주소 : 172.17.0.2
		- 포트번호 : 3306 으로 설정되어 있습니다.
		- user.py 와 admin.py 2개의 파일 최상단에 mysql 연결 설정이 존재합니다.

3. 프로그램 구동 영상 유튜브 링크 : https://youtu.be/m26ccDVykBY
