import sys
d = sys.stdin.read().split()
a = d[0]
b = d[1] if len(d) > 1 else '-'
c = d[2] if len(d) > 2 else '-'
print(a, b, c)