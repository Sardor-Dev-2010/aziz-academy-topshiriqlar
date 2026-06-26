
n = int(input())
i = 1
while i <= n:
    if i % 6 == 0:
        i += 1
        continue
    print(i)
    i += 1
