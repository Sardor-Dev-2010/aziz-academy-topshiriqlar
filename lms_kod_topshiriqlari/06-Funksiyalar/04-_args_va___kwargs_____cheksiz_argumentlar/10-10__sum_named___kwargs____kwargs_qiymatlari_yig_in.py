import sys
lines = sys.stdin.read().splitlines()
n = int(lines[0])
s = 0
for i in range(n):
    k, v = lines[1 + i].split()
    s += int(v)
print(s)