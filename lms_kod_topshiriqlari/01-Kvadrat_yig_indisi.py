# for siklida sonlar kvadratini yig'indisini toping
# 1, 3 -> 1 + 4 + 9 = 14
a = int(input())
n = 3
summa = 0
for i in range(1, n + 1):
    summa += i * i
print(summa)