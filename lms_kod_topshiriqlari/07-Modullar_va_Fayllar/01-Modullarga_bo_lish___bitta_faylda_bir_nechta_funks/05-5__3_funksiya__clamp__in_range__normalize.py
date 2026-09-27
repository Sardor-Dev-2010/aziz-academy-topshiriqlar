def clamp(x, lo, hi):
    if x < lo:
        return lo
    if x > hi:
        return hi
    return x

def in_range(x, lo, hi):
    return lo <= x <= hi

def normalize(x, lo, hi):
    return (x - lo) / (hi - lo)

x, lo, hi = map(int, input().split())
print(clamp(x, lo, hi))
print(in_range(x, lo, hi))
print("%.2f" % normalize(x, lo, hi))