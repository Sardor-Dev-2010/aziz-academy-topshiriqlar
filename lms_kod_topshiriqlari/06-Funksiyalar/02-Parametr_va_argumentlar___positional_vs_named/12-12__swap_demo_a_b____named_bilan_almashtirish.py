def pair(a, b):
    return f"a={a} b={b}"
a, b = map(int, input().split())
print(pair(a, b))
print(pair(a=b, b=a))