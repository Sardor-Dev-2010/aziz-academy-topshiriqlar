sonlar = list(map(int, input().split()))
print(sum([x for x in sonlar if x > 0]))