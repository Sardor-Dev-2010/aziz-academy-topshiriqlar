n = int(input())
d = {}
for i in range(n):
    key, value = input().split()
    value = int(value)
    if abs(value) >= 2:
        if value % 2 != 0:
            d[key] = value * 3
        else:
            d[key] = value * 2
print(d)