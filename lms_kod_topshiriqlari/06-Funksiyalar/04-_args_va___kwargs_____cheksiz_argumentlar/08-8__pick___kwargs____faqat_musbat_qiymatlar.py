import sys
lines = sys.stdin.read().splitlines()
n = int(lines[0])
d = {}
for i in range(n):
    k, v = lines[1 + i].split()
    if int(v) > 0:
        d[k] = int(v)
print(d)