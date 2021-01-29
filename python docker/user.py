
import pymysql
from datetime import datetime, timezone



# mysql 연결
def mysql_connect():
    global conn
    conn = pymysql.connect(host='172.17.0.2', user='root', password='', port=3306, db='hyomin_db', charset='utf8')
    global cursor
    cursor = conn.cursor()

# mysql 연결해제
def mysql_deconnect():
    conn.commit()
    cursor.close()
    conn.close()

# id 중복체크 - 회원가입 시
def id_check(uid):
    mysql_connect()

    sql = 'select * from member where id = %s;'

    try:
        cursor.execute(sql, (uid))
        result = cursor.fetchall()
        mysql_deconnect()
    except Exception as e:
        return e
    else:
        if result:
            # print('중복')
            return 0 # 중복 id 없음 
        else:
            # print('성공')
            return 1 # 중복 id 존재


# 회원가입
def join(uid, pw, name, email, qn, answer):
    mysql_connect()

    now = datetime.now()
    f = '%Y-%m-%d'
    now2 = now.strftime(f)

    sql = 'insert into member(id, pw, name, email, u_date, question, answer) values (%s, %s, %s, %s, %s, %s, %s);'
    val = (uid, pw, name, email, now2, qn, answer)
    
    try:  # 예외가 발생할 가능성이 있는 코드
        cursor.execute(sql, val)
    except Exception as e: # 예외 발생시 실행하는 코드
        mysql_deconnect()
        return e
    else: # 예외가 발생하지 않았을 때 실행하는 코드
        mysql_deconnect()
        return 1

# 로그인
def login(uid, pw):
    mysql_connect()

    # 회원 존재 여부 sql
    sql = 'select id, name from member where id = %s and pw = %s;'
    val = (uid, pw)

    try:
        cursor.execute(sql, val)
        result = cursor.fetchall()
        mysql_deconnect()
    except Exception as e: # 예외 발생시 실행하는 코드
        return e
    else:
        if not result:
            return 0 # 회원 없음
        else:
            return result # 로그인 성공


# 아이디 찾기
def id_find(email, name):
    mysql_connect()

    sql = 'select id from member where name = %s and email = %s;'
    try:
        cursor.execute(sql, (name, email))
        result = cursor.fetchone()
        mysql_deconnect()
    except Exception as e:
        return 0
    else:
        if not result:
            return 0
        else:
            return result



# 본인확인 질문 / 답변 전송
def qna_find(uid, name):
    mysql_connect()

    sql = 'select question, answer from member where id = %s and name = %s;'

    try:
        cursor.execute(sql, (uid, name))
        result = cursor.fetchall()
        mysql_deconnect()
    except Exception as e:
        return 0
    else:
        if not result:
            return 0
        else:
            return result


# 내 정보 목록
def my_data(uid):
    mysql_connect()
    sql = 'select * from member where id = %s;'
    val = (uid)
    try:
        cursor.execute(sql, val)
        result = cursor.fetchall()
    except Exception as e: # 예외 발생시 실행하는 코드
        mysql_deconnect()
        return e
    else:
        mysql_deconnect()
        return result


# 비밀번호 변경
def pw_change(uid, pw):
    mysql_connect()

    sql = 'update member set pw = %s where id = %s;'
    val = (pw, uid)

    try:
        cursor.execute(sql, val)
    except Exception as e: # 예외 발생시 실행하는 코드
        mysql_deconnect()
        return e
    else:
        mysql_deconnect()
        return 1

# 이름 변경
def name_change(uid, name):
    mysql_connect()

    sql = 'update member set name = %s where id = %s;'
    val = (name, uid)

    try:
        cursor.execute(sql, val)
    except Exception as e: # 예외 발생시 실행하는 코드
        mysql_deconnect()
        return e
    else:
        mysql_deconnect()
        return 1


# 이메일 변경
def email_change(uid, email):
    mysql_connect()

    sql = 'update member set email = %s where id = %s;'
    val = (email, uid)

    try:
        cursor.execute(sql, val)
    except Exception as e: # 예외 발생시 실행하는 코드
        mysql_deconnect()
        return e
    else:
        mysql_deconnect()
        return 1

# 본인확인 질문 답변 변경
def qna_change(uid, qn, answer):
    mysql_connect()

    sql = 'update member set question = %s, answer = %s where id = %s;'
    val = (qn, answer, uid)

    try:
        cursor.execute(sql, val)
    except Exception as e: # 예외 발생시 실행하는 코드
        mysql_deconnect()
        return e
    else:
        mysql_deconnect()
        return 1


# 회원 탈퇴 
def user_del(uid):
    mysql_connect()

    sql = 'delete from member where id = %s;'
    val = (uid)

    try:
        cursor.execute(sql, val)
    except Exception as e:
        mysql_deconnect()
        return 0
    else:
        mysql_deconnect()
        return 1


# 내 주문 목록 조회
def my_order(uid):
    mysql_connect()

    sql = 'select * from item_order where id = %s;'
    val = (uid)

    try:
        cursor.execute(sql, val)
        result = cursor.fetchall()
    except Exception as e:
        mysql_deconnect()
        return e
    else:
        mysql_deconnect()
        return result



