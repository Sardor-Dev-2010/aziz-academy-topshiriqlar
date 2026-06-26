
n = int(input())
son = list(map(int, input().split()))
total = [i for i in son if i % 2 == 0]
if total:
    print(min(total))
else:
     print("No")
    