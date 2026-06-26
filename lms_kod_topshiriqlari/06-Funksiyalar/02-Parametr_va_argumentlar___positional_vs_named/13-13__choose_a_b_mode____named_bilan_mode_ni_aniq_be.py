def choose(a, b, mode):
    if mode == 'max':
        return max(a, b)
    elif mode == 'min':
        return min(a, b)
    else:
        return a
a, b = map(int, input().split())
mode = input().strip()
print(choose(a, b, mode))
print(choose(mode=mode, a=a, b=b))