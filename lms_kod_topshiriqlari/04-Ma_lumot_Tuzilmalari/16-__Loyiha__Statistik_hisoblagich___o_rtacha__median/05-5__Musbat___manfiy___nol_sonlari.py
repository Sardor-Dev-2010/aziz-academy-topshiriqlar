n = list(map(int, input().split()))
c1 = 0
c2 = 0
c3 = 0
for i in n:
    if i > 0:
        c1 += 1
    elif i < 0:
        c2 += 1
    else:
        c3 += 1
print(c1)
print(c2)
print(c3)