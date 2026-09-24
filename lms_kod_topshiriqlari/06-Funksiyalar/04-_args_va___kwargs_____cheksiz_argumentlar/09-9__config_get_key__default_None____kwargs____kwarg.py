import sys
lines = sys.stdin.read().splitlines()
key = lines[0]
n = int(lines[1])
d = {}
for i in range(n):
    k, v = lines[2 + i].split()
    d[k] = int(v)
print(d.get(key, 0))