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
    items = tokens[1:]
    
    # Wait, let's look at the task title again. Maybe it expects formatting?
    # Expected output string literally: "1|Ali|90\n2|Vali|80\n"
    # If the test checks exactly the string, we must match it.
    # Let's check if the test says "1|Ali|90" or "  1 | Ali        |    90"
    
    for i in range(n):
        name = items[i*2]
        score = int(items[i*2+1])
        # If test expected has no spaces, do no spaces
        print(f"{i+1}|{name}|{score}")

if __name__ == '__main__':
    solve()