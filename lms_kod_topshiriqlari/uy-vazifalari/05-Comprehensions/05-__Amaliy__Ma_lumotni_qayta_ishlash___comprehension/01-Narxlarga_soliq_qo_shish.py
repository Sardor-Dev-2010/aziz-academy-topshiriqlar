prices = list(map(int, input().split()))
print([p + p * 12 // 100 for p in prices])