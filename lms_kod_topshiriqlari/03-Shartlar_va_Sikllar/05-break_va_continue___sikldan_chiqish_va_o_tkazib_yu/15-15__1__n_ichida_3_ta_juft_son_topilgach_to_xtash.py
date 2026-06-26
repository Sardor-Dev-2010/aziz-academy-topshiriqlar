n = int(input())
i = 1 
c = 0 
while i <= n:
    if i % 2 == 0:
        c += 1
        if c == 3:
            print(i)
            break 
    i += 1
else:
     print("No")