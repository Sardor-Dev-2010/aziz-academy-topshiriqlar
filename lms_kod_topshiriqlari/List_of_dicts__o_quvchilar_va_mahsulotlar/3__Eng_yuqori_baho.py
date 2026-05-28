n = int(input())
students = []
for _ in range(n):
    name, score = input().split()
    students.append({'name': name, 'score': int(score)})
max_score = max(s['score'] for s in students)
print(max_score)