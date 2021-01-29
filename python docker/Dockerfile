# FROM python:3.7.9-alpine3.12
FROM python:3.8

WORKDIR /usr/src
RUN pip install pymysql

COPY ./main.py ./
COPY ./user.py ./
COPY ./admin.py ./
COPY ./user_func.py ./
COPY ./admin_func.py ./

CMD ["python", "main.py"]