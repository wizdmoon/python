
age = int(input("나이를 입력하세요: "))
if age >= 18 :
    print("성인입니다.")
    if age >= 65 :
        print("노인이십니다.")
    else :
        print("아직 노인은 아닙니다.")
else :
    print("미성년자입니다.")