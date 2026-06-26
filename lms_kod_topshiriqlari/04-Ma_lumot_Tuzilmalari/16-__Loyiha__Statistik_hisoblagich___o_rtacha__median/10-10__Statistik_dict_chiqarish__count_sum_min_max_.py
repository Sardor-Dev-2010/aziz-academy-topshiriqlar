n = list(map(int, input().split()))
s = {
    'count': len(n),
    'sum': sum(n),
    'min': min(n),
    'max': max(n)
}
print(s)