# 상품 목록 보기
def item_list():
    mysql_connect()

    sql = 'select * from item;'
    
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
    except Exception as e:
        mysql_deconnect()
        return 0
    else:
        mysql_deconnect()
        return result


# 상품 검색
def item_search(i_name):
    s_name = '%' + i_name + '%'
    mysql_connect()
    sql = 'select * from item where iname like %s;'
    val = (s_name)
    try:
        cursor.execute(sql, val)
        result = cursor.fetchall()
        mysql_deconnect()
    except Exception as e:
        return 0
    else:
        if not result:
            return 0
        else:
            return result


# 상품 존재 유무 및 재고 판단
def item_check(iname):
    mysql_connect()
    sql = 'select * from item where icode = %s;'
    val = iname

    try:
        cursor.execute(sql, val)
        result = cursor.fetchall()
        mysql_deconnect()
    except Exception as e:
        return e
    else:
        if not result:
            return 0
        elif result[0][3] == 0:
            return 1
        else:
            return result


# 상품 주문
def order_item(uid, name, icode, iname, iprice, order_qty, order_price):
    mysql_connect()
    sql = 'insert into item_order(id, order_name, icode, iname, iprice, order_qty, order_price, order_date) values (%s, %s, %s, %s, %s, %s, %s, %s);'
    now = datetime.now()
    f = '%Y-%m-%d'
    now2 = now.strftime(f)
    val = (uid, name, icode, iname, iprice, order_qty, order_price, now2)
    try:
        cursor.execute(sql, val)
        mysql_deconnect()
    except Exception as e:
        return e
    else:
        mysql_connect()
        sql2 = 'update item set iqty = iqty - %s where icode = %s;'
        val2 = (order_qty, icode)
        try:
            cursor.execute(sql2, val2)
            mysql_deconnect()
        except Exception as e2:
            return e2
        else:
            return 1


# 위시리스트 목록
def my_wishlist(uid):
    mysql_connect()
    sql = 'SELECT * from item where icode IN (SELECT icode FROM wishlist where id = %s);'
    val = (uid)
    try:
        cursor.execute(sql, val)
        result = cursor.fetchall()
        mysql_deconnect()
    except Exception as e:
        return 0
    else:
        if not result:
            return 0
        else:
            return result


# 위시리스트 추가
def add_wishlist(uid, icode):
    mysql_connect()
    sql = 'select * from wishlist where id = %s and icode = %s;'
    val = (uid, icode)
    try:
        cursor.execute(sql, val)
        result = cursor.fetchall()
        mysql_deconnect()
    except Exception as e:
        return e
    else:
        if not result:
            mysql_connect()
            sql2 = 'insert into wishlist(id, icode) values(%s, %s);'
            val2 = (uid, icode)
            try:
                cursor.execute(sql2, val2)
                mysql_deconnect()
            except Exception as e2:
                return 0 # 실패
            else:
                return 1 # 성공
        else:
            return 2 # 이미 위시리시트에 존재


# 위시리스트 삭제
def del_wishlist(uid, icode):
    mysql_connect()
    sql = 'delete from wishlist where id = %s and icode = %s;'
    val = (uid, icode)
    try:
        cursor.execute(sql, val)
        mysql_deconnect()
    except Exception as e:
        return e
    else:
        return 1


# 해당 상품 리뷰 가져오기
def review_list(icode):
    mysql_connect()
    sql = 'select * from review where icode = %s;'
    val = (icode)
    try:
        cursor.execute(sql, val)
        result = cursor.fetchall()
        mysql_deconnect()
    except Exception as e:
        return e
    else:
        if not result:
            return 0
        else:
            return result



# 내가 작성한 리뷰 목록
def review_my(uid):
    mysql_connect()
    sql = 'select * from review where id = %s;'
    val = (uid)
    try:
        cursor.execute(sql, val)
        result = cursor.fetchall()
        mysql_deconnect()
    except Exception as e:
        return e
    else:
        if not result:
            return 0
        else:
            return result



# 새로운 리뷰 작성
def new_review(uid, icode, name, text):
    mysql_connect()
    sql = 'select * from item_order where id = %s and icode = %s;'
    val = (uid, icode)
    try:
        cursor.execute(sql, val)
        result = cursor.fetchall()
        mysql_deconnect()
    except Exception as e:
        return e
    else:
        if not result:
            return 0 # 해당 상품을 주문한 내역이 없음
        else:
            now = datetime.now()
            f = '%Y-%m-%d'
            now2 = now.strftime(f)
            mysql_connect()
            sql2 = 'insert into review(icode, id, name, rtext, r_date) values(%s, %s, %s, %s, %s);'
            val2 = (icode, uid, name, text, now2)
            try:
                cursor.execute(sql2, val2)
                mysql_deconnect()
            except Exception as e2:
                return e2
            else:
                return 1 # 리뷰 작성 성공


# 리뷰 삭제 
def del_review(uid, icode):
    mysql_connect()
    sql = 'delete from review where id = %s and icode = %s;'
    val = (uid, icode)
    try:
        cursor.execute(sql, val)
        mysql_deconnect()
    except Exception as e:
        return e
    else:
        return 1

