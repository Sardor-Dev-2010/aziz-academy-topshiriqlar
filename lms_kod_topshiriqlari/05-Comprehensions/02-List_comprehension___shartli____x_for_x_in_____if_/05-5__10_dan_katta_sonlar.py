
num = list(map(int, input().split()))
num1 = [str(x) for x in num if x > 10]
if num1:
    print(' '.join(num1))
else:
    print("BO'SH")