def make_report(a, b):
    return f"sum: {a + b}\ndiff: {a - b}\nprod: {a * b}"
a, b = map(int, input().split())
print(make_report(a, b))