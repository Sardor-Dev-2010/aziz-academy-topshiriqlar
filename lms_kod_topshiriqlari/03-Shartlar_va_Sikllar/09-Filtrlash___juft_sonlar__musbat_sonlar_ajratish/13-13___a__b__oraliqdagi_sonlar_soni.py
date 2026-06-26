
n = int(input())
son = list(map(int, input().split()))
a, b = map(int, input().split())
total = 0
for i in son:
    if a <= i <= b:
        total += 1
print(total)
        