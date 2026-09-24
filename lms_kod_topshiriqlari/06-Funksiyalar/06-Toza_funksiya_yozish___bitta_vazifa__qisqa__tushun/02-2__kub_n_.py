import sys
def kub(n):
    return n ** 3
data = sys.stdin.read().split()
if data:
    print(kub(int(data[0])))