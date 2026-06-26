
n = int(input())
s = {x for x in range(1, n + 1) if x % 3 == 0}
if s:
    print(*sorted(s))
else:
    print("BO'SH")