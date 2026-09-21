soz = input()
hisob = {}
for h in soz:
    hisob[h] = hisob.get(h, 0) + 1
print(' '.join(f'{k}:{v}' for k, v in hisob.items()))