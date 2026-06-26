n = int(input().strip())
data = {'courses': []}
for _ in range(n):
    parts = input().split()
    name = parts[0]
    k = int(parts[1])
    students = parts[2:2+k]
    data['courses'].append({'name': name, 'students': students})
total = sum(len(c['students']) for c in data['courses'])
print(total)

