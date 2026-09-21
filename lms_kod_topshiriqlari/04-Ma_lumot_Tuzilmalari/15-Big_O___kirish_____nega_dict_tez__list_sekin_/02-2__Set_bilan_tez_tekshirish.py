n = int(input())
s = set()
for i in range(n):
    s.add(int(input()))
target = int(input())
print(target in s)