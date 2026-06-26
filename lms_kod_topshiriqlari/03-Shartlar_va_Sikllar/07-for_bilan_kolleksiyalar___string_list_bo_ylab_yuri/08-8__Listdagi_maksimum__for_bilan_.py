
n = int(input())
s = list(map(int, input().split()))
m = s[0]
for i in range(1, n):
    if s[i] > m:
        m = s[i]
print(m)
