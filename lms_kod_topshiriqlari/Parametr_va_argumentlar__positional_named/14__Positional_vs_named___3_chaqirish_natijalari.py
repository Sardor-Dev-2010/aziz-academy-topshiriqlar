def f(a, b, c):
    return a * 100 + b * 10 + c
a, b, c = map(int, input().split())
print(f(a, b, c))
print(f(c=c, a=a, b=b))
print(f(a=c, b=b, c=a))