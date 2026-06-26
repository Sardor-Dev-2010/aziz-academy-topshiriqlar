
n = int(input())
son = list(map(int, input().split()))
min = son[0]
for i in son:
    if i < min:
        min = i
print(min)