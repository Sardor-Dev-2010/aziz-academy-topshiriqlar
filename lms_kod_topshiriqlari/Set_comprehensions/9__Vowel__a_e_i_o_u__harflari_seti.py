w = input().strip()
unli = {'a', 'e', 'i', 'o', 'u'}
top = set()
for h in w.lower():
    if h in unli:
        top.add(h)
if top:
    print(' '.join(sorted(top)))
else:
    print("BO'SH")