n = int(input())
talabalar = []
for _ in range(n):
    ism, baho = input().split()
    talabalar.append({"ism": ism, "baho": int(baho)})
soni = 0
for t in talabalar:
    if t["baho"] > 80:
        soni += 1
print(soni)