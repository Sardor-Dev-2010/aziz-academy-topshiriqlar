n = int(input())
rows = []
for i in range(n):
    name, score = input().split()
    score = int(score)
    if 90 <= score <= 100:
        grade = "A"
    elif 80 <= score <= 89:
        grade = "B"
    elif 70 <= score <= 79:
        grade = "C"
    elif 60 <= score <= 69:
        grade = "D"
    else:
        grade = "F"
    rows.append((name, grade))
print(f"{'Name':<10} | {'Grade'}")
print("-" * 10 + "+" + "-" * 6)
for name, grade in rows:
    print(f"{name:<10} | {grade:>3}")