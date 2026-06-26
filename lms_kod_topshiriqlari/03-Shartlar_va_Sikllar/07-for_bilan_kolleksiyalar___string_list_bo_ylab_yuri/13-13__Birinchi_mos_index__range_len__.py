
n = int(input())
s = list(map(int, input().split()))
x = int(input())
total = -1
for i in range(len(s)):
    if s[i] == x:
        total = i
        break
print(total)