n = int(input().strip())
items = []
for _ in range(n):
    name, price, qty = input().split()
    items.append({'name': name, 'price': int(price), 'qty': int(qty)})
total = 0
for item in items:
    total += item['price'] * item['qty']
print(total)