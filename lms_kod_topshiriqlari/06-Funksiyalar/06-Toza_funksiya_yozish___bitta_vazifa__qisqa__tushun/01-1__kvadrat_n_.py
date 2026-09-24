import sys
def kvadrat(n):
    return n * n
data = sys.stdin.read().split()
if data:
    print(kvadrat(int(data[0])))