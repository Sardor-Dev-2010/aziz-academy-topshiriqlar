
n = int(input())
i = 1
while i <= n:
    if i % 4 == 0:
        print(i)
        break
    i += 1
else:
    print("No")