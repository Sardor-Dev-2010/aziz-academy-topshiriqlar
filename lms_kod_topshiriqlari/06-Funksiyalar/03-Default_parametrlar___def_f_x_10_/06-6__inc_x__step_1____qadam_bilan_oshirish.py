import sys
d = sys.stdin.read().split()
x = int(d[0])
step = int(d[1]) if len(d) > 1 else 1
print(x + step)