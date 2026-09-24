n = int(input())
groups = {}
for _ in range(n):
    parts = input().split()
    groups[parts[0]] = parts[1:]
best = None
bestc = -1
for g in groups:
    if len(groups[g]) > bestc:
        bestc = len(groups[g])
        best = g
print(best)