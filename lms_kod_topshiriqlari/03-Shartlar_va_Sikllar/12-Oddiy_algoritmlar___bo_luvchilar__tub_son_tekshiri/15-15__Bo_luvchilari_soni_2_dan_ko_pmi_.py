
n = int(input())
tub = True
if n == 1:
    tub = False
else:
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            tub = False
            break
print("No" if tub else 'Yes')
        