import sys
def kattaroq(a, b):
    if a > b:
        return a
    else:
        return b
data = sys.stdin.read().split()
if data:
    print(kattaroq(int(data[0]), int(data[1])))