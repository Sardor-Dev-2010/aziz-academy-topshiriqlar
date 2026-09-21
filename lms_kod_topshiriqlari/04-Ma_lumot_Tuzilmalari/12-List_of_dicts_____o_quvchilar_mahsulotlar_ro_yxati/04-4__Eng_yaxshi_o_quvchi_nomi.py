n = int(input())
talabalar = []
for _ in range(n):
    ism, baho = input().split()
    talabalar.append({"ism": ism, "baho": int(baho)})
eng_yaxshi = max(talabalar, key=lambda t: t["baho"])
print(eng_yaxshi["ism"])