n = int(input())
products = []
for _ in range(n):
    name, price = input().split()
    products.append({'name': name, 'price': int(price)})
x = input().strip()
found = any(p['name'] == x for p in products)
if found:
    print("YES")
else:
    print("NO")
