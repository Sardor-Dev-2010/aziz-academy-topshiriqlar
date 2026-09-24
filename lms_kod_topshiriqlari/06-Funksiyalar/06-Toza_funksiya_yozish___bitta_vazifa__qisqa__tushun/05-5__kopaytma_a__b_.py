import sys
def kopaytma(a, b):
    return a * b
data = sys.stdin.read().split()
if data:
    print(kopaytma(int(data[0]), int(data[1])))