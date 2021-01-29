
import user

class User_function:

    def __init__(self):
        self.cache_id = ''
        self.name = ''
    # 메인 메뉴로 돌아가기
    def back_menu(self):
        import main
        m = main.Main_function()
        m.main_menu()

    # 로그인
    def user_login(self):
        print('')
        print('*' * 30)
        print('일반회원 로그인')
        print('*' * 30)

        uid = input('아이디 : ')
        pw = input('비밀번호 : ')

        result = user.login(uid, pw)

        # print(result)

        if result == 0:
            print('아이디 및 비밀번호를 잘못입력했습니다.')
            self.back_menu()
        elif result[0][0] == uid:
            print('로그인 성공 !')
            self.cache_id = result[0][0]
            self.name = result[0][1]
            print(self.cache_id, self.name)
            self.user_manu()
        else:
            print('로그인 실패', result)
            self.back_menu()

    # 사용자 메뉴
    def user_manu(self):
        print('')
        print('*' * 30)
        print('0. 메인 메뉴 돌아가기')
        print('1. 내 정보 목록')
        print('2. 내 정보 수정')
        print('3. 상품 목록 보기')
        print('4. 상품 검색')
        print('5. 상품 주문하기')
        print('6. 위시리스트')
        print('7. 내 주문 목록')
        print('8. 주문 리뷰')
        print('9. 회원 탈퇴')
        print('*' * 30)

        num = -1

        while True:
            try:
                num = int(input('메뉴 선택 : '))
            except Exception:
                print('숫자를 입력해주세요')
            
            if num >= 0 and num < 10:
                break
            else:
                print('올바른 메뉴 선택을 해주세요.')

        if num == 0:
            self.back_menu()
        elif num == 1:
            self.my_info()
        elif num == 2:
            self.myinfo_update()
        elif num == 3:
            self.all_item()
        elif num == 4:
            self.search_item()
        elif num == 5:
            self.item_order()
        elif num == 6:
            self.wishlist()
        elif num == 7:
            self.my_orderList()
        elif num == 8:
            self.review()
        elif num == 9:
            self.user_out()


    # 1. 내 정보 목록
    def my_info(self):
        result = user.my_data(self.cache_id)
        print('')
        print('{:^15s} {:^10s} {:^10s} {:^12s} {:^25s} {:^15s} {:^25s}'.format(
            'ID', 'Password','name', 'create_Date', 'Question', 'Answer', 'E-mail'))
        print('- ' * 70)
        for i, p, n, cd, q, a, e in result:
            print(f'{i:^15s} {p:^10s} {n:^10s} {cd:^12s} {q:^25s} {a:^15s} {e:^25s}')
        self.user_manu()


    # 2. 내 정보 수정
    def myinfo_update(self):
        print('')
        print('*' * 20)
        print('0. 돌아가기')
        print('1. 비밀번호 변경')
        print('2. 이름 변경')
        print('3. 이메일 변경')
        print('4. 본인확인 질문/답변 변경')
        print('*' * 20)
        num = -1
        while True:
            try:
                num = int(input('메뉴 선택 : '))
            except Exception:
                print('숫자를 입력해주세요.')
            
            if num >= 0 and num < 5:
                break
            else:
                print('올바른 메뉴를 선택해주세요. (0~4)')
        
        update_text = ''
        update_text2 = ''
        if num == 0:
            self.user_manu()
        elif num < 4:
            while True:
                try:
                    update_text = input('변경할 입력 값 : ')
                except Exception:
                    print('올바르게 입력하세요.')
                if update_text == '':
                    print('변경할 데이터를 입력하세요.')
                elif len(update_text) > 25:
                    print('입력한 데이터가 너무 깁니다.')
                else:
                    break
        elif num == 4:
            while True:
                try:
                    update_text = input('새로운 본인확인 질문 : ')
                    update_text2 = input('새로운 본인확인 답변 : ')
                except Exception:
                    print('올바르게 입력하세요.')
                
                if update_text == '' or update_text2 == '':
                    print('질문 / 답변을 입력해주세요.')
                elif len(update_text) > 30 or len(update_text2) > 30:
                    print('입력한 값이 너무 깁니다.')
                else:
                    break
        
        if num == 1:
            r = user.pw_change(self.cache_id, update_text)
            if r == 1:
                print('-- 비밀번호 변경 성공 --')
            else:
                print('-- 비밀번호 변경 실패 --')
        elif num == 2:
            r = user.name_change(self.cache_id, update_text)
            if r == 1:
                print('-- 이름 변경 성공 --')
            else:
                print('-- 이름 변경 실패 --')
        elif num == 3:
            r = user.email_change(self.cache_id, update_text)
            if r == 1:
                print('-- 이메일 변경 성공 --')
            else:
                print('-- 이메일 변경 실패 --')
        elif num == 4:
            r = user.qna_change(self.cache_id, update_text, update_text2)
            if r == 1:
                print('-- 질문/답변 변경 성공 --')
            else:
                print('-- 질문/답변 변경 실패 --')

        self.myinfo_update()


    # 3. 상품 목록 보기
    def all_item(self):
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
        self.user_manu()


    # 4. 상품 검색
    def search_item(self):
        print('')
        print('*' * 20)
        print('# 상품 검색')
        print('*' * 20)

        t = ''
        while True:
            try:
                t = input('검색 입력 : ')
            except Exception:
                print('올바르게 검색하세요.')
            
            if t == '':
                print('검색 단어를 입력해주세요.')
            else:
                break

        r = user.item_search(t)
        if r == 0:
            print('검색 결과가 없습니다.')
        else:
            print('')
            print('< ' * 15 + '검색 결과' + ' >' * 15)
            print('{:^10s} {:^20s} {:^10s} {:^6s} {:^12s}'.format(
            'icode', 'iname','iprice', 'iqty', 'item_date'))
            print('- ' * 40)
            for i, n, p, q, d in r:
                print(f'{i:^10d} {n:^20s} {p:^10d} {q:^6d} {d:^12s}')
        
        self.user_manu()

    
    # 5. 상품 주문하기
    def item_order(self):
        print('')
        print('*' * 30)
        print('# 상품 주문')
        print('*' * 30)
        print('')
        num = 0
        order_price = 0
        price = 0
        order_qty = 0
        iqty = 0
        iname = ''
        while True:
            try:
                num = int(input('주문할 상품 코드를 입력하세요.'))
                r = user.item_check(num)
            except Exception:
                print('주문 실패')
            else:
                if r == 0:
                    print('해당 상품이 존재하지 않습니다.')
                elif r == 1:
                    print('해당 상품의 재고가 없어 주문할 수 없습니다.')
                else:
                    iqty = r[0][3]
                    price = r[0][2]
                    iname = r[0][1]
                    print('')
                    print('< ' * 15 + '선택 상품' + ' >' * 15)
                    print('{:^10s} {:^20s} {:^10s} {:^6s} {:^12s}'.format(
                        'icode', 'iname','iprice', 'iqty', 'item_date'))
                    print('- ' * 40)
                    for i, n, p, q, d in r:
                        print(f'{i:^10d} {n:^20s} {p:^10d} {q:^6d} {d:^12s}')
                    break
        while True:
            try:
                order_qty = int(input('주문 수량 : '))
            except Exception:
                print('수량을 정확히 입력해주세요.')
            
            if order_qty > iqty:
                print('주문 수량이 상품 재고를 넘었습니다.')
                print('현재 재고 수량 : ', iqty)
            elif order_qty == 0:
                print('0개는 주문할 수 없습니다.')
                self.user_manu()
            else:
                order_price = price * order_qty
                break
        
        print('총 주문 금액 : ', order_price)
        while True:
            try:
                text = input('주문하시겠습니까 ? (y/n) : ')
            except Exception:
                print('올바르게 입력해주세요.')
            
            if text == 'n':
                self.user_manu()
            elif text == 'y':
                break
            else:
                print('y 와 n 으로 입력해주세요.')
        
        rr = user.order_item(self.cache_id, self.name, num, iname, price, order_qty, order_price)
        if rr == 1:
            print('-- 주문 성공 --')
        else:
            print('주문 실패', rr)
        self.user_manu()



    # 6. 위시리스트
    def wishlist(self):
        print('')
        print('*' * 30)
        print('### 위시리스트 ###')
        print('0. 사용자 메뉴')
        print('1. 나의 위시리스트 목록')
        print('2. 위시리스트 추가')
        print('3. 위시리스트 삭제')
        print('*' * 30)
        print('')
        num = -1
        while True:
            try:
                num = int(input('메뉴 선택 : '))
            except Exception:
                print('숫자를 입력해주세요.')
            if num >= 0 and num < 5:
                break
            else:
                print('올바른 메뉴 선택을 해주세요. (0~4)')
        
        if num == 0:
            self.user_manu()
        elif num == 1:
            self.my_wishlist()
        elif num == 2:
            self.add_wishlist()
        elif num == 3:
            self.del_wishlist()


    # 6 - 1 내 위시리스트 목록 보기 -> 주문하기
    def my_wishlist(self):
        result = user.my_wishlist(self.cache_id)
        if result == 0:
            print('위시리스트에 상품이 존재하지 않습니다.')
            self.wishlist()
        else:
            print('')
            print('{:^10s} {:^20s} {:^10s} {:^6s} {:^12s}'.format(
                'icode', 'iname','iprice', 'iqty', 'item_date'))
            print('- ' * 40)
            for i, n, p, q, d in result:
                print(f'{i:^10d} {n:^20s} {p:^10d} {q:^6d} {d:^12s}')
            print('')
        t = ''
        while True:
            t = input('위시리스트에서 상품을 주문하시겠습니까? (y / n) : ')
            if t == '':
                print('대답을 입력해주세요.')
            elif t == 'y' or t == 'n':
                break
            else:
                print('y 나 n 을 입력해주세요.')
        if t == 'n':
            self.wishlist()
        else:
            self.item_order()


    # 6 - 2 위시리스트 추가
    def add_wishlist(self):
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
            print('')
        
        num = 0
        while True:
            try:
                num = int(input('위시리스트에 추가할 상품 코드 : '))
            except Exception:
                print('숫자를 입력해주세요.')
            if num == 0:
                print('상품 코드를 입력해주세요.')
            else:
                break
        
        r = user.add_wishlist(self.cache_id, num)
        if r == 1:
            print('위시리스트 추가 성공')
        elif r == 2:
            print('이미 위시리스트에 존재합니다.')
        else:
            print('추가 실패', r)
        self.wishlist()


        
    # 6 - 3 위시리스트 삭제
    def del_wishlist(self):
        result = user.my_wishlist(self.cache_id)
        if result == 0:
            print('위시리스트에 상품이 존재하지 않습니다.')
            self.wishlist()
        else:
            print('')
            print('{:^10s} {:^20s} {:^10s} {:^6s} {:^12s}'.format(
                'icode', 'iname','iprice', 'iqty', 'item_date'))
            print('- ' * 40)
            for i, n, p, q, d in result:
                print(f'{i:^10d} {n:^20s} {p:^10d} {q:^6d} {d:^12s}')
            print('')
        icode = 0
        while True:
            try:
                icode = int(input('삭제할 상품 코드 : '))
            except Exception:
                print('숫자를 입력해주세요.')
            if icode == 0:
                print('올바른 상품 코드를 입력해주세요.')
            else:
                break
        
        r = user.del_wishlist(self.cache_id, icode)
        if r == 1:
            print('위시리스트 삭제 성공')
        else:
            print('삭제 실패', r)
        self.wishlist()
        


    # 7. 내 주문 목록 보기
    def my_orderList(self):

        r = user.my_order(self.cache_id)
        print('')
        print('< ' * 20 + '내 주문 목록' + ' >' * 20)
        print('{:^6s} {:^16s} {:^12s} {:^6s} {:^20s} {:^10s} {:^8s} {:^10s} {:^12s}'.format(
            'ocode', 'id','order_name', 'icode', 'iname', 'iprice', 'order_qty', 'order_price', 'order_date'))
        print('- ' * 40)
        for ocode, i, name, icode, iname, iprice, o_qty, o_price, o_date in r:
            print(f'{ocode:^6d} {i:^16s} {name:^12s} {icode:^6d} {iname:^20s} {iprice:^10d} {o_qty:^8d} {o_price:^10d} {o_date:^12s}')
        print('')
        self.user_manu()


    # 8. 리뷰
    def review(self):
        print('')
        print('*' * 30)
        print('### 주문 리뷰 ###')
        print('0. 사용자 메뉴')
        print('1. 상품 리뷰 보기')
        print('2. 내 리뷰 목록')
        print('3. 리뷰 작성')
        print('4. 리뷰 삭제')
        print('*' * 30)
        print('')
        
        num = -1

        while True:
            try:
                num = int(input('메뉴 선택 : '))
            except Exception:
                print('숫자를 입력하세요.')
            if num >= 0 and num < 5:
                break
            else:
                print('정확한 메뉴를 선택하세요 (0~4)')

        if num == 0:
            self.user_manu()
        elif num == 1:
            self.all_review()
        elif num == 2:
            self.my_review()
        elif num == 3:
            self.add_review()
        elif num == 4:
            self.del_review()

    
    # 8 - 1 상품 리뷰 보기
    def all_review(self):
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
        
        num = 0
        while True:
            try:
                num = int(input('리뷰를 볼 상품 코드 : '))
            except Exception:
                print('숫자 코드를 입력하세요.')
            if num == 0:
                print('0은 존재하지 않는 상품 코드입니다.')
            else:
                break

        r = user.review_list(num)
        if r == 0:
            print('해당 상품은 현재 리뷰가 없습니다')
        else:
            print('')
            print('< ' * 20 + '리뷰 목록' + ' >' * 20)
            print('{:^8s} {:^8s} {:^16s} {:^16s} {:^50s} {:^12s}'.format(
                'rcode', 'icode','id', 'name', 'rtext', 'r_date'))
            print('- ' * 50)
            for i, n, p, q, d, e in r:
                print(f'{i:^8d} {n:^8d} {p:^10s} {q:^16s} {d:^50s} {e:^12s}')

        self.review()

    # 8 - 2 내 리뷰 목록
    def my_review(self):
        r = user.review_my(self.cache_id)
        if r == 0:
            print('현재 작성한 리뷰가 없습니다.')
            self.review()
        else:
            print('')
            print('< ' * 20 + '내 리뷰 목록' + ' >' * 20)
            print('{:^8s} {:^8s} {:^16s} {:^16s} {:^50s} {:^12s}'.format(
                'rcode', 'icode','id', 'name', 'rtext', 'r_date'))
            print('- ' * 50)
            for i, n, p, q, d, e in r:
                print(f'{i:^8d} {n:^8d} {p:^10s} {q:^16s} {d:^50s} {e:^12s}')
            print('')
        self.review()


    # 8 - 3 리뷰 작성
    def add_review(self):
        r = user.my_order(self.cache_id)
        print('')
        print('< ' * 20 + '내 주문 목록' + ' >' * 20)
        print('{:^6s} {:^16s} {:^12s} {:^6s} {:^20s} {:^10s} {:^8s} {:^10s} {:^12s}'.format(
            'ocode', 'id','order_name', 'icode', 'iname', 'iprice', 'order_qty', 'order_price', 'order_date'))
        print('- ' * 40)
        for ocode, i, name, icode, iname, iprice, o_qty, o_price, o_date in r:
            print(f'{ocode:^6d} {i:^16s} {name:^12s} {icode:^6d} {iname:^20s} {iprice:^10d} {o_qty:^8d} {o_price:^10d} {o_date:^12s}')
        print('')

        num = 0
        while True:
            try:
                num = int(input('리뷰 작성할 상품 코드 : '))
            except Exception:
                print('숫자 코드를 입력해주세요.')
            
            if num == 0:
                print('0은 존재하지 않는 코드입니다.')
            else:
                break
        t = ''
        while True:
            t = input('리뷰 작성 : ')
            if t == '':
                print('리뷰를 작성해주세요.')
            else:
                break
                
        r2 = user.new_review(self.cache_id, num, self.name, t)
        if r2 == 1:
            print('리뷰 작성 성공')
        elif r2 == 0:
            print('해당 상품을 주문한 내역이 없습니다. 작성 실패')
        else:
            print(r2)
        self.review()



    # 8 - 4 리뷰 삭제
    def del_review(self):
        r = user.review_my(self.cache_id)
        if r == 0:
            print('현재 작성한 리뷰가 없습니다.')
            self.review()
        else:
            print('')
            print('< ' * 20 + '내 리뷰 목록' + ' >' * 20)
            print('{:^8s} {:^8s} {:^16s} {:^16s} {:^50s} {:^12s}'.format(
                'rcode', 'icode','id', 'name', 'rtext', 'r_date'))
            print('- ' * 50)
            for i, n, p, q, d, e in r:
                print(f'{i:^8d} {n:^8d} {p:^10s} {q:^16s} {d:^50s} {e:^12s}')
            print('')
        
        num = 0
        while True:
            try:
                num = int(input('리뷰를 삭제할 상품 코드 : '))
            except Exception:
                print('숫자 코드를 입력해주세요.')
            
            if num == 0:
                print('0은 존재하지 않는 코드입니다.')
            else:
                break
        r2 = user.del_review(self.cache_id, num)
        if r2 == 1:
            print('리뷰 삭제 성공')
        else:
            print(r2)
        self.review()



    # 9. 회원 탈퇴
    def user_out(self):
        print('')
        print('*' * 30)
        print('# 회원 탈퇴')
        print('*' * 30)
        print('')
        t = ''
        while True:
            try:
                t = input('현재 계정을 탈퇴하시겠습니까? (y/n) : ')
            except Exception:
                print('올바르게 입력해주세요.')
            
            if t == 'y':
                break
            elif t == 'n':
                print('계정 탈퇴 취소')
                self.user_manu()
            else:
                print('y 혹은 n을 입력해주세요.')
        
        r = user.user_del(self.cache_id)
        if r == 1:
            print('회원 탈퇴 완료')
            self.cache_id = ''
            self.name = ''
            self.back_menu()
        else:
            print('회원 탈퇴 실패')
            self.user_manu()
        