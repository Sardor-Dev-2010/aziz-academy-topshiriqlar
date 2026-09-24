import sys
def teskari(s):
    return s[::-1]
data = sys.stdin.read().split()
if data:
    print(teskari(data[0]))