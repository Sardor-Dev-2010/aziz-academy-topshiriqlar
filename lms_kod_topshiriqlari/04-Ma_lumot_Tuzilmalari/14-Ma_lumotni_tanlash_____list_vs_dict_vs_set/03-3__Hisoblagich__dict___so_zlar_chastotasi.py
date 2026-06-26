gap = input().lower().split()
sanoq = {}
for soz in gap:
    if soz in sanoq:
        sanoq[soz] += 1
    else:
        sanoq[soz] = 1

sozlar = sorted(sanoq.keys())
for s in sozlar:
    print(f"{s} {sanoq[s]}")