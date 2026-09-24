import sys
d = list(map(float, sys.stdin.read().split()))
print('%.2f' % (sum(d) / len(d)))