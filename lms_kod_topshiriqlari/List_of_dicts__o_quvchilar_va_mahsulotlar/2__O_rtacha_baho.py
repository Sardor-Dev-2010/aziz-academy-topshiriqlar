n = int(input())
students = []
for _ in range(n):
    name, score = input().split()
    students.append({'name': name, 'score': int(score)})
total = sum(s['score'] for s in students)
print(float(total / n))
