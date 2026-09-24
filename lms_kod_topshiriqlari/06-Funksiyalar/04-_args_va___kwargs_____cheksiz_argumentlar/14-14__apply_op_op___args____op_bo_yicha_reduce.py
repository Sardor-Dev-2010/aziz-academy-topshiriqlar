import sys
lines = sys.stdin.read().splitlines()
op = lines[0]
nums = list(map(int, lines[1].split()))
if op == 'sum':
    print(sum(nums))
elif op == 'prod':
    p = 1
    for x in nums:
        p *= x
    print(p)
elif op == 'max':
    print(max(nums))
else:
    print(min(nums))