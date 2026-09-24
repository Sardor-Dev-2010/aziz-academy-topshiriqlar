import sys
def uzunlik(s):
    return len(s)
data = sys.stdin.read().split()
if data:
    print(uzunlik(data[0]))