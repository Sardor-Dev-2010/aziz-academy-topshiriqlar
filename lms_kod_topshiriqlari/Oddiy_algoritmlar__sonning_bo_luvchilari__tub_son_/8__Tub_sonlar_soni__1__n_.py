
n = int(input())
total = 0
for son in range(2, n + 1):
    for i in range(2, son):
        if son % i == 0:
            break
    else:
         total += 1
print(total)
