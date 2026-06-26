n = int(input())
d = {}
s = set()
for i in range(n):
    key, value = input().split()
    value = int(value)
    if value not in s:
        d[key] = value
        s.add(value)
print(d)