w = input().split()
words = {i.lower() for i in w}
print(*sorted(words))