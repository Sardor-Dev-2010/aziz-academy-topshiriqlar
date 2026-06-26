n = int(input())
rows = []
for i in range(n):
    product, qty, price = input().split()
    rows.append((product, int(qty), int(price)))
print(f"{'Product':<12} | {'Qty':>5} | {'Price':>7}")
print("-" * 12 + "+" + "-" * 5 + "+" + "-" * 7)
for product, qty, price, in rows:
    print(f"{product:<12} | {qty:>5} | {price:>7}")