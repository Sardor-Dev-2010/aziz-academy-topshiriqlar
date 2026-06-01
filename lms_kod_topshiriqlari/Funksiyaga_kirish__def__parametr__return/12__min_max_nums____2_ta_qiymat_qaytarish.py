def min_max(nums):
    return min(nums), max(nums)
nums = list(map(int, input().split()))
kichik, katta = min_max(nums)
print(kichik)
print(katta)
