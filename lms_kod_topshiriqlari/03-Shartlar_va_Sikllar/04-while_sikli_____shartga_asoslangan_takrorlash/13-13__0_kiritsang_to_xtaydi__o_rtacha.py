
sonlar = []
while True:
    son = int(input())
    if son == 0:
        break
    sonlar.append(son)
if not sonlar:
    print(0)
else:
    ortacha = sum(sonlar) / len(sonlar)
    print(ortacha)