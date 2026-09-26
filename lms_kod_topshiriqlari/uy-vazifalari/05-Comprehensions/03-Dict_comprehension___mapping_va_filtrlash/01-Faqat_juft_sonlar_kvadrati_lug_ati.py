nums = list(map(int, input().split()))
print({x: x * x for x in nums if x % 2 == 0})