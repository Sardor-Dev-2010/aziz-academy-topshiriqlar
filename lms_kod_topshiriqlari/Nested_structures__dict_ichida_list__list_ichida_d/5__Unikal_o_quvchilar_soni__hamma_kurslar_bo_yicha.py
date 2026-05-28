
n = int(input().strip())
courses = []
for _ in range(n):
    parts = input().split()
    name = parts[0]
    k = int(parts[1])
    students = parts[2:2+k]
    courses.append({'name': name, 'students': students})
student1 = set()
for course in courses:
    for student in course['students']:
        student1.add(student)
print(len(student1))

