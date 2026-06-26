
n, m = map(int, input().split())
for j in range(1, m + 1):
    total = 0
    for i in range(1, n+  1):
        total += i * j
    print(total)
