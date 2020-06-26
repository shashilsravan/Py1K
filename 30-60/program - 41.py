students = {}
for _ in range(int(input())):
    student = input().split()
    lis = [int(each) for each in student[1:]]
    students[student[0]] = lis
name = input()
if name in students:
    print(sum(students[name])/len(students[name]))