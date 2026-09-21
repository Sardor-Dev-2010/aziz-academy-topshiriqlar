soz = input()
d = {}
for h in soz:
    d[h] = d.get(h, 0) + 1
for h in sorted(d):
    print(f'{h}={d[h]}')