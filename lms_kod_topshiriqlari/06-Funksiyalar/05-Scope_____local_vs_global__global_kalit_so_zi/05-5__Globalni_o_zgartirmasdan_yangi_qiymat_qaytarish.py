import sys
x = 100
a = int(sys.stdin.read().split()[0])
def f(a):
    y = x + a
    return y
print(f(a))
print(x)