
a, b = map(int, input().split())
kichik = min(a, b)
for i in range(1, kichik + 1):
    if a % i == 0 and b % i == 0:
        print(i)
