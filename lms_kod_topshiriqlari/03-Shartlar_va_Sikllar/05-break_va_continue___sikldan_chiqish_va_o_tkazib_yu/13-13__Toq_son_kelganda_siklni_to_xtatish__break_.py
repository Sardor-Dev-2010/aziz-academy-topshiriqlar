total = 0 
while True:
    n = int(input())
    if n % 2 != 0:
        break 
    total += n
print(total)