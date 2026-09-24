narxlar = list(map(int, input().split()))
print([p-10 for p in narxlar if p > 0])