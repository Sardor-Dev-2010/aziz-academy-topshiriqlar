nums = input().split()
seen = set()
ans = "Yo'q"
for x in nums:
    if x in seen:
        ans = x
        break
    seen.add(x)
print(ans)