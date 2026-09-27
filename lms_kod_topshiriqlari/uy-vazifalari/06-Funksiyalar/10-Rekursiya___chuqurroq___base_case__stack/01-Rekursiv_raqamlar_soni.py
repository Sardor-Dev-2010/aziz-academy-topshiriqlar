def raqamlar_soni(n):
    if n < 10:
        return 1
    return 1 + raqamlar_soni(n // 10)

n = int(input())
print(raqamlar_soni(n))