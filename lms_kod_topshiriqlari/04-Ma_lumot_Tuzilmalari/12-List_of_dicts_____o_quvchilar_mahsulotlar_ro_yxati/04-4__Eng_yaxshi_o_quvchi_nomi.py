
n = int(input())
students = []
for _ in range(n):
    name, score = input().split()
    students.append({'name': name, 'score': int(score)})

max_students = max(students, key=lambda s: s['score'] )
print(max_students['name'])
