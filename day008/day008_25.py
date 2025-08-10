# -실습-2-해답
import os   # 화면을 클리어 하는 도스명령어(cmd) cls를 사용하기 위해서,  
            # 도스명령어를 실행하는 함수인 system( ) 함수를 사용하기 위한 라이브러리 os 를 import함
def myMax(firstNum, secondNum):
    if firstNum > secondNum:
        return firstNum
    else:
        return secondNum

def myMin(firstNum, secondNum):
    if firstNum < secondNum:
        return firstNum
    else:
        return secondNum

while (True) :
    os.system('cls')
    print("최대값 / 최소값 판단 프로그램입니다.")
    su1,op,su2 = int(input("숫자:")),input("최대값은 B 최소값은 S 종료는 x 입력 :"),int(input("숫자:"))
    if op =='X' or op == 'x':
        print('종료합니다.')
        break 
    elif su1 == su2 :
        print("최대값, 최소값이 같습니다.")
        input("앤터키를치세요")      
    elif op == 'B' or op == 'b':
        result = myMax(su1, su2)
        print(su1,'와',su2,'중 최대값은 ',result,'입니다.')
        input("앤터키를치세요")
    elif op=='S' or op == 's':
        result = myMin(su1, su2)
        print(su1,'와',su2,'중 최소값은 ',result,'입니다.')
        input("앤터키를치세요")
    else :
        print("최대값, 최소값 선택 입력이 오류입니다.")
        input("앤터키를치세요")