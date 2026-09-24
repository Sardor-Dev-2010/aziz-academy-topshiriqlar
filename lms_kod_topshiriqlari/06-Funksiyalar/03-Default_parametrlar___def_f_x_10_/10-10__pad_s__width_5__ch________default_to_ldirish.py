import sys
d = sys.stdin.read().split()
s = d[0]
width = int(d[1]) if len(d) > 1 else 5
ch = d[2] if len(d) > 2 else '.'
print(s.ljust(width, ch))