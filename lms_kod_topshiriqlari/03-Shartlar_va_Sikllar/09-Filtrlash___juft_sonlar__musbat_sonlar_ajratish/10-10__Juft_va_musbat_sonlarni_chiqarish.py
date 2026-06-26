
n = int(input())
son = list(map(int, input().split()))
for i in son:
    if i % 2 == 0 and i > 0:
        print(i)
        