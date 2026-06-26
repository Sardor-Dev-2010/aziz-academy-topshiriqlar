n = int(input())
products = []
for _ in range(n):
    name, price = input().split()
    products.append({'name': name, 'price': int(price)})
products.sort(key=lambda p: p['price'])
for p in products:
    print(f"{p['name']} {p['price']}")
