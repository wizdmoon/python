num = int(input("높이를 입력하세요: "))

for i in range(num, 0, -1) :
    for j in range(i) :
        print('*', end="")
    print()