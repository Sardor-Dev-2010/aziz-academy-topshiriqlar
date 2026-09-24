vals = input().split()
print('Ha' if len(vals) != len(set(vals)) else 'Yoq')