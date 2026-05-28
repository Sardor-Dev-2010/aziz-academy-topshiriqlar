
n = int(input())
if n < 2:
    print("No")
else:
    s = 2
    while s <= n:
        t = True
        b = 2
        while b * b <= s:
            if s % b == 0:
                t = False
                break 
            b += 1
        if t:
            print(s)
            break 
        s += 1