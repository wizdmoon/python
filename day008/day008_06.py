def calc() :
    result = 0
    su1, op, su2 = int(input('숫자: ')), input('부호: '), int(input('숫자: '))
    if op == '+' : result = su1 + su2
    elif op == '-' : result = su1 - su2
    elif op == '*' : result = su1 * su2
    elif op == '/' : result = su1 / su2
    print(su1, op, su2, '=', result)

calc()
