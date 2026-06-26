n = int(input())
d = {}
for i in range(n):
    key, value = input().split()
    v = int(value)
    if v % 2 == 0:
        d[key] = 'even'
    else:
        d[key] = 'odd'
print(d)