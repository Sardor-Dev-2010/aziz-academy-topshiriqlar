def nod(a, b):
    if b == 0:
        return a
    return nod(b, a % b)
a, b = [int(x) for x in input().split()]
print(nod(a, b))