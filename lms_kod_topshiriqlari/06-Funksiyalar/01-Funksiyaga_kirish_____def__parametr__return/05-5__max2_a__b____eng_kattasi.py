def max2(a, b):
    if a >= b:
        return a
    else:
        return b 
a, b = map(int, input().split())
print(max2(a, b))