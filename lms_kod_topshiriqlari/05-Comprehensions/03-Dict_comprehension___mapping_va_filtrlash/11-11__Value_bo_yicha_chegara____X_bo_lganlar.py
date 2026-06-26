n = int(input())
d = {}
for i in range(n):
    key, value = input().split()
    d[key] = int(value)
x = int(input())
natija = {k: v for k, v in d.items() if v >= x}
print(natija)