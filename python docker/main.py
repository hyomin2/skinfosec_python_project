import sys
import user
import user_func
import admin_func
u = user_func.User_function()
ad = admin_func.Admin_function()

class Main_function:

    # 프로그램 시작 메뉴 (가장 처음)
    def main_menu(self):
        print('')
        print('$-'*15)
        print(' Sk인포섹 데이터 보안 쇼핑몰')
        print('          By. 훈련생 길효민')
        print('$-'*15)
        print('')
        print('*' * 30)
        print('메인 메뉴 선택창')
        print('1. 로그인')
        print('2. 회원가입')
        print('3. 아이디 찾기')
        print('4. 비밀번호 찾기')
        print('5. 종료')
        print('*' * 30)
        n = 0
        while True:
            try:
                n = int(input('메뉴 선택 : '))
            except Exception:
                print('숫자를 입력해주세요.')
            else:
                if n > 0 and n < 6:
                    break
                else:
                    print('메뉴 선택을 올바르게 해주세요. (1~5) ')
        if n == 1:
            self.login_menu()
        elif n == 2:
            self.user_join()
        elif n == 3:
            self.find_id()
        elif n == 4:
            self.pw_find()
        else:
            print('')
            print('*' * 30)
            print('### 프로그램 종료 ###')
            print('이용해주셔셔 감사합니다.')
            print('*' * 30)
            sys.exit()


    # 로그인 메뉴
    def login_menu(self):
        print('')
        print('*' * 30)
        print('0. 메인 메뉴')
        print('1. 일반회원 로그인')
        print('2. 관리자 로그인')
        print('*' * 30)
        n = -1
        while True:
            try:
                n = int(input('메뉴 선택 : '))
            except Exception:
                print('숫자를 입력해주세요.')
            else:
                if n >= 0 and n < 3:
                    break
                else:
                    print('메뉴를 올바르게 선택하세요. (1~2)')
        if n == 1:
            u.user_login()
        elif n == 2:
            ad.admin_login()
        else:
            self.main_menu()


    # 회원가입
    def user_join(self):
        print('')
        print('*' * 30)
        print('쇼핑몰 회원가입')
        print('*' * 30)
        uid = ''
        while True:
            uid = str(input('아이디 : '))
            result = user.id_check(uid)
            if result == 1:
                break
            elif result == 0:
                print('이미 존재하는 아이디입니다. 다른 아이디를 입력해주세요.')
            elif len(uid) < 5:
                print('아이디는 최소 5자리 이상이어야 합니다.')
            else:
                print(result)
        pw = input('비밀번호 : ')
        name = input('이름 : ')
        email = input('이메일 : ')
        qn = input('본인확인 질문 : ')
        answer = input('본인확인 답변 : ')
        result = user.join(uid, pw, name, email, qn, answer)
        if result == 1:
            print('')
            print('*' * 20)
            print('회원가입 성공 !!!')
            print('*' * 20)
            self.main_menu()
        else:
            print('')
            print('*' * 20)
            print('회원가입 실패', result)
            print('*' * 20)
            self.main_menu()


    # 아이디 찾기
    def find_id(self):
        print('')
        print('*' * 30)
        print('### 아이디 찾기 ###')
        print('*' * 30)
        print('')
        name = ''
        email = ''

        while True:
            try:
                name = input('가입 이름 : ')
                email = input('가입 이메일 : ')
            except Exception:
                print('올바르게 입력하세요.')
            
            if name == '' or email == '':
                print('이름 / 이메일을 입력해주세요.')
            else:
                break
        
        r = user.id_find(email, name)
        if r == 0:
            print('입력하신 가입정보가 존재하지 않습니다.')
        else:
            print(name + ' 회원님의 아이디는 : ' + r[0])

        self.main_menu()


    # 비밀번호 찾기 -> 본인확인 후 재설정
    def pw_find(self):
        print('')
        print('*' * 30)
        print('### 비밀번호 찾기 ###')
        print('*' * 30)
        print('')
        
        name = ''
        uid = ''
        while True:
            try:
                name = input('가입 이름 : ')
                uid = input('가입 아이디 : ')
            except Exception:
                print('올바르게 입력해주세요.')
            
            if name == '' or uid == '':
                print('이름과 아이디를 입력해주세요.')
            else:
                break
        r = user.qna_find(uid, name)
        if r == 0:
            print('입력하신 가입 정보가 존재하지 않습니다.', r)
            self.main_menu()
        else:
            print(name + ' 회원님의 본인확인 질문 : ' + r[0][0])
            answer = input('본인확인 답변 : ')
            if answer == r[0][1]:
                print('본인확인 성공')
                pw = input('재설정 비밀번호 : ')
                if len(pw) < 4:
                    print('비밀번호는 최소 4자리 이상 이어야햡니다.')
                else:
                    r2 = user.pw_change(uid, pw)
                    if r2 == 1:
                        print('비밀번호 재설정 성공')
                    else:
                        print('비밀번호 재설정 실패', r2)
            else:
                print('본인확인 실패', r)
            self.main_menu()
        

    



main1 = Main_function()
main1.main_menu()