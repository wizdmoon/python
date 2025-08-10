#009-실습-2-해답
# 
ls1 = [2,4,1,5,7,3,9,10,8,6]
ls2 = [ i ** 2  for i in ls1] # List Comprehension
              # ls1리스트의 첫번째 요소부터 차례로 i에 대입한 후, i를 제곱연산하고 이결과를
              # ls2 리스트에 append 한다.
print('ls1 : ',ls1)
print('ls2 : ',ls2)