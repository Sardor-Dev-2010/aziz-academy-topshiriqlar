n = int(input())
talabalar = []
for _ in range(n):
    ism, baho = input().split()
    talabalar.append({"ism": ism, "baho": int(baho)})
qidirilgan_baho = int(input())
soni = 0
for t in talabalar:
    if t["baho"] == qidirilgan_baho:
        soni += 1
print(soni)