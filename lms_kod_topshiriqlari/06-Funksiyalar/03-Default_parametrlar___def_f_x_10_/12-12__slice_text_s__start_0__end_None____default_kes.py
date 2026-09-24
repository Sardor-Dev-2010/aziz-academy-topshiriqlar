import sys
d = sys.stdin.read().split()
s = d[0]
start = int(d[1]) if len(d) > 1 else 0
end = int(d[2]) if len(d) > 2 else None
print(s[start:end])