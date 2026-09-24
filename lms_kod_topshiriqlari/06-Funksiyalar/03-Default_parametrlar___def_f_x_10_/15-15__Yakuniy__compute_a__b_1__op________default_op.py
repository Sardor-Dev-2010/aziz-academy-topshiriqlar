import sys
d = sys.stdin.read().split()
a = int(d[0])
b = int(d[1]) if len(d) > 1 else 1
op = d[2] if len(d) > 2 else '+'
if op == '+':
    print(a + b)
elif op == '-':
    print(a - b)
elif op == '*':
    print(a * b)
else:
    print('%.2f' % (a / b))