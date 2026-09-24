import sys
lines = sys.stdin.read().splitlines()
prefix = lines[0]
n = int(lines[1])
d = {}
for i in range(n):
    k, v = lines[2 + i].split()
    d[prefix + k] = int(v)
print(d)