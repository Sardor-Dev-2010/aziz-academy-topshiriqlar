n = int(input())
d = {}
for _ in range(n):
     k, v = input().split()
     d[k] = int(v)
d1 = {}
for k, v in d.items():
    d1[k] = v * 2
print(d1)