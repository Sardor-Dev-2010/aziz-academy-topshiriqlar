import sys
d = sys.stdin.read().split()
amount = d[0]
currency = d[1] if len(d) > 1 else 'UZS'
print(amount, currency)