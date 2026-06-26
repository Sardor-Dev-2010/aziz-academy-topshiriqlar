n = int(input())
son = list(map(int, input().split()))
for i in son:
    if i % 5 == 0:
        print(i)