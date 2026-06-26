n = int(input())
d = {}
for i in range(n):
    key, value = input().split()
    if key.startswith('a'):
        d[key] = int(value)
print(d)