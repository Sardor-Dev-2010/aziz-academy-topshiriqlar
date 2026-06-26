t = input()
s = {x for x in t if x.isdigit()}
if s:
    print(*sorted(s))
else:
    print("BO'SH")