n = list(map(int, input().split()))
nums = {x for x in n}
print(*sorted(nums))