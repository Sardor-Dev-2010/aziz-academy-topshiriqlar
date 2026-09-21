n = int(input())
mahsulotlar = []
for _ in range(n):
    nom, narx = input().split()
    mahsulotlar.append({"nom": nom, "narx": int(narx)})
qidirilayotgan = input()
nomlar = [m["nom"] for m in mahsulotlar]
if qidirilayotgan in nomlar:
    print("YES")
else:
    print("NO")