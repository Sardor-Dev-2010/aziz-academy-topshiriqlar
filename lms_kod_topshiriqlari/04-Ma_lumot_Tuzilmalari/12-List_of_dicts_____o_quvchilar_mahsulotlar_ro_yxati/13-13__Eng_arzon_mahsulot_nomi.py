n = int(input())
products = []
for _ in range(n):
    name, price = input().split()
    products.append({'name': name, 'price': int(price)})
min_price = min(products, key=lambda p: p['price'])
print(min_price['name'])
