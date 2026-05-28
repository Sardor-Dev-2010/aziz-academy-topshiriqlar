a = list(map(int, input().split()))
res = []
for x in a:
    if x % 2 == 0:
        res.append(str(x ** 2))
    else:
        res.append(str(x))
print(" ".join(res))