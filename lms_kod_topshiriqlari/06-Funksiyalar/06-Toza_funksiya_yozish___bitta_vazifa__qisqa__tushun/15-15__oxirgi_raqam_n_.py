import sys
def oxirgi_raqam(n):
    return n % 10
data = sys.stdin.read().split()
if data:
    print(oxirgi_raqam(int(data[0])))