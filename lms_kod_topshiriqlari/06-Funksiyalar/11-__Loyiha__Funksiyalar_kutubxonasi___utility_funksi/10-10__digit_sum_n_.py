import sys

def digit_sum(n):
    jami = 0
    while n > 0:
        jami += n % 10
        n = n // 10
    return jami

data = sys.stdin.read().split()
if data:
    print(digit_sum(int(data[0])))