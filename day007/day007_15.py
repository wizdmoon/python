num = int(input("점수를 입력하세요: "))

result = 0

if num >= 90 :
    if num >= 95 :
        result = "A+ 학점"
    else :
        result = "A 학점"
elif num >= 80 :
    result = "B 학점"
elif num >= 70 :
    result = "C 학점"
elif num >= 60 :
    result = "D 학점"
else :
    result = "F 학점"

print(result)