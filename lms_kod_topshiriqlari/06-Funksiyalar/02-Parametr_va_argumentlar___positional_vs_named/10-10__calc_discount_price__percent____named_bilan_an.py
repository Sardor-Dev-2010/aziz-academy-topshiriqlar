def calc_discount(price, percent):
    return price - price * percent / 100
price, percent = map(int, input().split())
natija1 = (calc_discount(price, percent))
natija2 = (calc_discount(percent=percent, price=price))
print(f"{natija1:.2f}")
print(f"{natija2:.2f}")
