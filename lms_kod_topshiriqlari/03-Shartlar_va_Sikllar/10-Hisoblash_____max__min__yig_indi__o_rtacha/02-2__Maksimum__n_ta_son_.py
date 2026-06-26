
n = int(input())
son = list(map(int, input().split()))
maksimal = son[0]
for i in son:
    if i > maksimal:
        maksimal = i
print(maksimal)