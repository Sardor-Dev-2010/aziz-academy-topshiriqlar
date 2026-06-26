n = int(input())
d = {}
for _ in range(n):
     k, v = input().split()
     d[k] = int(v)
for s in d.values():
    print(s)