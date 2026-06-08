def calc(a, b, c):
    return a + b * c
a, b, c = map(int, input().split())
print(calc(a, b, c))
print(calc(a, c=c, b=b))