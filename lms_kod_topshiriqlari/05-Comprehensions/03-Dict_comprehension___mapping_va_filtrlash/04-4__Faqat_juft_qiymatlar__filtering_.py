n = int(input())
d = {}
for i in range(n):
    key, value = input().split()
    value = int(value)
    if value % 2 == 0:
        d[key] = value
print(d)