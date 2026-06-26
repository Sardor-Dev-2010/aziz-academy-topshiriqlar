w = input().split()
s = {i[0].lower() for i in w if i}
print(*sorted(s))