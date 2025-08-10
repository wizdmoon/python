num1 = int(input("첫번째 숫자를 입력하세요: "))
num2 = int(input("두번째 숫자를 입력하세요: "))

#for i in range(num1, num2+1) :
#    print(i, end="")

if num1 > num2 :
    for i in range(num1, num2 -1, -1) :
        print(i, end=" ")
elif num1 < num2 :
    for i in range(num1, num2 + 1, +1) :
        print(i, end=" ")