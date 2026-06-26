def power(a, b):
    return a ** b
a, b = map(int, input().split())
print(power(a, b))
print(power(b=b, a=a))