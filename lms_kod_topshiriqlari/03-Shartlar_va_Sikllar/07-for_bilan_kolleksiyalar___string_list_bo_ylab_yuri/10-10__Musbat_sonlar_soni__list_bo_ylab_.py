
n = int(input())
s = list(map(int, input().split()))
m = 0
for i in s:
    if i > 0:
        m += 1
print(m)