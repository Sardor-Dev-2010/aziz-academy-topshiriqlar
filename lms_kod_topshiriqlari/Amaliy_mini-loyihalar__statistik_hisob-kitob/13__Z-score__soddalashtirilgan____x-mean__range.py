nums = list(map(int, input().split()))
mean = sum(nums) / len(nums)
farq = max(nums) - min(nums)
print(*(format((x - mean) / farq if farq != 0 else 0, ".2f") for x in nums))