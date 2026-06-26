
i = 42 
while True:
    n = int(input())
    if n > i:
        print("High")
    elif n < i:
        print("Low")
    else:
        if n == i:
            print("Correct")
            break