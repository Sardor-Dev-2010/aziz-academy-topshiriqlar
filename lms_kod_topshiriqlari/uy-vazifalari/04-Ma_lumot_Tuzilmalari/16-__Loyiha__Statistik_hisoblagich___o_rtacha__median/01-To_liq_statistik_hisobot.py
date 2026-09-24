nums = [int(x) for x in input().split()]
n = len(nums)
print("O'rtacha:", round(sum(nums) / n, 2))
nums.sort()
if n % 2 == 1:
    med = nums[n // 2]
else:
    med = (nums[n // 2 - 1] + nums[n // 2]) // 2
print("Mediana:", med)
freq = {}
for x in nums:
    freq[x] = freq.get(x, 0) + 1
maxc = max(freq.values())
mode = min([x for x in freq if freq[x] == maxc])
print("Moda:", mode)