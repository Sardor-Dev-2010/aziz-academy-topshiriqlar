n = int(input())
tokens = []
while len(tokens) < n * 3:
    tokens.extend(input().split())

print(f"{'Product':<12} | {'Qty':>5} | {'Price':>7} | {'Total':>9}")
print("-" * 12 + "+" + "-" * 5 + "+" + "-" * 7 + "+" + "-" * 9)

grand = 0

for i in range(n):
    name = tokens[i*3]
    qty = int(tokens[i*3 + 1])
    price = int(tokens[i*3 + 2])
    total = qty * price
    grand += total
    
    print(f"{name:<12} | {qty:>5} | {price:>7} | {total:>9}")

print(f"GRAND: {grand}")