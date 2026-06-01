def div(a, b):
    if b == 0:
        return "ERROR"
    return a / b
a, b = map(int, input().split())
natija = div(a, b)
if natija == "ERROR":
    print(natija)
else:
    print(f"{natija:.2f}")