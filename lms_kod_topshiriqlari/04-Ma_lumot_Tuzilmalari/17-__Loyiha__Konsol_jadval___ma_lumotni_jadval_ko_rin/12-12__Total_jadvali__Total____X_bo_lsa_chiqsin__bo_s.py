# Task 12 Fix
n_line = input().split()
if not n_line:
    n = 0
else:
    n = int(n_line[0])

tokens = []
while len(tokens) < n * 3 + 1:
    tokens.extend(input().split())

limit = int(tokens[-1])
all_items = tokens[:-1]

print(f"{'Product':<12} | {'Qty':>5} | {'Price':>7} | {'Total':>9}")
print("-" * 12 + "+" + "-" * 5 + "+" + "-" * 7 + "+" + "-" * 9)

bor_mi = False
for i in range(n):
    p_name = all_items[i*3]
    p_qty = int(all_items[i*3+1])
    p_price = int(all_items[i*3+2])
    p_total = p_qty * p_price
    
    if p_total >= limit:
        print(f"{p_name:<12} | {p_qty:>5} | {p_price:>7} | {p_total:>9}")
        bor_mi = True

if not bor_mi:
    print("EMPTY")