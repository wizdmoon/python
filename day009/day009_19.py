'''009일차-실습-6
------------------------------------------------------------------
<문제>, <배경설명>, <요구사항>, <실행결과> 를 충족하는 실습을 수행하고 결과를 제출하세요.
------------------------------------------------------------------
<문제>
이전 실습을 참조하여 <실행결과> 를 구현하는 프로그램으로 변경하세요.

------------------------------------------------------------------
<요구사항1>
- 009일차-실습-5 프로그램을 편의상 슾앰 프로그램이라고 합니다.
- 슾앰 프로그램을  009일차-실습-4에서 작성한  프로그램에 끼워 넣으세요.

- 1은, 제곱 프로그램, 2는 홀수 프로그램, 3은 슾앰 프로그램입니다.
기타 조건은 009일차-실습-3,  009일차-실습-4와 동일합니다.

------------------------------------------------------------------
<요구사항2>
단, 리스트변수를 전역변수로 선언하는 것은 불가합니다.

------------------------------------------------------------------
이상의 실습결과를 techmr@daum.net; ty@doublerock.io 메일로 전송하세요.
메일제목은 '009일차-실습-6-완료' 라고 지정하세요.
'''

import os

ls = [2, 4, 1, 5, 7, 3, 9, 10, 8, 6]

def odd_number() :
    odd_numbers = [num for num in ls if num % 2 == 1]
    return odd_numbers

def squared() :
    squared_numbers = [num ** 2 for num in ls]
    return squared_numbers

def func3() :
    message = ['spam', 'ham', 'spam', 'ham', 'spam', 'spum', 'stam', 'spam']
    spam_list = [i for i in message if i == 'spam']
    return print('message:', message, '\nspam_list:', spam_list)


while 1 :
    os.system('cls')
    input_num = input('1, 2, 3 중 한 개를 입력하세요. 종료는 0 을 입력하세요: ')

    if input_num == '0' :
        print('프로그램을 종료합니다')
        input_key = input('엔터키를 누르세요')
        if input_key == '' :
            break
    elif input_num == '1' :
        print('제곱 프로그램을 수행합니다.')
        print(f'원본: {ls}')
        print(f'제곱: {squared()}')
        input_key = input('제곱프로그램이 모두 실행되었습니다. 엔터키를 누르세요')
    elif input_num == '2' :
        print('홀수 프로그램을 수행합니다.')
        print(f'원본: {ls}')
        print(f'홀수: {odd_number()}')
        input_key = input('홀수프로그램이 모두 실행되었습니다. 엔터키를 누르세요')
    elif input_num == '3' :
        print('스팸 프로그램을 수행합니다.')
        func3()
        input_key = input('스팸프로그램이 모두 실행되었습니다. 엔터키를 누르세요')
        
    else :
        print('입력값이 오류입니다. 다시 입력하세요.')
        input_key = input('엔터키를 누르세요')