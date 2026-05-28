nums = list(map(int, input().split()))
mean = sum(nums) / len(nums)
print(*(format(x - mean, ".2f") for x in nums))