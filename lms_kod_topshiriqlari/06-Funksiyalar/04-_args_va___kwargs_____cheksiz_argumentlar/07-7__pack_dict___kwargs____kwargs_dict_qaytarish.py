import sys
lines = sys.stdin.read().splitlines()
n = int(lines[0])
d = {}
for i in range(n):
    k, v = lines[1 + i].split()
    d[k] = int(v)
print(d)