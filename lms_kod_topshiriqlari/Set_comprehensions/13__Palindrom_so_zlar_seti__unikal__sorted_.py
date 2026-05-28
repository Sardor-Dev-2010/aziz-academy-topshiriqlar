w = input().split()
p = {i.lower() for i in w if i.lower() == i.lower()[::-1]}
if p:
    for x in sorted(p):
        print(x, end=' ')
else:
    print("BO'SH")