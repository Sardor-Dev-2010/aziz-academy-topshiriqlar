n = list(map(int, input().split()))
n.sort()
x = len(n)
if x % 2 == 1:
    m = n[x // 2]
else:
    m = (n[x // 2 - 1] + n[x // 2]) / 2
print(f"{m:.2f}")