data = input().split()
chastota = {}
for d in data:
    s = int(d)
    chastota[s] = chastota.get(s, 0) + 1

bir_marta = []
for k in chastota:
    if chastota[k] == 1:
        bir_marta.append(k)

if not bir_marta:
    print("EMPTY")
else:
    print(*sorted(bir_marta))