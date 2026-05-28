
num = list(map(int, input().split()))
num1 = ['pos' if x > 0 else 'neg' if x < 0 else 'zero' for x in num]
print(' '.join(num1))