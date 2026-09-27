def mean(xs):
    return sum(xs) / len(xs)

def variance(xs):
    m = mean(xs)
    return sum((x - m) ** 2 for x in xs) / len(xs)

def std(xs):
    return variance(xs) ** 0.5

xs = list(map(int, input().split()))
print("%.2f" % mean(xs))
print("%.2f" % variance(xs))
print("%.2f" % std(xs))