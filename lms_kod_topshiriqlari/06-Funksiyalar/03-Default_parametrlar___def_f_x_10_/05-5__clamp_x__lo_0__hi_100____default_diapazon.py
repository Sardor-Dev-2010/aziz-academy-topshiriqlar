import sys
d = sys.stdin.read().split()
x = int(d[0])
lo = int(d[1]) if len(d) > 1 else 0
hi = int(d[2]) if len(d) > 2 else 100
print(max(lo, min(hi, x)))