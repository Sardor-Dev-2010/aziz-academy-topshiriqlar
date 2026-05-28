n = int(input())
d = {}
for i in range(n):
    k, v = input().split()
    d[k] = f"{k}:{v}"
print(d)