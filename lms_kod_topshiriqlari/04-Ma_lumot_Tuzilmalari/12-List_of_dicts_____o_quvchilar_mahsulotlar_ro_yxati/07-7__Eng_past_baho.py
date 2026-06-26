n = int(input())
students = []
for _ in range(n):
    name, score = input().split()
    students.append({'name': name, 'score': int(score)})

min_score = min(s['score'] for s in students)
print(min_score)