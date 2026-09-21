n = int(input())
sonlar = []
for i in range(n):
    sonlar.append(int(input()))
target = int(input())
if target in sonlar:
    print("bor")
else:
    print("yo'q")