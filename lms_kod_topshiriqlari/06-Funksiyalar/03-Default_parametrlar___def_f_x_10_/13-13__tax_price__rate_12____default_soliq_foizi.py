import sys
d = sys.stdin.read().split()
price = float(d[0])
rate = float(d[1]) if len(d) > 1 else 12
print('%.2f' % (price * (1 + rate / 100)))