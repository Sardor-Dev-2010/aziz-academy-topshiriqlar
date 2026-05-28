
i = 20
x = 0
while True:
    n = int(input())
    x += 1
    if n == i:
        print("Correct")
        break
    elif n < i:
        print("Low")
    elif n > i:
        print("Invalid")
print(x)
        