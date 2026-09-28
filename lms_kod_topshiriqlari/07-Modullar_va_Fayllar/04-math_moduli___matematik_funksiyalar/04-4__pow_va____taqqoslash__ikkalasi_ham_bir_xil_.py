import math

a, b = input().split()
a = float(a)
b = float(b)
print('%.0f' % math.pow(a, b))
print(int(float(a) ** float(b)))