def diff(a, b):
    return a - b
a, b = map(int, input().split())
result1 = diff(a, b)
result2 = diff(b=a, a=b)
print(result1)
print(result2)