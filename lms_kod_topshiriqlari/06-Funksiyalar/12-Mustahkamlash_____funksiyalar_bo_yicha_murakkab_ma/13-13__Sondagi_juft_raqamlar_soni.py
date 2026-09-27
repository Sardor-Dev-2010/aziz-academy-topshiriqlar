def juft_raqamlar_soni(n):
    soni = 0
    for d in str(n):
        if int(d) % 2 == 0:
            soni = soni + 1
    return soni

n = int(input())
print(juft_raqamlar_soni(n))