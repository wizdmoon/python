# 009일차-실습-3-해답-ver2
def func1(ls1):
    print('제곱 프로그램을 수행합니다\n','\b원본:',ls1)  # \b : 한 줄 띄우지 않고 줄바꿈만 하는 기능구현
    ls2=[i*i for i in ls1]
    return ls2
def func2(ls1):
    print('홀수 프로그램을 수행합니다\n','\b원본:',ls1)  # \b : 한 줄 띄우지 않고 줄바꿈만 하는 기능구현
    ls2=[i for i in ls1 if i % 2 != 0]
    return ls2
#
ls0=[2, 4, 1, 5, 7, 3, 9, 10, 8, 6]
while True:
    sel = int(input("1, 2 중 한 개를 입력하세요. 종료는 0 을 입력하세요 : "))
    if sel == 0:
        break
    elif sel == 1:
        result= func1(ls0)
        print('제곱:',result)
    elif sel == 2:
        result=func2(ls0)
        print('홀수:',result)
    else:
        print("입력값이 오류입니다. 다시 입력하세요.")