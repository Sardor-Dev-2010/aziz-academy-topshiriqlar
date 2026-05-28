s_sonlar = input().split()
sonlar = []
for s in s_sonlar:
    sonlar.append(int(s))
unikal = sorted(set(sonlar))
print(*unikal)