
while True:
    qator = input().split()
    if len(qator) == 1:
        n = int(qator[0])
        if n == 0:
            print("Exit")
            break
    else:
        a, b = map(int, qator)
        n = int(input())
        if n == 1:
            print(a + b)
        elif n == 0:
            print("Exit")
            break
