import sys
d = sys.stdin.read().split()
s = d[0]
n = int(d[1]) if len(d) > 1 else 2
print(s * n)