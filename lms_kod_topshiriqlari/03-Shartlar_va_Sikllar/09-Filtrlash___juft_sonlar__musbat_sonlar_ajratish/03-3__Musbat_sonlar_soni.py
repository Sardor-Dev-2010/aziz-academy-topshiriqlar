
n = int(input())
son = list(map(int, input().split()))
total = 0
for i in son:
    if i > 0:
        total += 1
print(total)