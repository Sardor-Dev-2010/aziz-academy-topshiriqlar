n = int(input())
s = 0
for i in range(1, n):
    if n % i == 0:
        s += i
print('MUKAMMAL' if s == n and n > 1 else 'MUKAMMAL EMAS')