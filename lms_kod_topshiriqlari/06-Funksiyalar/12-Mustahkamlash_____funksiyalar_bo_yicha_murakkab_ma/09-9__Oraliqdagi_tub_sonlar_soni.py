def tub(x):
    if x < 2:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

a, b = map(int, input().split())
soni = 0
for x in range(a, b + 1):
    if tub(x):
        soni = soni + 1
print(soni)