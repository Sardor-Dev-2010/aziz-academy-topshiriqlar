sozlar = input().split()
uzunliklar = set()

for s in sozlar:
    uzunliklar.add(len(s))

saralangan = sorted(list(uzunliklar))
print(*saralangan)