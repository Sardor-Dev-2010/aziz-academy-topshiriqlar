import sys
def ikki_barobar(n):
    return n * 2
data = sys.stdin.read().split()
if data:
    print(ikki_barobar(int(data[0])))