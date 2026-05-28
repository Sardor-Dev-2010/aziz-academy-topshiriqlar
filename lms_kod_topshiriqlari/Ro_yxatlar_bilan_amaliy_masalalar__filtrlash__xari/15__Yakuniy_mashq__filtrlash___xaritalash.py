
n = int(input())
son = list(map(int, input().split()))
lst = []
for i in son:
    if i > 0:
        lst.append(i * 2)
print(lst)