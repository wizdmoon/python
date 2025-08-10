student = {"name": "Alice", "age": 25, "grade": "A"}
dic1 = {1: "Alice", 2: 25, 3: "A"}

print(student["name"])
print(student.get("age"))

print(dic1[1])
print(dic1.get(2))

student["major"] = "Computer Science"
student["age"] = 26
del student["grade"]

print(student)

student = {"name": "alice", "age": 25, "grade": "a" }
print(type(student))
print(student["name"])
print(student.get("age"))
student['major'] = 'Computer Science'
print('1--->',student)
student["age"] = 26
print('2--->',student)
del student['grade']
print('3--->',student)