
n = int(input().strip())
courses = []
for _ in range(n):
    parts = input().split()
    name = parts[0]
    k = int(parts[1])
    students = parts[2:2+k]
    courses.append({'name': name, 'students': students})

target = input().strip()
found = False 
for c in courses:
    if c['name'] == target:
        print(len(c['students']))
        found = True
        break
if not found:
    print(0)

