def normalize(nums):
    mean = sum(nums) / len(nums)
    return [x - mean for x in nums]
numbers = list(map(int, input().split()))
result = normalize(numbers)
print(' '.join(f'{x:.2f}' for x in result))