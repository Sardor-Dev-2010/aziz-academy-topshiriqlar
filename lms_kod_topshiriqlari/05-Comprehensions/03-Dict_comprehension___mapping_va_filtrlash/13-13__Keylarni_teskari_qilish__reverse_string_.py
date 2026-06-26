n = int(input())
d = {}
for i in range(n):
    key, value = input().split()
    d[key[::-1]] = int(value)
print(d)