w = input().split()
s = {len(i) for i in w}
print(*sorted(s))