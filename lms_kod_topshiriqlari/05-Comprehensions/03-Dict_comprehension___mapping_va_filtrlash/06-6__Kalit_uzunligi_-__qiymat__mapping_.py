
n = int(input())
d = {}
for i in range(n):
    key, value = input().split()
    d[len(key)] = int(value)
print(d)