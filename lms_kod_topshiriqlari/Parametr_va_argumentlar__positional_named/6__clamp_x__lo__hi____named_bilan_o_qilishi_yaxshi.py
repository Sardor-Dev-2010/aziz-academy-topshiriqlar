def clamp(x, lo, hi):
    if x < lo:
        return lo
    if x > hi:
        return hi
    else:
        return x
x, lo, hi = map(int, input().split())
print(clamp(x, lo, hi))
print(clamp(lo=lo, hi=hi, x=x))
