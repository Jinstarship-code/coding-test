n = int(input())

students = []

for i in range(n):
  students.append(list(input().split()))  

students.sort(students, key=lambda x: (-int(x[1]),int(x[2]),(-int(x[3]),x[0])))

for student in students:
  print(student[0])