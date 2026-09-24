import sys
lines = sys.stdin.read().splitlines()
n = int(lines[0])
x = 2
def mul(k):
    global x
    x *= k
    print(x)
for i in range(n):
    mul(int(lines[1 + i]))