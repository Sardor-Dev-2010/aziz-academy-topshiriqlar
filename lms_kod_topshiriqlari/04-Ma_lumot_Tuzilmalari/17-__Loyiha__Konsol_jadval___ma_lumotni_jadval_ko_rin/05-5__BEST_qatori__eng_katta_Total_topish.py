n = int(input())
tokens = []
while len(tokens) < n * 3:
    tokens.extend(input().split())

print(f"{'Product':<12} | {'Qty':>5} | {'Price':>7} | {'Total':>9}")
print("-" * 12 + "+" + "-" * 5 + "+" + "-" * 7 + "+" + "-" * 9)

best_name = ""
best_total = -1

for i in range(n):
    name = tokens[i*3]
    qty = int(tokens[i*3 + 1])
    price = int(tokens[i*3 + 2])
    total = qty * price
    
    print(f"{name:<12} | {qty:>5} | {price:>7} | {total:>9}")
    
    if total > best_total or (total == best_total and (best_name == "" or name < best_name)):
        best_total = total
        best_name = name

print(f"BEST: {best_name} {best_total}")