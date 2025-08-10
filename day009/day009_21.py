#006일차-실습-6-해답
#-----------------------------------------------------------------
import os
def func1(ls1):
    print('제곱 프로그램을 수행합니다\n','\b원본:',ls1)
    return [i*i for i in ls1]
#
def func2(ls1):
    print('홀수 프로그램을 수행합니다\n','\b원본:',ls1)
    return [i for i in ls1 if i % 2!=0]
#
def func3(ls1):
    print('슾앰 프로그램을 수행합니다\n','\b원본:',ls1)
    spam_list = [ spam_txt for spam_txt in ls1 if spam_txt == "spam" ]
    return spam_list  
#
#ls0 = [2, 4, 1, 5, 7, 3, 9, 10, 8, 6]   # <요구사항2>를 반영함
#ls1 = ['spam', 'ham','spam', 'ham', 'spam', 'spum', 'stam', 'spam']    # <요구사항2>를 반영함
#
while True:
    os.system('cls')
    sel = int(input("1, 2, 3 중 한 개를 입력하세요. 종료는 0 을 입력하세요 : "))
    if sel == 0:
        print("프로그램을 종료합니다.")
        input('앤터키를 누르세요')
        break
    elif sel == 1:
        #result= ls0
        result= func1([2, 4, 1, 5, 7, 3, 9, 10, 8, 6])
        print('제곱:',result)
        input('제곱프로그램이 모두 실행되었습니다. 앤터키를 누르세요')
    elif sel == 2:
        #result= ls0
        result=func2([2, 4, 1, 5, 7, 3, 9, 10, 8, 6])
        print('홀수:',result)
        input('홀수프로그램이 모두 실행되었습니다. 앤터키를 누르세요')
    elif sel == 3:
        #result= ls1
        result=func3(['spam', 'ham','spam', 'ham', 'spam', 'spum', 'stam', 'spam'])
        print('슾앰:',result)
        input('슾앰프로그램이 모두 실행되었습니다. 앤터키를 누르세요')
    else:
        print("입력값이 오류입니다. 다시 입력하세요.")
        input('앤터키를 누르세요')