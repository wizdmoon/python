print("\n문제 1: 리스트 활용")
fruits = ["apple", "banana", "cherry"]
print(fruits)
fruits[1] = "grape"
print(fruits)
fruits.remove("cherry")
print(fruits)
fruits.append("orange")
print(fruits)

print("\n문제 2: 튜플 활용")
colors = ("red", "green", "blue", "yellow")
print(colors[2])

print("\n문제 3: 집합 활용")
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print("합집합: ", A | B)
print("교집합: ", A & B)
print("차집합: ", A - B)

print("\n문제 4: 딕셔너리 활용")
student = {"이름" : "김철수", "나이" : 20, "학교" : "서울대학교"}
print(student)
student["학과"] = "컴퓨터공학과"
print(student)
student["나이"] = 21
print(student)
del student["학교"]
print(student)