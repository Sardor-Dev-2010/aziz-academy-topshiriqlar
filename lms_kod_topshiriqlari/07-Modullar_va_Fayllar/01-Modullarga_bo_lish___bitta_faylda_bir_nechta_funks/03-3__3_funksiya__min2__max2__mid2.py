def min2(a, b):
    if a < b:
        return a
    return b

def max2(a, b):
    if a > b:
        return a
    return b

def mid2(a, b):
    return (a + b) / 2

a, b = map(int, input().split())
print(min2(a, b))
print(max2(a, b))
print("%.2f" % mid2(a, b))