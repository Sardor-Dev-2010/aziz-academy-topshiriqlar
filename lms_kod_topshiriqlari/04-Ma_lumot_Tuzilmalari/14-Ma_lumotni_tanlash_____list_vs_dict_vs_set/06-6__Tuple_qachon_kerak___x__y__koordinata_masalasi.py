line1 = input().split()
if line1:
    n = int(line1[0])
    tokens = line1[1:]
    while len(tokens) < n * 2:
        tokens.extend(input().split())
        
    best_x = -10**18
    best_y = 10**18
    
    for i in range(n):
        x = int(tokens[i*2])
        y = int(tokens[i*2+1])
        
        if x > best_x:
            best_x = x
            best_y = y
        elif x == best_x:
            if y < best_y:
                best_y = y
    print(best_x, best_y)