import sys
def ayirma(a, b):
    return a - b
data = sys.stdin.read().split()
if data:
    print(ayirma(int(data[0]), int(data[1])))