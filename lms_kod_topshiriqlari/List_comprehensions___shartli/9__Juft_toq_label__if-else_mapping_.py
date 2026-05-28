
num = list(map(int, input().split()))
nums = ['even' if x % 2 == 0 else 'odd' for x in num]
print(' '.join(nums))
