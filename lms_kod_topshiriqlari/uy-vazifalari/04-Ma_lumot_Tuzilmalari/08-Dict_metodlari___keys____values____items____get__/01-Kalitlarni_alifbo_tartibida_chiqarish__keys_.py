n = int(input())
d = {}
for _ in range(n):
    p = input().split()
    d[p[0]] = p[1]
print(*sorted(d.keys()))