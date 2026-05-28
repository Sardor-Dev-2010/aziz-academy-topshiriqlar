
n = int(input())
if n == 1:
    print(0)
else:
    for i in range(2, n):
        if n % i == 0:
            print(i)
            break
    else:
         print(n)
        
