n = int(input().strip())
items = []
for _ in range(n):
    name, price, qty = input().split()
    items.append({'name': name, 'price': int(price), 'qty': int(qty)})
max_value = -1 
max_name = ""
for item in items:
    value = item['price'] * item['qty']
    if value > max_value:
        max_value = value
        max_name = item['name']
print(max_name)

