
n = int(input())
son = list(map(int, input().split()))
lst = []
for x in son:
    if x % 2 != 0:
        lst.append(x ** 2)
print(lst)
        