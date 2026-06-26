
num = list(map(str, input().split()))
num1 = [str(x) for x in num if len(x) >= 5]
if num1:
    print(' '.join(num1))
else:
    print("BO'SH")
