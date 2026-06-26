
total = 0
n = int(input())
for i in range(1, n + 1):
    if i % 9 == 0:
        continue
    total += i  
print(total) 