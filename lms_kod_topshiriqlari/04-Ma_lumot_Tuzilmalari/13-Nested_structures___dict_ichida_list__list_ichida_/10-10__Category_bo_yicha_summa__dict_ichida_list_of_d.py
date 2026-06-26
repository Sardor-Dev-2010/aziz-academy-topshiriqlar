n = int(input().strip())
items = []
for _ in range(n):
    cat, name, price, qty = input().split()
    items.append({'cat': cat, 'name': name, 'price': int(price), 'qty': int(qty)})
total1 = {}
for item in items:
    cat = item['cat']
    total = item['price'] * item['qty']
    if cat in total1:
        total1[cat] += total
    else:
        total1[cat]= total
for cat in sorted(total1.keys()):
    print(cat, total1[cat])
