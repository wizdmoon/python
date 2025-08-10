num1, num2, num3 = map(int, input("3개의 숫자를 입력하세요: ").split())

if num1 > num2 and num1 > num3 :
    print(f"가장 큰 숫자는 {num1}입니다.")
elif num2 > num1 and num2 > num3 :
    print(f"가장 큰 숫자는 {num2}입니다.")
else :
    print(f"가장 큰 숫자는 {num3}입니다.")
