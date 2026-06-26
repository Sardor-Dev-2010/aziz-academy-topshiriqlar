
n = list(map(int, input().split()))
s = {x for x in n if x % 2 == 0}
if s:
    print(*sorted(s))
else:
    print("BO'SH")