A = input().split()
B = input().split()

juftlar = set()

for a in A:
    for b in B:
        juftlar.add((int(a), int(b)))

saralangan_juftlar = sorted(list(juftlar))

print(len(saralangan_juftlar))
for j in saralangan_juftlar:
    print(j[0], j[1])