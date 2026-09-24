nums = [int(x) for x in input().split()]
nums.sort()
n = len(nums)
if n % 2 == 1:
    print(nums[n // 2])
else:
    print((nums[n // 2 - 1] + nums[n // 2]) // 2)