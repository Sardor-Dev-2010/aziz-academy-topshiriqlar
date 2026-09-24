nums = [int(x) for x in input().split()]
target = int(input())
seen = set()
ans = 'Yoq'
for x in nums:
    if (target - x) in seen:
        ans = 'Ha'
        break
    seen.add(x)
print(ans)