
n = int(input())
total = 0
i = n
while i > 0:
    total += i % 10
    i //= 10
print(total)