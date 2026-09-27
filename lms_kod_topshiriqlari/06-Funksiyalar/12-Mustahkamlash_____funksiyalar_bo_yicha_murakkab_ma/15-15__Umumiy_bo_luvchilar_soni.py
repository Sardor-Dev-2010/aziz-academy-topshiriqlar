def umumiy_bo_luvchilar_soni(a, b):
    soni = 0
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            soni = soni + 1
    return soni

a, b = map(int, input().split())
print(umumiy_bo_luvchilar_soni(a, b))