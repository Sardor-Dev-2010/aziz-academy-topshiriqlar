n = int(input())
total = 0
for i in range(1, n + 1):
    if i == 2:
        total += i
if total > 0:
    print(total)
else:
    print("No")