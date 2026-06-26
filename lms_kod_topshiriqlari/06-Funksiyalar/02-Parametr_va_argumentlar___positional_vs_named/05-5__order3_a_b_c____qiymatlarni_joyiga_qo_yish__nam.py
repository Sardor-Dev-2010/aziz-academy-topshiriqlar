def order3(a, b, c):
    return f"a={a} b={b} c={c}"
x, y, z = map(int, input().split())
print(order3(x, y, z))
print(order3(c=x, b=y, a=z))