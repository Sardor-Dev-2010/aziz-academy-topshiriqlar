n = int(input())
students = []
for _ in range(n):
    parts = input().split()
    scores = []
    for x in parts[1:]:
        scores.append(int(x))
    students.append({'name': parts[0], 'scores': scores})
best_name = None
best = -1
for s in students:
    for sc in s['scores']:
        if sc > best:
            best = sc
            best_name = s['name']
print(best_name, best)