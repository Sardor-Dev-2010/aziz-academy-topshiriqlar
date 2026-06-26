
def clamp(x, lo, hi):
    if x < lo:
        return lo
    elif x > hi:
        return hi
    else:
        return x
x, lo, hi = map(int, input().split())
print(clamp(x, lo, hi))