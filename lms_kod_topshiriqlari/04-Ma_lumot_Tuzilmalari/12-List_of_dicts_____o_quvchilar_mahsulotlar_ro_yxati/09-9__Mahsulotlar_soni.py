n = int(input())
mahsulotlar = []
for _ in range(n):
    nom, narx = input().split()
    mahsulotlar.append({"nom": nom, "narx": int(narx)})
print(len(mahsulotlar))