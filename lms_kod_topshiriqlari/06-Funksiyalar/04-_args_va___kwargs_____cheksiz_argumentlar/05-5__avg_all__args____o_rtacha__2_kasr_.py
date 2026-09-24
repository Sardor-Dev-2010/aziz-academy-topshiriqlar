import sys
nums = list(map(int, sys.stdin.read().split()))
print('%.2f' % (sum(nums) / len(nums)))