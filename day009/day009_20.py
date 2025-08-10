
import os
def func1(ls1):
    print('제곱 프로그램을 수행합니다\n','\b원본:',ls1)
    return [i*i for i in ls1]
def func2(ls1):
    print('홀수 프로그램을 수행합니다\n','\b원본:',ls1)
    return [i for i in ls1 if i % 2!=0]

def func3(text):
    print('슾앰 프로그램을 수행합니다\n', '\b원본:',message)
    return[t for t in text if t == 'spam']


ls0 = [2, 4, 1, 5, 7, 3, 9, 10, 8, 6]
while True:
    os.system('cls')
    sel = int(input("1, 2, 3 중 한 개를 입력하세요. 종료는 0 을 입력하세요 : "))
    if sel == 0:
        print("프로그램을 종료합니다.")
        input('앤터키를 누르세요')
        break
    elif sel == 1:
        result = func1(ls0)
        print('제곱:',result)
        input('제곱프로그램이 모두 실행되었습니다. 앤터키를 누르세요')
        #os.system('cls')
    elif sel == 2:
        result = func2(ls0)
        print('홀수:',result)
        input('홀수프로그램이 모두 실행되었습니다. 앤터키를 누르세요')
        #os.system('cls')
    elif sel == 3:
        message = ['spam', 'ham', 'spam','ham', 'spam', 'spum', 'stam', 'spam']
        result = func3(message)
        print('슾앰:',result)
        input('슾앰프로그램이 모두 실행되었습니다. 엔터키를 누르세요')
        #os.system('cls')
    else:
        print("입력값이 오류입니다. 다시 입력하세요.")
        input('앤터키를 누르세요')
        #os.system('cls')