n = int(input())
i = 1
if n < 7:
    print("No")
else:
    while i <= n:
        if i % 7 == 0:
            print(i)
            break
        i += 1


        