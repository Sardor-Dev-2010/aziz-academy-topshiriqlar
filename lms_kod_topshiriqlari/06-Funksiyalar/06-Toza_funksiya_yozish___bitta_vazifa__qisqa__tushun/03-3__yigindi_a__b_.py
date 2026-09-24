import sys
def yigindi(a, b):
    return a + b
data = sys.stdin.read().split()
if data:
    print(yigindi(int(data[0]), int(data[1])))