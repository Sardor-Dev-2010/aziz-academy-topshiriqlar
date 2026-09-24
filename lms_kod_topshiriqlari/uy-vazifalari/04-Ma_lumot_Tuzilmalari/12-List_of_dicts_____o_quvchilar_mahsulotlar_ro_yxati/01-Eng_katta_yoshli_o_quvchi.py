n = int(input())
students = []
for _ in range(n):
    p = input().split()
    students.append({'name': p[0], 'age': int(p[1])})
best = students[0]['name']
bestage = students[0]['age']
for s in students:
    if s['age'] > bestage:
        bestage = s['age']
        best = s['name']
print(best)