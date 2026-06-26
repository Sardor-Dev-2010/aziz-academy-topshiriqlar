def solve():
    tokens = []
    while True:
        try:
            line = input()
            if not line: break
            tokens.extend(line.split())
        except EOFError:
            break
            
    if not tokens: return
    
    n = int(tokens[0])
    items = tokens[1:1+n*2]
    x = int(tokens[-1])
    
    data = []
    for i in range(n):
        name = items[i*2]
        score = int(items[i*2+1])
        if score >= x:
            data.append(f"{name}={score}")
            
    if not data:
        print("EMPTY")
    else:
        for item in data:
            print(item)

if __name__ == '__main__':
    solve()