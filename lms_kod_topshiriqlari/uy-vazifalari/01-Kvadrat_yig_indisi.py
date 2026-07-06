# for siklida sonlar kvadratini yig'indisini toping
# 1, 3 -> 1 + 4 + 9 = 14
a = int(input())
summa = 0
for i in range(1, a):
    summa += i * i
print(summa)