n = int(input().strip())
data = {'courses': []}
for _ in range(n):
    parts = input().split()
    name = parts[0]
    k = int(parts[1])
    students = parts[2:2+k]
    data['courses'].append({'name': name, 'students': students})
best = max(data['courses'], key=lambda c: len(c['students']))
print(best['name'])
