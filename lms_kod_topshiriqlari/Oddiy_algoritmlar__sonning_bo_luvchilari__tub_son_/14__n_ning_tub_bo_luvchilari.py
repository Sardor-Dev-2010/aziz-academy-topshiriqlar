
n = int(input())
for i in range(2, n + 1):
    if n % i == 0:
        tub = True
        for j in range(2, i):
            if i % j == 0:
                tub = False
        if tub:
            print(i)
