def collatz_qadamlari(n):
    qadam = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        qadam = qadam + 1
    return qadam

n = int(input())
print(collatz_qadamlari(n))