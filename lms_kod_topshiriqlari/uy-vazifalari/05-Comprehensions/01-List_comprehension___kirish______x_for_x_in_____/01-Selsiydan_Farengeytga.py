nums = list(map(int, input().split()))
f = [c * 9 // 5 + 32 for c in nums]
print(f)