n = int(input())
d = {}
for _ in range(n):
    p = input().split()
    d[p[0]] = int(p[1])
print(sum(d.values()))