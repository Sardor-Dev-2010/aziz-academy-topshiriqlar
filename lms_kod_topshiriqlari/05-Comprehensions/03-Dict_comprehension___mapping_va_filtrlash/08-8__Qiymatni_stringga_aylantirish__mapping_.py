n = int(input())
d = {}
for i in range(n):
    key, value = input().split()
    d[key] = str(value)
print(d)