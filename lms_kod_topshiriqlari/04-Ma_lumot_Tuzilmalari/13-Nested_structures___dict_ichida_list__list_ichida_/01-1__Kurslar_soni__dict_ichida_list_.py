n = int(input().strip())
data = {'courses': []}
for _ in range(n):
    parts = input().split()
    course_name = parts[0]
    k = int(parts[1])
    students = parts[2:2+k]
    data['courses'].append({'name': course_name, 'students': students})
print(len(data['courses']))

