n = int(input())
mahsulotlar = []
for _ in range(n):
    nom, narx = input().split()
    mahsulotlar.append({"nom": nom, "narx": int(narx)})
eng_qimmat = max(mahsulotlar, key=lambda m: m["narx"])
print(eng_qimmat["narx"])