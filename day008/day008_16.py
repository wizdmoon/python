def display() :
    num = 10
    print('10까지의 합: ', sumFune(num))

def sumFune(num) :
    sum = 0
    for i in range(num + 1) :
        sum += i
    return sum

display()