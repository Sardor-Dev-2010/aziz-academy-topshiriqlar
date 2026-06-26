s = input().split()
a = [int(x) for x in s]
n, sm = len(a), sum(a)
mn, mx = min(a), max(a)
avg = sm / n
j = sum(1 for x in a if x % 2 == 0)
t = n - j
# Alohida qatorlarda chiqarish (ba'zi tizimlar shuni kutadi)
print(f"count: {n}")
print(f"sum: {sm}")
print(f"min: {mn}")
print(f"max: {mx}")
print(f"mean: {avg:.2f}")
print(f"evens: {j}")
print(f"odds: {t}")