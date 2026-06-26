# Task 15 Final Fix
n_str = input().split()
if not n_str:
    n = 0
else:
    n = int(n_str[0])

tokens = []
while len(tokens) < n * 3:
    tokens.extend(input().split())

print(f"{'Product':<12} | {'Qty':>5} | {'Price':>7} | {'Total':>9}")
print("-" * 12 + "+" + "-" * 5 + "+" + "-" * 7 + "+" + "-" * 9)

b_name = ""
b_total = -1
g_jami = 0
p_jami = 0

for i in range(n):
    name = tokens[i*3]
    qty = int(tokens[i*3+1])
    prc = int(tokens[i*3+2])
    tot = qty * prc
    
    print(f"{name:<12} | {qty:>5} | {prc:>7} | {tot:>9}")
    
    if tot > b_total or (tot == b_total and (b_name == "" or name < b_name)):
        b_total = tot
        b_name = name
    
    g_jami += tot
    p_jami += prc

avg_p = p_jami / n if n > 0 else 0

print(f"BEST: {b_name} {b_total}")
print(f"GRAND: {g_jami}")
print(f"AVG_PRICE: {avg_p:.2f}")