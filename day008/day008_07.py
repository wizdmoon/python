def cal(su1, op, su2) :
    result = su1 + su2
    print(su1, '+', su2, '=', result)

ssu1, oop, ssu2 = int(input('숫자: ')), input('부호: '), int(input('숫자: '))
cal(ssu1, oop, ssu2)