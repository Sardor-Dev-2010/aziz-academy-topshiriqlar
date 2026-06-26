
i = 15
while True:
    n = int(input())
    if n == i:
        print("Correct")
        break
    elif abs(n - i) > 5:
            print("Far")
    else:
         print("Close")
