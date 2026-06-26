def calc_all(a, b, c):
    return a + b + c, a * b * c, max(a, b, c), min(a, b, c)
a, b, c = map(int, input().split())
pos_sum, pos_prod, pos_max, pos_min = calc_all(a, b, c)
named_sum, named_prod, named_max, named_min = calc_all(c = c, b = b, a = a)
print(f"pos: {pos_sum} {pos_prod} {pos_max} {pos_min}")
print(f"named: {named_sum} {named_prod} {named_max} {named_min}")
