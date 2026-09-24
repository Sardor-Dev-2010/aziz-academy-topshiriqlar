import sys
n = int(sys.stdin.read().split()[0])
counter = 0
def inc():
    global counter
    counter += 1
    print(counter)
for _ in range(n):
    inc()