n = int(input())
d = {}
for i in range(n):
    key, value = input().split()
    abs_value = abs(int(value))
    if abs_value >= 5:
        d[key] = abs_value
print(d)