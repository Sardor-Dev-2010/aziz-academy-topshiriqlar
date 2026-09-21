n = int(input())
mahsulotlar = []
for _ in range(n):
    nom, narx = input().split()
    mahsulotlar.append({"nom": nom, "narx": int(narx)})
soni = 0
for m in mahsulotlar:
    if m["narx"] < 50:
        soni += 1
print(soni)