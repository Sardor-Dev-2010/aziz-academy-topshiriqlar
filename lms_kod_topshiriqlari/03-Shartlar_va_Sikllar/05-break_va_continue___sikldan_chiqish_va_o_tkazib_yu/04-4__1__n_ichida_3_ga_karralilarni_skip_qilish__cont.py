
n = int(input())
i = 1
while i <= n:
    if i % 3 == 0:
        i += 1
        continue
    print(i)
    i += 1