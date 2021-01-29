
import admin
import user

class Admin_function:

    # 메인 메뉴로 돌아가기
    def back_menu(self):
        import main
        m = main.Main_function()
        m.main_menu()

    # 관리자 로그인
    def admin_login(self):

        print('')
        print('*' * 30)
        print('관리자 로그인')
        print('*' * 30)
        uid = ''
        pw = ''
        while True:
            try:
                uid = input('아이디 : ')
                pw = input('비밀번호 : ')
            except Exception:
                print('로그인 실패, 올바르게 입력하세요.')
            
            if uid == '' or pw == '':
                print('아이디 / 비밀번호를 입력해주세요.')
            elif len(uid) > 15 or len(pw) > 20:
                print('아이디 혹은 비밀번호가 너무 깁니다.')
            else:
                break

        r = admin.ad_login(uid, pw)
        if r == 0:
            print('아이디 혹은 비밀번호가 틀렸습니다.')
            self.back_menu()
        elif r == 1:
            print('관리자 로그인 성공')
            self.admin_menu()


    # 관리자 서비스 메뉴
    def admin_menu(self):
        print('')
        print('*' * 20)
        print('0. 메인메뉴 돌아가기')
        print('1. 전체 회원 목록')
        print('2. 회원 검색')
        print('3. 전체 주문 목록')
        print('4. 회원 별 주문 목록')
        print('5. 주문 목록 검색')
        print('6. 상품 목록')
        print('7. 상품 추가')
        print('8. 상품 수정')
        print('9. 상품 삭제')
        print('10. 날짜별 최대 주문자')
        print('11. 날짜별 최대 주문 상품')
        print('*' * 20)

        num = -1

        while True:
            try:
                num = int(input('메뉴 선택 : '))
            except Exception:
                print('숫자를 입력하세요.')
            
            if num >= 0 and num < 12:
                break
            else:
                print('메뉴를 올바르게 선택해주세요. (0~9)')
        if num == 0:
            self.back_menu()
        elif num == 1:
            self.all_users()
        elif num == 2:
            self.search_users()
        elif num == 3:
            self.all_orders()
        elif num == 4:
            self.user_orderList()
        elif num == 5:
            self.search_itemorder()
        elif num == 6:
            self.all_items()
        elif num == 7:
            self.add_items()
        elif num == 8:
            self.item_update()
        elif num == 9:
            self.item_del()
        elif num == 10:
            self.max_user()
        elif num == 11:
            self.max_item()
        


    # 1. 전체 회원 목록
    def all_users(self):
        r = admin.all_user()
        print('')
        print('{:^15s} {:^10s} {:^10s} {:^12s} {:^25s} {:^15s} {:^25s}'.format(
            'ID', 'Password','name', 'create_Date', 'Question', 'Answer', 'E-mail'))
        print('- ' * 70)
        for i, p, n, cd, q, a, e in r:
            print(f'{i:^15s} {p:^10s} {n:^10s} {cd:^12s} {q:^25s} {a:^15s} {e:^25s}')
        self.admin_menu()


    # 2. 회원 검색
    def search_users(self):
        print('')
        print('*' * 20)
        print('# 회원 검색')
        print('*' * 20)
        print('')
        s_t = ''

        while True:
            try:
                s_t = input('검색 입력 : ')
            except Exception:
                print('검색 실패')
            
            if len(s_t) < 2:
                print('검색어는 최소 2개이상 입력해야합니다.')
            else:
                break
        r = admin.user_search(s_t)
        if r == 0:
            print('검색 결과가 존재하지 않습니다.')
        else:
            print('')
            print('{:^15s} {:^10s} {:^10s} {:^12s} {:^25s} {:^15s} {:^25s}'.format(
                'ID', 'Password','name', 'create_Date', 'Question', 'Answer', 'E-mail'))
            print('- ' * 70)
            for i, p, n, cd, q, a, e in r:
                print(f'{i:^15s} {p:^10s} {n:^10s} {cd:^12s} {q:^25s} {a:^15s} {e:^25s}')
        self.admin_menu()


    # 3. 전체 주문 목록
    def all_orders(self):

        r = admin.all_orderList()
        print('')
        print('< ' * 20 + '전체 주문 목록' + ' >' * 20)
        print('{:^6s} {:^16s} {:^12s} {:^6s} {:^20s} {:^10s} {:^8s} {:^10s} {:^12s}'.format(
            'ocode', 'id','order_name', 'icode', 'iname', 'iprice', 'order_qty', 'order_price', 'order_date'))
        print('- ' * 40)
        for ocode, i, name, icode, iname, iprice, o_qty, o_price, o_date in r:
            print(f'{ocode:^6d} {i:^16s} {name:^12s} {icode:^6d} {iname:^20s} {iprice:^10d} {o_qty:^8d} {o_price:^10d} {o_date:^12s}')
        self.admin_menu()


    # 4. 회원 별 주문 목록
    def user_orderList(self):
        print('')
        print('*' * 20)
        print('# 회원 별 주문 목록')
        print('*' * 20)
        print('')

        uid = ''
        while True:
            try:
                uid = input('주문 목록을 볼 회원 아이디 : ')
            except Exception:
                print('올바르게 입력하세요')
            
            if uid == '':
                print('아이디를 입력해주세요.')
            else:
                break
        r = admin.user_orderList(uid)
        if r == 0:
            print('주문 검색 결과가 없습니다.')
        else:
            print('< ' * 20 + uid + ' 회원 주문 목록' + ' >' * 20)
            print('{:^6s} {:^16s} {:^12s} {:^6s} {:^20s} {:^10s} {:^8s} {:^10s} {:^12s}'.format(
                'ocode', 'id','order_name', 'icode', 'iname', 'iprice', 'order_qty', 'order_price', 'order_date'))
            print('- ' * 40)
            for ocode, i, name, icode, iname, iprice, o_qty, o_price, o_date in r:
                print(f'{ocode:^6d} {i:^16s} {name:^12s} {icode:^6d} {iname:^20s} {iprice:^10d} {o_qty:^8d} {o_price:^10d} {o_date:^12s}')
        self.admin_menu()


    # 5. 주문 목록 검색
    def search_itemorder(self):
        print('')
        print('*' * 20)
        print('# 주문 목록 검색')
        print('*' * 20)
        print('')

        t = ''
        while True:
            try:
                t = input('주문 목록 검색 : ')
            except Exception:
                print('올바르게 입력하세요')
            
            if t == '':
                print('검색어를 입력해주세요.')
            elif len(t) < 2:
                print('검색어는 최소 2글자 이상 입력해주세요.')
            else:
                break
        r = admin.order_search(t)
        if r == 0:
            print('검색 결과가 없습니다.')
        else:
            print('< ' * 20 + t + ' 검색 주문 목록' + ' >' * 20)
            print('{:^6s} {:^16s} {:^12s} {:^6s} {:^20s} {:^10s} {:^8s} {:^10s} {:^12s}'.format(
                'ocode', 'id','order_name', 'icode', 'iname', 'iprice', 'order_qty', 'order_price', 'order_date'))
            print('- ' * 40)
            for ocode, i, name, icode, iname, iprice, o_qty, o_price, o_date in r:
                print(f'{ocode:^6d} {i:^16s} {name:^12s} {icode:^6d} {iname:^20s} {iprice:^10d} {o_qty:^8d} {o_price:^10d} {o_date:^12s}')
        self.admin_menu()


    # 6. 상품 목록
    def all_items(self):
        result = user.item_list()
        if result == 0:
            print('현재 상품이 없습니다.')
        else:
            print('')
            print('{:^10s} {:^20s} {:^10s} {:^6s} {:^12s}'.format(
                'icode', 'iname','iprice', 'iqty', 'item_date'))
            print('- ' * 40)
            for i, n, p, q, d in result:
                print(f'{i:^10d} {n:^20s} {p:^10d} {q:^6d} {d:^12s}')
        self.admin_menu()


    
    # 7. 상품 추가
    def add_items(self):
        print('')
        print('*' * 20)
        print('# 상품 추가')
        print('*' * 20)
        print('')
        name = ''
        price = 0
        qty = 0

        while True:
            try:
                name = input('상품 이름 : ')
                price = int(input('상품 가격 : '))
                qty = int(input('상품 초기 개수 : '))
            except Exception:
                print('올바르게 입력해주세요.')
            
            if name == '':
                print('상품 이름을 입력해주세요.')
            else:
                break
        r = admin.add_item(name, price, qty)
        if r == 1:
            print('상품 추가 성공')
        else:
            print('상품 추가 실패')
        self.admin_menu()


    # 8. 상품 수정
    def item_update(self):
        print('')
        print('*' * 20)
        print('# 상품 수정')
        print('*' * 20)
        print('')

        icode = 0
        while True:
            try:
                icode = int(input('수정할 상품 코드 : '))
            except Exception:
                print('상품 코드를 올바르게 입력해주세요.')
            if icode == 0:
                print('상품 코드를 입력해주세요.')
                self.admin_menu()
            else:
                break
        r = admin.one_item(icode)
        if r == 0:
            print('해당 코드에 맞는 상품이 없습니다.')
            self.admin_menu()
        else:
            print('')
            print('{:^10s} {:^20s} {:^10s} {:^6s} {:^12s}'.format(
                'icode', 'iname','iprice', 'iqty', 'item_date'))
            print('- ' * 40)
            for i, n, p, q, d in r:
                print(f'{i:^10d} {n:^20s} {p:^10d} {q:^6d} {d:^12s}')
        
        print('')
        print('*' * 30)
        print('### 상품 수정 메뉴 ###')
        print('0. 관리자 메뉴로 돌아가기')
        print('1. 상품 이름 수정')
        print('2. 상품 가격 수정')
        print('3. 상품 수량 수정')
        print('*' * 30)
        num = -1
        while True:
            try:
                num = int(input('메뉴 선택 : '))
            except Exception:
                print('숫자를 입력해주세요. (0~3)')
            
            if num >=0 and num < 4:
                break
            else:
                print('올바른 메뉴를 선택하세요. (0~3)')
        
        if num == 0:
            self.admin_menu()
        elif num == 1:
            self.item_name_update(icode)
        elif num == 2:
            self.item_price_update(icode)
        elif num == 3:
            self.item_qty_update(icode)


    # 8-1 상품 이름 수정
    def item_name_update(self, icode):
        name = ''
        while True:
            try:
                name = input('수정 이름 : ')
            except Exception:
                print('올바르게 입력해주세요.')
            
            if name == '':
                print('수정할 이름을 입력해주세요.')
            else:
                break
        r = admin.item_name_update(icode, name)
        if r == 1:
            print('상품 이름 수정 완료')
        else:
            print('상품 이름 수정 실패', r)
        self.admin_menu()

    # 8-1 상품 가격 수정
    def item_price_update(self, icode):
        price = 0
        while True:
            try:
                price = int(input('수정 가격 : '))
            except Exception:
                print('가격을 입력해주세요.')
            
            if price < 10:
                print('가격은 10원 이상이어야 합니다..')
            else:
                break
        r = admin.item_price_update(icode, price)
        if r == 1:
            print('상품 가격 수정 완료')
        else:
            print('상품 가격 수정 실패', r)
        self.admin_menu()

    # 8-3 상품 수량 수정
    def item_qty_update(self, icode):
        qty = -1
        while True:
            try:
                qty = int(input('수정 수량 : '))
            except Exception:
                print('수량을 입력해주세요.')
            
            if qty < 0:
                print('수량은 0개 이상이어야 합니다.')
            else:
                break
        r = admin.item_qty_update(icode, qty)
        if r == 1:
            print('상품 수량 수정 완료')
        else:
            print('상품 수량 수정 실패', r)
        self.admin_menu()


    # 9. 상품 삭제
    def item_del(self):
        print('')
        print('*' * 20)
        print('# 상품 삭제')
        print('*' * 20)
        print('')
        icode = 0
        while True:
            try:
                icode = int(input('삭제할 상품 코드 : '))
            except Exception:
                print('상품 코드를 입력해주세요.')
                self.admin_menu()

            if icode == 0:
                print('상품 코드를 입력해주세요.')
                self.admin_menu()
            else:
                break
        
        r = admin.del_item(icode)
        if r == 1:
            print('상품 삭제 완료')
        else:
            print('상품 삭제 실패', r)
        self.admin_menu()


    # 10. 날짜별 최대 주문금액 사용자
    def max_user(self):
        print('')
        print('*' * 30)
        print('### 최대 구매자 보기 ###')
        print('0. 관리자 메뉴 돌아가기')
        print('1. 월 별 최대 구매자')
        print('2. 주 별 최대 구매자')
        print('*' * 30)
        print('')
        num = -1
        while True:
            try:
                num = int(input('메뉴 선택 : '))
            except Exception:
                print('숫자를 입력하세요.')
            
            if num >= 0 and num < 3:
                break
            else:
                print('올바른 메뉴를 선택해주세요.')
        
        if num == 0:
            self.admin_menu()
        elif num == 1:
            y = 0
            m = 0
            while True:
                try:
                    y = int(input('탐색 년도 : '))
                    m = int(input('탐색 월 : '))
                except Exception:
                    print('숫자를 정확히 입력해주세요.')
                if y == 0 or m == 0:
                    print('0은 입력할 수 없습니다.')
                elif m > 12:
                    print('월은 1~12까지 입력해주세요.')
                else:
                    break
            if m < 10:
                m = '0' + str(m)
            date = str(y) + '-' + m
            r = admin.month_order_user(date)
            if r == 0:
                print('해당날짜에는 주문내역이 없습니다.', r)
                self.admin_menu()
            else:
                print('')
                print('< ' * 20 + date +' 최대 주문자 목록' + ' >' * 20)
                print('{:^6s} {:^16s} {:^12s} {:^6s} {:^20s} {:^10s} {:^8s} {:^10s} {:^12s}'.format(
                    'ocode', 'id','order_name', 'icode', 'iname', 'iprice', 'order_qty', 'order_price', 'order_date'))
                print('- ' * 40)
                for ocode, i, name, icode, iname, iprice, o_qty, o_price, o_date in r:
                    print(f'{ocode:^6d} {i:^16s} {name:^12s} {icode:^6d} {iname:^20s} {iprice:^10d} {o_qty:^8d} {o_price:^10d} {o_date:^12s}')
                self.admin_menu()
        elif num == 2:
            y = 0
            m = 0
            d = 0
            while True:
                try:
                    y = int(input('탐색 년도 : '))
                    m = int(input('탐색 월 : '))
                    d = int(input('탐색 주차(1~4주) : '))
                except Exception:
                    print('숫자를 정확히 입력해주세요.')
                if y == 0 or m == 0 or d == 0:
                    print('0은 입력할 수 없습니다.')
                elif m > 12:
                    print('월은 1~12까지 입력해주세요.')
                elif d > 4:
                    print('주는 1~4주차를 입력해주세요.')
                else:
                    break
            if m < 10:
                m = '0' + str(m)
            date = str(y) + '-' + m + '-'
            r = admin.date_order_user(date, d)
            if r == 0:
                print('해당날짜에는 주문내역이 없습니다.')
                self.admin_menu()
            else:
                print('')
                print('< ' * 20 + date + str(d) +'주차 최대 주문자 목록' + ' >' * 20)
                print('{:^6s} {:^16s} {:^12s} {:^6s} {:^20s} {:^10s} {:^8s} {:^10s} {:^12s}'.format(
                    'ocode', 'id','order_name', 'icode', 'iname', 'iprice', 'order_qty', 'order_price', 'order_date'))
                print('- ' * 40)
                for ocode, i, name, icode, iname, iprice, o_qty, o_price, o_date in r:
                    print(f'{ocode:^6d} {i:^16s} {name:^12s} {icode:^6d} {iname:^20s} {iprice:^10d} {o_qty:^8d} {o_price:^10d} {o_date:^12s}')
                self.admin_menu()


    # 11. 날짜별 최대 주문된 상품
    def max_item(self):
        print('')
        print('*' * 30)
        print('### 최대 주문상품 보기 ###')
        print('0. 관리자 메뉴 돌아가기')
        print('1. 월 별 최대 주문상품')
        print('2. 주 별 최대 주문상품')
        print('*' * 30)
        print('')
        num = -1
        while True:
            try:
                num = int(input('메뉴 선택 : '))
            except Exception:
                print('숫자를 입력하세요.')
            
            if num >= 0 and num < 3:
                break
            else:
                print('올바른 메뉴를 선택해주세요.')
        
        if num == 0:
            self.admin_menu()
        elif num == 1:
            y = 0
            m = 0
            while True:
                try:
                    y = int(input('탐색 년도 : '))
                    m = int(input('탐색 월 : '))
                except Exception:
                    print('숫자를 정확히 입력해주세요.')
                if y == 0 or m == 0:
                    print('0은 입력할 수 없습니다.')
                elif m > 12:
                    print('월은 1~12까지 입력해주세요.')
                else:
                    break
            if m < 10:
                m = '0' + str(m)
            date = str(y) + '-' + m
            r = admin.month_order_item(date)
            if r == 0:
                print('해당날짜에는 주문내역이 없습니다.', r)
                self.admin_menu()
            else:
                r2 = admin.one_item(r[0][0])
                print('')
                print('< ' * 10 + date +' 최대 주문 상품' + ' >' * 10)
                print('{:^10s} {:^20s} {:^10s} {:^6s} {:^12s}'.format(
                    'icode', 'iname','iprice', 'count', 'item_date'))
                print('- ' * 40)
                for i, n, p, q, d in r2:
                    print(f'{i:^10d} {n:^20s} {p:^10d} {r[0][1]:^6d} {d:^12s}')
                self.admin_menu()
        elif num == 2:
            y = 0
            m = 0
            d = 0
            while True:
                try:
                    y = int(input('탐색 년도 : '))
                    m = int(input('탐색 월 : '))
                    d = int(input('탐색 주차(1~4주) : '))
                except Exception:
                    print('숫자를 정확히 입력해주세요.')
                if y == 0 or m == 0 or d == 0:
                    print('0은 입력할 수 없습니다.')
                elif m > 12:
                    print('월은 1~12까지 입력해주세요.')
                elif d > 4:
                    print('주는 1~4주차를 입력해주세요.')
                else:
                    break
            if m < 10:
                m = '0' + str(m)
            date = str(y) + '-' + m + '-'
            r = admin.date_order_item(date, d)
            if r == 0:
                print('해당날짜에는 주문내역이 없습니다.')
                self.admin_menu()
            else:
                r2 = admin.one_item(r[0][0])
                print('')
                print('< ' * 10 + date + str(d) +'주차 최대 주문 상품' + ' >' * 10)
                print('{:^10s} {:^20s} {:^10s} {:^6s} {:^12s}'.format(
                    'icode', 'iname','iprice', 'count', 'item_date'))
                print('- ' * 40)
                for i, n, p, q, d in r2:
                    print(f'{i:^10d} {n:^20s} {p:^10d} {r[0][1]:^6d} {d:^12s}')
                self.admin_menu()