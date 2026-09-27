def ekub(a, b):
    if b == 0:
        return a
    return ekub(b, a % b)

a, b = map(int, input().split())
print(ekub(a, b))