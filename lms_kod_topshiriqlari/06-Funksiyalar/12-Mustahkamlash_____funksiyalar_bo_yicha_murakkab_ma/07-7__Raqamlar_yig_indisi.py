def raqamlar_yigindisi(n):
    return sum(int(d) for d in str(n))

n = int(input())
print(raqamlar_yigindisi(n))