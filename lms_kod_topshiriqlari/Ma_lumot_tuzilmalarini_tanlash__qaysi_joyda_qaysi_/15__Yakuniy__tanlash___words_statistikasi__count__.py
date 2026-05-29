gap = input().split()
jami = len(gap)

hisoblagich = {}
for s in gap:
    soz = s.lower()
    hisoblagich[soz] = hisoblagich.get(soz, 0) + 1

unikal = len(hisoblagich)

sozlar = sorted(list(hisoblagich.keys()))
max_m = -1
eng_yaxshi = ""

for k in sozlar:
    if hisoblagich[k] > max_m:
        max_m = hisoblagich[k]
        eng_yaxshi = k

print(f"total: {jami}")
print(f"unique: {unikal}")
print(f"top: {eng_yaxshi} {max_m}")