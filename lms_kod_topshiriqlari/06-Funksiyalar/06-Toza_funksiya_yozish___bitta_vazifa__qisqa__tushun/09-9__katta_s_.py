import sys
def katta(s):
    return s.upper()
data = sys.stdin.read().split()
if data:
    print(katta(data[0]))