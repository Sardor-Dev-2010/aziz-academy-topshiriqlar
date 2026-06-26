n = int(input())
product_width = 12
qty_width = 5
price_width = 7
total_width = 9
print(f"{'Product':<{product_width}} | {'Qty':>{qty_width}} | {'Price':>{price_width}} | {'Total':>{total_width}}")
print('-' * product_width + '+' + '-' * qty_width + '+' + '-' * price_width + '+' + '-' * total_width)
grand_total = 0 
for i in range(n):
    product, qty, price = input().split()
    qty = int(qty)
    price = int(price)
    total = qty * price 
    grand_total += total 
    print(f"{product:{product_width}} | {qty:>{qty_width}} | {price:>{price_width}} | {total:>{total_width}}")
    