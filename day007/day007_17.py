num = int(input("높이를 입력하세요: "))

for i in range(1, num + 1) :
    for j in range(i) :
        print("*", end="")
    print()