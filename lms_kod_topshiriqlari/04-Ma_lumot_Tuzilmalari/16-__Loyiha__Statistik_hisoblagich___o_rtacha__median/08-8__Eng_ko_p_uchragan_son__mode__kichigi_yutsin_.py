n = list(map(int, input().split()))
c = {}
for i in n:
    c[i] = c.get(i, 0) + 1
c2 = - 1
m = None
for x, d in c.items():
    if d > c2 or (d == c2 and x < m):
        c2 = d
        m = x
print(m)