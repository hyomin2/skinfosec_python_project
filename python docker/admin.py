
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


# id / pw -> admin / admin1234

# 관리자 로그인
def ad_login(uid, pw):
    if (uid == 'admin' and pw == 'admin1234'):
        return 1
    else:
        return 0

# 전체 회원 목록 조회
def all_user():
    mysql_connect()

    sql = 'select * from member;'

    try:
        cursor.execute(sql)
        result = cursor.fetchall()
        mysql_deconnect()
    except Exception as e:
        return 0
    else:
        return result


# 회원 검색
def user_search(u_search):
    s = '%' + u_search + '%'

    mysql_connect()

    sql = 'select * from member where id like %s or name like %s or email like %s;'
    val = (s, s, s)

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


# 전체 주문 목록
def all_orderList():
    mysql_connect()

    sql = 'select * from item_order;'

    try:
        cursor.execute(sql)
        result = cursor.fetchall()
        mysql_deconnect()
    except Exception as e:
        return e
    else:
        if not result:
            return 0
        else:
            return result


# 회원별 주문 목록
def user_orderList(search):
    mysql_connect()

    sql = 'select * from item_order where id = %s;'
    val = (search)

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


# 전체 주문 목록 검색
def order_search(search):
    s = '%' + search + '%'
    
    mysql_connect()
    
    sql = 'select * from item_order where iname like %s or order_name like %s or id like %s;'
    val = (s, s, s)

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


# 새로운 상품 추가
def add_item(name, price, qty):
    mysql_connect()

    now = datetime.now()
    f = '%Y-%m-%d'
    now2 = now.strftime(f)

    sql = 'insert into item(iname, iprice, iqty, i_date) values(%s, %s, %s, %s);'
    val = (name, price, qty, now2)

    try:
        cursor.execute(sql, val)
        mysql_deconnect()
    except Exception as e:
        return e
    else:
        return 1


# 상품 삭제
def del_item(icode):
    mysql_connect()
    sql = 'delete from item where icode = %s;'
    val = (icode)
    try:
        cursor.execute(sql, val)
        mysql_deconnect()
    except Exception as e:
        return e
    else:
        return 1
    

# 상품 이름 수정
def item_name_update(icode, name):
    mysql_connect()
    sql = 'update item set iname = %s where icode = %s;'
    val = (name, icode)
    try:
        cursor.execute(sql, val)
        mysql_deconnect()
    except Exception as e:
        return e
    else:
        return 1


# 상품 가격 수정
def item_price_update(icode, price):
    mysql_connect()
    sql = 'update item set iprice = %s where icode = %s;'
    val = (price, icode)
    try:
        cursor.execute(sql, val)
        mysql_deconnect()
    except Exception as e:
        return e
    else:
        return 1


# 상품 수량 수정
def item_qty_update(icode, qty):
    mysql_connect()
    sql = 'update item set iqty = %s where icode = %s;'
    val = (qty, icode)
    try:
        cursor.execute(sql, val)
        mysql_deconnect()
    except Exception as e:
        return e
    else:
        return 1


# icode -> 해당 item 반환
def one_item(icode):
    mysql_connect()
    sql = 'select * from item where icode = %s;'
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
    



# 월별 가장 많은 금액 사용자 목록
def month_order_user(date):
    mysql_connect()
    sql = "select * from item_order where order_price = (select MAX(order_price) from item_order where order_date LIKE %s);"
    val = (date+'%')

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

# 주별 가장 많은 금액 사용자 목록
def date_order_user(date, d):
    d1 = ''
    d2 = ''
    if d == 1:
        d1 = '01'
        d2 = '07'
    elif d == 2:
        d1 = '08'
        d2 = '14'
    elif d == 3:
        d1 = '15'
        d2 = '21'
    elif d == 4:
        d1 == '22'
        d2 == '31'
    mysql_connect()
    sql = "select * from item_order where order_price = (select MAX(order_price) from item_order where order_date BETWEEN %s AND %s);"
    val = (date+d1, date+d2)
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


# 월별 가장 많이 주문된 상품 목록
def month_order_item(date):
    mysql_connect()
    sql = "SELECT icode, COUNT(*) fROM item_order WHERE order_date LIKE %s GROUP BY icode HAVING COUNT(*) > 1 LIMIT 1;"
    val = (date+'%')

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


# 주별 가장 많이 주문된 상품 목록
def date_order_item(date, d):
    d1 = ''
    d2 = ''
    if d == 1:
        d1 = '01'
        d2 = '07'
    elif d == 2:
        d1 = '08'
        d2 = '14'
    elif d == 3:
        d1 = '15'
        d2 = '21'
    elif d == 4:
        d1 == '22'
        d2 == '31'
    mysql_connect()
    sql = "SELECT icode, COUNT(*) fROM item_order WHERE order_date BETWEEN %s AND %s GROUP BY icode HAVING COUNT(*) > 1 LIMIT 1;"
    val = (date+d1, date+d2)
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