
n = int(input())
son = list(map(int, input().split()))
total = 0
for i in son:
    if i > 10:
        total += i
print(total)