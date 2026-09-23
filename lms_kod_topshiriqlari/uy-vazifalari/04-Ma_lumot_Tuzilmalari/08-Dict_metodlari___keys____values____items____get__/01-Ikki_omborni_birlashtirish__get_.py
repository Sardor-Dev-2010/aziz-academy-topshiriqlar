n = int(input())
total = {}
for _ in range(n):
    p = input().split()
    total[p[0]] = total.get(p[0], 0) + int(p[1])
m = int(input())
for _ in range(m):
    p = input().split()
    total[p[0]] = total.get(p[0], 0) + int(p[1])
for k in sorted(total):
    print(k, total[k])