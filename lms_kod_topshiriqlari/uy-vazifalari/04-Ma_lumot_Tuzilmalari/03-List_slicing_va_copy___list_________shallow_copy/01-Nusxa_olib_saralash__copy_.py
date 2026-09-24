nums = input().split()
copy = nums[:]
copy.sort(key=int)
print(*nums)
print(*copy)