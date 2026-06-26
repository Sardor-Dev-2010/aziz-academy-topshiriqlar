
i = 7
while True:
    n = int(input())
    if i < n:
        print("High")
    elif i > n:
        print("Low")
    else:
        if i == n:
            print("Correct")
            break

