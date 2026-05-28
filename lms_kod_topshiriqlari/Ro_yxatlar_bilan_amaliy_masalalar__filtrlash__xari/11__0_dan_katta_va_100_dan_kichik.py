
n = int(input())
son = list(map(int, input().split()))
lst = []
for x in son:
    if 0 < x < 100:
        lst.append(x)
print(lst)