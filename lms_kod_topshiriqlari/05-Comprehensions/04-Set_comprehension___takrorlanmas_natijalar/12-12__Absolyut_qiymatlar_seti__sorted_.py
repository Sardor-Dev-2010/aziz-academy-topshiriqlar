s = list(map(int, input().split()))
a = {abs(x) for x in s}
for value in sorted(a):
    print(value, end=' ')