def raqamlar_yigindisi(n):
    yigindi = 0
    while n > 0:
        yigindi += n % 10
        n //= 10
    return yigindi

n = int(input())
print(raqamlar_yigindisi(n))