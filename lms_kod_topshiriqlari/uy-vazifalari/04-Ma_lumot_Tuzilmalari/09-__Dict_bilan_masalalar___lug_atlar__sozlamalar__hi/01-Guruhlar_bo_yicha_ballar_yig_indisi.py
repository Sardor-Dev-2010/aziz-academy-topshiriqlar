n = int(input())
d = {}
for _ in range(n):
    p = input().split()
    d[p[0]] = d.get(p[0], 0) + int(p[1])
for k in sorted(d):
    print(k, d[k])