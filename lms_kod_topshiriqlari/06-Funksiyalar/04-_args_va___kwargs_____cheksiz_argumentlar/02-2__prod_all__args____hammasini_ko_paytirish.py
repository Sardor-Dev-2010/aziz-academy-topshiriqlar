import sys
nums = list(map(int, sys.stdin.read().split()))
p = 1
for x in nums:
    p *= x
print(p)