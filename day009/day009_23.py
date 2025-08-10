#009일차-실습-7-해답
#함수(머슴)영역
def StarCount(height):
    count = 0
    for i in range(1, height + 1):
        print('*' * i)
        count += i
    return count
#
#본체(주인마님)영역
#키보드 입력
height = int(input('height : '))
#Star 갯수 출력
print('star 개수 : %d'%StarCount(height))