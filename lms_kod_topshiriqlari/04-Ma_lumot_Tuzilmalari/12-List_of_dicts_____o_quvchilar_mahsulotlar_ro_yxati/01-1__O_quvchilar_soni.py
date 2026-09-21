n = int(input())
talabalar = []
for _ in range(n):
    ism, baho = input().split()
    talabalar.append({"ism": ism, "baho": int(baho)})
print(len(talabalar))