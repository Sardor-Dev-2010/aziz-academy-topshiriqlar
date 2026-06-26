n = list(map(int, input().split()))
s = {x ** 2 for x in n}
print(*sorted(s))