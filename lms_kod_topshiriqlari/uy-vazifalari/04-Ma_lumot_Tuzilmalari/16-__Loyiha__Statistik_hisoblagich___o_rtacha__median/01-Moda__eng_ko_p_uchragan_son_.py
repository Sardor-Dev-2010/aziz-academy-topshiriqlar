nums = [int(x) for x in input().split()]
freq = {}
for x in nums:
    freq[x] = freq.get(x, 0) + 1
best = nums[0]
bestc = freq[best]
for x in nums:
    if freq[x] > bestc:
        bestc = freq[x]
        best = x
print(best)